import PySimpleGUI as sg
def error_window():
    layout2 = [[sg.VPush()], [sg.Cancel("Device, channel or data were not choosen properly!", key="-new-")],
               [sg.VPush()]]
    window = sg.Window("ERROR!", layout2, resizable=False, finalize=True, element_justification="center",
                       font="Helvetica", size=(600, 100))
    while True:
        event2, values2 = window.read()
        if event2 == "Exit" or event2 == sg.WIN_CLOSED or event2 == '-new-':
            break

    window.close()
