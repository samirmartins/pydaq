import nidaqmx
import PySimpleGUI as sg
import os.path
from step_response import step_response

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
        [sg.Text('Choose device: '), sg.DD(device_type, size=(20, 8), enable_events=True, default_value=device_type[0], key="-DDDev-")],
        [sg.Text('Choose channel: '),
         sg.DD(nidaqmx.system.device.Device(device_names[0]).ai_physical_chans.channel_names, enable_events=True, size=(20, 8),
               default_value=nidaqmx.system.device.Device(device_names[0]).ai_physical_chans.channel_names[0],
               key="-DDChan-")],
        [sg.Text("Sample period (s)"), sg.I("1.0", enable_events=True, key='-TS-')],
        [sg.Text("Session Duration (s)"), sg.I("10.0", enable_events=True, key='-SD-')],
        [sg.Text('Save data?'), sg.Radio("Yes", "save_radio", default=True, key='-Save-'), sg.Radio("No", "save_radio", default=False)],
        [sg.Text("Path"),
         sg.In(size=(25, 1), enable_events=True, key="-Path-", default_text=os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop')),
         sg.FolderBrowse(), ],
        [sg.Button('Start', key='-Start-'), sg.Button('Stop', key='-Stop-')]
    ]

    # For now will only show the name of the file that was chosen
    second_column = [
        [sg.Canvas(key="-Plot-")],
        [sg.Button('Clear Screen', '-Clr-')]
    ]

    # ----- Full layout -----
    layout = [
        [sg.Column(first_column),
         sg.VSeperator(),
         sg.Column(second_column), ]
    ]

    window = sg.Window("Step Response", layout, resizable=True, finalize=True, element_justification="center", font="Helvetica")

    # Initializing variables
    ts = 1.0 # Sample period
    session_duration = 10.0 # Session duration

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
            step_response(device, channel, ts, session_duration, save, path)

        # Changing availables channels if device changes
        if event == "-DDDev-":
            # Discovering new ai channels
            new_ai_channels = nidaqmx.system.device.Device(device_names[device_type.index(values['-DDDev-'])]).ai_physical_chans.channel_names
            # Default channel
            try:
                default_channel = new_ai_channels[0]
            except:
                default_channel = 'There is no analog input in this board'

            # Rewriting new ai channels into the right place
            window['-DDChan-'].update(default_channel,new_ai_channels)


    window.close()

    return

if __name__ == '__main__':
    step_response_gui()