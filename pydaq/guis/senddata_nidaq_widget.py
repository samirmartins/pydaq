import os
import nidaqmx
import numpy as np

from PySide6.QtWidgets import QFileDialog, QWidget

from ..uis.ui_PyDAQ_send_data_NIDAQ_widget import Ui_NIDAQ_SendData_W
from .error_window_gui import Error_window
from ..utils import *

from ..send_data import SendData


class SendData_NIDAQ_Widget(QWidget, Ui_NIDAQ_SendData_W):
    def __init__(self, *args):
        super(SendData_NIDAQ_Widget, self).__init__()
        self.setupUi(self)

        # Gathering nidaq info
        self._nidaq_info()

        try:
            chan = nidaqmx.system.device.Device(
                self.device_names[0]
            ).ao_physical_chans.channel_names
            defchan = chan[0]
        except BaseException:
            chan = ""
            defchan = ""

        # Setting the starting values for some widgets
        self.device_combo.addItems(self.device_type)
        self.path_line_edit.setText(
            os.path.join(os.path.join(os.path.expanduser("~")), "Desktop", "data.dat")
        )
        self.channel_combo.addItems(chan)

        defchan_index = self.channel_combo.findText(defchan)

        if defchan_index == -1:
            pass
        else:
            self.channel_combo.setCurrentIndex(defchan_index)

        # Connecting Signals
        self.path_folder_browse.released.connect(self.locate_path)
        self.start_send_data.released.connect(self.start_func_send_data)
        self.device_combo.currentIndexChanged.connect(self.update_channels)

    def start_func_send_data(self):  # Start sending data
        try:
            # Instantiating the SendData class
            s = SendData()

            s.ao_max = self.out_range_max_in.value()
            s.ao_min = self.out_range_min_in.value()

            # Reading data from defined path
            s.path = self.path_line_edit.text()
            s.data = np.loadtxt(s.path)

            # Check if max(data) < self.ao_max
            if (max(s.data) > float(s.ao_max)) or (min(s.data) < float(s.ao_min)):
                s._range_error()
                s.error_max = True
            else:
                s.error_max = False

            # Separating variables
            s.device = self.channel_combo.currentText().split("/")[0]
            s.channel = self.channel_combo.currentText().split("/")[1]
            s.ts = self.Ts_in.value()
            s.plot = True if self.plot_radio_group.checkedId() == -2 else False
            s.error_path = False

        except BaseException:
            error_w = Error_window()
            error_w.exec()
            s.error_path = True

        if not s.error_path:
            # Calling send data method
            s.send_data_nidaq()

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

    def _nidaq_info(self):
        """Gathering NIDAQ info"""

        # Getting all available devices
        self.device_names = []
        self.device_categories = []
        self.device_type = []
        self.local_system = nidaqmx.system.System.local()

        for device in self.local_system.devices:
            self.device_names.append(device.name)
            self.device_categories.append(device.product_category)
            self.device_type.append(device.product_type)

    def update_channels(self):
        # Changing availables channels if device changes

        # Discovering new ao channels
        new_ao_channels = nidaqmx.system.device.Device(
            self.device_names[self.device_type.index(self.device_combo.currentText())]
        ).ao_physical_chans.channel_names

        # Default channel
        try:
            default_channel = new_ao_channels[0]
        except:
            default_channel = "There is no analog output in this board"

        # Rewriting new ai channels into the right place
        self.channel_combo.clear()
        self.channel_combo.addItems(new_ao_channels)
        defchan_index = self.channel_combo.findText(default_channel)

        if defchan_index == -1:
            pass
        else:
            self.channel_combo.setCurrentIndex(defchan_index)
        pass
