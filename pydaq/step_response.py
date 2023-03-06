import os
import time
import numpy as np
import PySimpleGUI as sg
import serial
import serial.tools.list_ports
from pydaq.utils.base import Base
import os
import PySimpleGUI as sg
import numpy as np
import serial
import serial.tools.list_ports
from pydaq.utils.base import Base
import matplotlib.pyplot as plt
import warnings

class Step_response(Base):
    """
        Class developed to construct Graphical User Interface for step
        response using arduino and nidaqmx

       :author: Samir Angelo Milani Martins
             - https://www.samirmartins.com.br
             - https://www.github.com/samirmartins/

        :params:
            ts: sample period, in seconds.
            session_duration: session duration, in seconds.
            step_time: time when step will be applied, in seconds
            plot: if True, plot data iteractively as they are sent/acquired

    """

    def __init__(self, ts=0.5, session_duration=10.0, step_time=3.0, plot=True):

        super().__init__()
        self.ts = ts
        self.session_duration = session_duration
        self.plot = plot
        self.step_time = step_time

        # COM ports
        self.com_ports = [i.description for i in serial.tools.list_ports.comports()]
        self.com_port = self.com_ports[0]  # Default COM port

        # Initializing variables
        self.time_var, self.input, self.output = [], [], []

        # Plot title
        self.title = None

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
                   default_text=os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop')),
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

        window = sg.Window("PYDAQ - Data Acquisition", layout, resizable=False, finalize=True, element_justification="center",
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
            temp = int(self.ser.read(14).split()[-2].decode('UTF-8')) / 204.6  # Get the last complete value

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

if __name__ == '__main__':

    from pydaq.step_response import Step_response
    s = Step_response()
    s.step_response_arduino_gui()