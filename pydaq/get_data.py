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
            plot_mode="no", # Options: "realtime", "end", "no"
    ):
        super().__init__()
        self.device = device
        self.channel = channel
        self.ts = ts
        self.session_duration = session_duration
        self.save = save
        self.plot_mode = plot_mode

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
        self.plot_ready_event = threading.Event()

    def _acquisition_worker_nidaq(self, data_queue):
        """
        This function runs in a separate thread to acquire data from NIDAQ.
        It does not touch the GUI, it only collects data and puts it on the queue.
        """
        # Wait for plot to be ready before starting acquisition to synchronize time_now to ~0
        self.plot_ready_event.wait() 

        task = nidaqmx.Task()
        
        try:
            task.ai_channels.add_ai_voltage_chan(
                self.device + "/" + self.channel, terminal_config=self.terminal
            )
            num_cycles_performed = 0
            
            st_worker = time.perf_counter()
            self.st_worker = st_worker
            
            for k in range(self.cycles):
                if not self.acquisition_running:
                    break
                temp = task.read()
                time_now = time.perf_counter() - st_worker
                data_queue.put((time_now, temp))
                num_cycles_performed += 1

                wait_time = (st_worker + (k + 1) * self.ts) - time.perf_counter()
                if wait_time > 0:
                    time.sleep(wait_time)
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
                print(f"\nAcquisition Thread finished. Total time: {total_acquisition_duration:.5f}s | Cycles acquired: {num_cycles_performed} | Average time per cycle: {avg_acquisition_time_per_cycle:.5f}s")
            else:
                print("\nAcquisition Thread finished. No data cycles acquired.")

    # Handler for plot window closure
    def _on_plot_close(self, event):
        """
        Event handler for Matplotlib figure closure.
        Sets acquisition_running to False and plot_closed_by_user to True.
        """
        print("Plot window closed by user. Initiating graceful shutdown...")
        self.acquisition_running = False # Signal acquisition to stop
        self.plot_closed_by_user = True # Signal that plot was closed manually
        
    def get_data_nidaq(self, filter_coefs=None):
        """
        Data acquisition method using NI-DAQ and threading.
        Now includes a secondary plot thread using a complete redraw approach.
        """
        self.data = []
        self.data_filtered = []
        self.time_var = []
        self.coeffs = []
        if filter_coefs is not None and (isinstance(filter_coefs, tuple) or len(filter_coefs) > 0):
            self.coeffs = filter_coefs
        else:
            self.coeffs = []

        data_queue = queue.Queue()
        self.acquisition_running = True
        self.plot_closed_by_user = False
        self.plot_ready_event.clear()

        self._check_path()
        self.cycles = int(np.floor(self.session_duration / self.ts)) + 1

        acquisition_thread = threading.Thread(
            target=self._acquisition_worker_nidaq,
            args=(data_queue,),
            daemon=True
        )
        acquisition_thread.start()

        if self.plot_mode == 'realtime':
            self.title = f"PYDAQ - Data Acquisition. {self.device}, {self.channel}"
            self._start_updatable_plot(title_str=self.title) 
            self.fig.canvas.mpl_connect('close_event', self._on_plot_close)
            time.sleep(0.5)
            self.plot_ready_event.set()
        else:
            self.plot_ready_event.set()

        if self.ts >= 0.05:
            plot_update_interval = 0.05
        else:
            plot_update_interval = 0.25

        last_plot_update_time = time.perf_counter()

        while (self.acquisition_running and not self.plot_closed_by_user) or not data_queue.empty():
            try:
                item = data_queue.get(timeout=0.01)

                if item is None:
                    self.acquisition_running = False
                    # Flushes the queue to ensure all data is processed
                    while not data_queue.empty():
                        remaining_item = data_queue.get_nowait()
                        if remaining_item is not None:
                            timestamp, value = remaining_item
                            self.time_var.append(timestamp)
                            self.data.append(value)
                    break

                timestamp, value = item
                self.time_var.append(timestamp)
                self.data.append(value)

                now = time.perf_counter()
                if self.plot_mode == 'realtime' and (now - last_plot_update_time >= plot_update_interval or not self.acquisition_running):
                    # Applies the filter for real-time plotting
                    if filter_coefs is not None and (isinstance(filter_coefs, tuple) or len(filter_coefs) > 0):
                        if isinstance(filter_coefs, tuple) and len(filter_coefs) == 2:
                            b, a = filter_coefs
                            self.data_filtered = lfilter(b, a, np.array(self.data)).tolist()
                        else:
                            self.data_filtered = lfilter(filter_coefs, 1.0, np.array(self.data)).tolist()

                    self._update_plot(
                        self.time_var,
                        self.data,
                        y2_values=self.data_filtered if self.data_filtered else None,
                        y1_label="Original Data",
                        y2_label="Filtered Data"
                    )
                    last_plot_update_time = now

            except queue.Empty:
                time.sleep(0.01)
                if not self.acquisition_running and data_queue.empty():
                    break

        acquisition_thread.join()

        # Applies final filter if coefficients are present (to save and plot at the end)
        if filter_coefs is not None and (isinstance(filter_coefs, tuple) or len(filter_coefs) > 0):
            if isinstance(filter_coefs, tuple) and len(filter_coefs) == 2:
                b, a = filter_coefs
                self.data_filtered = lfilter(b, a, np.array(self.data)).tolist()
            else:
                self.data_filtered = lfilter(filter_coefs, 1.0, np.array(self.data)).tolist()

        if self.plot_mode == 'realtime' and not self.plot_closed_by_user:
            print("Plot remaining open. Close window manually to exit.")
            plt.show(block=True)

        # NEW BLOCK: Logic to plot at the end
        if self.plot_mode == 'end' and self.time_var:
            print("\nGenerating plot at the end of acquisition...")
            self.title = f"PYDAQ - Final Acquisition: {self.device}, {self.channel}"
            self._start_updatable_plot(title_str=self.title)
            self._update_plot(
                self.time_var,
                self.data,
                y2_values=self.data_filtered if self.data_filtered else None,
                y1_label="Original Data",
                y2_label="Filtered Data"
            )
            plt.show(block=True) # Keeps the final plot open

        if self.save:
            print("\nSaving data ...")
            time_formated = [f"{t:.10f}" for t in self.time_var]
            self._save_data(time_formated, "time.dat")
            self._save_data(self.data, "data.dat")
            if self.data_filtered:
                self._save_data(self.data_filtered, "data_filtered.dat")
            if len(self.coeffs) > 0:
                self._save_data(self.coeffs, "filter_coeffs.dat")
            print("\nData saved ...")

        if self.plot_mode == 'realtime' and self.plot_closed_by_user:
            plt.ioff()
            plt.close(self.fig)
        return

    def _acquisition_worker_arduino(self, data_queue):
        """
        This function runs in a separate thread to acquire data from Arduino via serial.
        It does not touch the GUI, it only collects data and puts it on the queue.
        """
        # Wait for plot to be ready before starting acquisition to synchronize time_now to ~0
        self.plot_ready_event.wait()

        num_cycles_performed = 0
        try:
            self.ser = serial.Serial(
                self.com_port,
                timeout=1,
                baudrate=9600 
            )
            print(f"Serial port {self.com_port} opened successfully.")
            
            st_worker = time.perf_counter()
            self.st_worker = st_worker

            for k in range(self.cycles):
                if not self.acquisition_running:
                    break
                
                self.ser.reset_input_buffer()
                try:
                    line_bytes = self.ser.readline()
                    temp = int(line_bytes.split()[-2].decode("UTF-8")) * self.ard_vpb
                except (ValueError, IndexError, UnicodeDecodeError, serial.SerialException) as e:
                    warnings.warn(f"Error reading from Arduino: {e}. Skipping sample.")
                    temp = 0
                #temp = int(self.ser.read(14).split()[-2].decode("UTF-8")) * self.ard_vpb

                time_now = time.perf_counter() - st_worker
                data_queue.put((time_now, temp))
                num_cycles_performed += 1

                wait_time = (st_worker + (k + 1) * self.ts) - time.perf_counter()
                if wait_time > 0:
                    time.sleep(wait_time)
                else:
                    warnings.warn(
                        "Time spent to append data and update interface was greater than ts. You CANNOT trust time.dat"
                    )
        except serial.SerialException as e:
            warnings.warn(f"Failed to open serial port {self.com_port}: {e}")
            print(f"ERROR: Failed to open serial port {self.com_port}: {e}")
            self.acquisition_running = False
        finally:
            if hasattr(self, 'ser') and self.ser.is_open:
                self.ser.close()
                print(f"Serial port {self.com_port} closed.")
            data_queue.put(None)
            total_acquisition_duration = time.perf_counter() - st_worker
            if num_cycles_performed > 0:
                avg_acquisition_time_per_cycle = total_acquisition_duration / num_cycles_performed
                print(f"\nAcquisition Thread finished. Total time: {total_acquisition_duration:.5f}s | Cycles acquired: {num_cycles_performed} | Average time per cycle: {avg_acquisition_time_per_cycle:.5f}s")
            else:
                print("\nAcquisition Thread finished. No data cycles acquired.")

    def get_data_arduino(self, filter_coefs=None):
        """
        This function can be used for data acquisition and step response experiments using Python + Arduino
        through serial communication. Now adapted to threading model for consistent plot handling.
        """
        self.data = []
        self.data_filtered = []
        self.time_var = []
        self.coeffs = []
        if filter_coefs is not None and (isinstance(filter_coefs, tuple) or len(filter_coefs) > 0):
            self.coeffs = filter_coefs
        else:
            self.coeffs = []

        data_queue = queue.Queue()
        self.acquisition_running = True
        self.plot_closed_by_user = False
        self.plot_ready_event.clear()

        self._check_path()
        self.cycles = int(np.floor(self.session_duration / self.ts)) + 1

        acquisition_thread = threading.Thread(
            target=self._acquisition_worker_arduino,
            args=(data_queue,), 
            daemon=True
        )
        acquisition_thread.start()

        if self.plot_mode == 'realtime':
            self.title = f"PYDAQ - Data Acquisition. Arduino, Port: {self.com_port}"
            self._start_updatable_plot(title_str=self.title)
            self.fig.canvas.mpl_connect('close_event', self._on_plot_close)
            time.sleep(0.5)
            self.plot_ready_event.set()
        else:
            # If it is not in real time, release the acquisition immediately.
            self.plot_ready_event.set()

        if self.ts >= 0.05:
            plot_update_interval = 0.05
        else:
            plot_update_interval = 0.25

        last_plot_update_time = time.perf_counter()

        while (self.acquisition_running and not self.plot_closed_by_user) or not data_queue.empty():
            try:
                item = data_queue.get(timeout=0.01)

                if item is None:
                    self.acquisition_running = False
                    # Flushes the queue to ensure all data is processed
                    while not data_queue.empty():
                        remaining_item = data_queue.get_nowait()
                        if remaining_item is not None:
                            timestamp, value = remaining_item
                            self.time_var.append(timestamp)
                            self.data.append(value)
                    break

                timestamp, value = item
                self.time_var.append(timestamp)
                self.data.append(value)

                now = time.perf_counter()
                if self.plot_mode == 'realtime' and (now - last_plot_update_time >= plot_update_interval or not self.acquisition_running):
                    # Applies the filter for real-time plotting
                    if filter_coefs is not None and (isinstance(filter_coefs, tuple) or len(filter_coefs) > 0):
                        if isinstance(filter_coefs, tuple) and len(filter_coefs) == 2:
                            b, a = filter_coefs
                            self.data_filtered = lfilter(b, a, np.array(self.data)).tolist()
                        else:
                            self.data_filtered = lfilter(filter_coefs, 1.0, np.array(self.data)).tolist()
                    
                    self._update_plot(
                        self.time_var,
                        self.data,
                        y2_values=self.data_filtered if self.data_filtered else None,
                        y1_label="Original Data",
                        y2_label="Filtered Data"
                    )
                    last_plot_update_time = now

            except queue.Empty:
                time.sleep(0.01)
                if not self.acquisition_running and data_queue.empty():
                    break
        
        acquisition_thread.join()

        # Applies final filter if coefficients are present (to save and plot at the end)
        if filter_coefs is not None and (isinstance(filter_coefs, tuple) or len(filter_coefs) > 0):
            if isinstance(filter_coefs, tuple) and len(filter_coefs) == 2:
                b, a = filter_coefs
                self.data_filtered = lfilter(b, a, np.array(self.data)).tolist()
            else:
                self.data_filtered = lfilter(filter_coefs, 1.0, np.array(self.data)).tolist()

        if self.plot_mode == 'realtime' and not self.plot_closed_by_user:
            print("Plot remaining open. Close window manually to exit.")
            plt.show(block=True)

        # NEW BLOCK: Logic to plot at the end
        if self.plot_mode == 'end' and self.time_var:
            print("\nGenerating plot at the end of acquisition...")
            self.title = f"PYDAQ - Final Acquisition: Arduino, Port: {self.com_port}"
            self._start_updatable_plot(title_str=self.title)
            self._update_plot(
                self.time_var,
                self.data,
                y2_values=self.data_filtered if self.data_filtered else None,
                y1_label="Original Data",
                y2_label="Filtered Data"
            )
            plt.show(block=True) # Keeps the final plot open

        if self.save:
            print("\nSaving data ...")
            time_formated = [f"{t:.10f}" for t in self.time_var]
            self._save_data(time_formated, "time.dat")
            self._save_data(self.data, "data.dat")
            if self.data_filtered:
                self._save_data(self.data_filtered, "data_filtered.dat")
            if len(self.coeffs) > 0:
                self._save_data(self.coeffs, "filter_coeffs.dat")
            print("\nData saved ...")

        if self.plot_mode == 'realtime' and self.plot_closed_by_user:
            plt.ioff()
            plt.close(self.fig)

        return


    def _update_plot_dual(self, time_var, data, data_filtered):
        warnings.warn("`_update_plot_dual` is deprecated. Use `_update_plot` from Base class instead.")
        plt.ion() # This would cause issues if called within a loop

        fig = plt.gcf()
        ax = fig.gca()

        ax.clear()

        ax.plot(time_var, data, label="Original Data", color="blue", marker='o', linestyle='-')
        ax.plot(time_var, data_filtered, label="Filtered Data", color="red", marker='o', linestyle='-')

        ax.set_title(self.title if hasattr(self, 'title') else "Plot")
        ax.set_xlabel("Time (s)")
        ax.set_ylabel("Amplitude")
        ax.grid()
        ax.legend()

        plt.draw()
        plt.pause(self.ts)
        plt.ioff()