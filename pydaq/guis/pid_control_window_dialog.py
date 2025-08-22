import sys, os
import serial
import serial.tools.list_ports
import numpy as np
import warnings
import time
import asyncio
import qasync
import queue
import threading
from pydaq.utils.base import Base
from PySide6 import QtWidgets
from PySide6.QtWidgets import QDialog, QFileDialog, QApplication, QWidget, QVBoxLayout, QPushButton, QSizePolicy
from PySide6.QtGui import *
from PySide6.QtCore import *
from ..uis.ui_PyDAQ_pid_control_window_dialog import Ui_Dialog_Plot_PID_Window
from ..pid_control import PIDControl
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure


class PID_Control_Window_Dialog(QDialog, Ui_Dialog_Plot_PID_Window, Base):

# Signal to send back to QWidget the values
    send_values = Signal(float, float, float, int, float)
    update_plot_signal = Signal()  # Added next to send_values


    def __init__(self, *args):
        super(PID_Control_Window_Dialog, self).__init__()
        self.setupUi(self)

        self.pushButton_startstop.clicked.connect(self.stopstart)
        self.pushButton_close.clicked.connect(self.go_back)
        self.pushButton_apply.clicked.connect(self.apply_parameters)
        self.comboBox_TypeDialog.currentIndexChanged.connect(self.on_type_combo_changed)
        self.paused = False
        self.pid = None
        self.control_running = False

        self.path = os.path.join(os.path.join(os.path.expanduser("~")), "Desktop") # Defining default path
        self.figure = plt.figure(figsize =(6.4,4.8), facecolor='#404040') #Starting the canvas
        self.figure.patch.set_facecolor('#404040')  # External background
        self.ax = self.figure.add_subplot(111, facecolor='#505050')  # Output graph
        self.ax2 = self.ax.twinx()
        self.canvas = FigureCanvas(self.figure)
        self.image_layout.addWidget(self.canvas)
        self.canvas.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.canvas.setMinimumHeight(350)

        self.k = 0
        self.system_values = []
        self.errors = []
        self.setpoints = []
        self.controls = []
        self.time_var = []
        self.elapsed_time = 0.0
        
        self.lock = threading.Lock()
        self.update_plot_signal.connect(self._update_plot_gui_safe)


    def stopstart(self):
        self.paused = not self.paused
        if self.paused:
            self.plot_running = False
            self.control_running = False
            # saves the time accumulated so far
            self.elapsed_time += time.perf_counter() - self.t0
            self.pushButton_startstop.setText("START")
        else:
            self.plot_running = True
            self.control_running = True
            self.pushButton_startstop.setText("STOP")
            self.start_threaded_control()
            
    def go_back(self): #def to save and go back
        if hasattr(self, "_already_closed") and self._already_closed:
            return
        self._already_closed = True
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
            try:
                if self.pid.task_ao:
                    self.pid.task_ao.write(0)
                    self.pid.task_ao.close()
                if self.pid.task_ai:
                    self.pid.task_ai.close()
            except Exception as e:
                print("Warning when closing NI-DAQ tasks:", e)

        self.plot_running = False
        self.control_running = False
        self.close()

    def closeEvent(self, event):
        # Ensures the same behavior as the "CLOSE" or "SAVE AND CLOSE" button
        if not hasattr(self, "_already_closed"):
            self.go_back()
        event.accept()         # The event needs to be explicitly accepted for PySide6 to close the window

    def apply_parameters(self): #apply all pid parameters while the event goes on
        try:
            self.setpoint = self.doubleSpinBox_SetpointDialog.value()
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
        self.disturbe = self.doubleSpinBox_DisturbeDialog.value() #changing the disturbe
        self.pid.disturbe = self.disturbe

    # Both function below are to set the comboBox enabled/desabled status
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

    # Defining the fuctions
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
        self.init_plot()
        self.start_control()

 # Inicializate variables and start controling 
    def start_control(self):
        try:
            self.pid = PIDControl(
                self.kp, self.ki, self.kd, self.setpoint,
                self.numerator, self.denominator,
                self.calibration_equation_vu, self.calibration_equation_uv,
                self.unit, self.period
            )
            self.check_start()
            self.start_threaded_control()
        except Exception as e:
            print("Error starting control:", e)

    def start_threaded_control(self):
        self.data_queue = queue.Queue()
        self.plot_running = True
        self.control_running = True
        self.ts = self.period
        self.k = 1

        self.control_thread = threading.Thread(target=self.control_loop_task, daemon=True)
        self.plot_thread = threading.Thread(target=self.update_plot_task, daemon=True)
        self.save_thread = threading.Thread(target=self.save_data_task, daemon=True)

        self.control_thread.start()
        self.plot_thread.start()
        self.save_thread.start()

    def control_loop_task(self):
        st_worker = time.perf_counter()
        self.t0 = st_worker
        self.k = 0

        while not self.paused:
            if not self.control_running:
                break

            with self.lock:
                if self.simulate:
                    self.output, self.error, self.setpoint, self.control = self.pid.update_simulated_system()
                elif self.board == 'arduino':
                    self.output, self.error, self.setpoint, self.control = self.pid.update_plot_arduino()
                elif self.board == 'nidaq':
                    self.output, self.error, self.setpoint, self.control = self.pid.update_plot_nidaq()

            time_now = (time.perf_counter() - self.t0) + self.elapsed_time
            
            self.data_queue.put((time_now, self.output, self.error, self.setpoint, self.control))

            target_time = st_worker + (self.k + 1) * self.ts
            wait_time = target_time - time.perf_counter()
            if wait_time > 0:
                time.sleep(wait_time)
            else:
                warnings.warn("Loop overran the period. You CANNOT trust time precision for this sample.")

            self.k += 1

    def _update_plot(self):
        if len(self.time_var) == 0:
            return

        self.line1.set_data(self.time_var, self.system_values)
        self.line2.set_data(self.time_var, self.setpoints)
        self.line3.set_data(self.time_var, self.errors)

        self.ax.set_xlim(0, max(self.time_var))
        y_min = min(min(self.system_values, default=0), self.setpoint * -1.1)
        y_max = max(max(self.system_values, default=0), self.setpoint * 1.1)
        self.ax.set_ylim(y_min, y_max)
        self.ax2.set_ylim(y_min, y_max)

        self.canvas.draw()

    def check_start(self):
        if self.simulate == True:
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

# Changing the text of the pid parameters inputs
    def set_text(self):
        self.comboBox_TypeDialog.setCurrentIndex(self.index)
        self.doubleSpinBox_KpDialog.setValue(self.kp)
        self.doubleSpinBox_KiDialog.setValue(self.ki)
        self.doubleSpinBox_KdDialog.setValue(self.kd)
        self.doubleSpinBox_SetpointDialog.setValue(self.setpoint)
        if self.save == True:
            self.pushButton_close.setText("SAVE AND CLOSE")
            self.pushButton_close.setMinimumWidth(180)
        else:
            self.pushButton_close.setText("CLOSE")
            self.pushButton_close.setMinimumWidth(100)

    def check_board(self, board, device, ao, ai, terminal, simulate):
        self.board = board
        self.simulate = simulate
        if self.simulate == True:
            print ('Starting simulation ...')
        elif self.board == 'arduino':
            self.com_port = device
            print ('Starting control in arduino ...')
        elif self.board == 'nidaq':
            self.device = device
            self.ao_channel = ao
            self.ai_channel = ai
            self.terminal = terminal
            print ('Starting control in nidaq ...')

    def enable_pid_parameters(self, kp_enabled, ki_enabled, kd_enabled):
        self.doubleSpinBox_KpDialog.setEnabled(kp_enabled)
        self.doubleSpinBox_KiDialog.setEnabled(ki_enabled)
        self.doubleSpinBox_KdDialog.setEnabled(kd_enabled)
        if ki_enabled == False:
            self.doubleSpinBox_KiDialog.setValue(0)
        if kd_enabled == False:
            self.doubleSpinBox_KdDialog.setValue(0)

    def init_plot(self):
        self.line1, = self.ax.plot([], [], 'x', label='System Output', color='cyan')
        self.line2, = self.ax.plot([], [], '-', label='Setpoint', color='lime')
        self.line3, = self.ax2.plot([], [], '--', label='Error', color='red')

        if not hasattr(self, 'ax2'):
            self.ax2 = self.ax.twinx()

        self.ax.set_xlim(0, self.period * 10)
        self.ax.set_ylim(-1.1 * self.setpoint, 1.1 * self.setpoint)
        self.ax2.set_ylim(-1.1 * self.setpoint, 1.1 * self.setpoint)

        self.ax.set_xlabel('Sample (s)')
        self.ax.set_ylabel(self.unit)
        self.ax2.set_ylabel('Error')

        # Force label color
        self.ax.xaxis.label.set_color('white')      # Sample (s)
        self.ax.yaxis.label.set_color('white')      # Voltage (V)
        self.ax2.yaxis.label.set_color('white')     # Error

        # Force tick and border color
        for spine in ['bottom', 'top', 'left', 'right']:
            self.ax.spines[spine].set_color('white')
            self.ax2.spines[spine].set_color('white')

        self.ax.tick_params(axis='x', colors='white')
        self.ax.tick_params(axis='y', colors='white')
        self.ax2.tick_params(axis='y', colors='white')

        self.ax.title.set_color('white')
        self.ax.grid(True, which='both', linestyle='--', linewidth=0.5, color='gray', alpha=0.7)
        self.ax.legend(loc='upper left')
        self.ax2.legend(loc='upper right')

        self.figure.subplots_adjust(bottom=0.25)

    def update_plot_task(self):
        while self.plot_running:
            self.update_plot_signal.emit()
            time.sleep(self.ts + 0.5)

    def save_data_task(self):
        while self.control_running or not self.data_queue.empty():
            try:
                item = self.data_queue.get(timeout=0.05)
            except queue.Empty:
                continue
            t, y, e, s, u = item
            self.time_var.append(t)
            self.system_values.append(y)
            self.errors.append(e)
            self.setpoints.append(s)
            self.controls.append(u)

    def _update_plot_gui_safe(self):
        with self.lock:
            self._update_plot()
            self.canvas.draw()