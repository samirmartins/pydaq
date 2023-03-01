import nidaqmx
import time
import matplotlib.pyplot as plt
import matplotlib as mpl
import os
import numpy as np
import warnings
import PySimpleGUI as sg
import os.path


class Get_data:
    """
        Class able to get data from data acquisition boards using (or not) a graphical user interface (GUI)

        :author: Samir Angelo Milani Martins
             - https://www.samirmartins.com.br
             - https://www.github.com/samirmartins/

        :param:
            device: nidaqmx device from where data will be colected. Example: "Dev1"
            channel: channel from where data will be acquired. Example: ai0
            ts: sample period, in seconds.
            session_duration: session duration, in seconds.
            save: if True, saves data in path defined by path.
            path: where data will be saved.
            plot: if True, plot data iteractively as they are acquired
    """

    def __init__(self,
                 device="Dev1",
                 channel="ai0",
                 ts=0.5,
                 session_duration=10.0,
                 save=True,
                 path=None,
                 plot=True
                 ):

        self.device = device
        self.channel = channel
        self.ts = ts
        self.session_duration = session_duration
        self.save = save
        self.path = path
        self.plot = plot

        # Initializing variables
        self.data = []
        self.time_var = []

        # Getting all available devices
        self.device_names = []
        self.device_categories = []
        self.device_type = []
        self.local_system = nidaqmx.system.System.local()

        for device in self.local_system.devices:
            self.device_names.append(device.name)
            self.device_categories.append(device.product_category)
            self.device_type.append(device.product_type)

    def get_data_nidaqmx(self):
        """
            This function can be used for data acquisition and step response experiments using Python + NIDAQmx boards.

        :example:
            get_data_nidaqmx_gui()
        """

        # Checking if path were or not defined by the user
        if self.path is None:  # Saving in Desktop if it is not defined
            self.path = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop')

        # Check if able to save data in defined path
        if not os.path.exists(self.path):
            warnings.warn('Defined path does not exists! Please redefine path and run the code again')
            return

        # Number of cycles necessary
        cycles = int(np.floor(self.session_duration / self.ts))+1

        # Initializing device, with channel defined
        task = nidaqmx.Task()
        task.ai_channels.add_ai_voltage_chan(self.device + '/' + self.channel)

        if self.plot:  # If plot,

            # Changing Matplotlib backend
            mpl.use('Qt5Agg')

            # create the figure and axes objects
            fig, ax = plt.subplots()
            fig._label = 'iter_plot'  # Defining label

            # Run GUI event loop
            plt.ion()

            # Title and labels and plot creation
            plt.title("PYDAQ - Data Acquisition")
            plt.xlabel("Time (seconds)")
            plt.ylabel("Voltage")
            plt.grid()
            line, = ax.plot(self.time_var, self.data)
            plt.show()

        # Main loop, where data will be acquired
        for k in range(cycles):

            # Acquire data
            temp = task.read()

            # Counting time to append data and update interface
            st = time.time()

            # Queue data in a list
            self.data.append(temp)
            self.time_var.append(k * self.ts)

            if self.plot:

                # Checking if there is still an open figure. If not, stop the for loop.
                try:
                    plt.get_figlabels().index('iter_plot')
                except:
                    break

                # Updating data values
                line.set_xdata(self.time_var)
                line.set_ydata(self.data)
                fig.canvas.draw()
                fig.canvas.flush_events()
                ax.set_xlim([0, 1.1 * self.session_duration])
                ax.set_ylim([-1.1 * max(np.abs(self.data)), 1.1 * max(np.abs(self.data))])

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

        # Check if data will or not be saved, and save accordingly
        if self.save:

            print('\nSaving data ...')

            # Saving time_var
            file_time = open(self.path + '\\time.dat', 'w')
            for t in self.time_var:
                file_time.write(str(t) + "\n")
            file_time.close()

            # Saving data
            file_data = open(self.path + '\\data.dat', 'w')
            for d in self.data:
                file_data.write(str(d) + "\n")
            file_data.close()

            print('\nData saved ...')

        return

    def get_data_nidaqmx_gui(self):
        """
        This functions provides a Graphical User Interface (GUI) that allows one to get data
        from National Instruments acquisition boards.

        :example:
            get_data_nidaqmx_gui()

        """

        # Theme
        sg.theme('Dark')

        # First the window layout in 2 columns
        first_column = [
            [sg.Text('Choose device: ')],
            [sg.Text('Choose channel: ')],
            [sg.Text("Sample period (s)")],
            [sg.Text("Session duration (s)")],
            [sg.Text('Plot data?')],
            [sg.Text('Save data?')],
            [sg.Text("Path")],
        ]

        # For now will only show the name of the file that was chosen
        try:
            chan = nidaqmx.system.device.Device(self.device_names[0]).ai_physical_chans.channel_names
            defchan = nidaqmx.system.device.Device(self.device_names[0]).ai_physical_chans.channel_names[0]
        except:
            chan = ''
            defchan = ''

        # For now will only show the name of the file that was chosen
        second_column = [
            [sg.DD(self.device_type, size=(40, 8), enable_events=True, default_value=self.device_type[0], key="-DDDev-")],
            [sg.DD(chan, enable_events=True, size=(40, 8), default_value=defchan,
                   key="-DDChan-")],
            [sg.I("1.0", enable_events=True, key='-TS-', size=(40, 8))],
            [sg.I("10.0", enable_events=True, key='-SD-', size=(40, 8))],
            [sg.Radio("Yes", "plot_radio", default=True, key='-Plot-'), sg.Radio("No", "plot_radio", default=False)],
            [sg.Radio("Yes", "save_radio", default=True, key='-Save-'), sg.Radio("No", "save_radio", default=False)],
            [sg.In(size=(32, 8), enable_events=True, key="-Path-",
                   default_text=os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop')),
             sg.FolderBrowse()],
        ]

        bottom_line = [
            [sg.Button('GET DATA', key='-Start-', auto_size_button=True)]
        ]

        # ----- Full layout -----
        layout = [
            [sg.Column(first_column),
             sg.VSeparator(),
             sg.Column(second_column)],
            [sg.HSeparator()],
            [sg.Column(bottom_line)]
        ]

        window = sg.Window("PYDAQ - Data Acquisition", layout, resizable=False, finalize=True, element_justification="center",
                           font="Helvetica")

        # Event Loop
        while True:

            event, values = window.read()

            if event == sg.WIN_CLOSED:
                break

            # Start
            if event == '-Start-':
                # Separating variables
                self.ts = float(values['-TS-'])
                self.session_duration = float(values['-SD-'])
                self.device = values['-DDChan-'].split('/')[0]
                self.channel = values['-DDChan-'].split('/')[1]
                self.save = values['-Save-']
                self.path = values['-Path-']
                self.plot = values['-Plot-']

                # Restarting variables
                self.data = []
                self.time_var = []

                # Calling data aquisition method
                self.get_data_nidaqmx()

            # Changing availables channels if device changes
            if event == "-DDDev-":
                # Discovering new ai channels
                new_ai_channels = nidaqmx.system.device.Device(
                    self.device_names[self.device_type.index(values['-DDDev-'])]).ai_physical_chans.channel_names
                # Default channel
                try:
                    default_channel = new_ai_channels[0]
                except:
                    default_channel = 'There is no analog input in this board'

                # Rewriting new ai channels into the right place
                window['-DDChan-'].update(default_channel, new_ai_channels)

        window.close()

        return
