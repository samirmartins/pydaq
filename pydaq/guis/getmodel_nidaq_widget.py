import os
import nidaqmx
import serial
import serial.tools.list_ports
from sysidentpy.parameter_estimation import Estimators

from PySide6.QtWidgets import QFileDialog, QWidget

from ..uis.ui_PyDAQ_get_model_NIDAQ_widget import Ui_Arduino_GetModel_W
from .error_window_gui import Error_window
from ..utils import *

from ..get_model import GetModel
from .prbs_config_widget import PRBSConfig_W
from .getmodel_sysconfig_arduino_widget import SysIdentConfig_W


class GetModel_Nidaq_Widget(QWidget, Ui_Arduino_GetModel_W):
    def __init__(self, *args):
        super(GetModel_Nidaq_Widget, self).__init__()
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

        ai_def_chan_index = self.ai_channel_combo.findText(ai_def_chan)

        if ai_def_chan_index == -1:
            pass
        else:
            self.ai_channel_combo.setCurrentIndex(ai_def_chan_index)

        self.terminal_config_combo.addItems(["Diff", "RSE", "NRSE"])

        self.inp_signal_combo.addItem("PRBS")

        self.signal_bits = 6
        self.signal_seed = 100
        self.signal_var_tb = 1
        self.degree = 2
        self.out_lag = 3
        self.inp_lag = 3
        self.num_info_val = 6
        self.estimator = "least_squares"
        self.ext_lsq = False
        self.perc_value = 15
        self.ao_channel = "ao0"
        self.ai_channel = "ai0"

        estimators_list = [i for i in Estimators.__dict__.keys() if i[:1] != "_"]
        self.estimators_handle_dict = dict()

        for i in estimators_list:
            self.estimators_handle_dict[" ".join(i.split("_")).capitalize()] = i

        # Connecting signals
        self.path_folder_browse.released.connect(self.locate_path)
        self.start_get_model.released.connect(self.start_func_get_model)
        self.device_combo.currentIndexChanged.connect(self.update_channels)
        self.reload_devices.released.connect(self.reload_devices_handler)
        self.config_signal_button.released.connect(self.open_sig_config)
        self.system_settings_button.released.connect(self.open_sysident_config)

    def locate_path(self):  # Calling the Folder Browser Widget
        output_folder_path = QFileDialog.getExistingDirectory(
            self, caption="Choose a folder to save the data file"
        )
        if output_folder_path == "":
            pass
        else:
            self.path_line_edit.setText(output_folder_path.replace("/", "\\"))

    def open_sig_config(self):
        if self.inp_signal_combo.currentText() == "PRBS":
            # Creating Instance of the config window
            config = PRBSConfig_W()

            # Setting default values
            config.ui.prbs_bits_in.setValue(self.signal_bits)
            config.ui.prbs_seed_in.setText(str(self.signal_seed))
            config.ui.prbs_tb_var_in.setValue(self.signal_var_tb)
            config.ui.prbs_seed_in.setCursorPosition(len(str(self.signal_seed)))

            # Executing the config window
            config.exec()

            # Fetching data
            self.signal_bits = config.ui.prbs_bits_in.value()
            self.signal_seed = int(config.ui.prbs_seed_in.text())
            self.signal_var_tb = config.ui.prbs_tb_var_in.value()

    def open_sysident_config(self):
        # Creating Instance of the config window
        config = SysIdentConfig_W()

        # Setting default values
        config.ui.degree_sysid_in.setValue(self.degree)
        config.ui.out_lag_sysid_in.setValue(self.out_lag)
        config.ui.inp_lag_sysid_in.setValue(self.inp_lag)
        config.ui.num_inf_value_sysid_in.setValue(self.num_info_val)
        config.ui.esti_sysid_in.addItems(list(self.estimators_handle_dict.keys()))

        # Handling the default value for radio button
        if self.ext_lsq:
            config.ui.true_ext_lsq.setChecked(True)
        else:
            config.ui.false_ext_lsq.setChecked(True)

        config.ui.perc_data_val_in.setValue(self.perc_value)

        # Handling the past estimator value
        for key_d, value_d in self.estimators_handle_dict.items():
            if value_d == self.estimator:
                config.ui.esti_sysid_in.setCurrentText(key_d)

        # Executing the config window
        config.exec()

        # Fetching the data from the popup to the main widget
        self.degree = config.ui.degree_sysid_in.value()
        self.out_lag = config.ui.out_lag_sysid_in.value()
        self.inp_lag = config.ui.inp_lag_sysid_in.value()
        self.num_info_val = config.ui.num_inf_value_sysid_in.value()
        self.estimator = self.estimators_handle_dict[
            config.ui.esti_sysid_in.currentText()
        ]
        self.ext_lsq = (
            True if config.ui.extended_lsq_radio_group.checkedId() == -2 else False
        )
        self.perc_value = config.ui.perc_data_val_in.value()

    def start_func_get_model(self):  # Start getting model
        try:
            # Instantiating the GetModel class
            g = GetModel()

            # Getting the values from the GUI

            g.device = self.ao_channel_combo.currentText().split("/")[0]
            g.ao_channel = self.ao_channel_combo.currentText().split("/")[1]
            g.ai_channel = self.ai_channel_combo.currentText().split("/")[1]
            g.terminal = g.term_map[self.terminal_config_combo.currentText()]
            g.ts = self.Ts_in.value()
            g.start_save_time = self.save_time_in.value()
            g.session_duration = self.sesh_dur_in.value()
            g.plot = True if self.plot_radio_group.checkedId() == -2 else False
            g.save = True if self.save_radio_group.checkedId() == -2 else False
            g.path = self.path_line_edit.text()

            g.prbs_bits = self.signal_bits
            g.prbs_seed = self.signal_seed
            g.var_tb = self.signal_var_tb

            g.degree = self.degree
            g.out_lag = self.out_lag
            g.inp_lag = self.inp_lag
            g.num_info_val = self.num_info_val
            g.estimator = self.estimator
            g.ext_lsq = self.ext_lsq
            g.perc_value = self.perc_value

            # Checking if a path was set
            if self.path_line_edit.text() == "":
                raise BaseException

            # Restarting variables
            g.data = []
            g.time_var = []
            g.out_read = []
            g.error_path = False

        except BaseException:
            error_w = Error_window()
            error_w.exec()

        if not g.error_path:
            # Calling data aquisition method
            g.get_model_nidaq()

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

    def reload_devices_handler(self):
        """Updates the devices combo box"""
        self._nidaq_info()

        # If the signal is not disconnect, it will run into a warning
        self.device_combo.currentIndexChanged.disconnect(self.update_channels)

        # Updating items on combo box
        self.device_combo.clear()
        self.device_combo.addItems(self.device_type)

        # Reconnecting the signal
        self.device_combo.currentIndexChanged.connect(self.update_channels)
