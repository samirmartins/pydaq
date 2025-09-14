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

        # Initialize plot related attributes
        self.fig = None
        self.ax = None
        self.line = None
        self.line2 = None
        
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

    def _start_updatable_plot(self, title_str="Data Acquisition"): # Removed has_filter_line as _update_plot handles it
        """
        Method to start an updatable plot.
        Initializes matplotlib figure and axes. Lines are drawn by _update_plot.
        """
        # Changing Matplotlib backend if necessary
        # This can sometimes cause issues if called multiple times or with different backends
        # It's often best to set this once at the very beginning of the script if possible.
        # mpl.use("Qt5Agg") 

        # create the figure and axes objects
        self.fig, self.ax = plt.subplots()
        self.fig._label = "iter_plot"  # Defining label

        # Iteractive plot on
        plt.ion()

        # Title and labels and plot creation
        self.ax.set_title(title_str) # Use passed title
        self.ax.set_xlabel("Time (s)") # Adjusted label for general use
        self.ax.set_ylabel("Amplitude") # Adjusted label for general use
        self.ax.grid(True)
        
        # Show non-blocking
        plt.show(block=False)

    def _update_plot(self, x_values, y1_values, y2_values=None, y1_label="Original Data", y2_label="Filtered Data"):
        """
        Method to update plot by clearing and redrawing all points up to current moment.
        """
        if self.fig is None or self.ax is None:
            warnings.warn("Plot not initialized. Call _start_updatable_plot first.")
            return

        self.ax.clear() # Clear all artists from the axes

        # Set title, labels, and grid again after clearing (matplotlib quirk)
        self.ax.set_title(self.title if hasattr(self, 'title') and self.title else "Data Acquisition")
        self.ax.set_xlabel("Time (s)") # Ensure labels are set again after clear
        self.ax.set_ylabel("Amplitude") # Ensure labels are set again after clear
        self.ax.grid(True)
        
        # Plot original data (always)
        # Using marker='o' and linestyle='-' separately for 'o-' style
        self.ax.plot(x_values, y1_values, color="blue", marker='o', linestyle='-', label=y1_label)
        
        # Plot filtered data if provided
        if y2_values is not None:
            self.ax.plot(x_values, y2_values, color="red", marker='o', linestyle='-', label=y2_label)
        
        self.ax.relim() # Recalculate limits
        self.ax.autoscale_view() # Autoscale axes

        self.ax.legend() # Update legend to reflect current plots

        self.fig.canvas.draw()
        self.fig.canvas.flush_events()

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
        
    def _save_data(self, data, name):
        """Method to save data in self.path with name"""

        try:

            os.makedirs(self.path, exist_ok=True)

            # Safely join the path components for cross-platform compatibility
            full_path = os.path.join(self.path, name)
            
            with open(full_path, "w") as file:
                for d in data:
                    file.write(str(d) + "\n")        

        except OSError as e:
            warnings.warn(f"Error saving data to {full_path}: {e}")

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
