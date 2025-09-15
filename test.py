import sys, os, serial.tools.list_ports
from PySide6.QtWidgets import QApplication
from pydaq.guis.pid_control_window_dialog import PID_Control_Window_Dialog

app = QApplication(sys.argv)
plot_window = PID_Control_Window_Dialog()

# Selection NIDAQ board
plot_window.check_board(board="nidaq", device="Dev1", ao="ao0", ai="ai0", terminal="RSE", simulate=False)

# Define PID parameters
kp, ki, kd, setpoint, period = 1.0, 0.2, 0.05, 2.0, 0.1
index, path, save = 3, None, True  
# index = 0 -> P, 1 -> PI, 2 -> PD, 3 -> PID.

# when path = None, by defaut saves to C:\Users\Desktop

plot_window.set_parameters(kp, ki, kd, index, " ", " ", setpoint, "Voltage (V)", "", "", period, path, save)

# Open GUI
plot_window.exec()