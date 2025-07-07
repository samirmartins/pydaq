import os
import time
import warnings
import threading
import asyncio
import threading
import queue

import matplotlib.pyplot as plt
import nidaqmx
from nidaqmx.constants import TerminalConfiguration
import numpy as np
import serial
import serial.tools.list_ports
from pydaq.utils.base import Base
from scipy.signal import lfilter, butter, firwin, filtfilt


class GetData(Base):
    """
    Class able to get data from data acquisition boards using (or not) a graphical user interface (GUI)

    :author: Samir Angelo Milani Martins
         - https://www.samirmartins.com.br
         - https://www.github.com/samirmartins/

    :param:
        device: nidaq device from where data will be colected. Example: "Dev1"
        channel: channel from where data will be acquired. Example: ai0
        terminal: 'Diff', 'RSE' or 'NRSE': terminal configuration (differential, referenced single ended or non-referenced single ended)
        com: arduino COM port. Example: 'COM1'
        ts: sample period, in seconds.
        session_duration: session duration, in seconds.
        save: if True, saves data in path defined by path.
        path: where data will be saved.
        plot: if True, plot data iteractively as they are acquired

    """

    def __init__(
            self,
            device="Dev1",
            channel="ai0",
            terminal="Diff",
            com="COM1",
            ts=0.5,
            session_duration=10.0,
            save=True,
            plot=True,
    ):
        super().__init__()
        self.device = device
        self.channel = channel
        self.ts = ts
        self.session_duration = session_duration
        self.save = save
        self.plot = plot

        # Terminal configuration
        self.terminal = self.term_map[terminal]

        # Initializing variables
        self.data = []
        self.data_filtered = []
        self.time_var = []
        self.coeffs = []

        # Gathering nidaq info
        self._nidaq_info()

        # Error flags
        self.error_path = False

        # COM ports
        self.com_ports = [i.description for i in serial.tools.list_ports.comports()]
        self.com_port = com  # Default COM port

        # Plot title
        self.title = None

        # Plot legend
        self.legend = ["Input"]

        # Defining default path
        self.path = os.path.join(os.path.join(os.path.expanduser("~")), "Desktop")

        # Arduino ADC resolution (in bits)
        self.arduino_ai_bits = 10

        # Arduino analog input max and min
        self.ard_ai_max, self.ard_ai_min = 5, 0

        # Value per bit - Arduino
        self.ard_vpb = (self.ard_ai_max - self.ard_ai_min) / ((2 ** self.arduino_ai_bits)-1)

        # Flag to control the acquisition thread
        self.acquisition_running = False

    def _acquisition_worker(self, data_queue, print_queue):
        """
        This function runs in a separate thread to acquire data.
        It does not touch the GUI, it only collects data and puts it on the queue.
        """
        st_worker = time.perf_counter()
        self.st_worker = st_worker  # Store the start time for the worker thread
        task = nidaqmx.Task()
        try:
            task.ai_channels.add_ai_voltage_chan(
                self.device + "/" + self.channel, terminal_config=self.terminal
            )
            
            # Main data acquisition loop
            for k in range(self.cycles):
                if not self.acquisition_running:
                    break

                start_iteration_time = time.perf_counter()
                
                # Acquire data
                temp = task.read()
                time_now = time.perf_counter() - st_worker
                
                # Put raw data onto the queue for the main thread to process
                data_queue.put((time_now, temp))

                # Precise timing logic
                wait_time = (st_worker + (k + 1) * self.ts) - time.perf_counter()
                if wait_time > 0:
                    time.sleep(wait_time)
                    # You can uncomment the line below if you still want printouts
                    print_queue.put(f"Iteration: {k} | Time: {time_now:.5f} | Wait: {wait_time:.9f}")
                else:
                    warnings.warn(
                        "Time spent to append data and update interface was greater than ts. "
                        "You CANNOT trust time.dat"
                    )

            total_time = time.perf_counter() - st_worker
            iterations = len(self.data) # Get the actual number of iterations performed
            if iterations > 0:
                average_time = total_time / iterations
                print(f"\nLoop time spent: {total_time:.5f}s | Iterations: {iterations} | Average time: {average_time:.5f}s")
        
        finally:
            task.close()
            # Signal that acquisition is done by putting None in the queue
            data_queue.put(None) 
            # You can uncomment the line below if you still want printouts
            # print_queue.put(f"\nAcquisition loop finished. Total time: {time.perf_counter() - st_worker:.5f}s")


    def get_data_nidaq(self, filter_coefs=None):
        """
        This function can be used for data acquisition and step response experiments using Python + NIDAQ boards.

        :example:
            get_data_nidaq()
        """
        
        # Cleaning data from previous sessions
        self.data = []
        self.data_filtered = []
        self.time_var = []
        self.coeffs = []

        # Use the thread-safe queue for multi-threading
        data_queue = queue.Queue()
        print_queue = queue.Queue()

        # Checking if path was defined
        self._check_path()

        # Number of self.cycles necessary
        self.cycles = int(np.floor(self.session_duration / self.ts)) + 1

        # This inner function is fine, but it also depends on the correct queue type
        def print_worker():
            while True:
                try:
                    message = print_queue.get(timeout=0.5) # Get message from the queue with a timeout
                    if message is None: break
                    print(message)
                except queue.Empty:
                    if not self.acquisition_running and print_queue.empty():
                        break

        print_thread = threading.Thread(target=print_worker, daemon=True)
        print_thread.start()

        # Setting up and starting the acquisition thread
        self.acquisition_running = True
        acquisition_thread = threading.Thread(
            target=self._acquisition_worker,
            # Pass self as the first argument to the instance method
            args=(data_queue, print_queue)
        )
        acquisition_thread.start()

        if self.plot:
            self.title = f"PYDAQ - Data Acquisition. {self.device}, {self.channel}"
            self._start_updatable_plot()

        # Main loop (in the main thread) that consumes data and updates the plot
        while self.acquisition_running:
            try:
                # Try to get data from the queue with a small timeout to keep the GUI responsive
                item = data_queue.get(timeout=0.5) # timeout is set to 0.5 seconds for delay the plot update

                if item is None: # Signal that acquisition is done
                    self.acquisition_running = False
                    break

                timestamp, value = item
                self.time_var.append(timestamp)
                self.data.append(value)

                # If plotting is active, update the plot
                if self.plot:
                    # The filter is applied here, in the main thread
                    if filter_coefs:
                        if isinstance(filter_coefs, tuple) and len(filter_coefs) == 2:
                            b, a = filter_coefs
                            self.coeffs = filter_coefs
                            self.data_filtered = lfilter(b, a, self.data)
                        else:
                            fir_coeff = filter_coefs
                            self.coeffs = filter_coefs
                            self.data_filtered = lfilter(fir_coeff, 1.0, self.data)

                        self._update_plot_dual(self.time_var, self.data, self.data_filtered)
                    else:
                        self._update_plot(self.time_var, self.data)

            except queue.Empty:
                # If the queue is empty, just continue.
                # This allows the loop to keep running and the GUI to remain responsive.
                # We check if the thread is still alive in case it finished between calls.
                if not acquisition_thread.is_alive() and data_queue.empty():
                    self.acquisition_running = False

        # Wait for the threads to finish
        acquisition_thread.join()
        print_queue.put(None) # Signal the end for the print thread
        print_thread.join()

        # Check if data will or not be saved, and save accordingly
        if self.save:
            print("\nSaving data ...")
            # Saving time_var and data
            time_formated = [f"{t:.10f}" for t in self.time_var]
            self._save_data(time_formated, "time.dat")
            self._save_data(self.data, "data.dat")
            self._save_data(self.data_filtered, "data_filtered.dat")
            self._save_data(self.coeffs, "filter_coeffs.dat")
            print("\nData saved ...")

        return

    async def get_data_arduino(self, filter_coefs=None):
        """
            This function can be used for data acquisition and step response experiments using Python + Arduino
            through serial communication

        :example:
            get_data_arduino()
        """

        # Cleaning data array
        self.data = []
        self.data_filtered = []
        self.time_var = []
        self.coeffs = []
        # Start asynchronous queue
        self.data_queue = asyncio.Queue()
        self.print_queue = asyncio.Queue()

        # Check if path was defined
        self._check_path()

        # Number of self.cycles necessary
        self.cycles = int(np.floor(self.session_duration / self.ts)) + 1

        # Start plotting task if enabled
        self.plot_running = False
        plot_task = None

        # Oppening ports
        self._open_serial()

        # Start plotting task if enabled
        self.plot_running = False
        plot_task = None

        if self.plot:  # If plot, start updatable plot
            self.title = f"PYDAQ - Data Acquisition. Arduino, Port: {self.com_port}"
            self._start_updatable_plot()
            await asyncio.sleep(0.5)  # Wait for Arduino and Serial to start up


        # To plot parallel with acquisition
        async def plot_updater():
            while self.plot_running:
                if filter_coefs is not None and len(filter_coefs) > 0:
           
                    if isinstance(filter_coefs, tuple) and len(filter_coefs) == 2:
                        b, a = filter_coefs
                        self.coeffs = filter_coefs
                        self.data_filtered = lfilter(b, a, self.data)
    
                    else:
            
                        fir_coeff = filter_coefs
                        self.coeffs = filter_coefs
                        self.data_filtered = lfilter(fir_coeff, 1.0, self.data)

                elif filter_coefs is None:
                    self.data_filtered = self.data.copy()
            
                if filter_coefs is None:
                    self._update_plot(self.time_var, self.data)
                    await asyncio.sleep(self.ts+1)  # Update plot less frequently than data acquisition
                else:
                    self._update_plot_dual(self.time_var, self.data, self.data_filtered)
                    await asyncio.sleep(self.ts+1)  # Update plot less frequently than data acquisition

        def filter_data(value, filter_coefs):
            if filter_coefs is not None and len(filter_coefs) > 0:
                if isinstance(filter_coefs, tuple) and len(filter_coefs) == 2:
                    b, a = filter_coefs
                    y = lfilter(b, a, self.data)[-1]  
                else:
                    fir_coeff = filter_coefs
                    y = lfilter(fir_coeff, 1.0, self.data)[-1]
            else:
                y = value  

            self.data_filtered.append(y)
        
        # Append task (runs in parallel with acquisition)
        async def store_data():
            while True:
                item = await self.data_queue.get()
                if item is None:
                    break
                timestamp, value = item
                self.time_var.append(timestamp)
                self.data.append(value)

        # Function to print parallel with acquisition
        async def print_worker():
            while True:
                message = await self.print_queue.get()
                if message is None:
                    break
                print(message)

        # Starting asynchronous tasks
        consumer_task = asyncio.create_task(store_data())
        print_task = asyncio.create_task(print_worker())
        # Starting asynchronous task if request
        if self.plot:
            self.plot_running = True
            plot_task = asyncio.create_task(plot_updater())

        st = time.perf_counter()  # Loop start time

        # Main loop, where data will be acquired
        for k in range(self.cycles):

            # Counting time to append data and update interface
            Start_iteration_time = time.perf_counter()

            # Acquire data
            self.ser.reset_input_buffer()  # Reseting serial input buffer
            # Get the last complete value
            temp = int(self.ser.read(14).split()[-2].decode("UTF-8")) * self.ard_vpb 
            #temp = 0

            # Acquire real time data
            time_var = time.perf_counter() - st

            # Queue data for storage
            await self.data_queue.put((time_var, temp))

            self.wait_time = (st + (k + 1) * self.ts) - time.perf_counter()

            # Wait for (ts - delta_time) seconds
            try:
                if self.wait_time > 0:
                    await asyncio.sleep(self.wait_time)
                    await self.print_queue.put(
                        f"Iteration: {k} of {self.cycles - 1} | Start time = {(Start_iteration_time - st):.5f} | Wait time = {self.wait_time:.9f}"
                    )
            except BaseException:
                warnings.warn(
                    "Time spent to append data and update interface was greater than ts. "
                    "You CANNOT trust time.dat"
                )

        total_time = time.perf_counter() - st
        await self.print_queue.put(
            f"\nLoop time spent: {total_time:.10f}s | Iterations: {k + 1} | Average sleep: {(total_time / (k + 1)):.10f}s"
        )

        # Closing port
        self.ser.close()

        # Finalizing data, print and plot consumer
        await self.data_queue.put(None)
        await consumer_task
        await self.print_queue.put(None)
        await print_task
        if self.plot:
            self.plot_running = False
            await plot_task

        # Check if data will or not be saved, and save accordingly
        if self.save:
            print("\nSaving data ...")
            # Saving time_var and data
            time_formated = [f"{t:.10f}" for t in self.time_var]
            self._save_data(time_formated, "time.dat")
            self._save_data(self.data, "data.dat")
            self._save_data(self.data_filtered, "data_filtered.dat")
            self._save_data(self.coeffs, "filter_coeffs.dat")
            print("\nData saved ...")
        
        # Extra Time to Finalize all tasks

        await asyncio.sleep(0.5)
        
        return

    def _update_plot_dual(self, time_var, data, data_filtered):
        plt.ion()  

        fig = plt.gcf()
        ax = fig.gca()

        ax.clear()

        ax.plot(time_var, data, label="Original Data", color="blue")
        ax.scatter(time_var, data, color='blue')
        ax.plot(time_var, data_filtered, label="Filtered Data", color="red")
        ax.scatter(time_var, data_filtered, color='red')

        ax.set_title(self.title)
        ax.set_xlabel("Time (s)")
        ax.set_ylabel("Amplitude")
        ax.grid()
        ax.legend()

        plt.draw()
        plt.pause(self.ts)  
        plt.ioff()
        