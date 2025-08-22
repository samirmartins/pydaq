import os
import time
import warnings
import threading
import queue

import matplotlib.pyplot as plt
import nidaqmx
import numpy as np
import serial
import serial.tools.list_ports
from pydaq.utils.base import Base


class SendData(Base):
    """
    Class able to send data from data acquisition boards using (or not) a graphical user interface (GUI)

    :author: Samir Angelo Milani Martins
         - https://www.samirmartins.com.br
         - https://www.github.com/samirmartins/

    :params:
        data: data array (list or np.array) that will be sent to the board
        device: nidaq device from where data will be colected. Example: "Dev1"
        channel: channel from where data will be acquired. Example: ao0
        com: arduino COM port. Example: 'COM1'
        ts: sample period, in seconds.
        ao_min: minimum allowed analog output value
        ao_max: maximum allowed analog output value
        plot: if True, plot data iteractively as they are acquired
    """

    def __init__(
        self,
        data=None,
        device="Dev1",
        channel="ao0",
        com="COM1",
        ts=0.5,
        ao_min=0,
        ao_max=5,
        plot_mode="no", # Options: "realtime", "end", "no"
    ):

        super().__init__()
        self.device = device
        self.channel = channel
        self.ts = ts
        self.plot_mode = plot_mode
        self.ao_min = ao_min
        self.ao_max = ao_max

        if data is not None and type(data) == list:
            self.data = np.array(data)
        else:
            self.data = data

        # Gathering nidaq info
        self._nidaq_info()

        # Time variable for plotting progress
        self.time_var = []
        # History of sent data for plotting
        self.sent_data_history = []

        # Defining default path
        self.path = os.path.join(
            os.path.join(os.path.expanduser("~")), "Desktop", "data.dat"
        )

        # COM ports
        self.com_ports = [i.description for i in serial.tools.list_ports.comports()]
        self.com_port = com

        # Plot title and legend
        self.title = None
        self.legend = ["Output"]

        # Threading control
        self.sending_running = False
        self.plot_closed_by_user = False
        self.plot_ready_event = threading.Event()

    # Handler for plot window closure
    def _on_plot_close(self, event):
        """..."""
        print("Plot window closed by user. Halting data sending...")
        self.sending_running = False
        self.plot_closed_by_user = True

    def _send_data_worker_nidaq(self, progress_queue):
        self.plot_ready_event.wait() # Wait for plot to be ready

        try:
            task.ao_channels.add_ao_voltage_chan(
                f"{self.device}/{self.channel}",
                min_val=float(self.ao_min),
                max_val=float(self.ao_max),
            )

            cycles = len(self.data)
            
            st_worker = time.perf_counter()
            task = nidaqmx.Task()
            
            for k in range(cycles):
                if not self.sending_running:
                    break

                current_value = self.data[k]
                task.write(current_value)
                
                time_now = time.perf_counter() - st_worker
                
                # Put progress on the queue for the main thread to plot
                progress_queue.put((time_now, current_value))

                wait_time = (st_worker + (k + 1) * self.ts) - time.perf_counter()
                if wait_time > 0:
                    time.sleep(wait_time)
        finally:
            task.write(0) # Ensure output is zeroed at the end
            task.close()
            progress_queue.put(None) # Signal end of sending

    def send_data_nidaq(self):
        """
            This function can be used to send experimental data  using Python + NIDAQ boards.

        :example:
            send_data_nidaq()
        """

        if self.data is None:
            warnings.warn("You must define data to be sent.")
            return

        self.time_var, self.sent_data_history = [], []
        progress_queue = queue.Queue()
        self.sending_running = True
        self.plot_closed_by_user = False
        self.plot_ready_event.clear()

        sending_thread = threading.Thread(
            target=self._send_data_worker_nidaq,
            args=(progress_queue,),
            daemon=True
        )
        sending_thread.start()

        if self.plot_mode == 'realtime':
            self.title = f"PYDAQ - Sending Data. {self.device}, {self.channel}"
            self._start_updatable_plot(title_str=self.title)
            self.fig.canvas.mpl_connect('close_event', self._on_plot_close)

            # Add a short delay to allow the plot window to open fully
            print("\nReal-time plot started. Waiting 0.5s for the window to render...")
            time.sleep(0.5)

            self.plot_ready_event.set()
        else:
            self.plot_ready_event.set()

        # Control variables for periodic plot update
        if self.ts >= 0.05:
            plot_update_interval = 0.05
        else:
            plot_update_interval = 0.25
            
        last_plot_time = time.perf_counter()

        # Main loop to consume progress and update plot
        while (self.sending_running and not self.plot_closed_by_user) or not progress_queue.empty():
            try:
                item = progress_queue.get(timeout=0.01)

                if item is None:
                    self.sending_running = False
                    # Drain the queue to ensure all data is processed
                    while not progress_queue.empty():
                        remaining_item = progress_queue.get_nowait()
                        if remaining_item:
                            timestamp, sent_value = remaining_item
                            self.time_var.append(timestamp)
                            self.sent_data_history.append(sent_value)
                    break

                timestamp, sent_value = item
                self.time_var.append(timestamp)
                self.sent_data_history.append(sent_value)

                now = time.perf_counter()
                # Improved plot condition to ensure the final frame is drawn
                if self.plot_mode == 'realtime' and (now - last_plot_time >= plot_update_interval or not self.sending_running):
                    self._update_plot(self.time_var, self.sent_data_history, y1_label="Sent Data")
                    last_plot_time = now
            
            except queue.Empty:
                time.sleep(0.01)
                if not self.sending_running and progress_queue.empty():
                    break

        sending_thread.join()

        # Plotting at the end logic remains the same
        if self.plot_mode == 'end' and self.sent_data_history:
            self.title = f"PYDAQ - Final Sent Data (NIDAQ)"
            self._start_updatable_plot(title_str=self.title)
            # Use the actual sent data history for the final plot
            self._update_plot(self.time_var, self.sent_data_history, y1_label="Sent Data")
            plt.show(block=True)
            
        if self.plot_mode == 'realtime' and not self.plot_closed_by_user:
            print("\nPlot remains open. Close window manually to exit.")
            plt.show(block=True)

        return

    def _send_data_worker_arduino(self, progress_queue):
        self.plot_ready_event.wait()
        
        # This logic is specific to sending digital signals based on a voltage threshold
        data_to_send = [b"1" if i > 2.5 else b"0" for i in self.data]
        cycles = len(data_to_send)

        try:
            self._open_serial()
            time.sleep(0.5) # Wait for serial to settle
            
            st_worker = time.perf_counter()

            for k in range(cycles):
                if not self.sending_running:
                    break
                
                self.ser.write(data_to_send[k])
                
                time_now = time.perf_counter() - st_worker
                # Send original data value for plotting, not the b'1'/b'0'
                progress_queue.put((time_now, self.data[k]))

                wait_time = (st_worker + (k + 1) * self.ts) - time.perf_counter()
                if wait_time > 0:
                    time.sleep(wait_time)
        
        except serial.SerialException as e:
            warnings.warn(f"Failed to open or use serial port {self.com_port}: {e}")
        finally:
            if hasattr(self, 'ser') and self.ser.is_open:
                self.ser.write(b"0")
                self.ser.close()
            progress_queue.put(None)

    def send_data_arduino(self):
        """
            This function can be used to send experimental data  using Python +
            Arduino boards (digital output only). If "High", the value should be greather
            than 2.5. Else, "Low"

        :example:
            send_data_arduino()
        """
        if self.data is None:
            warnings.warn("You must define data to be sent.")
            return

        self.time_var, self.sent_data_history = [], []
        progress_queue = queue.Queue()
        self.sending_running = True
        self.plot_closed_by_user = False
        self.plot_ready_event.clear()

        sending_thread = threading.Thread(
            target=self._send_data_worker_arduino,
            args=(progress_queue,),
            daemon=True
        )
        sending_thread.start()

        if self.plot_mode == 'realtime':
            self.title = f"PYDAQ - Sending Data. Arduino, Port: {self.com_port}"
            self._start_updatable_plot(title_str=self.title)
            self.fig.canvas.mpl_connect('close_event', self._on_plot_close)

            # Add a short delay to allow the plot window to open fully
            print("\nReal-time plot started. Waiting 0.5s for the window to render...")
            time.sleep(0.5)

            self.plot_ready_event.set()
        else:
            self.plot_ready_event.set()

        # Control variables for periodic plot update
        if self.ts >= 0.05:
            plot_update_interval = 0.05
        else:
            plot_update_interval = 0.25

        last_plot_time = time.perf_counter()

        # Main loop to consume progress and update plot
        while (self.sending_running and not self.plot_closed_by_user) or not progress_queue.empty():
            try:
                item = progress_queue.get(timeout=0.01)

                if item is None:
                    self.sending_running = False
                    # Drain the queue to ensure all data is processed
                    while not progress_queue.empty():
                        remaining_item = progress_queue.get_nowait()
                        if remaining_item:
                            timestamp, sent_value = remaining_item
                            self.time_var.append(timestamp)
                            self.sent_data_history.append(sent_value)
                    break
                
                timestamp, sent_value = item
                self.time_var.append(timestamp)
                self.sent_data_history.append(sent_value)

                now = time.perf_counter()
                # Improved plot condition to ensure the final frame is drawn
                if self.plot_mode == 'realtime' and (now - last_plot_time >= plot_update_interval or not self.sending_running):
                    self._update_plot(self.time_var, self.sent_data_history, y1_label="Sent Data")
                    last_plot_time = now
            
            except queue.Empty:
                time.sleep(0.01)
                if not self.sending_running and progress_queue.empty():
                    break

        sending_thread.join()

        if self.plot_mode == 'end' and self.sent_data_history:
            self.title = f"PYDAQ - Final Sent Data (Arduino)"
            self._start_updatable_plot(title_str=self.title)
            # Use the actual sent data history for the final plot
            self._update_plot(self.time_var, self.sent_data_history, y1_label="Sent Data")
            plt.show(block=True)
        
        if self.plot_mode == 'realtime' and not self.plot_closed_by_user:
            print("\nPlot remains open. Close window manually to exit.")
            plt.show(block=True)
            
        return