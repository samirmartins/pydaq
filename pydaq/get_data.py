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
        # Flag to signal plot window closure
        self.plot_closed_by_user = False

    def _acquisition_worker(self, data_queue, print_queue):
        """
        This function runs in a separate thread to acquire data.
        It does not touch the GUI, it only collects data and puts it on the queue.
        """
        st_worker = time.perf_counter()
        self.st_worker = st_worker
        task = nidaqmx.Task()
        try:
            task.ai_channels.add_ai_voltage_chan(
                self.device + "/" + self.channel, terminal_config=self.terminal
            )
            num_cycles_performed = 0
            for k in range(self.cycles):
                if not self.acquisition_running:
                    break
                # Start_iteration_time = time.perf_counter() # Not used in acquisition thread for prints
                temp = task.read()
                time_now = time.perf_counter() - st_worker
                data_queue.put((time_now, temp))
                num_cycles_performed += 1

                wait_time = (st_worker + (k + 1) * self.ts) - time.perf_counter()
                if wait_time > 0:
                    time.sleep(wait_time)
                    # print_queue.put( # Removed from here, handled by main loop
                    #     f"Iteration: {k} of {self.cycles - 1} | Start time = {(Start_iteration_time - st_worker):.5f} | Wait time = {wait_time:.9f}"
                    # )
                else:
                    warnings.warn(
                        "Time spent to append data and update interface was greater than ts. You CANNOT trust time.dat"
                    )
        finally:
            task.close()
            data_queue.put(None) # Signal end of data acquisition
            total_acquisition_duration = time.perf_counter() - st_worker
            if num_cycles_performed > 0:
                avg_acquisition_time_per_cycle = total_acquisition_duration / num_cycles_performed
                print_queue.put(f"\nAcquisition Thread finished. Total time: {total_acquisition_duration:.5f}s | Cycles acquired: {num_cycles_performed} | Average time per cycle: {avg_acquisition_time_per_cycle:.5f}s")
            else:
                print_queue.put("\nAcquisition Thread finished. No data cycles acquired.")


    # Handler for plot window closure
    def _on_plot_close(self, event):
        """
        Event handler for Matplotlib figure closure.
        Sets acquisition_running to False and plot_closed_by_user to True.
        """
        print("Plot window closed by user. Initiating graceful shutdown...")
        self.acquisition_running = False # Signal acquisition to stop
        self.plot_closed_by_user = True # Signal that plot was closed manually
        # plt.close(self.fig) # No need to manually close here, it's already closing
        
    def get_data_nidaq(self, filter_coefs=None):
        """
        Data acquisition method using NI-DAQ and threading.
        Now includes a secondary plot thread using a complete redraw approach.
        """
        self.data = []
        self.data_filtered = []
        self.time_var = []
        self.coeffs = []
        # Corrected: Initialize self.coeffs using robust check (same as Arduino logic)
        if filter_coefs is not None and (isinstance(filter_coefs, tuple) or len(filter_coefs) > 0):
            self.coeffs = filter_coefs
        else:
            self.coeffs = []

        data_queue = queue.Queue()
        print_queue = queue.Queue() # Keep status mensages
        self.acquisition_running = True
        self.plot_closed_by_user = False # Reset flag for new acquisition

        self._check_path()
        self.cycles = int(np.floor(self.session_duration / self.ts)) + 1

        # Start acquisition thread
        acquisition_thread = threading.Thread(
            target=self._acquisition_worker,
            args=(data_queue, print_queue),
            daemon=True
        )
        acquisition_thread.start()

        if self.plot:
            self.title = f"PYDAQ - Data Acquisition. {self.device}, {self.channel}"
            # Call the centralized plot initialization from Base
            self._start_updatable_plot(title_str=self.title) 
            # Connect the figure close event to our handler
            self.fig.canvas.mpl_connect('close_event', self._on_plot_close)

        k_iteration = 0
        start_main_loop_time = time.perf_counter()
        plot_update_interval = 0.5 # Frequency for plot updates (e.g., 500ms) - Adjusted as requested
        last_plot_update_time = time.perf_counter()


        # Loop principal (GUI + consumo da fila) - Runs as long as acquisition_running is True AND plot is open, OR data/print queues are not empty
        while (self.acquisition_running and not self.plot_closed_by_user) or not data_queue.empty() or not print_queue.empty():
            try:
                # Try to get data from data_queue with a short timeout
                item = data_queue.get(timeout=0.01) # Use a very short timeout to remain responsive

                if item is None:
                    self.acquisition_running = False # Acquisition worker explicitly signaled end
                    # Once acquisition is flagged as False by worker, we continue to drain queues
                    # This loop will now terminate when both data_queue and print_queue are empty AND plot is closed by user or internal stop.
                    
                else: # Process the received data item
                    timestamp, value = item
                    self.time_var.append(timestamp)
                    self.data.append(value)

                    # Processing and Plotting (controlled update frequency)
                    now = time.perf_counter()
                    
                    # Update plot and apply filter at a controlled rate, or when acquisition finishes
                    # Also plot if acquisition just finished to show final state
                    if self.plot and (now - last_plot_update_time >= plot_update_interval or not self.acquisition_running or len(self.data) % self.cycles == 0): # Added check for final plot update
                        # Filtering logic: CORRECTED to use robust check (same as Arduino logic)
                        if filter_coefs is not None and (isinstance(filter_coefs, tuple) or len(filter_coefs) > 0):
                            if isinstance(filter_coefs, tuple) and len(filter_coefs) == 2:
                                b, a = filter_coefs
                                self.data_filtered = lfilter(b, a, np.array(self.data)).tolist()
                            else: # FIR
                                self.data_filtered = lfilter(filter_coefs, 1.0, np.array(self.data)).tolist()
                        else: # If filter_coefs is None or empty, just copy data
                            self.data_filtered = self.data.copy()

                        # Call the centralized plot update from Base
                        if filter_coefs is not None and (isinstance(filter_coefs, tuple) or len(filter_coefs) > 0):
                            self._update_plot(self.time_var, self.data, y2_values=self.data_filtered) # Pass filtered data
                        else:
                            self._update_plot(self.time_var, self.data) # Only original data
                        
                        last_plot_update_time = now # Update last plot time

                    # Progress print (controlled by iteration count)
                    if k_iteration % 10 == 0:
                        print(f"Main Thread - Processed Iteration: {k_iteration} | Time: {timestamp:.5f}")
                    
                    k_iteration += 1 # Increment iteration counter

                # Consume messages from print_queue, if any (moved outside data_queue.get's main if/else)
                try:
                    msg = print_queue.get_nowait()
                    print(msg)
                except queue.Empty:
                    pass

            except queue.Empty: # If data_queue is empty, process prints and sleep briefly
                time.sleep(0.01)
                # Ensure print_queue is drained even if data_queue is empty
                try:
                    msg = print_queue.get_nowait()
                    print(msg)
                except queue.Empty:
                    pass

                # Exit conditions for the main loop
                # If acquisition has finished OR plot was closed, and both queues are empty
                if (not self.acquisition_running or self.plot_closed_by_user) and data_queue.empty() and print_queue.empty():
                    print("Main thread: Acquisition/Plotting finished. Exiting processing loop gracefully.")
                    break
            except Exception as e:
                print(f"Error in main thread processing: {e}")
                self.acquisition_running = False # Stop on error
                self.plot_closed_by_user = True # Ensure loop terminates if error is critical
                break
        
        acquisition_thread.join()
        print("Main thread: Acquisition thread joined.")

        total_main_loop_time = time.perf_counter() - start_main_loop_time
        if k_iteration > 0:
            avg_time_per_iteration = total_main_loop_time / k_iteration
            print(f"\nMain loop finished. Total time: {total_main_loop_time:.5f}s | Iterations: {k_iteration} | Average time per iteration: {avg_time_per_iteration:.5f}s")
        else:
            print("\nMain loop finished. No data processed.")

        # FINAL PLOT STATE: Keep plot open if not closed by user, otherwise close it.
        if self.plot and not self.plot_closed_by_user:
            print("Plot remaining open. Close window manually to exit.")
            # This line is crucial: it keeps the main thread alive and Matplotlib processing GUI events
            # until the figure is manually closed by the user.
            plt.show(block=True) # BLOCKING CALL: this keeps the main thread alive for the GUI

        if self.save:
            print("\nSaving data ...")
            time_formated = [f"{t:.10f}" for t in self.time_var]
            self._save_data(time_formated, "time.dat")
            self._save_data(self.data, "data.dat")
            self._save_data(self.data_filtered, "data_filtered.dat")
            self._save_data(self.coeffs, "filter_coeffs.dat")
            print("\nData saved ...")

        # After plt.show(block=True) returns (user closed window), then proceed to exit.
        if self.plot and self.plot_closed_by_user:
             plt.ioff() # Turn off interactive mode explicitly
             plt.close(self.fig) # Explicitly close the figure once plt.show(block=True) returns.


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
        