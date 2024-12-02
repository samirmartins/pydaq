import os
import matplotlib as mpl
import matplotlib.pyplot as plt
import serial
import serial.tools.list_ports
import nidaqmx
from nidaqmx.constants import TerminalConfiguration
import warnings
from ..guis.error_window_gui import Error_window


class Base:
    """
    Base class for data acquisition and to send data.
    """

    def __init__(self):

        # Terminal configuration Map
        self.term_map = {
            "Diff": TerminalConfiguration.DIFF,
            "RSE": TerminalConfiguration.RSE,
            "NRSE": TerminalConfiguration.NRSE,
        }

    def _range_error(self):
        """Out of range window"""

        error_w = Error_window()
        error_w.ui.confirm.setText("Out of range value (check step_max and ao_min)!")
        error_w.exec()

    def _check_path(self):
        """Method to check if path was or not defined by the user"""

        # Checking if path was or not defined by the user
        if self.path is None:  # Saving in Desktop if it is not defined
            self.path = os.path.join(os.path.join(os.path.expanduser("~")), "Desktop")

        # Check if able to save data in defined path
        if not os.path.exists(self.path):
            warnings.warn(
                "Defined path does not exists! Please redefine path and run the code again"
            )
            return

    def _open_serial(self):
        """Opening ports for serial communication"""

        self.ser = serial.Serial()
        self.ser.dtr = True
        self.ser.baudrate = 115200
        self.ser.port = self.com_port  # Defining port

        if not self.ser.isOpen():  # Open port if not openned
            self.ser.open()  # Opening port

    def _start_updatable_plot(self):
        """Method to start updatable plot"""

        # Changing Matplotlib backend
        mpl.use("Qt5Agg")

        # create the figure and axes objects
        self.fig, self.ax = plt.subplots()
        self.fig._label = "iter_plot"  # Defining label

        # Iteractive plot on
        plt.ion()

        # Title and labels and plot creation
        plt.title(self.title)
        plt.xlabel("Time (samples)")
        plt.ylabel("Voltage")
        plt.grid()
        self.line = self.ax.plot([], [])
        plt.show()

    def _update_plot(self, x_value, y_value, number_of_inputs=1):
        """Method to update plot already started using _start_updatable_plot
        using x_value and y_value as new data"""

        self.ax.clear()
        plt.title(self.title)
        plt.xlabel("Time (samples)")
        plt.ylabel("Voltage")
        plt.grid()
        if number_of_inputs > 1:
            for k in range(number_of_inputs):
                self.ax.plot(x_value[k], y_value[k], "o-")
                plt.legend(self.legend)
        else:
            self.ax.plot(x_value, y_value, "o-")
            plt.legend(self.legend)
        self.fig.canvas.draw()
        self.fig.canvas.flush_events()

    def _save_data(self, data, name):
        """Method to save data in self.path with name"""

        file = open(self.path + "\\" + name, "w")
        for d in data:
            file.write(str(d) + "\n")
        file.close()

    def _nidaq_info(self):
        """Gathering NIDAQ info"""

        # Getting all available devices
        self.device_names = []
        self.device_categories = []
        self.device_type = []
        self.local_system = nidaqmx.system.System.local()

        for device in self.local_system.devices:
            self.device_names.append(device.name)
            self.device_categories.append(device.product_category)
            self.device_type.append(device.product_type)

    def adjust_string(label_string):
        spaced_string = " ".join(label_string.split("_"))
        return spaced_string.capitalize()

    def get_acronym(string):
        if string == "R2 score":
            return "R2S"
        else:
            oupt = string[0]

            for i in range(1, len(string)):
                if string[i - 1] == " ":
                    oupt += string[i]
            return oupt.upper()
