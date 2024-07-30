import os
import time
import warnings

import matplotlib.pyplot as plt
import nidaqmx
from nidaqmx.constants import TerminalConfiguration
import numpy as np
import serial
import serial.tools.list_ports
from pydaq.utils.base import Base


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
        self.time_var = []

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
        self.ard_vpb = (self.ard_ai_max - self.ard_ai_min) / (2 ** self.arduino_ai_bits)

    def get_data_nidaq(self):
        """
            This function can be used for data acquisition and step response experiments using Python + NIDAQ boards.

        :example:
            get_data_nidaq()
        """

        # Cleaning data array
        self.data = []
        self.time_var = []

        # Checking if path was defined
        self._check_path()

        # Number of self.cycles necessary
        self.cycles = int(np.floor(self.session_duration / self.ts)) + 1

        # Initializing device, with channel defined
        task = nidaqmx.Task()
        task.ai_channels.add_ai_voltage_chan(
            self.device + "/" + self.channel, terminal_config=self.terminal
        )

        if self.plot:  # If plot, start updatable plot
            self.title = f"PYDAQ - Data Acquisition. {self.device}, {self.channel}"
            self._start_updatable_plot()

        # Main loop, where data will be acquired
        for k in range(self.cycles):

            # Counting time to append data and update interface
            st = time.time()

            # Acquire data
            temp = task.read()

            # Queue data in a list
            self.data.append(temp)
            self.time_var.append(k * self.ts)

            if self.plot:

                # Checking if there is still an open figure. If not, stop the
                # for loop.
                try:
                    plt.get_figlabels().index("iter_plot")
                except BaseException:
                    break

                # Updating data values
                self._update_plot(self.time_var, self.data)

            print(f"Iteration: {k} of {self.cycles - 1}")

            # Getting end time
            et = time.time()

            # Wait for (ts - delta_time) seconds
            try:
                time.sleep(self.ts + (st - et))
            except BaseException:
                warnings.warn(
                    "Time spent to append data and update interface was greater than ts. "
                    "You CANNOT trust time.dat"
                )

        # Closing task
        task.close()

        # Check if data will or not be saved, and save accordingly
        if self.save:
            print("\nSaving data ...")
            # Saving time_var and data
            self._save_data(self.time_var, "time.dat")
            self._save_data(self.data, "data.dat")
            print("\nData saved ...")

        return

    def get_data_arduino(self):
        """
            This function can be used for data acquisition and step response experiments using Python + Arduino
            through serial communication

        :example:
            get_data_arduino()
        """

        # Cleaning data array
        self.data = []
        self.time_var = []

        # Check if path was defined
        self._check_path()

        # Number of self.cycles necessary
        self.cycles = int(np.floor(self.session_duration / self.ts)) + 1

        # Oppening ports
        self._open_serial()

        if self.plot:  # If plot, start updatable plot
            self.title = f"PYDAQ - Data Acquisition. Arduino, Port: {self.com_port}"
            self._start_updatable_plot()

        time.sleep(2)  # Wait for Arduino and Serial to start up

        # Main loop, where data will be acquired
        for k in range(self.cycles):

            # Counting time to append data and update interface
            st = time.time()

            # Acquire data
            self.ser.reset_input_buffer()  # Reseting serial input buffer
            
            # Get the last complete value
            temp = int(self.ser.read(14).split()[-2].decode("UTF-8")) * self.ard_vpb

            # Queue data in a list
            self.data.append(temp)
            self.time_var.append(k * self.ts)

            if self.plot:

                # Checking if there is still an open figure. If not, stop the
                # for loop.
                try:
                    plt.get_figlabels().index("iter_plot")
                except BaseException:
                    break

                # Updating data values
                self._update_plot(self.time_var, self.data)

            print(f"Iteration: {k} of {self.cycles - 1}")

            # Getting end time
            et = time.time()

            # Wait for (ts - delta_time) seconds
            try:
                time.sleep(self.ts + (st - et))
            except BaseException:
                warnings.warn(
                    "Time spent to append data and update interface was greater than ts. "
                    "You CANNOT trust time.dat"
                )

        # Closing port
        self.ser.close()

        # Check if data will or not be saved, and save accordingly
        if self.save:
            print("\nSaving data ...")
            # Saving time_var and data
            self._save_data(self.time_var, "time.dat")
            self._save_data(self.data, "data.dat")
            print("\nData saved ...")
        return
