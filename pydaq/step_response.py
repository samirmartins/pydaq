import os
import time
import numpy as np

import serial
import serial.tools.list_ports
from pydaq.utils.base import Base

import threading
import queue

import os
import serial
import serial.tools.list_ports
import matplotlib.pyplot as plt
import warnings
import nidaqmx
from nidaqmx.constants import TerminalConfiguration


class StepResponse(Base):
    """
     Class developed to construct Graphical User Interface for step
     response using arduino and NIDAQ boards

    :author: Samir Angelo Milani Martins
          - https://www.samirmartins.com.br
          - https://www.github.com/samirmartins/

     :params:
         device: nidaq default device.
         ao_channel: nidaq default analog output channel
         ai_channel: nidaq default analog input channel
         ts: sample period, in seconds.
         session_duration: session duration, in seconds.
         step_time: time when step will be applied, in seconds
         step_min: minimum step  value
         step_max: maximum step value
         terminal: 'Diff', 'RSE' or 'NRSE': terminal configuration (differential, referenced single ended or non-referenced single ended)
         plot: if True, plot data iteractively as they are sent/acquired


    """

    def __init__(
        self,
        device="Dev1",
        ao_channel="ao0",
        ai_channel="ai0",
        ts=0.5,
        session_duration=10.0,
        step_time=3.0,
        step_min=0,
        step_max=5,
        terminal="Diff",
        com="COM1",
        plot_mode="realtime", # Options: "realtime", "end", "no"
        save=True,
    ):

        super().__init__()
        self.ts = ts
        self.session_duration = session_duration
        self.plot_mode = plot_mode
        self.step_time = step_time
        self.device = device
        self.ai_channel = ai_channel
        self.ao_channel = ao_channel
        self.step_min = step_min
        self.step_max = step_max
        self.save = save

        # Terminal configuration
        self.terminal = self.term_map[terminal]

        # COM ports
        self.com_ports = [i.description for i in serial.tools.list_ports.comports()]
        self.com_port = com

        # Initializing variables
        self.time_var, self.input, self.output = [], [], []

        # Plot title
        self.title = None

        # Defining default path
        self.path = os.path.join(os.path.join(os.path.expanduser("~")), "Desktop")

        # Arduino ADC resolution (in bits)
        self.arduino_ai_bits = 10
        self.ard_ao_max, self.ard_ao_min = 5, 0
        self.ard_vpb = (self.ard_ao_max - self.ard_ao_min) / ((2**self.arduino_ai_bits) - 1)

        # Legends
        self.legend = ["Output", "Input"]

        # Threading control flags and events
        self.acquisition_running = False
        self.plot_closed_by_user = False
        self.plot_ready_event = threading.Event()

    # Handler for plot window closure
    def _on_plot_close(self, event):
        """..."""
        print("Plot window closed by user. Initiating graceful shutdown...")
        self.acquisition_running = False
        self.plot_closed_by_user = True

    def _step_response_worker_arduino(self, data_queue):
        self.plot_ready_event.wait()
        
        st_worker = time.perf_counter()
        
        try:
            self._open_serial()
            sent_data = b"0"
            self.ser.write(sent_data)

            for k in range(self.cycles):
                if not self.acquisition_running:
                    break
                
                # Update step value
                if k * self.ts >= float(self.step_time):
                    sent_data = b"1"
                else:
                    sent_data = b"0"

                self.ser.write(sent_data)
                self.ser.reset_input_buffer()
                
                try:
                    line_bytes = self.ser.readline()
                    # A robust parsing is important here
                    temp = int(line_bytes.decode("UTF-8").strip()) * self.ard_vpb
                except (ValueError, IndexError, UnicodeDecodeError, serial.SerialException):
                    temp = 0 # Default to 0 on error
                
                time_now = time.perf_counter() - st_worker
                data_queue.put((time_now, 5.0 * float(sent_data.decode()), temp))

                wait_time = (st_worker + (k + 1) * self.ts) - time.perf_counter()
                if wait_time > 0:
                    time.sleep(wait_time)

        except serial.SerialException as e:
            warnings.warn(f"Failed to open or use serial port {self.com_port}: {e}")
        finally:
            if hasattr(self, 'ser') and self.ser.is_open:
                self.ser.write(b"0")
                self.ser.close()
            data_queue.put(None)
    

    def step_response_arduino(self):
        """
        This method performs the step response using an Arduino board for given parameters.

        :example:
            step_response_arduino()

        """

        # --- Start of placeholder implementation ---
        print("Running step response for Arduino...")
        self.time_var, self.input, self.output = [], [], []
        data_queue = queue.Queue()
        self.acquisition_running = True
        self.plot_closed_by_user = False
        self.plot_ready_event.clear()

        self._check_path()
        self.cycles = int(np.floor(self.session_duration / self.ts)) + 1

        acquisition_thread = threading.Thread(
            target=self._step_response_worker_arduino,
            args=(data_queue,),
            daemon=True
        )
        acquisition_thread.start()

        if self.plot_mode == 'realtime':
            self.title = f"PYDAQ - Step Response (Arduino), Port: {self.com_port}"
            self._start_updatable_plot(title_str=self.title)
            self.fig.canvas.mpl_connect('close_event', self._on_plot_close)
            self.plot_ready_event.set()
        else:
            self.plot_ready_event.set()

        while (self.acquisition_running and not self.plot_closed_by_user) or not data_queue.empty():
            try:
                item = data_queue.get(timeout=0.01)
                if item is None:
                    self.acquisition_running = False
                    break
                timestamp, input_val, output_val = item
                self.time_var.append(timestamp)
                self.input.append(input_val)
                self.output.append(output_val)

                if self.plot_mode == 'realtime':
                    self._update_plot(
                        [self.time_var, self.time_var],
                        [self.output, self.input],
                        y1_label=self.legend[0],
                        y2_label=self.legend[1]
                    )
            except queue.Empty:
                if self.plot_mode == 'realtime':
                    plt.pause(0.01)
                else:
                    time.sleep(0.01)

        acquisition_thread.join()

        if self.plot_mode == 'end' and self.time_var:
            self.title = f"PYDAQ - Final Step Response (Arduino)"
            self._start_updatable_plot(title_str=self.title)
            self._update_plot(
                [self.time_var, self.time_var],
                [self.output, self.input],
                y1_label=self.legend[0],
                y2_label=self.legend[1]
            )
            plt.show(block=True)
            
        if self.save:
            print("\nSaving data ...")
            self._save_data(self.time_var, "time.dat")
            self._save_data(self.input, "input.dat")
            self._save_data(self.output, "output.dat")
            print("\nData saved ...")
            
        if self.plot_mode == 'realtime' and not self.plot_closed_by_user:
            print("\nPlot remains open. Close window manually to exit.")
            plt.show(block=True)
            
        return

    def _step_response_worker_nidaq(self, data_queue):
        # Wait for plot to be ready to synchronize start time
        self.plot_ready_event.wait()
        
        st_worker = time.perf_counter()
        task_ao = nidaqmx.Task()
        task_ai = nidaqmx.Task()
    
        try:
            task_ao.ao_channels.add_ao_voltage_chan(
                f"{self.device}/{self.ao_channel}",
                min_val=float(self.step_min),
                max_val=float(self.step_max),
            )
            task_ai.ai_channels.add_ai_voltage_chan(
                f"{self.device}/{self.ai_channel}", terminal_config=self.terminal
            )
            
            sent_data = self.step_min
            task_ao.write(sent_data)

            for k in range(self.cycles):
                if not self.acquisition_running:
                    break

                # Update step value
                if k * self.ts >= float(self.step_time):
                    sent_data = self.step_max
                else:
                    sent_data = self.step_min
                
                task_ao.write(sent_data)
                temp = task_ai.read()
                
                time_now = time.perf_counter() - st_worker
                data_queue.put((time_now, float(sent_data), temp))

                wait_time = (st_worker + (k + 1) * self.ts) - time.perf_counter()
                if wait_time > 0:
                    time.sleep(wait_time)
        
        finally:
            task_ao.write(0) # Turn off output at the end
            task_ao.close()
            task_ai.close()
            data_queue.put(None) # Signal end of acquisition

    def step_response_nidaq(self):
        """
        This method performs the step response using a NIDAQ board for given parameters.

        :example:
            step_response_nidaq()

        """

        self.time_var, self.input, self.output = [], [], []
        data_queue = queue.Queue()
        self.acquisition_running = True
        self.plot_closed_by_user = False
        self.plot_ready_event.clear()

        self._check_path()
        self.cycles = int(np.floor(self.session_duration / self.ts)) + 1

        acquisition_thread = threading.Thread(
            target=self._step_response_worker_nidaq,
            args=(data_queue,),
            daemon=True
        )
        acquisition_thread.start()

        if self.plot_mode == 'realtime':
            self.title = f"PYDAQ - Step Response (NIDAQ). {self.device}, {self.ai_channel}, {self.ao_channel}"
            self._start_updatable_plot(title_str=self.title)
            self.fig.canvas.mpl_connect('close_event', self._on_plot_close)
            self.plot_ready_event.set()
        else:
            self.plot_ready_event.set() # Allow acquisition to start immediately

        # Main loop for data consumption and plotting
        while (self.acquisition_running and not self.plot_closed_by_user) or not data_queue.empty():
            try:
                item = data_queue.get(timeout=0.01)

                if item is None:
                    self.acquisition_running = False
                    break

                timestamp, input_val, output_val = item
                self.time_var.append(timestamp)
                self.input.append(input_val)
                self.output.append(output_val)

                # Periodic plot update for 'realtime' mode
                if self.plot_mode == 'realtime':
                    # A simple periodic update can be added here if needed for performance
                    self._update_plot(
                        [self.time_var, self.time_var],
                        [self.output, self.input],
                        y1_label=self.legend[0],
                        y2_label=self.legend[1]
                    )

            except queue.Empty:
                # This keeps the loop responsive and allows GUI event processing
                if self.plot_mode == 'realtime':
                    plt.pause(0.01)
                else:
                    time.sleep(0.01)

        acquisition_thread.join()

        if self.plot_mode == 'end' and self.time_var:
            self.title = f"PYDAQ - Final Step Response (NIDAQ)"
            self._start_updatable_plot(title_str=self.title)
            self._update_plot(
                [self.time_var, self.time_var],
                [self.output, self.input],
                y1_label=self.legend[0],
                y2_label=self.legend[1]
            )
            plt.show(block=True)
            
        if self.save:
            print("\nSaving data ...")
            self._save_data(self.time_var, "time.dat")
            self._save_data(self.input, "input.dat")
            self._save_data(self.output, "output.dat")
            print("\nData saved ...")

        if self.plot_mode == 'realtime' and not self.plot_closed_by_user:
            print("\nPlot remains open. Close window manually to exit.")
            plt.show(block=True)
        
        return
