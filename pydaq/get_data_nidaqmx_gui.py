import nidaqmx
import PySimpleGUI as sg
import os.path
from pydaq.get_data_nidaqmx import get_data_nidaqmx


def get_data_nidaqmx_gui():
    """
    This functions provides a Graphical User Interface (GUI) that allows one to get data
    from National Instruments acquisition boards.

    :example:
        get_data_nidaqmx_gui()

    """

    # Theme
    sg.theme('Dark')

    device_names = []
    device_categories = []
    device_type = []

    # Getting all available devices
    local_system = nidaqmx.system.System.local()

    for device in local_system.devices:
        device_names.append(device.name)
        device_categories.append(device.product_category)
        device_type.append(device.product_type)

    # First the window layout in 2 columns
    first_column = [
        [sg.Text('Choose device: ')],
        [sg.Text('Choose channel: ')],
        [sg.Text("Sample period (s)")],
        [sg.Text("Session duration (s)")],
        [sg.Text('Save data?')],
        [sg.Text("Path")],
    ]

    # For now will only show the name of the file that was chosen
    second_column = [
        [sg.DD(device_type, size=(40, 8), enable_events=True, default_value=device_type[0], key="-DDDev-")],
        [sg.DD(nidaqmx.system.device.Device(device_names[0]).ai_physical_chans.channel_names, enable_events=True,
               size=(40, 8),
               default_value=nidaqmx.system.device.Device(device_names[0]).ai_physical_chans.channel_names[0],
               key="-DDChan-")],
        [sg.I("1.0", enable_events=True, key='-TS-', size=(40, 8))],
        [sg.I("10.0", enable_events=True, key='-SD-', size=(40, 8))],
        [sg.Radio("Yes", "save_radio", default=True, key='-Save-'), sg.Radio("No", "save_radio", default=False)],
        [sg.In(size=(32, 8), enable_events=True, key="-Path-",
               default_text=os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop')),
         sg.FolderBrowse()],
    ]

    bottom_line = [
        [sg.Button('START EXPERIMENT', key='-Start-', auto_size_button=True)]
    ]

    # ----- Full layout -----
    layout = [
        [sg.Column(first_column),
         sg.VSeparator(),
         sg.Column(second_column)],
        [sg.HSeparator()],
        [sg.Column(bottom_line)]
    ]

    window = sg.Window("Step Response", layout, resizable=False, finalize=True, element_justification="center",
                       font="Helvetica")

    # Initializing variables
    ts = 1.0  # Sample period
    session_duration = 10.0  # Session duration

    # Event Loop
    while True:

        event, values = window.read()

        if event == sg.WIN_CLOSED:
            break

        # Start
        if event == '-Start-':
            # Separating variables
            ts = float(values['-TS-'])
            session_duration = float(values['-SD-'])
            device = values['-DDChan-'].split('/')[0]
            channel = values['-DDChan-'].split('/')[1]
            save = values['-Save-']
            path = values['-Path-']

            # Calling main function
            get_data_nidaqmx(device, channel, ts, session_duration, save, path)

        # Changing availables channels if device changes
        if event == "-DDDev-":
            # Discovering new ai channels
            new_ai_channels = nidaqmx.system.device.Device(
                device_names[device_type.index(values['-DDDev-'])]).ai_physical_chans.channel_names
            # Default channel
            try:
                default_channel = new_ai_channels[0]
            except:
                default_channel = 'There is no analog input in this board'

            # Rewriting new ai channels into the right place
            window['-DDChan-'].update(default_channel, new_ai_channels)

    window.close()

    return
