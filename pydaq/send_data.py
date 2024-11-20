import os
import time
import warnings

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
        plot=True,
    ):

        super().__init__()
        self.device = device
        self.channel = channel
        self.ts = ts
        self.plot = plot
        self.ao_min = ao_min
        self.ao_max = ao_max

        if type(data) == list:
            self.data = np.array(data)
        else:
            self.data = data

        # Gathering nidaq info
        self._nidaq_info()

        # Time variable
        self.time_var = []

        # Defining default path
        self.path = os.path.join(
            os.path.join(os.path.expanduser("~")), "Desktop", "data.dat"
        )

        # Error flags
        self.error_max, self.error_path = False, False

        # COM ports
        self.com_ports = [i.description for i in serial.tools.list_ports.comports()]
        self.com_port = com  # Default COM port

        # Number of necessary cycles
        self.cycles = None

        # Plot title
        self.title = None

        self.legend = ["Output"]

    def send_data_nidaq(self):
        """
            This function can be used to send experimental data  using Python + NIDAQ boards.

        :example:
            send_data_nidaq()
        """

        # Checking if there is data to be sent
        if self.data is None:
            warnings.warn(
                "You must define data that will be sent to the board. Please, re-run the code providing them"
            )
            return

        # Number of cycles necessary
        self.cycles = len(self.data)

        # Initializing device, with channel defined
        task = nidaqmx.Task()
        task.ao_channels.add_ao_voltage_chan(
            self.device + "/" + self.channel,
            min_val=float(self.ao_min),
            max_val=float(self.ao_max),
        )

        if self.plot:  # If plot, start updatable plot
            self.title = f"PYDAQ - Sending Data. {self.device}, {self.channel}"
            self._start_updatable_plot()

        # Main loop, where data will be sent
        for k in range(self.cycles):

            # Counting time to append data and update interface
            st = time.time()

            # Sending data
            task.write(self.data[k])

            # Queue data in a list
            self.time_var.append(k * self.ts)

            if self.plot:

                # Checking if there is still an open figure. If not, stop the for loop.
                try:
                    plt.get_figlabels().index("iter_plot")
                except:
                    break

                # Updating data values
                self._update_plot(self.time_var, self.data[0 : k + 1])

            print(f"Iteration: {k} of {self.cycles - 1}")

            # Getting end time
            et = time.time()

            # Wait for (ts - delta_time) seconds
            try:
                time.sleep(self.ts + (st - et))
            except:
                warnings.warn(
                    "Time spent to append data and update interface was greater than ts. "
                    "You CANNOT trust time.dat"
                )

        # Closing task
        task.close()

        return

    def send_data_arduino(self):
        """
            This function can be used to send experimental data  using Python +
            Arduino boards (digital output only). If "High", the value should be greather
            than 2.5. Else, "Low"

        :example:
            send_data_arduino()
        """

        # Checking if there is data to be sent
        if self.data is None:
            warnings.warn(
                "You must define data that will be sent to the board. Please, re-run the code providing them"
            )
            return

        # Number of cycles necessary
        self.cycles = len(self.data)

        # Opening ports and serial communication
        self._open_serial()

        # Rearranjing data to be send and also loaded data
        self.data_send = list(self.data).copy()
        self.data_send = [b"1" if i > 2.5 else b"0" for i in self.data]
        self.data = np.array(self.data)

        if self.plot:  # If plot, start updatable plot
            self.title = f"PYDAQ - Sending Data. Arduino, Port: {self.com_port}"
            self._start_updatable_plot()

        time.sleep(2)  # Wait for Arduino and Serial to start up
        print(self.cycles)
        # Main loop, where data will be sent
        for k in range(self.cycles):

            # Counting time to append data and update interface
            st = time.time()

            # Sending data
            self.ser.reset_input_buffer()  # Reseting serial input buffer
            self.ser.write(self.data_send[k])

            # Queue data in a list
            self.time_var.append(k * self.ts)

            if self.plot:

                # Checking if there is still an open figure. If not, stop the for loop.
                try:
                    plt.get_figlabels().index("iter_plot")
                except:
                    break

                # Updating data values
                self._update_plot(self.time_var, self.data[0 : k + 1])

            print(f"Iteration: {k} of {self.cycles - 1}")

            # Getting end time
            et = time.time()

            # Wait for (ts - delta_time) seconds
            try:
                time.sleep(self.ts + (st - et))
            except:
                warnings.warn(
                    "Time spent to append data and update interface was greater than ts. "
                    "You CANNOT trust time.dat"
                )

        # Turning off the output
        self.ser.write(b"0")
        # Closing port
        self.ser.close()
        return
