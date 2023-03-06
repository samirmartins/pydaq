import os
import time
import numpy as np
import PySimpleGUI as sg
import serial
import serial.tools.list_ports
from pydaq.utils.base import Base
import os
import serial
import serial.tools.list_ports
from pydaq.utils.base import Base
import matplotlib.pyplot as plt
import warnings
import nidaqmx

class Step_response(Base):
    """
        Class developed to construct Graphical User Interface for step
        response using arduino and NIDAQ boards

       :author: Samir Angelo Milani Martins
             - https://www.samirmartins.com.br
             - https://www.github.com/samirmartins/

        :params:
            ts: sample period, in seconds.
            session_duration: session duration, in seconds.
            step_time: time when step will be applied, in seconds
            plot: if True, plot data iteractively as they are sent/acquired
            device: nidaq default device.
            channel: nidaq default channel
            ao_min: minimum allowed analog output value
            ao_max: maximum allowed analog output value


    """

    def __init__(self, ts=0.5, session_duration=10.0, step_time=3.0, plot=True, device = "Dev1", ao_channel = "ao0", ai_channel = "ai0", ao_min = 0, ao_max = 5, ai_min = 0, ai_max = 5):



        super().__init__()
        self.ts = ts
        self.session_duration = session_duration
        self.plot = plot
        self.step_time = step_time
        self.device = device
        self.ai_channel = ai_channel
        self.ao_channel = ao_channel
        self.ao_min = ao_min
        self.ao_max = ao_max
        self.ai_min = ai_min
        self.ai_max = ai_max


        # COM ports
        self.com_ports = [i.description for i in serial.tools.list_ports.comports()]
        self.com_port = self.com_ports[0]  # Default COM port

        # Initializing variables
        self.time_var, self.input, self.output = [], [], []

        # Plot title
        self.title = None

        # Getting all available devices
        self.device_names = []
        self.device_categories = []
        self.device_type = []
        self.local_system = nidaqmx.system.System.local()

        for device in self.local_system.devices:
            self.device_names.append(device.name)
            self.device_categories.append(device.product_category)
            self.device_type.append(device.product_type)

        # Defining default path
        self.path = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop')

        # Gathering nidaq info
        self._nidaq_info()

        # Arduino ADC resolution (in bits)
        self.arduino_ai_bits = 10

        # Arduino analog input max and min
        self.ard_ao_max, self.ard_ao_min = 5,0

        # Value per bit
        self.ard_vpb = (self.ard_ao_max - self.ard_ao_min)/(2**self.arduino_ai_bits)

    def step_response_arduino_gui(self):
        """
        This functions provides a Graphical User Interface (GUI) that allows one to
        perform a step_response with Arduino boards.

        :example:
            step_response_arduino()

        """

        # Theme
        sg.theme('Dark')

        # First the window layout in 2 columns
        first_column = [
            [sg.Text('Choose your arduino: ')],
            [sg.Text("Sample period (s)")],
            [sg.Text("Session duration (s)")],
            [sg.Text("Step ON (s)")],
            [sg.Text('Plot data?')],
            [sg.Text('Save data?')],
            [sg.Text("Path")],
        ]

        # Second column
        second_column = [
            [sg.DD(self.com_ports, size=(40, 1), enable_events=True, default_value=self.com_ports[-1], key="-COM-")],
            [sg.I(self.ts, enable_events=True, key='-TS-', size=(40, 1))],
            [sg.I(self.session_duration, enable_events=True, key='-SD-', size=(40, 1))],
            [sg.I(self.step_time, enable_events=True, key='-Step-', size=(40, 1))],
            [sg.Radio("Yes", "plot_radio", default=True, key='-Plot-'), sg.Radio("No", "plot_radio", default=False)],
            [sg.Radio("Yes", "save_radio", default=True, key='-Save-'), sg.Radio("No", "save_radio", default=False)],
            [sg.In(size=(32, 1), enable_events=True, key="-Path-",
                   default_text=self.path),
             sg.FolderBrowse()],
        ]

        bottom_line = [
            [sg.Button('STEP RESPONSE', key='-Start-', auto_size_button=True)]
        ]

        # ----- Full layout -----
        layout = [
            [sg.Column(first_column, vertical_alignment='top'),
             sg.VSeparator(),
             sg.Column(second_column, vertical_alignment='center')],
            [sg.HSeparator()],
            [sg.Column(bottom_line, vertical_alignment='center')]
        ]

        window = sg.Window("PYDAQ - Step Response (Arduino)", layout, resizable=False, finalize=True, element_justification="center",
                           font="Helvetica")

        # Event Loop
        while True:

            event, values = window.read()

            if event == sg.WIN_CLOSED:
                break

            # Start
            if event == '-Start-':  # Start data acquisition

                # Separating variables
                self.ts = float(values['-TS-'])
                self.session_duration = float(values['-SD-'])
                self.com_port = serial.tools.list_ports.comports()[self.com_ports.index(values['-COM-'])].name
                self.save = values['-Save-']
                self.path = values['-Path-']
                self.step_time = values['-Step-']
                self.plot = values['-Plot-']

                # Restarting variables
                self.time_var, self.input, self.output = [], [], []

                self.step_response_arduino()

            if event == '-Step-':  # Applying step
                pass  #

            if event == '-COM-':  # Updating com ports

                self.com_ports = [i.description for i in serial.tools.list_ports.comports()]
                port = values['-COM-']
                window['-COM-'].update(port, self.com_ports)

        window.close()

        return

    def step_response_arduino(self):
        """
        This method performs the step response using an Arduino board for given parameters.

        :example:
            step_response_arduino(self)

        """

        # Check if path was defined
        self._check_path()

        # Number of self.cycles necessary
        self.cycles = int(np.floor(self.session_duration / self.ts)) + 1

        # Opening ports and serial communication
        self._open_serial()

        if self.plot:  # If plot, start updatable plot
            self.title = f'PYDAQ - Sending Data. Arduino, Port: {self.com_port}'
            self._start_updatable_plot()

        # Data to be sent
        sent_data = b'0'

        # Turning off the output before starting
        self.ser.write(b'0')

        # Main loop, where data will be sent/acquired
        for k in range(self.cycles):

            # Sending and acquiring data
            self.ser.write(sent_data)
            self.ser.reset_input_buffer()  # Reseting serial input buffer
            temp = int(self.ser.read(14).split()[-2].decode('UTF-8')) * self.ard_vpb # Get the last complete value

            # Counting time to append data and update interface
            st = time.time()

            # Queue data in a list
            self.output.append(temp)
            self.input.append(float(sent_data))
            self.time_var.append(k * self.ts)

            if self.plot:

                # Checking if there is still an open figure. If not, stop the for loop.
                try:
                    plt.get_figlabels().index('iter_plot')
                except:
                   break

                # Updating data values
                self._update_plot([self.time_var, self.time_var], [self.output, self.input], 2)

            print(f'Iteration: {k} of {self.cycles - 1}')

            # Updating sent_data
            if k*self.ts > float(self.step_time):
                sent_data = b'1'
            else:
                sent_data = b'0'

            # Getting end time
            et = time.time()

            # Wait for (ts - delta_time) seconds
            try:
                time.sleep(self.ts + (st - et))
            except:
                warnings.warn("Time spent to append data and update interface was greater than ts. "
                              "You CANNOT trust time.dat")

        # Turning off the output at the end
        self.ser.write(b'0')
        # Closing port
        self.ser.close()

        # Check if data will or not be saved, and save accordingly
        if self.save:
            print('\nSaving data ...')
            # Saving time_var and data
            self._save_data(self.time_var, 'time.dat')
            self._save_data(self.input, 'input.dat')
            self._save_data(self.output, 'output.dat')
            print('\nData saved ...')
        return

    def step_response_nidaq_gui(self):
        """
        This functions provides a Graphical User Interface (GUI) that allows one to send data
        from a .dat file to a National Instruments acquisition boards.

        :example:
            send_data_nidaq_gui()

        """

        # Theme
        sg.theme('Dark')

        # First the window layout in 2 columns
        first_column = [
            [sg.Text('Choose device: ')],
            [sg.Text('AO channel: ')],
            [sg.Text('AI channel: ')],
            [sg.Text("Step range (V)")],
            [sg.Text("Output range (V)")],
            [sg.Text("Sample period (s)")],
            [sg.Text("Session duration (s)")],
            [sg.Text("Step ON (s)")],
            [sg.Text('Plot data?')],
            [sg.Text('Save data?')],
            [sg.Text("Path")],
        ]

        try:
            ao_chan = nidaqmx.system.device.Device(self.device_names[0]).ao_physical_chans.channel_names
            ao_def_chan = ao_chan[0]
        except:
            ao_chan = ''
            ao_def_chan = 'There is no analog output in this board'

        try:
            ai_chan = nidaqmx.system.device.Device(self.device_names[0]).ai_physical_chans.channel_names
            ai_def_chan = ai_chan[0]
        except:
            ai_chan = ''
            ai_def_chan = 'There is no analog input in this board'

        second_column = [
            [sg.DD(self.device_type, size=(40, 1), enable_events=True, default_value=self.device_type[0],
                   key="-DDDev-")],
            [sg.DD(ao_chan, enable_events=True, size=(40, 1), default_value=ao_def_chan, key="-DDAOChan-")],
            [sg.DD(ai_chan, enable_events=True, size=(40, 1), default_value=ai_def_chan, key="-DDAIChan-")],
            [sg.Text("Minimum"), sg.In(default_text=self.ai_min, size=(10, 1), enable_events=True, key='-ai_min-'),
             sg.VSeparator(), sg.Text("Maximum"),
             sg.In(default_text=self.ai_max, size=(10, 1), enable_events=True, key='-ai_max-')],
            [sg.Text("Minimum"), sg.In(default_text=self.ao_min, size=(10, 1), enable_events=True, key='-ao_min-'),
             sg.VSeparator(), sg.Text("Maximum"),
             sg.In(default_text=self.ao_max, size=(10, 1), enable_events=True, key='-ao_max-')],
            [sg.I(self.ts, enable_events=True, key='-TS-', size=(40, 1))],
            [sg.I(self.session_duration, enable_events=True, key='-SD-', size=(40, 1))],
            [sg.I(self.step_time, enable_events=True, key='-Step-', size=(40, 1))],
            [sg.Radio("Yes", "plot_radio", default=True, key='-Plot-'), sg.Radio("No", "plot_radio", default=False)],
            [sg.Radio("Yes", "save_radio", default=True, key='-Save-'), sg.Radio("No", "save_radio", default=False)],
            [sg.In(size=(32, 1), enable_events=True, key="-Path-",
                   default_text=self.path),
             sg.FolderBrowse()],
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

        window = sg.Window("PYDAQ - Step Response (NIDAQ)", layout, resizable=False, finalize=True, element_justification="center",
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
                self.ai_max = values['-ai_max-']
                self.ai_min = values['-ai_min-']


                # Reading data from defined path
                self.path = values['-Path-']
                self.data = np.loadtxt(self.path)

                # Check if max(data) < self.ao_max
                if (max(self.data) > float(self.ao_max)) or (min(self.data) < float(self.ao_min)):
                    self.range_error()
                    self.error_max = True
                else:
                    self.error_max = False

                try:
                    # Separating variables
                    self.ts = float(values['-TS-'])
                    self.device = values['-DDAOChan-'].split('/')[0]
                    self.ao_channel = values['-DDAOChan-'].split('/')[1]
                    self.ai_channel = values['-DDAIChan-'].split('/')[1]
                    self.plot = values['-Plot-']
                    self.error_path = False

                except:
                    self.error_window()
                    self.error_path = True

                # Calling send data method
                if not self.error_max and not self.error_path:
                    self.send_data_nidaq()

            # Changing availables channels if device changes
            if event == "-DDDev-":
                # Discovering new ao/ai channels
                new_ao_channels = nidaqmx.system.device.Device(
                    self.device_names[self.device_type.index(values['-DDDev-'])]).ao_physical_chans.channel_names
                new_ai_channels = nidaqmx.system.device.Device(
                    self.device_names[self.device_type.index(values['-DDDev-'])]).ai_physical_chans.channel_names

                # Default channel
                try:
                    default_ao_channel = new_ao_channels[0]
                except:
                    default_ao_channel = 'There is no analog output in this board'
                try:
                    default_ai_channel = new_ai_channels[0]
                except:
                    default_ai_channel = 'There is no analog input in this board'


                # Rewriting new ai channels into the right place
                window['-DDAOChan-'].update(default_ao_channel, new_ao_channels)
                window['-DDAIChan-'].update(default_ai_channel, new_ai_channels)

        window.close()

        return



if __name__ == '__main__':

    from pydaq.step_response import Step_response
    s = Step_response()
    s.step_response_nidaq_gui()