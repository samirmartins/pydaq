import os
import nidaqmx

import numpy as np
import matplotlib.pyplot as plt


from PySide6.QtWidgets import QFileDialog, QWidget
from pydaq.utils.signals import GuiSignals
from scipy.signal import firwin, lfilter, freqz
import scipy.signal as signal

from ..uis.ui_PyDAQ_get_data_NIDAQ_widget import Ui_NIDAQ_GetData_W
from ..guis.digital_filters_nidaq_widget import Digital_Filters_NIDAQ_Widget

from .error_window_gui import Error_window
from ..get_data import GetData

from scipy.signal import lfilter, butter, firwin, cheby1, cheby2, ellip

class GetData_NIDAQ_Widget(QWidget, Ui_NIDAQ_GetData_W):
    def __init__(self, *args):
        super(GetData_NIDAQ_Widget, self).__init__()
        self.setupUi(self)

        # Gathering nidaq info
        self._nidaq_info()

        try:
            chan = nidaqmx.system.device.Device(
                self.device_names[0]
            ).ai_physical_chans.channel_names
            defchan = chan[0]

        except BaseException:
            chan = ""
            defchan = ""

        # Setting the starting values for some widgets
        self.device_combo.addItems(self.device_type)
        self.channel_combo.addItems(chan)
        self.path_line_edit.setText(
            os.path.join(os.path.join(os.path.expanduser("~")), "Desktop")
        )
        self.terminal_config_combo.addItems(["Diff", "RSE", "NRSE"])

        defchan_index = self.channel_combo.findText(defchan)

        if defchan_index == -1:
            pass
        else:
            self.channel_combo.setCurrentIndex(defchan_index)

        # Connecting Signals
        self.path_folder_browse.released.connect(self.locate_path)
        self.start_get_data.released.connect(self.start_func_get_data)
        self.device_combo.currentIndexChanged.connect(self.update_channels)
        self.reload_devices.released.connect(self.reload_devices_handler)
        self.yes_radio.clicked.connect(self.openFilterWindow)
        self.signals = GuiSignals()
        
        
    def openFilterWindow(self):
        self.filterWindow = Digital_Filters_NIDAQ_Widget()
        self.filterWindow.dataEntered.connect(self.update_values)
        self.filterWindow.show()
            
    def update_values(self, data):
        # type of filter
        self.filter = data['filter']
        
        # FIR values
        self.orderfir = data['numtaps_fir']
        self.orderfir = int(self.orderfir)
        
        self.cutofffir = data['Cutoff']
        self.cutofffir = float(self.cutofffir)
        
        self.fc1 = data['Fc1']
        self.fc1 = float(self.fc1)
        
        self.fc2 = data['Fc2']
        self.fc2 = float(self.fc2)
        
        self.design = data['design']
        self.type = data['type']
        self.fr = data['fr']
        
        # IIR values
        self.orderiir = data['numtaps_iir']
        self.orderiir = int(self.orderiir)
        
        self.cutoffiir = data['Cutoff_iir']
        self.cutoffiir = float(self.cutoffiir)
        
        self.design_iir = data['design_iir']
        self.type_irr = data['type_iir']
        
        self.rp = data['rp']
        self.rp = int(self.rp)
        
        self.rs = data['rs']
        self.rs = int(self.rs)
     
    def locate_path(self):  # Calling the Folder Browser Widget
        output_folder_path = QFileDialog.getExistingDirectory(
            self, caption="Choose a folder to save the data file"
        )
        if output_folder_path == "":
            pass
        else:
            self.path_line_edit.setText(output_folder_path.replace("/", "\\"))

   
    def start_func_get_data(self):  # Start getting data
        try:
            # Instantiating the GetData class
            g = GetData()

            # Separating variables
            g.device = self.channel_combo.currentText().split("/")[0]
            g.channel = self.channel_combo.currentText().split("/")[1]
            g.terminal = g.term_map[self.terminal_config_combo.currentText()]
            g.ts = self.Ts_in.value()
            g.session_duration = self.sesh_dur_in.value()
            g.plot = True if self.plot_radio_group.checkedId() == -2 else False
            g.save = True if self.save_radio_group.checkedId() == -2 else False
            g.path = self.path_line_edit.text()

            # Checking if a path was set
            if self.path_line_edit.text() == "":
                raise BaseException

            # Restarting variables
            g.data = []
            g.time_var = []
            g.error_path = False

        except BaseException:
            error_w = Error_window()
            error_w.exec()
            g.error_path = True

        # this conditional checks if will have filter or not
        if not g.error_path:
            if self.No_radio.isChecked():
                g.get_data_nidaq()
                self.signals.returned.emit(g)
            else:
                fs = (1/float(self.Ts_in.value()))*2.5
                if self.filter == 'FIR':
                    
                    fc_fir = self.cutofffir
                    numtaps_fir = self.orderfir
                    window_fir = self.design
                    type_fir = self.type
                    
                    if window_fir == 'Blackman':
                        window_fir = 'blackman'
                        
                    elif window_fir == 'Hamming':
                        window_fir = 'hamming'
                    
                    elif window_fir == 'Hann':
                        window_fir = 'hann'
                        
                    elif window_fir == 'Bartlett-Hann':
                        window_fir = 'barthann'
                        
                    elif window_fir == 'Kaiser':
                        window_fir = 'kaiser'
                        
                    elif window_fir == 'Gauss':
                        window_fir == 'gauss'
                        
                    if type_fir == 'bandstop':
                        fc1 = self.fc1
                        fc2 = self.fc2
                        self.fir_coeff = firwin(numtaps_fir, [fc1/(0.5*fs), fc2/(0.5*fs)], window=window_fir, pass_zero='bandstop')

                    elif type_fir == 'bandpass':
                        fc1 = self.fc1
                        fc2 = self.fc2
                        self.fir_coeff = firwin(numtaps_fir, [fc1/(0.5*fs), fc2/(0.5*fs)], window=window_fir, pass_zero='bandpass')

                    else:
                        self.fir_coeff = firwin(numtaps_fir, fc_fir/(0.5*fs), window=window_fir, pass_zero=type_fir)
    
                    
                    g.get_data_nidaq(filter_coefs=(self.fir_coeff))
                    self.signals.returned.emit(g)
                    self.frequency_response()
                
                elif self.filter == 'IIR':
                    # Create the project of IIR filter
                    fc_iir = self.cutoffiir
                    numtaps_iir = self.orderiir
                    window_iir = self.design_iir
                    type_iir = self.type_irr
                    rp = self.rp 
                    rs = self.rs
                    
                    if window_iir == 'Chebyshev Type I':
                        self.b, self.a = cheby1(numtaps_iir, rp, fc_iir/(0.5*fs), btype=type_iir)
                        
                    elif window_iir == 'Chebyshev Type II':
                        self.b, self.a = cheby2(numtaps_iir, rs, fc_iir/(0.5*fs), btype=type_iir)
                        
                    elif window_iir == 'Butterworth':
                        self.b, self.a = butter(numtaps_iir, fc_iir/(0.5*fs), btype=type_iir)
                        
                    elif window_iir == 'Elliptic':
                        self.b, self.a = ellip(numtaps_iir, rp, rs, fc_iir/(0.5*fs), btype=type_iir)
                        
                    g.get_data_nidaq(filter_coefs=(self.b, self.a))
                    self.signals.returned.emit(g)
                    self.frequency_response()

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
        new_ai_channels = nidaqmx.system.device.Device(
            self.device_names[self.device_type.index(self.device_combo.currentText())]
        ).ai_physical_chans.channel_names

        # Default channel
        try:
            default_channel = new_ai_channels[0]
        except BaseException:
            default_channel = "There is no analog input in this board"

        # Rewriting new ai channels into the right place
        self.channel_combo.clear()
        self.channel_combo.addItems(new_ai_channels)
        defchan_index = self.channel_combo.findText(default_channel)

        if defchan_index == -1:
            pass
        else:
            self.channel_combo.setCurrentIndex(defchan_index)

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

    def frequency_response(self):
        if self.fr == True:
            if self.filter == 'FIR':
                x = np.loadtxt(self.path_line_edit.text() + "\\" + "time.dat")
                y = np.loadtxt(self.path_line_edit.text() + "\\" + "data_filtered.dat")
                y2 = np.loadtxt(self.path_line_edit.text() + "\\" + "data.dat")
                
                ts = x[1] - x[0]
                fs = 1/ts
                
                w, h = signal.freqz(self.fir_coeff, 1.0, worN=None, fs=fs)
                mag = 20*np.log10(np.abs(h))
                phase = np.angle(h)
                
                dt = 1/(fs*2.5)  # 1/(fs*2)
        
                fft_data = np.fft.fft(y2)
                freqs = np.fft.fftfreq(len(y2), dt)

                
                fft_data_filtered = np.fft.fft(y)

                
                positive_freqs = freqs[:len(freqs) // 2]
                fft_data_magnitude = np.abs(fft_data[:len(freqs) // 2])
                fft_data_filtered_magnitude = np.abs(fft_data_filtered[:len(freqs) // 2])
                
                fft_data_magnitude_norm = (fft_data_magnitude/np.max(fft_data_magnitude))*100
                fft_data_filtered_magnitude_norm = (fft_data_filtered_magnitude/np.max(fft_data_filtered_magnitude))*100
                
                
                plt.figure(figsize=(7,5))
                
                plt.subplot(2,1,1)
                plt.plot(positive_freqs, fft_data_magnitude_norm, label='FFT Original', color='r')
                plt.title('Original Signal in Frequency')
                plt.xlabel('Frequency (Hz)')
                plt.ylabel('Magnitude')
                plt.legend()
                plt.grid()
                
                plt.subplot(2,1,2)
                plt.plot(positive_freqs, fft_data_filtered_magnitude_norm, label='FFT Filtered', color='r')
                plt.title('Filtered Signal in Frequency')
                plt.xlabel('Frequency (Hz)')
                plt.ylabel('Magnitude')
                plt.legend()
                plt.grid()
                
                plt.tight_layout()
                plt.show()
                
            else:
                x = np.loadtxt(self.path_line_edit.text() + "\\" + "time.dat")
                y = np.loadtxt(self.path_line_edit.text() + "\\" + "data_filtered.dat")
                y2 = np.loadtxt(self.path_line_edit.text() + "\\" + "data.dat")
                
                ts = x[1] - x[0]
                fs = 1/ts
                
                w, h = signal.freqz(self.b, self.a, worN=None, fs=fs)
                mag = 20*np.log10(np.abs(h))
                phase = np.angle(h)
                
               
                dt = 1/(fs*2.5)  # 1/(fs*2)
        
                
                fft_data = np.fft.fft(y2)
                freqs = np.fft.fftfreq(len(y2), dt)

                fft_data_filtered = np.fft.fft(y)

                positive_freqs = freqs[:len(freqs) // 2]
                fft_data_magnitude = np.abs(fft_data[:len(freqs) // 2])
                fft_data_filtered_magnitude = np.abs(fft_data_filtered[:len(freqs) // 2])
                
                
                plt.figure(figsize=(7,5))
                
                plt.subplot(2,1,1)
                plt.plot(positive_freqs, fft_data_magnitude, label='FFT Original', color='r')
                plt.title('Original Signal in Frequency')
                plt.xlabel('Frequency (Hz)')
                plt.ylabel('Magnitude')
                plt.legend()
                plt.grid()
                
                plt.subplot(2,1,2)
                plt.plot(positive_freqs, fft_data_filtered_magnitude, label='FFT Original', color='r')
                plt.title('Filtered Signal in Frequency')
                plt.xlabel('Frequency (Hz)')
                plt.ylabel('Magnitude')
                plt.legend()
                plt.grid()
                
                plt.tight_layout()
                plt.show()
        else:
            pass