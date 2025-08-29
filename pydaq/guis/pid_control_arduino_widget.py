import sys, os
import serial
import serial.tools.list_ports
import matplotlib.pyplot as plt
import matplotlib.animation as animation

from PySide6 import QtWidgets
from PySide6.QtWidgets import QFileDialog, QApplication, QWidget, QVBoxLayout, QPushButton
from PySide6.QtGui import *
from PySide6.QtCore import *

from ..uis.ui_PyDAQ_pid_control_Arduino_widget import Ui_Arduino_PID_Control
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from ..guis.pid_control_window_dialog import PID_Control_Window_Dialog

class PID_Control_Arduino_Widget(QWidget, Ui_Arduino_PID_Control):
    def __init__(self, *args):
        super(PID_Control_Arduino_Widget, self).__init__()
        self.setupUi(self)

# Calling the functions
        self.update_com_ports()
        self.reload_devices.clicked.connect(self.update_com_ports)
        self.on_unit_change()
        self.comboBox_setpoint.currentIndexChanged.connect(self.on_unit_change)
        self.simulate_radio_group.buttonClicked.connect(self.on_simulate_change)
        self.on_simulate_change()
        self.on_type_combo_changed(0)
        self.comboBox_type.currentIndexChanged.connect(self.on_type_combo_changed)
        self.pushButton_confirm.released.connect(self.show_pid_equation)
        self.pushButton_start.clicked.connect(self.show_graph_window)
        self.path_folder_browse.released.connect(self.locate_path)
        # Setting the starting values for some widgets
        self.path_line_edit.setText(
            os.path.join(os.path.join(os.path.expanduser("~")), "Desktop")
        )
       
    def update_com_ports(self):  # Updating com ports
        self.com_ports = [i.description for i in serial.tools.list_ports.comports()]
        selected = self.comboBox_arduino.currentText()

        self.comboBox_arduino.clear()
        self.comboBox_arduino.addItems(self.com_ports)
        index_current = self.comboBox_arduino.findText(selected)

        if index_current == -1:
            pass
        else:
            self.comboBox_arduino.setCurrentIndex(index_current)

# Condiction to show the line edit equation and unit
    def on_unit_change(self):
        selected_unit = self.comboBox_setpoint.currentText()
        if selected_unit == 'Other':
            self.widget_unit.show()
            self.label_unit.show()
            self.label_equation.show()
            self.widget_equation.show()
            self.label_i_equation.show()
        elif selected_unit == 'Voltage (V)':
            self.widget_unit.hide()
            self.label_unit.hide()
            self.label_equation.hide()
            self.widget_equation.hide()
            self.label_i_equation.hide()
        else:
            self.widget_unit.hide()
            self.label_unit.hide()
            self.label_equation.show()
            self.widget_equation.show()
            self.label_i_equation.show()

    def on_simulate_change(self):
        self.simulate = True if self.simulate_radio_group.checkedId() == -2 else False
        if self.simulate is False: #Simulate = False
            self.widget_arduino.show()
            self.label_arduino.show()
            self.widget_polynomial.hide()
            self.label_system_equation.hide()
            self.label_i_polinomial.hide()
        elif self.simulate is True: #Simulate = True
            self.widget_arduino.hide()
            self.label_arduino.hide()
            self.widget_polynomial.show()
            self.label_system_equation.show()
            self.label_i_polinomial.show()

# Enable the pid parameters inputs 
    def on_type_combo_changed(self, index):
        if index == 0:  
            self.enable_pid_parameters(True, False, False)
        elif index == 1:  
            self.enable_pid_parameters(True, True, False)
        elif index == 2: 
            self.enable_pid_parameters(True, False, True)
        elif index == 3:  
            self.enable_pid_parameters(True, True, True)

    def enable_pid_parameters(self, kp_enabled, ki_enabled, kd_enabled):
        self.doubleSpinBox_kp.setEnabled(kp_enabled)
        self.doubleSpinBox_ki.setEnabled(ki_enabled)
        self.doubleSpinBox_kd.setEnabled(kd_enabled)
        if ki_enabled == False:
            self.doubleSpinBox_ki.setValue(0)
        if kd_enabled == False:
            self.doubleSpinBox_kd.setValue(0)

# Method to create a image and show the pid equation
    def show_pid_equation(self):
# Condiction to read only the inputs enable and set 'None' on desable inputs
        if self.doubleSpinBox_kp.isEnabled():
            self.kp = self.doubleSpinBox_kp.value()
        else:
            self.kp = None
        if self.doubleSpinBox_ki.isEnabled():
            self.ki = self.doubleSpinBox_ki.value()
        else:
            self.ki = None
        if self.doubleSpinBox_kd.isEnabled():
            self.kd = self.doubleSpinBox_kd.value()
        else:
            self.kd = None
        equation_parts = []
# Create a pid equation to show when the line edits are able
        if self.kp is not None:
            kp_display = f"{self.kp:.2f}"
            equation_parts.append(rf"{kp_display} \cdot e(t)")
        if self.ki is not None:
            ki_display = f"{self.ki:.2f}"
            equation_parts.append(rf"{ki_display} \int_{{0}}^{{t}} e(\tau) \, d\tau")
        if self.kd is not None:
            kd_display = f"{self.kd:.2f}"
            equation_parts.append(rf"{kd_display} \frac{{d}}{{dt}} e(t)")
        if not equation_parts:
            return
# Equation on latex
        latex = "u(t) = " + " + ".join(equation_parts)
# Figure created showing the equation, without axes
        fig = Figure(figsize=(9, 3), facecolor='#404040')
        ax = fig.add_subplot(111, facecolor='#404040')
        ax.text(0.5, 0.5, f"${latex}$", fontsize=15, ha='center', va='center', color='white')
        ax.axis('off')
        canvas = FigureCanvas(fig)
# Remove the widgets from central content layout in reverse and reset the widget from parents too        
        for i in reversed(range(self.image_layout.count())):
            widget_to_remove = self.image_layout.itemAt(i).widget()
            self.image_layout.removeWidget(widget_to_remove)
            widget_to_remove.setParent(None)
        self.image_layout.addWidget(canvas)

# Create the pid control window
    def show_graph_window(self):
        self.simulate = True if self.simulate_radio_group.checkedId() == -2 else False
        self.numerator = self.lineEdit_numerator.text()
        self.denominator = self.lineEdit_denominator.text()
        print('Simulated? ', self.simulate)
        if self.simulate == False:
            self.com_port = serial.tools.list_ports.comports()[
                    self.com_ports.index(self.comboBox_arduino.currentText())
                ].name
            print ('Com port1 ', self.com_port)
        else:    
            self.com_port = ' '
        self.setpoint = self.doubleSpinBox_setpoint.value()
        self.getunit()
        self.equationvu = self.lineEdit_equationvu.text()
        self.equationuv = self.lineEdit_equationuv.text()
        self.period = self.doubleSpinBox_period.value()
        self.path = self.path_line_edit.text()
        self.index = self.comboBox_type.currentIndex()
        self.save = True if self.save_radio_group.checkedId() == -2 else False
        print('Save? ', self.save)
        self.board = 'arduino'
        plot_window = PID_Control_Window_Dialog()
        plot_window.check_board(self.board, self.com_port, None, None, None, self.simulate)
        plot_window.set_parameters(self.kp, self.ki, self.kd, self.index, self.numerator, self.denominator, self.setpoint, self.unit, self.equationvu, self.equationuv, self.period, self.path, self.save)
        plot_window.send_values.connect(self.update_values)
        plot_window.exec()

    def locate_path(self):  # Calling the Folder Browser Widget
        output_folder_path = QFileDialog.getExistingDirectory( # To locate the data path to armazenate
            self, caption="Choose a folder to save the data file"
        )
        if output_folder_path == "":
            pass
        else:
            self.path_line_edit.setText(output_folder_path.replace("/", "\\"))

    def update_values(self, value1, value2, value3, value4, value5):
        # Sets the values in the corresponding QDoubleSpinBox
        self.doubleSpinBox_kp.setValue(value1)
        self.doubleSpinBox_ki.setValue(value2)
        self.doubleSpinBox_kd.setValue(value3)
        self.comboBox_type.setCurrentIndex(value4)
        self.doubleSpinBox_setpoint.setValue(value5)

    def getunit(self):
        if self.comboBox_setpoint.currentIndex() != 2:
            self.unit = self.comboBox_setpoint.currentText()
        else:
            self.unit = self.lineEdit_unit.text()