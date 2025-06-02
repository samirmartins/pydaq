import os
import time
import numpy as np
import sympy as sp
from scipy.signal import dlti, dlsim
import scipy.signal as signal
import serial
import serial.tools.list_ports
from pydaq.utils.base import Base
import os
import serial
import serial.tools.list_ports
import matplotlib.pyplot as plt
import warnings
import nidaqmx
from sympy import symbols, parse_expr
from nidaqmx.constants import TerminalConfiguration

class PIDControl(Base): 
    def __init__( 
        self, 
        Kp, 
        Ki, 
        Kd, 
        setpoint=0.0, 
        numerator = '1', 
        denominator = 's+0.2', 
        calibration_equation_vu = None, 
        calibration_equation_uv = None, 
        unit='Voltage (V)', 
        period=1 
        ):
        super().__init__() #Inicializating the matematical control
        self.Kp = float(Kp)
        self.Ki = float(Ki)
        self.Kd = float(Kd)
        self.disturbe = 0
        self.setpoint = float(setpoint)
        self.numerator = numerator
        self.denominator = denominator
        self.calibration_equation_vu = calibration_equation_vu
        self.calibration_equation_uv = calibration_equation_uv
        self.integral = 0.0
        self.previous_error = 0.0
        self.previous_output = 0.0
        self.period = period
        self.device = "Dev1" # To nidaq
        self.ao_channel="ao0"
        self.ai_channel="ai0"
        self.terminal="Diff"
        self.com_port = 'COM1' # To arduino  # Default COM port
        self.a = 0.2 # To simulated

    def update(self, feedback_value):
        error = self.setpoint - feedback_value
        self.integral = self.integral + error * self.period
        derivative = (error - self.previous_error) / self.period
        output = self.Kp * error + self.Ki * self.integral + self.Kd * derivative
        self.previous_error = error
        self.previous_output = output
        return output, error

    def pid_control_arduino(self):
        self.time_elapsed = 0.0
        self.feedback_value = 0
        self.feedback_calibrated = 0
        self.control_voltage = 0
        self.control_unit = 0
        self.control = 0

        self.com_ports = [i.description for i in serial.tools.list_ports.comports()] # COM ports
        self._open_serial() # Oppening ports
        self.arduino_ai_bits = 10 # Arduino ADC resolution (in bits)
        self.ard_ao_max, self.ard_ao_min = 5, 0 # Arduino analog input max and min
        self.ard_vpb = (self.ard_ao_max - self.ard_ao_min) / ((2 ** self.arduino_ai_bits)-1) # Value per bit - Arduino
        self.ser.reset_input_buffer()
        time.sleep(1)  # Wait for Arduino and Serial to start up
        self.title = f"PYDAQ - Step Response (Arduino), Port: {self.com_port}" # Start updatable plot

# Updating the Datas to plot
    def update_plot_arduino(self):
        if self.ser.in_waiting > 64:  # If there's more than 64 bits accumulated
            self.ser.reset_input_buffer()
        self.time_elapsed += self.period # Clock
        data = self.ser.read(14).decode("UTF-8") # Get the feedback sensor value
        try:
            self.feedback_value =  int(data.split()[-2]) * self.ard_vpb
        except (IndexError, ValueError):
            #print('using the data value ',self.feedback_value)
            self.feedback_value = self.feedback_value # Use the last valid value

        self.feedback_calibrated = self.calibrationuv(self.feedback_value) #Calibration by U(v)
        self.control_unit, error = self.update(self.feedback_calibrated) # Get the control value
        self.control_voltage = self.calibrationvu(self.control_unit) #Calibration by V(u)
        self.control = self.control_voltage
        if(self.control <= 0):
            self.control = 0
        elif (self.control >=5):
            self.control = 5
        self.duty_cycle_control = int((self.control/self.ard_ao_max) *255) # Change to a duty cicle
        self.ser.write(f"{self.duty_cycle_control}\n".encode("utf-8")) # Send data to arduino 
        self.error = error
        #print(f"Control (V)/(U): {self.control:.2f} / {self.control_unit:.2f}; Feedback (V)/(U): {self.feedback_value:.2f} / {self.feedback_calibrated:.2f}; Setpoint(U) {self.setpoint:.2f}; error (U) {self.error}")
        return self.feedback_calibrated, self.error, self.setpoint, self.control

    def pid_control_nidaq(self): #Inicializating the updating nidaq values
        terminal_config = self.terminal # Terminal configuration
        self._nidaq_info() # Gathering nidaq info
        self.task_ai = nidaqmx.Task()
        self.task_ao = nidaqmx.Task()   
        self.task_ai.ai_channels.add_ai_voltage_chan(
            self.device + "/" + self.ai_channel, terminal_config=terminal_config
        )
        self.task_ao.ao_channels.add_ao_voltage_chan(
            self.device + "/" + self.ao_channel,
            min_val=0.0,  # Max value to usb 6009
            max_val=5.0   # Max value to usb 6009
        )
        self.time_elapsed = 0.0
        self.feedback_value = 0
        self.control = 0
        self.control_unit = 0
        self.feedback_calibrated = 0

    def update_plot_nidaq(self):
        self.time_elapsed += self.period # Clock
        self.feedback_value = self.task_ai.read()
        self.feedback_calibrated = self.calibrationuv(self.feedback_value)
        self.control_voltage = self.calibrationvu(self.control_unit)
        self.control = self.control_voltage

        self.control = self.setpoint
        if(self.control <= 0):
            self.control = 0
        elif (self.control >=5):
            self.control = 5
        self.task_ao.write(self.control)
        self.error = self.setpoint - self.feedback_calibrated

        #print(f"Control (V)/(U): {self.control:.2f} / {self.control_unit:.2f}; Feedback (V)/(U): {self.feedback_value:.2f} / {self.feedback_calibrated:.2f}; Setpoint(U) {self.setpoint:.2f}; error (U) {self.error}")
        return self.feedback_calibrated, self.error, self.setpoint, self.control

    def simulate_system(self):
        self.feedback_voltages = []
        self.controls_voltages = []
        self.error = 0
        self.time_elapsed = 0.0
        self.feedback_value = 0
        self.control = 0
        self.control_voltage = 0
        self.feedback_calibrated = 0
        numerator_cont = self.parse_polynomial(self.numerator)
        denominator_cont = self.parse_polynomial(self.denominator)
        self.system_cont = signal.TransferFunction(numerator_cont, denominator_cont)

    def update_simulated_system(self):
        ordem = max(len(self.feedback_voltages), len(self.controls_voltages))  # Estimate the ordem
        while len(self.feedback_voltages) < ordem:
            self.feedback_voltages.insert(0, 0.0)  # Fill '0' 
        while len(self.controls_voltages) < ordem:
            self.controls_voltages.insert(0, 0.0)
        self.control_unit, error = self.update(self.feedback_calibrated) 
        self.control_unit = self.control_unit - self.disturbe
        self.control_voltage = self.calibrationvu(self.control_unit)
        self.control = self.control_voltage

        self.feedback_calibrated = self.calibrationuv(self.feedback_value)
        self.controls_voltages.append(self.control_voltage)
        self.feedback_voltages.append(self.feedback_value) # This one goes to re-update the system and is in 'voltage'

        _, self.feedback_value = self.get_value_simulate_system(self.system_cont, self.period, self.control, self.feedback_value)  # Get the system response value by euler descritization of system
        self.error = error
        self.time_elapsed += self.period # Clock        # Att the datas

        return self.feedback_calibrated, self.error, self.setpoint, self.control

    def calibrationvu(self, output):
        if not self.calibration_equation_vu.strip():
            return output
        else:
            equation = parse_expr(self.calibration_equation_vu)
            output_calibrated = equation.subs('x', output) # X is the variable used
            output_calibrated = float(output_calibrated)
            return output_calibrated

    def calibrationuv(self, output):
        if not self.calibration_equation_uv.strip():
            return output
        else:
            equation = parse_expr(self.calibration_equation_uv)
            output_calibrated = equation.subs('x', output) # X is the variable used
            output_calibrated = float(output_calibrated)
            return output_calibrated

    def parse_polynomial(self,poly_str):
        s = sp.symbols('s')
        poly_expr = sp.sympify(poly_str)
        coeffs = sp.Poly(poly_expr, s).all_coeffs()
        return [float(c) for c in coeffs]

    def get_value_simulate_system(self, system, period, control, x0):

        time_control = np.linspace(0, period, 100)  
        input_control_signal = np.full_like(time_control, control)
        time_array_output, system_output, _ = signal.lsim(system, input_control_signal, time_control,x0)
        last_time = time_array_output[-1]
        last_output = system_output[-1]
        return last_time, last_output