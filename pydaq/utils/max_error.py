import PySimpleGUI as sg
def max_error():
    layout2 = [[sg.VPush()], [sg.Cancel("You are trying to send a value greather than ao_max! Please, double check it", key="-new-")],
               [sg.VPush()]]
    window = sg.Window("ERROR!", layout2, resizable=False, finalize=True, element_justification="center",
                       font="Helvetica", size=(600, 100))
    while True:
        event2, values2 = window.read()
        if event2 == "Exit" or event2 == sg.WIN_CLOSED or event2 == '-new-':
            break

    window.close()
