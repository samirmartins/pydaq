import nidaqmx
from nidaqmx.constants import TerminalConfiguration
import time
import matplotlib.pyplot as plt
import matplotlib as mpl
import os
import numpy as np
import warnings
import PySimpleGUI as sg
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
            plot_input: if True, plot data iteractively as they are sent
            plot_output: if True, plot data iteractively as they are acquired

    """

    def __init__(self,
                 ts=0.5,
                 session_duration = 10,
                 plot_input=True,
                 plot_output=True,
                 ):

        self.ts = ts
        self.session_duration = session_duration
        self.plot_input = plot_input
        self.plot_output = plot_output

        # COM ports
        self.com_ports = [i.description for i in serial.tools.list_ports.comports()]


    def step_response_arduino(self):
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
            [sg.Text('Plot input?')],
            [sg.Text('Plot output?')],
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
            [sg.DD(self.com_ports, size=(40, 1), enable_events=True, default_value=self.com_ports[0], key="-COM-")],
            [sg.I("1.0", enable_events=True, key='-TS-', size=(40, 1))],
            [sg.I("10.0", enable_events=True, key='-SD-', size=(40, 1))],
            [sg.Radio("Yes", "plot_input_radio", default=True, key='-Plot-'),sg.Radio("No", "plot_input_radio", default=False)],
            [sg.Radio("Yes", "plot_output_radio", default=True, key='-Plot-'),sg.Radio("No", "plot_output_radio", default=False)],
            [sg.Radio("Yes", "save_radio", default=True, key='-Save-'), sg.Radio("No", "save_radio", default=False)],
            [sg.In(size=(32, 1), enable_events=True, key="-Path-",
                   default_text=os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop')),
             sg.FolderBrowse()],
        ]

        bottom_line = [
            [sg.Button('START ACQUISITION', key='-Start-', auto_size_button=True), sg.Button('APPLY STEP', key='-Start-', auto_size_button=True)]
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
            if event == '-Start-':

                try:
                    # Separating variables
                    self.ts = float(values['-TS-'])
                    self.session_duration = float(values['-SD-'])
                    self.com_port = serial.tools.list_ports.comports()[self.com_ports.index(values['-COM-'])].name
                    self.save = values['-Save-']
                    self.path = values['-Path-']
                    self.plot = values['-Plot-']

                    # Restarting variables
                    self.data = []
                    self.time_var = []
                    self.error_path = False

                except:
                    error_window()
                    self.error_path = True

                # Calling data aquisition method
                if not self.error_path:
                    self.get_data_arduino(self.com_port)

        window.close()

        return

