import nidaqmx
import time
import matplotlib.pyplot as plt
import matplotlib as mpl
import os
import numpy as np
import warnings
import PySimpleGUI as sg


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
    """

    def __init__(self,
                 data = None,
                 device="Dev1",
                 channel="ao0",
                 ts=0.5,
                 plot=True
                 ):

        self.device = device
        self.channel = channel
        self.ts = ts
        self.plot = plot

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

    def send_data_nidaqmx(self):
        """
            This function can be used to send experimental data  using Python + NIDAQmx boards.

        :example:
            send_data_nidaqmx_gui()
        """

        # Checking if there is data to be sent
        if self.data is None:
            warnings.warn("You must define data that will be sent to the board. Please, re-run the code providing them")
            return

        # Number of cycles necessary
        cycles = len(self.data)

        # Initializing device, with channel defined
        task = nidaqmx.Task()
        task.ao_channels.add_ao_voltage_chan(self.device + '/' + self.channel)

        if self.plot:  # If plot,

            # Changing Matplotlib backend
            mpl.use('Qt5Agg')

            # create the figure and axes objects
            fig, ax = plt.subplots()
            fig._label = 'iter_plot'  # Defining label

            # Run GUI event loop
            plt.ion()

            # Title and labels and plot creation
            plt.title("PYDAQ - Sending Data")
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
        ]

        # For now will only show the name of the file that was chosen
        second_column = [
            [sg.DD(self.device_type, size=(40, 8), enable_events=True, default_value=self.device_type[0], key="-DDDev-")],
            [sg.DD(nidaqmx.system.device.Device(self.device_names[0]).ai_physical_chans.channel_names, enable_events=True,
                   size=(40, 8),
                   default_value=nidaqmx.system.device.Device(self.device_names[0]).ai_physical_chans.channel_names[0],
                   key="-DDChan-")],
            [sg.I("1.0", enable_events=True, key='-TS-', size=(40, 8))],
            [sg.Radio("Yes", "plot_radio", default=True, key='-Plot-'), sg.Radio("No", "plot_radio", default=False)],
            [sg.In(size=(32, 8), enable_events=True, key="-Path-",
                   default_text=os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop')),
             sg.FolderBrowse()],
        ]

        bottom_line = [
            [sg.Button('SEND DATA', key='-Start-', auto_size_button=True)]
        ]

        # ----- Full layout -----
        layout = [
            [sg.Column(first_column),
             sg.VSeparator(),
             sg.Column(second_column)],
            [sg.HSeparator()],
            [sg.Column(bottom_line)]
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
                # Separating variables
                self.ts = float(values['-TS-'])
                self.device = values['-DDChan-'].split('/')[0]
                self.channel = values['-DDChan-'].split('/')[1]
                self.path = values['-Path-']
                self.plot = values['-Plot-']

                # Restarting variables

                # Calling data aquisition function
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


if __name__ == "__main__":
    data = [0, 1, 2, 3, 4, 5, 0, 1, 2, 3, 4, 5, 0, 1, 2, 3, 4, 5, 0, 1, 2, 3, 4, 5]
    s = Send_data(data, device='Dev2')
    s.send_data_nidaqmx_gui()
