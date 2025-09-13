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
from scipy.signal import savgol_filter

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
        plot_mode="no", # Options: "realtime", "end", "no"
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

        self.calculate_pid = False  # Flag to enable calculation
        self.sintony_type = 0  # Tuning type: 'P', 'PI', or 'PID'
        self.pid_parameters = []    # To store the results [Kp, Ki, Kd]

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
        
        try:
            self._open_serial()
            
            # --- WARM-UP SECTION ---
            # Send an initial command (b"0") to "wake up" the Arduino.
            self.ser.write(b"0")
            self.ser.reset_input_buffer()

            # Perform a "warm-up read". This is the call that will be slow.
            # We will not use this data, so we assign it to '_' (discard).
            _ = self.ser.readline()
            # --- END WARM-UP SECTION ---

            st_worker = time.perf_counter()

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
                
                temp = int(self.ser.read(14).split()[-2].decode("UTF-8")) * self.ard_vpb

                '''try:
                    self.ser.reset_input_buffer()
                    line_bytes = self.ser.readline()
                    #parts = line_bytes.split()
                    #temp = int(parts[0].decode("UTF-8")) * self.ard_vpb  
                    temp = int(line_bytes.split()[-2].decode("UTF-8")) * self.ard_vpb
                except (ValueError, IndexError, UnicodeDecodeError):
                    warnings.warn(f"Invalid read from Arduino on cycle {k}. Using value 0.")
                    temp = 0 # Error handling to avoid breaking the loop.'''
                
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
                print(f"Serial port {self.com_port} closed.")
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

            # Add a short delay to allow the plot window to open fully
            print("\nReal-time plot started. Waiting 0.5s for the window to render...")
            time.sleep(0.5)

            self.plot_ready_event.set()
        else:
            self.plot_ready_event.set()

        # Plot update throttling logic for performance
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
                    # Drain the queue to ensure all data is processed
                    while not data_queue.empty():
                        remaining_item = data_queue.get_nowait()
                        if remaining_item is not None:
                            timestamp, input_val, output_val = remaining_item
                            self.time_var.append(timestamp)
                            self.input.append(input_val)
                            self.output.append(output_val)
                    break

                timestamp, input_val, output_val = item
                self.time_var.append(timestamp)
                self.input.append(input_val)
                self.output.append(output_val)

                # Throttle plot updates for performance
                now = time.perf_counter()
                if self.plot_mode == 'realtime' and (now - last_plot_update_time >= plot_update_interval or not self.acquisition_running):
                    self._update_plot(
                        self.time_var,
                        self.output,
                        y2_values=self.input,
                        y1_label=self.legend[0],
                        y2_label=self.legend[1]
                    )
                    last_plot_update_time = now

            except queue.Empty:
                # This keeps the loop responsive
                time.sleep(0.01)
                if not self.acquisition_running and data_queue.empty():
                    break

        acquisition_thread.join()

        if self.calculate_pid and self.time_var:
            print("\nCalculating PID parameters using Ziegler-Nichols method...")
            Kp, Ki, Kd, tangent_plot, output_norm, gain_norm = self.get_parameters(
                self.time_var,
                self.output,
                self.step_time,
                self.sintony_type,
                self.ard_ao_min, # Min for Arduino
                self.ard_ao_max  # Max for Arduino
            )

            self.pid_parameters = [Kp, Ki, Kd]

            # Plot tuning results
            plt.figure(figsize=(10, 6))
            plt.plot(self.time_var, output_norm, label="Normalized System Output", linewidth=2)
            plt.plot(self.time_var, tangent_plot, '--', label="Tangent Line (Inflection)", linewidth=2, color='r')
            plt.plot(self.time_var, gain_norm, label="Normalized Step Input (Gain K)", linewidth=2)
            plt.title("Ziegler-Nichols Tuning Analysis", fontsize=16)
            plt.xlabel("Time (s)", fontsize=14)
            plt.ylabel("Normalized Amplitude", fontsize=14)
            plt.legend()
            plt.grid(True)
            plt.show(block=False) # Show the plot without blocking the code

        if self.plot_mode == 'end' and self.time_var:
            self.title = f"PYDAQ - Final Step Response (Arduino)"
            self._start_updatable_plot(title_str=self.title)
            self._update_plot(
                self.time_var,
                self.output,
                y2_values=self.input,  # Correct format
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

            # Add a short delay to allow the plot window to open fully
            print("\nReal-time plot started. Waiting 0.5s for the window to render...")
            time.sleep(0.5)

            self.plot_ready_event.set()
        else:
            self.plot_ready_event.set() # Allow acquisition to start immediately

        # Plot update throttling logic for performance
        if self.ts >= 0.05:
            plot_update_interval = 0.05
        else:
            plot_update_interval = 0.25
            
        last_plot_update_time = time.perf_counter()
        
        # Main loop for data consumption and plotting
        while (self.acquisition_running and not self.plot_closed_by_user) or not data_queue.empty():
            try:
                item = data_queue.get(timeout=0.01)

                if item is None:
                    self.acquisition_running = False
                    # Drain the queue to ensure all data is processed
                    while not data_queue.empty():
                        remaining_item = data_queue.get_nowait()
                        if remaining_item is not None:
                            timestamp, input_val, output_val = remaining_item
                            self.time_var.append(timestamp)
                            self.input.append(input_val)
                            self.output.append(output_val)
                    break

                timestamp, input_val, output_val = item
                self.time_var.append(timestamp)
                self.input.append(input_val)
                self.output.append(output_val)

                # Throttle plot updates for performance
                now = time.perf_counter()
                if self.plot_mode == 'realtime' and (now - last_plot_update_time >= plot_update_interval or not self.acquisition_running):
                    self._update_plot(
                        self.time_var,
                        self.output,
                        y2_values=self.input,
                        y1_label=self.legend[0],
                        y2_label=self.legend[1]
                    )
                    last_plot_update_time = now

            except queue.Empty:
                # This keeps the loop responsive
                time.sleep(0.01)
                if not self.acquisition_running and data_queue.empty():
                    break

        acquisition_thread.join()

        if self.calculate_pid and self.time_var:

            Kp, Ki, Kd, tangent_plot, output_norm, gain_norm = self.get_parameters(
                self.time_var,
                self.output,
                self.step_time,
                self.sintony_type,
                self.step_min, # Min for NIDAQ
                self.step_max  # Max for NIDAQ
            )
            self.pid_parameters = [Kp, Ki, Kd]

            # Plot tuning results
            plt.figure(figsize=(10, 6))
            plt.plot(self.time_var, output_norm, label="Normalized System Output", linewidth=2)
            plt.plot(self.time_var, tangent_plot, '--', label="Tangent Line (Inflection)", linewidth=2, color='r')
            plt.plot(self.time_var, gain_norm, label="Normalized Step Input (Gain K)", linewidth=2)
            plt.title("Ziegler-Nichols Tuning Analysis", fontsize=16)
            plt.xlabel("Time (s)", fontsize=14)
            plt.ylabel("Normalized Amplitude", fontsize=14)
            plt.legend()
            plt.grid(True)
            plt.show(block=False) # Show the plot without blocking the code

        if self.plot_mode == 'end' and self.time_var:
            self.title = f"PYDAQ - Final Step Response (NIDAQ)"
            self._start_updatable_plot(title_str=self.title)
            self._update_plot(
                self.time_var,
                self.output,
                y2_values=self.input,  # Correct format
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
    
    # PASTE THESE TWO METHODS INSIDE THE StepResponse CLASS

    def get_parameters(self, time, system_value, step_time, type_sintony, min_val, max_val):
        time = np.array(time)
        system_value = np.array(system_value)
        
        # Normalize output to start at zero
        system_value_normalized = system_value - system_value[0]

        # Calculate the process gain K
        delta_input = max_val - min_val
        if delta_input == 0:
            # Avoid division by zero if step is zero
            k = np.inf
        else:
            k = (system_value_normalized[-1] - system_value_normalized[0]) / delta_input

        max_derivative_idx, derivative = self.get_max_derivative_idx(time, system_value_normalized, step_time)

        time_inflection = time[max_derivative_idx]
        sys_inflection = system_value_normalized[max_derivative_idx]

        # Fit tangent line at the inflection point
        slope = derivative[max_derivative_idx]
        intercept = sys_inflection - slope * time_inflection
        tangent_line = slope * time + intercept

        # Find L (delay) and T (time constant)
        # L is the time until the tangent crosses the y=0 axis
        L = -intercept / slope
        # T is the time the tangent takes to go from y=0 to y=K
        T = k / slope

        # L adjusted by the step time
        L_adjusted = L - step_time
        
        type_sintony_code = type_sintony

        if type_sintony_code == 0:  # P
            Kp = T / L_adjusted
            Ki = 0
            Kd = 0
        elif type_sintony_code == 1: # PI
            Kp = 0.9 * (T / L_adjusted)
            Ti = L_adjusted / 0.3
            Ki = Kp / Ti
            Kd = 0
        else: # PID
            Kp = 1.2 * (T / L_adjusted)
            Ti = 2 * L_adjusted
            Ki = Kp / Ti
            Td = 0.5 * L_adjusted
            Kd = Kp * Td
        
        print(f"Gains: Kp={Kp:.4f}, Ki={Ki:.4f}, Kd={Kd:.4f}")

        gain_normalized = np.where(time < step_time, 0, k)
        
        return Kp, Ki, Kd, tangent_line, system_value_normalized, gain_normalized

    def get_max_derivative_idx(self, time, system_value, step_time, window_size=11, polyorder=2):
        time = np.array(time)
        system_value = np.array(system_value)
        system_value_smooth = savgol_filter(system_value, window_size, polyorder)
        derivative = np.gradient(system_value_smooth, time)
        
        valid_indices = time >= step_time
        derivative_valid = derivative[valid_indices]
        
        if len(derivative_valid) == 0:
            # Return 0 if no data is available after the step
            return 0, derivative

        max_derivative_local_idx = np.argmax(np.abs(derivative_valid))
        max_derivative_idx = np.where(valid_indices)[0][max_derivative_local_idx]
        
        return max_derivative_idx, derivative