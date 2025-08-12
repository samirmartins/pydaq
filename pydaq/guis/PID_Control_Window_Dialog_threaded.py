
import sys, os
import serial
import serial.tools.list_ports
import numpy as np
import time
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
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

class PID_Control_Window_Dialog(QDialog, Ui_Dialog_Plot_PID_Window, Base):
    send_values = Signal(float, float, float, int, float)

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

        self.path = os.path.join(os.path.expanduser("~"), "Desktop")
        self.figure = plt.figure(figsize =(6.4,4.8), facecolor='#404040')
        self.figure.patch.set_facecolor('#404040')
        self.ax = self.figure.add_subplot(111, facecolor='#505050')
        self.ax2 = self.ax.twinx()
        self.canvas = FigureCanvas(self.figure)
        self.image_layout.addWidget(self.canvas)
        self.canvas.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.canvas.setMinimumHeight(350)

        self.k = 1
        self.system_values = []
        self.errors = []
        self.setpoints = []
        self.controls = []
        self.time_var = []

        self.lock = threading.Lock()

    def stopstart(self):
        self.paused = not self.paused
        if self.paused:
            self.plot_running = False
            self.control_running = False
            self.pushButton_startstop.setText("START")
        else:
            self.plot_running = True
            self.control_running = True
            self.pushButton_startstop.setText("STOP")
            self.start_threaded_control()

    def go_back(self):
        if self.save:
            print("\nSaving data ...")
            self._save_data(self.time_var, "time.dat")
            self._save_data(self.system_values, "output.dat")
            self._save_data(self.errors, "error.dat")
            self._save_data(self.setpoints, "setpoint.dat")
            self._save_data(self.controls, "controls.dat")
            print("\nData saved ...")

        self.send_values.emit(self.kp, self.ki, self.kd, self.index, self.setpoint)

        if self.simulate:
            print('Closing')
        elif self.board == 'arduino':
            self.pid.ser.write(b"0")
            self.pid.ser.close()
        elif self.board == 'nidaq':
            self.pid.task_ao.write(0)
            self.pid.task_ao.close()
            self.pid.task_ai.close()
        self.plot_running = False
        self.control_running = False
        self.close()

    def closeEvent(self, event):
        self.go_back()
        event.accept()

    def apply_parameters(self):
        try:
            self.setpoint = self.doubleSpinBox_SetpointDialog.value()
            if self.pid:
                self.pid.setpoint = self.setpoint
        except ValueError:
            pass
        if self.doubleSpinBox_KpDialog.isEnabled():
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
        self.disturbe = self.doubleSpinBox_DisturbeDialog.value()
        self.pid.disturbe = self.disturbe

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
        self.path = path if path else os.path.expanduser("~/Desktop")
        self.save = save
        self._check_path()
        self.set_text()
        self.on_type_combo_changed(self.index)
        self.init_plot()
        self.start_control()

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
        self.t0 = time.perf_counter()
        self.ts = self.period
        self.k = 1

        self.control_thread = threading.Thread(target=self.control_loop_task, daemon=True)
        self.plot_thread = threading.Thread(target=self.update_plot_task, daemon=True)
        self.save_thread = threading.Thread(target=self.save_data_task, daemon=True)

        self.control_thread.start()
        self.plot_thread.start()
        self.save_thread.start()

    def control_loop_task(self):
        while not self.paused:
            if not self.control_running:
                break

            target_time = self.t0 + self.k * self.ts
            wait_time = target_time - time.perf_counter()
            if wait_time > 0:
                time.sleep(wait_time)

            with self.lock:
                if self.simulate:
                    self.output, self.error, self.setpoint, self.control = self.pid.update_simulated_system()
                elif self.board == 'arduino':
                    self.output, self.error, self.setpoint, self.control = self.pid.update_plot_arduino()
                elif self.board == 'nidaq':
                    self.output, self.error, self.setpoint, self.control = self.pid.update_plot_nidaq()

            timestamp = time.perf_counter() - self.t0
            self.data_queue.put((timestamp, self.output, self.error, self.setpoint, self.control))

            self.k += 1

    def update_plot_task(self):
        while self.plot_running:
            with self.lock:
                self._update_plot()
                self.canvas.draw()
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
