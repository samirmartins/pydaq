import os
import PySimpleGUI as sg
class Base:
    """
        Base class for data acquisition and to send data.
    """

    def __init__(self):
        pass
    def range_error(self):
        layout2 = [[sg.VPush()], [
            sg.Cancel("Out of range value (check ao_max and ao_min)!", key="-new-")],
                   [sg.VPush()]]
        window = sg.Window("ERROR!", layout2, resizable=False, finalize=True, element_justification="center",
                           font="Helvetica", size=(600, 100))
        while True:
            event2, values2 = window.read()
            if event2 == "Exit" or event2 == sg.WIN_CLOSED or event2 == '-new-':
                break

        window.close()

    def error_window(self):
        layout2 = [[sg.VPush()], [sg.Cancel("Device, channel or data were not choosen properly!", key="-new-")],
                   [sg.VPush()]]
        window = sg.Window("ERROR!", layout2, resizable=False, finalize=True, element_justification="center",
                           font="Helvetica", size=(600, 100))
        while True:
            event2, values2 = window.read()
            if event2 == "Exit" or event2 == sg.WIN_CLOSED or event2 == '-new-':
                break

        window.close()

    def _check_path(self):
        """ Method to check if path was or not defined by the user"""

        # Checking if path was or not defined by the user
        if self.path is None:  # Saving in Desktop if it is not defined
            self.path = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop')

        # Check if able to save data in defined path
        if not os.path.exists(self.path):
            warnings.warn('Defined path does not exists! Please redefine path and run the code again')
            return
