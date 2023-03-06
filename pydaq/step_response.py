import os
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
        self.com_ports = self.com_port[0]  # Default COM port

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
            [sg.DD(self.com_ports, size=(40, 1), enable_events=True, default_value=self.com_ports[0], key="-COM-")],
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
                self.data = []
                self.time_var = []

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

        # Number of cycles necessary
        cycles = int(np.floor(self.session_duration / self.ts)) + 1

        # Oppening ports
        self._open_serial()
