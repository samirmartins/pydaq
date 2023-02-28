import nidaqmx
import PySimpleGUI as sg
import os.path


def step_response_gui():
    """

    :return:
    """

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
        [sg.Text('Choose device: '), sg.DD(device_type, size=(20, 8), default_value=device_type[0], key="-DDDev-")],
        [sg.Text('Choose channel: '),
         sg.DD(nidaqmx.system.device.Device(device_names[0]).ai_physical_chans.channel_names, size=(20, 8),
               default_value=nidaqmx.system.device.Device(device_names[0]).ai_physical_chans.channel_names[0],
               key="-DDChan-")],
        [sg.Text("Sample period (s)"), sg.I("1.0", enable_events=True, key='-TS-')],
        [sg.Text("Session Duration (s)"), sg.I("10.0", enable_events=True, key='-SD-')],
        [sg.Text('Save data?'), sg.Radio("Yes", "save_radio", default=True, key='save'), sg.Radio("No", "save_radio", default=False)],
        [sg.Text("Path"),
         sg.In(size=(25, 1), enable_events=True, key="-FOLDER-"),
         sg.FolderBrowse(), ],
        [sg.Button('Start', key='-Start-'), sg.Button('Stop', key='-Stop-')]
    ]

    # For now will only show the name of the file that was chosen
    second_column = [
        [sg.Text("Choose an image from list on left:")],
        [sg.Text(size=(40, 1), key="-TOUT-")],
        [sg.Image(key="-IMAGE-")],
    ]

    # ----- Full layout -----
    layout = [
        [sg.Column(first_column),
         sg.VSeperator(),
         sg.Column(second_column), ]
    ]

    window = sg.Window("Step Response", layout, resizable=True, finalize=True)

    # Initializing variables
    ts = 1.0 # Sample period
    session_duration = 10.0 # Session duration

    # Event Loop
    while True:

        event, values = window.read()

        if event == sg.WIN_CLOSED:
            break

        # Redefining session_duration
        if event == '-SD-':
            session_duration = float(values['-SD-'])

        # Redefining sample period
        if event == '-TS-':
            ts = float(values['-TS-'])


    window.close()

    return
