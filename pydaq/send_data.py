import nidaqmx
import time
import matplotlib.pyplot as plt
import matplotlib as mpl
import os
import numpy as np
import warnings
import PySimpleGUI as sg
from pydaq.utils.error_window import error_window
from pydaq.utils.max_error import max_error
import serial
import serial.tools.list_ports

class Send_data:
    """
        Class able to send data from data acquisition boards using (or not) a graphical user interface (GUI)

        :author: Samir Angelo Milani Martins
             - https://www.samirmartins.com.br
             - https://www.github.com/samirmartins/

        :params:
            data: data array (list or np.array) that will be sent to the board
            device: nidaqmx device from where data will be colected. Example: "Dev1"
            channel: channel from where data will be acquired. Example: ao0
            ts: sample period, in seconds.
            plot: if True, plot data iteractively as they are acquired
            ao_min: minimum allowed analog output value
            ao_max: maximum allowed analog output value
    """

    def __init__(self,
                 data = None,
                 device="Dev1",
                 channel="ao0",
                 ts=0.5,
                 plot=True,
                 ao_min = 0,
                 ao_max = 5
                 ):

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

        # Getting all available devices
        self.device_names = []
        self.device_categories = []
        self.device_type = []
        self.local_system = nidaqmx.system.System.local()

        for device in self.local_system.devices:
            self.device_names.append(device.name)
            self.device_categories.append(device.product_category)
            self.device_type.append(device.product_type)

        # Time variable
        self.time_var = []

        # Defining default path
        self.path = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop', 'data.dat')

        # Error flags
        self.error_max, self.error_path = False, False

        # COM ports
        self.com_ports = [i.description for i in serial.tools.list_ports.comports()]


    def send_data_nidaqmx(self):
        """
            This function can be used to send experimental data  using Python + NIDAQmx boards.

        :example:
            send_data_nidaqmx()
        """

        # Checking if there is data to be sent
        if self.data is None:
            warnings.warn("You must define data that will be sent to the board. Please, re-run the code providing them")
            return

        # Number of cycles necessary
        cycles = len(self.data)

        # Initializing device, with channel defined
        task = nidaqmx.Task()
        task.ao_channels.add_ao_voltage_chan(self.device + '/' + self.channel, min_val = float(self.ao_min), max_val = float(self.ao_max))

        if self.plot:  # If plot,

            # Changing Matplotlib backend
            mpl.use('Qt5Agg')

            # create the figure and axes objects
            fig, ax = plt.subplots()
            fig._label = 'iter_plot'  # Defining label

            # Run GUI event loop
            plt.ion()

            # Title and labels and plot creation
            plt.xlabel("Time (seconds)")
            plt.ylabel("Voltage")
            plt.grid()
            line, = ax.plot(self.time_var, [])
            plt.show()

        # Main loop, where data will be sent
        for k in range(cycles):

            # Sending data
            task.write(self.data[k])

            # Counting time to append data and update interface
            st = time.time()

            # Queue data in a list
            plt.title(f'PYDAQ - Sending Data. {self.device}, {self.channel}')
            self.time_var.append(k * self.ts)

            if self.plot:

                # Checking if there is still an open figure. If not, stop the for loop.
                try:
                    plt.get_figlabels().index('iter_plot')
                except:
                    break

                # Updating data values
                line.set_xdata(self.time_var)
                line.set_ydata(self.data[0:k + 1])
                fig.canvas.draw()
                fig.canvas.flush_events()
                ax.set_xlim([0, 1.1 * len(self.data) * self.ts])
                ax.set_ylim([-1.1 * min(abs(self.data)), 1.1 * max(abs(self.data))])

            print(f'Iteration: {k} of {cycles-1}')

            # Getting end time
            et = time.time()

            # Wait for (ts - delta_time) seconds
            try:
                time.sleep(self.ts + (st - et))
            except:
                warnings.warn("Time spent to append data and update interface was greater than ts. "
                              "You CANNOT trust time.dat")

        # Closing task
        task.close()

    def send_data_nidaqmx_gui(self):
        """
        This functions provides a Graphical User Interface (GUI) that allows one to send data
        from a .dat file to a National Instruments acquisition boards.

        :example:
            send_data_nidaqmx_gui()

        """

        # Theme
        sg.theme('Dark')

        # First the window layout in 2 columns
        first_column = [
            [sg.Text('Choose device: ')],
            [sg.Text('Choose channel: ')],
            [sg.Text("Sample period (s)")],
            [sg.Text('Plot data?')],
            [sg.Text("Data")],
            [sg.Text("Output range (V)")],
        ]

        # For now will only show the name of the file that was chosen
        try:
            chan = nidaqmx.system.device.Device(self.device_names[0]).ao_physical_chans.channel_names
            defchan = nidaqmx.system.device.Device(self.device_names[0]).ao_physical_chans.channel_names[0]
        except:
            chan = ''
            defchan = 'There is no analog output in this board'

        second_column = [
            [sg.DD(self.device_type, size=(40, 1), enable_events=True, default_value=self.device_type[0], key="-DDDev-")],
            [sg.DD(chan, enable_events=True, size=(40, 1),default_value=defchan, key="-DDChan-")],
            [sg.I("1.0", enable_events=True, key='-TS-', size=(40, 1))],
            [sg.Radio("Yes", "plot_radio", default=True, key='-Plot-'), sg.Radio("No", "plot_radio", default=False)],
            [sg.In(size=(32, 1), enable_events=True, key="-Path-",
                   default_text=self.path),
             sg.FileBrowse()],
            [sg.Text("Minimum"), sg.In(default_text=self.ao_min, size = (10,1), enable_events=True, key = '-ao_min-'), sg.VSeparator(), sg.Text("Maximum"), sg.In(default_text=self.ao_max, size = (10,1), enable_events=True, key = '-ao_max-')]
        ]

        bottom_line = [
            [sg.Button('SEND DATA', key='-Start-', auto_size_button=True)]
        ]

        # ----- Full layout -----
        layout = [
            [sg.Column(first_column, vertical_alignment='top'),
             sg.VSeparator(),
             sg.Column(second_column, vertical_alignment='center')],
            [sg.HSeparator()],
            [sg.Column(bottom_line, vertical_alignment='center')]
        ]

        window = sg.Window("PYDAQ - Sending data", layout, resizable=False, finalize=True, element_justification="center",
                           font="Helvetica")

        # Event Loop
        while True:

            event, values = window.read()

            if event == sg.WIN_CLOSED:
                break

            # Start
            if event == '-Start-':

                self.ao_max = values['-ao_max-']
                self.ao_min = values['-ao_min-']

                # Reading data from defined path
                self.path = values['-Path-']
                self.data = np.loadtxt(self.path)

                # Check if max(data) < self.ao_max
                if max(self.data) > float(self.ao_max):
                    max_error()
                    self.error_max = True
                else:
                    self.error_max = False

                try:
                    # Separating variables
                    self.ts = float(values['-TS-'])
                    self.device = values['-DDChan-'].split('/')[0]
                    self.channel = values['-DDChan-'].split('/')[1]
                    self.plot = values['-Plot-']
                    self.error_path = False

                except:
                    error_window()
                    self.error_path = True

                # Calling send data method
                if not self.error_max and not self.error_path:
                    self.send_data_nidaqmx()

            # Changing availables channels if device changes
            if event == "-DDDev-":
                # Discovering new ao channels
                new_ao_channels = nidaqmx.system.device.Device(
                    self.device_names[self.device_type.index(values['-DDDev-'])]).ao_physical_chans.channel_names
                # Default channel
                try:
                    default_channel = new_ao_channels[0]
                except:
                    default_channel = 'There is no analog output in this board'

                # Rewriting new ai channels into the right place
                window['-DDChan-'].update(default_channel, new_ao_channels)

        window.close()

        return

    def send_data_arduino(self, COM):
        """
            This function can be used to send experimental data  using Python +
            Arduino boards (digital output only). If "High", the value should be greather
            than 2.5. Else, "Low"

        :example:
            send_data_arduino()
        """

        # Checking if there is data to be sent
        if self.data is None:
            warnings.warn("You must define data that will be sent to the board. Please, re-run the code providing them")
            return

        # Number of cycles necessary
        cycles = len(self.data)

        # Opening ports and serial communication
        ser = serial.Serial()
        ser.dtr = True
        ser.baudrate = (9600)
        ser.port = COM # Definind port

        if not ser.isOpen():# Open port if not openned
            ser.open() # Opening port

        # Rearranjing data to be send and also loaded data
        self.data_send = list(self.data).copy()
        self.data_send = [b'1' if i>2.5 else b'0' for i in self.data]
        self.data = np.array(self.data)

        if self.plot:  # If plot,

            # Changing Matplotlib backend
            mpl.use('Qt5Agg')

            # create the figure and axes objects
            fig, ax = plt.subplots()
            fig._label = 'iter_plot'  # Defining label

            # Run GUI event loop
            plt.ion()

            # Title and labels and plot creation
            plt.xlabel("Time (seconds)")
            plt.ylabel("Voltage")
            plt.grid()
            line, = ax.plot(self.time_var, [])
            plt.show()

        # Main loop, where data will be sent
        for k in range(cycles):

            # Sending data
            ser.write(self.data_send[k])

            # Counting time to append data and update interface
            st = time.time()

            # Queue data in a list
            plt.title(f'PYDAQ - Sending Data. Arduino, Port: {COM}')
            self.time_var.append(k * self.ts)

            if self.plot:

                # Checking if there is still an open figure. If not, stop the for loop.
                try:
                    plt.get_figlabels().index('iter_plot')
                except:
                    break

                # Updating data values
                line.set_xdata(self.time_var)
                line.set_ydata(self.data[0:k + 1])
                fig.canvas.draw()
                fig.canvas.flush_events()
                ax.set_xlim([0, 1.1 * len(self.data) * self.ts])
                ax.set_ylim([-1.1 * min(abs(self.data)), 1.1 * max(abs(self.data))])

            print(f'Iteration: {k} of {cycles-1}')

            # Getting end time
            et = time.time()

            # Wait for (ts - delta_time) seconds
            try:
                time.sleep(self.ts + (st - et))
            except:
                warnings.warn("Time spent to append data and update interface was greater than ts. "
                              "You CANNOT trust time.dat")

        ser.write(b'0') # Turning off the output
        # Closing port
        ser.close()

    def send_data_arduino_gui(self):
        """
        This functions provides a Graphical User Interface (GUI) that allows one to send data
        from a .dat file to a Arduino Board. Further
        details in send_data_arduino_gui

        :example:
            send_data_arduino_gui()

        """

        # Theme
        sg.theme('Dark')

        # First the window layout in 2 columns
        first_column = [
            [sg.Text('Choose your arduino: ')],
            [sg.Text("Sample period (s)")],
            [sg.Text('Plot data?')],
            [sg.Text("Data")],
        ]

        # For now will only show the name of the file that was chosen
        try:
            chan = nidaqmx.system.device.Device(self.device_names[0]).ao_physical_chans.channel_names
            defchan = nidaqmx.system.device.Device(self.device_names[0]).ao_physical_chans.channel_names[0]
        except:
            chan = ''
            defchan = 'There is no analog output in this board'

        second_column = [
            [sg.DD(self.com_ports, size=(40, 1), enable_events=True, default_value=self.com_ports[0], key="-COM-")],
            [sg.I("1.0", enable_events=True, key='-TS-', size=(40, 1))],
            [sg.Radio("Yes", "plot_radio", default=True, key='-Plot-'), sg.Radio("No", "plot_radio", default=False)],
            [sg.In(size=(32, 1), enable_events=True, key="-Path-",
                   default_text=self.path),
             sg.FileBrowse()]
        ]

        bottom_line = [
            [sg.Button('SEND DATA', key='-Start-', auto_size_button=True)]
        ]

        # ----- Full layout -----
        layout = [
            [sg.Column(first_column, vertical_alignment='top'),
             sg.VSeparator(),
             sg.Column(second_column, vertical_alignment='center')],
            [sg.HSeparator()],
            [sg.Column(bottom_line, vertical_alignment='center')]
        ]

        window = sg.Window("PYDAQ - Sending data", layout, resizable=False, finalize=True, element_justification="center",
                           font="Helvetica")


        # Event Loop
        while True:

            event, values = window.read()

            if event == sg.WIN_CLOSED:
                break

            # Start
            if event == '-Start-':

                # Restarting time and data
                self.time_var, self.data = [], []

                # Reading data from defined path and rearranjing it
                self.path = values['-Path-']
                self.data = np.loadtxt(self.path)
                self.data = list(self.data)
                self.data = [5 if i > 2.5 else 0 for i in self.data]

                try:
                    # Separating variables
                    self.ts = float(values['-TS-'])
                    self.com_port = serial.tools.list_ports.comports()[self.com_ports.index(values['-COM-'])].name
                    self.plot = values['-Plot-']
                    self.error_path = False

                except:
                    error_window()
                    self.error_path = True

                # Calling send data method
                if not self.error_path:
                    self.send_data_arduino(self.com_port)


        window.close()

        return
