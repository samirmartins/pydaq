import os
import nidaqmx

from PySide6.QtWidgets import QFileDialog, QWidget

from ..uis.ui_PyDAQ_step_response_NIDAQ_widget import Ui_NIDAQ_StepResponse_W
from .error_window_gui import Error_window
from ..utils import *

from ..step_response import StepResponse


class StepResponse_NIDAQ_Widget(QWidget, Ui_NIDAQ_StepResponse_W):
    def __init__(self, *args):
        super(StepResponse_NIDAQ_Widget, self).__init__()
        self.setupUi(self)

        # Gathering nidaq info
        self._nidaq_info()

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

        # Setting the starting values for some widgets
        self.device_combo.addItems(self.device_type)
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

        # Connecting Signals
        self.path_folder_browse.released.connect(self.locate_path)
        self.start_step_response.released.connect(self.start_func_step_response)
        self.device_combo.currentIndexChanged.connect(self.update_channels)

    def start_func_step_response(self):
        try:
            # Instantiating the StepResponse class
            s = StepResponse()

            # Cleaning data
            s.output, s.input, s.time_var = [], [], []

            # Separating variables
            # Input and output range
            s.device = self.device_combo.currentText().split("/")[0]
            s.ao_channel = self.ao_channel_combo.currentText().split("/")[1]
            s.ai_channel = self.ai_channel_combo.currentText().split("/")[1]
            s.terminal = s.term_map[self.terminal_config_combo.currentText()]
            s.step_max = self.step_range_max_in.value()
            s.step_min = self.step_range_min_in.value()
            s.ts = self.Ts_in.value()
            s.session_duration = self.sesh_dur_in.value()
            s.step_time = self.step_on_s_in.value()
            s.plot = True if self.plot_radio_group.checkedId() == -2 else False
            s.save = True if self.save_radio_group.checkedId() == -2 else False
            s.path = self.path_line_edit.text()
            s.error_path = False

        except BaseException:
            error_w = Error_window()
            error_w.exec()

        # Calling send data method
        if not s.error_path:
            s.step_response_nidaq()

    def locate_path(self):  # Calling the Folder Browser Widget
        output_folder_path = QFileDialog.getExistingDirectory(
            self, caption="Choose a folder to save the data file"
        )
        if output_folder_path == "":
            pass
        else:
            self.path_line_edit.setText(output_folder_path.replace("/", "\\"))

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

        # Discovering new ao/ai channels
        new_ao_channels = nidaqmx.system.device.Device(
            self.device_names[self.device_type.index(self.device_combo.currentText())]
        ).ao_physical_chans.channel_names
        new_ai_channels = nidaqmx.system.device.Device(
            self.device_names[self.device_type.index(self.device_combo.currentText())]
        ).ai_physical_chans.channel_names

        # Default channel
        try:
            default_ao_channel = new_ao_channels[0]
        except BaseException:
            default_ao_channel = "There is no analog output in this board"
        try:
            default_ai_channel = new_ai_channels[0]
        except BaseException:
            default_ai_channel = "There is no analog input in this board"

        # Rewriting new ai channels into the right place
        self.ao_channel_combo.clear()
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
