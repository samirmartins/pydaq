import os
import serial
import serial.tools.list_ports
import numpy as np

from PySide6.QtWidgets import QFileDialog, QWidget
from pydaq.utils.signals import GuiSignals

from ..uis.ui_PyDAQ_send_data_Arduino_widget import Ui_Arduino_SendData_W
from .error_window_gui import Error_window

from ..send_data import SendData


class SendData_Arduino_Widget(QWidget, Ui_Arduino_SendData_W):
    def __init__(self, *args):
        super(SendData_Arduino_Widget, self).__init__()
        self.setupUi(self)

        # Connecting Signals
        self.reload_devices.released.connect(self.update_com_ports)
        self.path_folder_browse.released.connect(self.locate_path)
        self.start_send_data.released.connect(self.start_func_send_data)
        self.label_warning.hide()
        self.plot_radio_group.buttonToggled.connect(self._update_warning_label)
        self.signals = GuiSignals()

        # Setting the starting values for some widgets
        self.update_com_ports()
        self.path_line_edit.setText(
            os.path.join(os.path.join(os.path.expanduser("~")), "Desktop", "data.dat")
        )

    def _update_warning_label(self):
        if self.yes_rt_plot_radio.isChecked():
            self.label_warning.show()
        else:
            self.label_warning.hide()
            
    def update_com_ports(self):  # Updating com ports
        self.com_ports = [i.description for i in serial.tools.list_ports.comports()]
        selected = self.device_combo.currentText()

        self.device_combo.clear()
        self.device_combo.addItems(self.com_ports)
        index_current = self.device_combo.findText(selected)

        if index_current == -1:
            pass
        else:
            self.device_combo.setCurrentIndex(index_current)

    def locate_path(self):  # Calling the File Browser Widget
        data_path = QFileDialog.getOpenFileName(
            self,
            caption="Search for the data file",
            filter="DAT Files (*.dat);;All Files (*)",
        )[0]
        if data_path == "":
            pass
        else:
            self.path_line_edit.setText(data_path.replace("/", "\\"))

    def start_func_send_data(self):  # Start sending data
        try:
            # Instantiating the SendData class
            s = SendData()

            # Restarting time and data
            s.time_var, s.data = [], []

            # Reading data from defined path and rearranjing it
            s.path = self.path_line_edit.text()
            s.data = np.loadtxt(s.path)
            s.data = list(s.data)
            s.data = [5 if i > 2.5 else 0 for i in s.data]

            # Getting the remaining values from the GUI
            s.com_port = serial.tools.list_ports.comports()[
                self.com_ports.index(self.device_combo.currentText())
            ].name
            s.ts = self.Ts_in.value()
            if self.yes_rt_plot_radio.isChecked(): # Assumindo que 'yes_radio' agora significa 'Real time'
                s.plot_mode = 'realtime'
            elif self.yes_ate_plot_radio.isChecked(): # Supondo que você criou um radio button com este nome
                s.plot_mode = 'end'
            else: # self.No_radio.isChecked()
                s.plot_mode = 'no'
            s.error_path = False

        except BaseException:
            error_w = Error_window()
            error_w.exec()
            s.error_path = True

        if not s.error_path:
            # Calling send data method
            s.send_data_arduino()
            self.signals.returned.emit(s)
