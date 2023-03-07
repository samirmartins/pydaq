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
from nidaqmx.constants import TerminalConfiguration


class Step_response(Base):
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

    def __init__(self,
                 device="Dev1",
                 ao_channel="ao0",
                 ai_channel="ai0",
                 ts=0.5,
                 session_duration=10.0,
                 step_time=3.0,
                 step_min=0,
                 step_max=5,
                 terminal='Diff',
                 com = 'COM1',
                 plot=True
                 ):

        super().__init__()
        self.ts = ts
        self.session_duration = session_duration
        self.plot = plot
        self.step_time = step_time
        self.device = device
        self.ai_channel = ai_channel
        self.ao_channel = ao_channel
        self.step_min = step_min
        self.step_max = step_max

        # Terminal configuration
        self.terminal = self.term_map[terminal]

        # COM ports
        self.com_ports = [
            i.description for i in serial.tools.list_ports.comports()]
        self.com_port = com  # Default COM port

        # Initializing variables
        self.time_var, self.input, self.output = [], [], []

        # Plot title
        self.title = None

        # Gathering nidaq info
        self._nidaq_info()

        # Defining default path
        self.path = os.path.join(
            os.path.join(
                os.path.expanduser('~')),
            'Desktop')

        # Arduino ADC resolution (in bits)
        self.arduino_ai_bits = 10

        # Arduino analog input max and min
        self.ard_ao_max, self.ard_ao_min = 5, 0

        # Value per bit - Arduino
        self.ard_vpb = (self.ard_ao_max - self.ard_ao_min) / \
            (2 ** self.arduino_ai_bits)

        self.legend = ['Input', 'Output']

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

        window = sg.Window(
            "PYDAQ - Step Response (Arduino)",
            layout,
            resizable=False,
            finalize=True,
            element_justification="center",
            font="Helvetica")

        # Event Loop
        while True:

            event, values = window.read()

            if event == sg.WIN_CLOSED:
                break

            # Start
            if event == '-Start-':  # Start data acquisition

                # Cleaning data
                self.output, self.input, self.time_var = [], [], []

                # Separating variables
                self.ts = float(values['-TS-'])
                self.session_duration = float(values['-SD-'])
                self.com_port = serial.tools.list_ports.comports(
                )[self.com_ports.index(values['-COM-'])].name
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

                self.com_ports = [
                    i.description for i in serial.tools.list_ports.comports()]
                port = values['-COM-']
                window['-COM-'].update(port, self.com_ports)

        window.close()

        return

    def step_response_arduino(self):
        """
        This method performs the step response using an Arduino board for given parameters.

        :example:
            step_response_arduino()

        """

        # Check if path was defined
        self._check_path()

        # Number of self.cycles necessary
        self.cycles = int(np.floor(self.session_duration / self.ts)) + 1

        # Opening ports and serial communication
        self._open_serial()

        if self.plot:  # If plot, start updatable plot
            self.title = f'PYDAQ - Step Response (Arduino), Port: {self.com_port}'
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
            # Get the last complete value
            temp = int(self.ser.read(14).split()
                       [-2].decode('UTF-8')) * self.ard_vpb

            # Counting time to append data and update interface
            st = time.time()

            # Queue data in a list
            self.output.append(temp)
            self.input.append(5 * float(sent_data))
            self.time_var.append(k * self.ts)

            if self.plot:

                # Checking if there is still an open figure. If not, stop the
                # for loop.
                try:
                    plt.get_figlabels().index('iter_plot')
                except BaseException:
                    break

                # Updating data values
                self._update_plot([self.time_var, self.time_var], [
                                  self.output, self.input], 2)

            print(f'Iteration: {k} of {self.cycles - 1}')

            # Updating sent_data
            if k * self.ts > float(self.step_time):
                sent_data = b'1'
            else:
                sent_data = b'0'

            # Getting end time
            et = time.time()

            # Wait for (ts - delta_time) seconds
            try:
                time.sleep(self.ts + (st - et))
            except BaseException:
                warnings.warn(
                    "Time spent to append data and update interface was greater than ts. "
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
            [sg.Text('Terminal Config.')],
            [sg.Text("Step range (V)")],
            [sg.Text("Sample period (s)")],
            [sg.Text("Session duration (s)")],
            [sg.Text("Step ON (s)")],
            [sg.Text('Plot data?')],
            [sg.Text('Save data?')],
            [sg.Text("Path")],
        ]

        try:
            ao_chan = nidaqmx.system.device.Device(
                self.device_names[-1]).ao_physical_chans.channel_names
            ao_def_chan = ao_chan[0]
        except BaseException:
            ao_chan = ''
            ao_def_chan = 'There is no analog output in this board'

        try:
            ai_chan = nidaqmx.system.device.Device(
                self.device_names[-1]).ai_physical_chans.channel_names
            ai_def_chan = ai_chan[0]
        except BaseException:
            ai_chan = ''
            ai_def_chan = 'There is no analog input in this board'

        second_column = [
            [sg.DD(self.device_type, size=(40, 1), enable_events=True, default_value=self.device_type[-1],
                   key="-DDDev-")],
            [sg.DD(ao_chan, enable_events=True, size=(40, 1), default_value=ao_def_chan, key="-DDAOChan-")],
            [sg.DD(ai_chan, enable_events=True, size=(40, 1), default_value=ai_def_chan, key="-DDAIChan-")],
            [sg.DD(['Diff', 'RSE', 'NRSE'], enable_events=True, size=(40, 1), default_value=['Diff'],
                   key="-Terminal-")],
            [sg.Text("Minimum"), sg.In(default_text=self.step_min, size=(10, 1), enable_events=True, key='-step_min-'),
             sg.VSeparator(), sg.Text("Maximum"),
             sg.In(default_text=self.step_max, size=(10, 1), enable_events=True, key='-step_max-')],
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

        window = sg.Window(
            "PYDAQ - Step Response (NIDAQ)",
            layout,
            resizable=False,
            finalize=True,
            element_justification="center",
            font="Helvetica")

        # Event Loop
        while True:

            event, values = window.read()

            if event == sg.WIN_CLOSED:
                break

            # Start
            if event == '-Start-':

                # Cleaning data
                self.output, self.input, self.time_var = [], [], []

                try:
                    # Separating variables
                    # Input and output range
                    self.device = values['-DDAOChan-'].split('/')[0]
                    self.ao_channel = values['-DDAOChan-'].split('/')[1]
                    self.ai_channel = values['-DDAIChan-'].split('/')[1]
                    self.terminal = self.term_map[values['-Terminal-']]
                    self.step_max = values['-step_max-']
                    self.step_min = values['-step_min-']
                    self.ts = float(values['-TS-'])
                    self.session_duration = float(values['-SD-'])
                    self.step_time = values['-Step-']
                    self.plot = values['-Plot-']
                    self.save = values['-Save-']
                    self.path = values['-Path-']
                    self.error_path = False

                except BaseException:
                    self._error_window()
                    self.error_path = True

                # Calling send data method
                if not self.error_path:
                    self.step_response_nidaq()

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
                except BaseException:
                    default_ao_channel = 'There is no analog output in this board'
                try:
                    default_ai_channel = new_ai_channels[0]
                except BaseException:
                    default_ai_channel = 'There is no analog input in this board'

                # Rewriting new ai channels into the right place
                window['-DDAOChan-'].update(default_ao_channel,
                                            new_ao_channels)
                window['-DDAIChan-'].update(default_ai_channel,
                                            new_ai_channels)

        window.close()

        return

    def step_response_nidaq(self):
        """
        This method performs the step response using a NIDAQ board for given parameters.

        :example:
            step_response_nidaq()

        """

        # Check if path was defined
        self._check_path()

        # Number of self.cycles necessary
        self.cycles = int(np.floor(self.session_duration / self.ts)) + 1

        # Initializing device, with channel defined
        task_ao = nidaqmx.Task()
        task_ai = nidaqmx.Task()
        task_ao.ao_channels.add_ao_voltage_chan(
            self.device + '/' + self.ao_channel,
            min_val=float(
                self.step_min),
            max_val=float(
                self.step_max))
        task_ai.ai_channels.add_ai_voltage_chan(
            self.device + '/' + self.ai_channel,
            terminal_config=self.terminal)

        if self.plot:  # If plot, start updatable plot
            self.title = f'PYDAQ - Step Response (NIDAQ). {self.device}, {self.ai_channel}, {self.ao_channel}'
            self._start_updatable_plot()

        # Data to be sent
        sent_data = self.step_min

        # Turning off the output before starting
        task_ao.write(sent_data)

        # Main loop, where data will be sent/acquired
        for k in range(self.cycles):

            # Sending and acquiring data
            task_ao.write(sent_data)
            temp = task_ai.read()

            # Counting time to append data and update interface
            st = time.time()

            # Queue data in a list
            self.output.append(temp)
            self.input.append(float(sent_data))
            self.time_var.append(k * self.ts)

            if self.plot:

                # Checking if there is still an open figure. If not, stop the
                # for loop.
                try:
                    plt.get_figlabels().index('iter_plot')
                except BaseException:
                    break

                # Updating data values
                self._update_plot([self.time_var, self.time_var], [
                                  self.output, self.input], 2)

            print(f'Iteration: {k} of {self.cycles - 1}')

            # Updating sent_data
            if k * self.ts > float(self.step_time):
                sent_data = self.step_max
            else:
                sent_data = self.step_min

            # Getting end time
            et = time.time()

            # Wait for (ts - delta_time) seconds
            try:
                time.sleep(self.ts + (st - et))
            except BaseException:
                warnings.warn(
                    "Time spent to append data and update interface was greater than ts. "
                    "You CANNOT trust time.dat")

        # Turning off the output at the end
        task_ao.write(0)
        # Closing task
        task_ao.close()
        task_ai.close()

        # Check if data will or not be saved, and save accordingly
        if self.save:
            print('\nSaving data ...')
            # Saving time_var and data
            self._save_data(self.time_var, 'time.dat')
            self._save_data(self.input, 'input.dat')
            self._save_data(self.output, 'output.dat')
            print('\nData saved ...')
        return
