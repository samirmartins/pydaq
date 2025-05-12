import sys, os
import nidaqmx
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *
from pydaq.utils.signals import GuiSignals
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from ..uis.ui_PyDAQ_pid_control_NIDAQ_widget import Ui_NIDAQ_PID_Control
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from ..guis.pid_control_window_dialog import PID_Control_Window_Dialog
from .error_window_gui import Error_window

class PID_Control_NIDAQ_Widget(QWidget, Ui_NIDAQ_PID_Control):
    def __init__(self, *args):
        super(PID_Control_NIDAQ_Widget, self).__init__()
        self.setupUi(self) #Calling the functions
        self.reload_devices.clicked.connect(self.reload_devices_handler)
        self.device_combo.currentIndexChanged.connect(self.update_channels)
        self.on_unit_change()
        self.comboBox_setpoint.currentIndexChanged.connect(self.on_unit_change)
        self.on_type_combo_changed(0)
        self.comboBox_type.currentIndexChanged.connect(self.on_type_combo_changed)
        self.on_simulate_change()
        self.simulate_radio_group.buttonClicked.connect(self.on_simulate_change)
        self.pushButton_confirm.released.connect(self.show_pid_equation)
        self.pushButton_start.clicked.connect(self.show_graph_window)
        self.path_folder_browse.released.connect(self.locate_path)
        self.path_line_edit.setText(
            os.path.join(os.path.join(os.path.expanduser("~")), "Desktop")
        )
        self.signals = GuiSignals()
        self._nidaq_info() # Gathering nidaq infos 
        try:
            ao_chan = nidaqmx.system.device.Device(
                self.device_names[-1]
            ).ao_physical_chans.channel_names
            ao_def_chan = ao_chan[0]
        except BaseException:
            ao_chan = ""
            ao_def_chan = "There is no analog output in this board"
        try:
            ai_chan = nidaqmx.system.device.Device(
                self.device_names[-1]
            ).ai_physical_chans.channel_names
            ai_def_chan = ai_chan[0]
        except BaseException:
            ai_chan = ""
            ai_def_chan = "There is no analog input in this board"
        self.device_combo.addItems(self.device_type) # Setting the starting values for some widgets
        self.path_line_edit.setText(
            os.path.join(os.path.join(os.path.expanduser("~")), "Desktop")
        )
        self.ao_channel_combo.addItems(ao_chan)
        ao_def_chan_index = self.ao_channel_combo.findText(ao_def_chan)
        if ao_def_chan_index == -1:
            pass
        else:
            self.ao_channel_combo.setCurrentIndex(ao_def_chan_index)
        self.ai_channel_combo.addItems(ai_chan)
        ai_def_chan_index = self.ao_channel_combo.findText(ai_def_chan)
        if ai_def_chan_index == -1:
            pass
        else:
            self.ao_channel_combo.setCurrentIndex(ai_def_chan_index)
        self.terminal_config_combo.addItems(["Diff", "RSE", "NRSE"])

    def on_unit_change(self): # Condiction to show the line edit equation and unit
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
            self.widget_ai_channel.show()
            self.widget_ao_channel.show()
            self.widget_nidaq.show()
            self.widget_terminal_config.show()
            self.label_ai_channel.show()
            self.label_ao_channel.show()
            self.label_nidaq.show()
            self.label_terminal.show()
            self.widget_polynomial.hide()
            self.label_system_equation.hide()
            self.label_i_polinomial.hide()
        elif self.simulate is True: #Simulate = True
            self.widget_ai_channel.hide()
            self.widget_ao_channel.hide()
            self.widget_nidaq.hide()
            self.widget_terminal_config.hide()
            self.label_ai_channel.hide()
            self.label_ao_channel.hide()
            self.label_nidaq.hide()
            self.label_terminal.hide()
            self.widget_polynomial.show()
            self.label_system_equation.show()
            self.label_i_polinomial.show()

    def on_type_combo_changed(self, index): # Enable the pid parameters inputs 
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

    def show_pid_equation(self): # Method to create a image and show the pid equation using latex
        if self.doubleSpinBox_kp.isEnabled(): # Condiction to read only the inputs enable and set 'None' on desable inputs
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
        if self.kp is not None: # Create a pid equation to show when the line edits are able
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
        latex = "u(t) = " + " + ".join(equation_parts) # Equation on latex
        fig = Figure(figsize=(9, 3), facecolor='#404040') # Figure created showing the equation, without axes
        ax = fig.add_subplot(111, facecolor='#404040')
        ax.text(0.5, 0.5, f"${latex}$", fontsize=15, ha='center', va='center', color='white')
        ax.axis('off')
        canvas = FigureCanvas(fig)
        for i in reversed(range(self.image_layout.count())): # Remove the widgets from central content layout in reverse and reset the widget from parents too        
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
        self.index = self.comboBox_type.currentIndex()
        self.setpoint = self.doubleSpinBox_setpoint.value()
        self.getunit()
        self.equationvu = self.lineEdit_equationvu.text()
        self.equationuv = self.lineEdit_equationuv.text()
        self.period = self.doubleSpinBox_period.value()
        self.path = self.path_line_edit.text()
        self.save = True if self.save_radio_group.checkedId() == -2 else False
        self.board = 'nidaq'
        self.device = self.ao_channel_combo.currentText().split("/")[0]
        self.ao_channel = self.ao_channel_combo.currentText().split("/")[1]
        self.ai_channel = self.ai_channel_combo.currentText().split("/")[1]
        self.terminal = self.terminal_config_combo.currentText()
        plot_window = PID_Control_Window_Dialog()
        plot_window.check_board(self.board, self.device, self.ao_channel, self.ai_channel, self.terminal, self.simulate)
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
    
    def _nidaq_info(self):
        """Gathering NIDAQ info""" # Getting all available devices
        self.device_names = []
        self.device_categories = []
        self.device_type = []
        self.local_system = nidaqmx.system.System.local()
        for device in self.local_system.devices:
            self.device_names.append(device.name)
            self.device_categories.append(device.product_category)
            self.device_type.append(device.product_type)

    def update_channels(self): # Changing availables channels if device changes
        new_ao_channels = nidaqmx.system.device.Device( # Discovering new ao/ai channels
            self.device_names[self.device_type.index(self.device_combo.currentText())]
        ).ao_physical_chans.channel_names
        new_ai_channels = nidaqmx.system.device.Device(
            self.device_names[self.device_type.index(self.device_combo.currentText())]
        ).ai_physical_chans.channel_names
        try: # Default channel
            default_ao_channel = new_ao_channels[0]
        except BaseException:
            default_ao_channel = "There is no analog output in this board"
        try:
            default_ai_channel = new_ai_channels[0]
        except BaseException:
            default_ai_channel = "There is no analog input in this board"
        self.ao_channel_combo.clear() # Rewriting new ai channels into the right place
        self.ai_channel_combo.clear()
        self.ao_channel_combo.addItems(new_ao_channels)
        self.ai_channel_combo.addItems(new_ai_channels)
        ao_defchan_index = self.ao_channel_combo.findText(default_ao_channel)
        if ao_defchan_index == -1:
            pass
        else:
            self.ao_channel_combo.setCurrentIndex(ao_defchan_index)
        ai_defchan_index = self.ai_channel_combo.findText(default_ai_channel)
        if ai_defchan_index == -1:
            pass
        else:
            self.ai_channel_combo.setCurrentIndex(ai_defchan_index)

    def reload_devices_handler(self):
        """Updates the devices combo box"""
        self._nidaq_info() # If the signal is not disconnect, it will run into a warning
        self.device_combo.currentIndexChanged.disconnect(self.update_channels)
        self.device_combo.clear() # Updating items on combo box
        self.device_combo.addItems(self.device_type)
        self.device_combo.currentIndexChanged.connect(self.update_channels)  # Reconnecting the signal