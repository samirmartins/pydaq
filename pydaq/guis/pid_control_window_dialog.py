import sys, os
import serial
import serial.tools.list_ports
import numpy as np
import time
from pydaq.utils.base import Base
from PySide6 import QtWidgets
from PySide6.QtWidgets import QDialog, QFileDialog, QApplication, QWidget, QVBoxLayout, QPushButton
from PySide6.QtGui import *
from PySide6.QtCore import *
from ..uis.ui_PyDAQ_pid_control_window_dialog import Ui_Dialog_Plot_PID_Window
from ..pid_control import PIDControl
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

class PID_Control_Window_Dialog(QDialog, Ui_Dialog_Plot_PID_Window, Base):

#signal to send back to QWidget the values
    send_values = Signal(float, float, float, int, float)

    def __init__(self, *args):
        super(PID_Control_Window_Dialog, self).__init__()
        self.setupUi(self)
        self.setMinimumSize(900, 700)
        self.pushButton_startstop.clicked.connect(self.stopstart)
        self.pushButton_close.clicked.connect(self.go_back)
        self.pushButton_apply.clicked.connect(self.apply_parameters)
        self.comboBox_TypeDialog.currentIndexChanged.connect(self.on_type_combo_changed)
        self.paused = False
        self.pid = None
        self.path = os.path.join(os.path.join(os.path.expanduser("~")), "Desktop") # Defining default path
        self.figure = plt.figure(figsize =(6.4,4.8), facecolor='#404040') #Starting the canvas
        self.ax = self.figure.add_subplot(111, facecolor='#505050')  # Output graph
        self.canvas = FigureCanvas(self.figure)
        self.image_layout.addWidget(self.canvas)

#Defining the fuctions
    def set_parameters(self, kp, ki, kd, index, numerator, denominator, setpoint, unit, equationvu, equationuv, period, path, save):
        self.kp = kp if kp else 1
        self.ki = ki if ki else 0
        self.kd = kd if kd else 0
        self.numerator = numerator if numerator else '1'
        self.denominator = denominator if denominator else 's+0.2'
        self.index = index if index else 0
        self.setpoint = setpoint if setpoint else 0.0
        self.unit = unit if unit else 'Voltage (V)'
        self.calibration_equation_vu = equationvu
        self.calibration_equation_uv = equationuv
        self.period = period if period else 1 
        self.path = path if path else os.path.join(os.path.join(os.path.expanduser("~")), "Desktop")
        self.save = save
        self._check_path()
        self.set_text()
        self.on_type_combo_changed(self.index)
        print('kp ', self.kp)
        print('ki ', self.ki)
        print('kd ', self.kd)
        print('Index ', self.index)
        #print('Com Port ', self.com_port)
        print('Setpoint ', self.setpoint)
        print('Unit ', self.unit)
        print('Equation V(unit) = ', self.calibration_equation_vu)
        print('Equation Unit(V) = ', self.calibration_equation_uv)
        print('Period ', self.period)
        print ('Path ', self.path)
        print ('Save ', self.save)
        self.start_control(self.kp, self.ki, self.kd, self.setpoint, self.numerator, self.denominator, self.calibration_equation_vu, self.calibration_equation_uv, self.unit, self.period)

    def stopstart (self): #stop/start the event and change the button text
        self.paused = not self.paused
        if self.paused:
            self.ani.event_source.stop()
            self.pushButton_startstop.setText("Start")
        else:
            self.ani.event_source.start()
            self.pushButton_startstop.setText("Stop")

    def go_back(self): #def to save and go back
        if self.save: #save if wanted
            print("\nSaving data ...")
            self._save_data(self.time_var, "time.dat") # Saving time_var and data
            self._save_data(self.system_values, "output.dat")
            self._save_data(self.errors, "error.dat")
            self._save_data(self.setpoints, "setpoint.dat")
            self._save_data(self.controls, "controls.dat")
            print("\nData saved ...")
        self.send_values.emit( #sending the values to QWidget
            self.kp,
            self.ki,
            self.kd,
            self.index,
            self.setpoint,
        ) 
        if self.simulate == True:
            print('Closing')
        elif self.board == 'arduino': #stop the event and close the dialog
            self.pid.ser.write(b"0") # Turning off the output at the end
            self.pid.ser.close() # Closing port
        elif self.board == 'nidaq':
                self.pid.task_ao.write(0) # Turning off the output at the end
                self.pid.task_ao.close() # Closing task
                self.pid.task_ai.close()
        self.ani.event_source.stop()
        self.close()

    def apply_parameters(self): #apply all pid parameters while the event goes on
        try:
            self.setpoint = self.doubleSpinBox_SetpointDialog.value()
            print ('The new setpoint is ', self.setpoint)
            if self.pid:
                self.pid.setpoint = self.setpoint
        except ValueError:
            pass  # Ignore invalid input  
        if self.doubleSpinBox_KpDialog.isEnabled(): #changing Kp Ki and Kd parameters
            self.kp = self.doubleSpinBox_KpDialog.value()
            self.pid.Kp = self.kp
        else:
            self.kp = None
            self.pid.Kp = 0
        if self.doubleSpinBox_KiDialog.isEnabled():
            self.ki = self.doubleSpinBox_KiDialog.value()
            self.pid.integral = 0
            self.pid.Ki = self.ki
        else:
            self.ki = None
            self.pid.Ki = 0
        if self.doubleSpinBox_KdDialog.isEnabled():
            self.kd = self.doubleSpinBox_KdDialog.value()
            self.pid.Kd = self.kd
        else:
            self.kd = None
            self.pid.Kd = 0
        print ('The new kp is ', self.kp)
        print ('The new ki is ', self.ki)
        print ('The new kd is ', self.kd)
        self.disturbe = self.doubleSpinBox_DisturbeDialog.value() #changing the disturbe
        self.pid.disturbe = self.disturbe
        print ('The new disturbe is ', self.disturbe)

#stating the control and inicializating variables
    def start_control(self, Kp, Ki, Kd, setpoint, numerator, denominator, calibration_equation_vu, calibration_equation_uv, unit, period):
        try:
            self.pid = PIDControl(Kp, Ki, Kd, setpoint, numerator, denominator, calibration_equation_vu, calibration_equation_uv, unit, period)
            self.check_start()
            self.ani = animation.FuncAnimation(
                self.figure, 
                self.update_plot, 
                frames=range(100), 
                init_func=self.init_plot, 
                blit=True, 
                interval=self.period*1000
                )
            plt.suptitle('PID Control', color='white')
            self.canvas.draw()
        except ValueError:
            print("Error")

# Changing the text of the pid parameters inputs
    def set_text(self):
        self.comboBox_TypeDialog.setCurrentIndex(self.index)
        self.doubleSpinBox_KpDialog.setValue(self.kp)
        self.doubleSpinBox_KiDialog.setValue(self.ki)
        self.doubleSpinBox_KdDialog.setValue(self.kd)
        self.doubleSpinBox_SetpointDialog.setValue(self.setpoint)
        self.comboBox_TypeDialog.setCurrentIndex(self.index)
        if self.save == True:
            self.pushButton_close.setText("Save and Close")
            self.pushButton_close.setMinimumWidth(150)
        else:
            self.pushButton_close.setText("Close")
            self.pushButton_close.setMinimumWidth(60)

#both function below are to set the comboBox enabled/desabled status
    def on_type_combo_changed(self, index):
        if index == 0:  
            self.enable_pid_parameters(True, False, False)
        elif index == 1:  
            self.enable_pid_parameters(True, True, False)
        elif index == 2: 
            self.enable_pid_parameters(True, False, True)
        elif index == 3:  
            self.enable_pid_parameters(True, True, True)  
        self.index = index  

    def check_board(self, board, device, ao, ai, terminal, simulate):
        self.board = board
        self.simulate = simulate
        if self.simulate == True:
            print ('Simulated system choosed')
        elif self.board == 'arduino':
            self.com_port = device
            print('Board ', self.board)
            print('Com_port ', self.com_port)
            print(' ')
        elif self.board == 'nidaq':
            self.device = device
            self.ao_channel = ao
            self.ai_channel = ai
            self.terminal = terminal
            print('Board ', self.board)
            print('Device ', self.device)
            print('Ao channel ', self.ao_channel)
            print('Ai channel ', self.ai_channel)
            print('Termnal ', self.terminal)
            print(' ')

    def check_start(self):
        if self.simulate == True:
            print('Starting simulated system ', self.simulate)
            self.pid.simulate_system()
        elif self.board == 'arduino':
            self.pid.com_port = self.com_port
            self.pid.pid_control_arduino() 
        elif self.board == 'nidaq':
            self.pid.device = self.device
            self.pid.ao_channel = self.ao_channel
            self.pid.ai_channel = self.ai_channel
            self.pid.terminal = self.pid.term_map[self.terminal]
            self.pid.pid_control_nidaq() 
            print(self.pid.terminal, ' = ', self.pid.term_map[self.terminal])

    def enable_pid_parameters(self, kp_enabled, ki_enabled, kd_enabled):
        self.doubleSpinBox_KpDialog.setEnabled(kp_enabled)
        self.doubleSpinBox_KiDialog.setEnabled(ki_enabled)
        self.doubleSpinBox_KdDialog.setEnabled(kd_enabled)
        if ki_enabled == False:
            self.doubleSpinBox_KiDialog.setValue(0)
        if kd_enabled == False:
            self.doubleSpinBox_KdDialog.setValue(0)

    def init_plot(self): # Init the plot with the right axes 
        self.line1, = self.ax.plot([], [], 'x', label='System Output', color = 'cyan')  
        self.line2, = self.ax.plot([], [], '-', label='Setpoint', color = 'lime')  
        self.line3, = self.ax.plot([], [], '--', label='Error', color = 'red')  
        if not hasattr(self, 'ax2'):
            self.ax2 = self.ax.twinx()  # Create the error axe the first time
        self.ax.set_xlim(0, self.period*10)
        self.ax.set_ylim(-1.1*self.setpoint,1.1*self.setpoint)
        self.ax2.set_ylim(-1.1 *self.setpoint, 1.1 * self.setpoint)
        self.ax.set_xlabel('Sample (s)', color = 'white')
        self.ax.set_ylabel(self.unit, color = 'white')
        self.ax2.set_ylabel('Error', color = 'white')
        for spine in ['bottom', 'top', 'left', 'right']: # Set the axes colors to white
            self.ax.spines[spine].set_color('white')
        self.ax.tick_params(axis='x', colors='white')
        self.ax.tick_params(axis='y', colors='white')
        self.ax2.tick_params(axis='y', colors='white')
        self.ax.title.set_color('white')
        self.ax.grid(True, which='both', linestyle='--', linewidth=0.5, color='gray', alpha=0.7)
        self.ax.legend(['System Output', 'Setpoint', 'Error'])
        #self.figure.tight_layout()
        return self.line1, self.line2, self.line3

    def update_plot(self, frame):
        if self.pid is None:
            print ('self.pid is none')
            return self.line1, self.line2, self.line3
        if self.simulate == True:
            self.system_values, self.errors, self.setpoints, self.time_var, self.time_elapsed, self.controls = self.pid.update_simulated_system()
        elif self.board == 'arduino':
            self.system_values, self.errors, self.setpoints, self.time_var, self.time_elapsed, self.controls = self.pid.update_plot_arduino()
        elif self.board == 'nidaq':
            self.system_values, self.errors, self.setpoints, self.time_var, self.time_elapsed, self.controls = self.pid.update_plot_nidaq()
        
        self.system_value = self.system_values[-1]
        #if abs(self.system_value - self.setpoint) <= 0.05 * self.setpoint:         # Change the color when the system value reaches 95% of setpoint
        #    self.line1.set_color('yellow')  
        #else:
        #    self.line1.set_color('cyan')
        
        new_color = 'yellow' if abs(self.system_value - self.setpoint) <= 0.05 * self.setpoint else 'cyan'
        # Atualiza a cor apenas se for diferente da atual
        if self.line1.get_color() != new_color:
            self.line1.set_color(new_color)  # Muda a cor da linha
        
            if self.ax.get_legend() is not None:
                self.ax.get_legend().remove()

            # Força atualização das labels
            self.ax.legend(handles=[self.line1, self.line2, self.line3])

        self.ax.set_xlim(0, self.time_elapsed) # Updating
        self.line1.set_data(np.arange(len(self.system_values)) * self.period, self.system_values)
        self.line2.set_data(np.arange(len(self.setpoints)) * self.period, self.setpoints)
        self.line3.set_data(np.arange(len(self.setpoints)) * self.period, self.errors)  
        if (min(self.setpoints + self.system_values + self.errors)<0): # Reloading the axes
            xmin = min(self.setpoints + self.system_values + self.errors) * 1.1
        elif(min(self.setpoints + self.system_values + self.errors)>0):
            xmin = min(self.setpoints + self.system_values + self.errors) * 0.9
        else:
            xmin = max(self.setpoints + self.system_values + self.errors) * -0.1
        self.ax.set_ylim(xmin, max(self.setpoints + self.system_values + self.errors) *1.1)
        self.ax2.set_ylim(xmin, max(self.setpoints + self.system_values + self.errors) *1.1) # Reload the error axe
        #if len(self.system_values) > 30: # Reload the X axe after 30 datas
        #    self.ax.set_xlim((len(self.system_values) - 30) * self.period, len(self.system_values) * self.period)
        #else:
        #    self.ax.set_xlim(0, self.time_elapsed)
        self.canvas.draw()
        return self.line1, self.line2, self.line3