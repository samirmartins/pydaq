from ..uis.ui_PYDAQ_Digital_filters_widget import Ui_Digitalfilters_arduino_widget
from PySide6.QtWidgets import QFileDialog, QWidget
import serial
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import ellip, filtfilt, freqz

class Digital_Filters_Arduino_Widget(QWidget, Ui_Digitalfilters_arduino_widget):
    def __init__(self, *args):
        super(Digital_Filters_Arduino_Widget, self).__init__()
        self.setupUi(self)
        self.filter_combox.currentTextChanged.connect(self.update_filter)
        self.update_filter(self.filter_combox.currentText())
        self.reload_devices.clicked.connect(self.update_com_ports)
        self.Filter_button.clicked.connect(self.cauer_iir)
        
        # setting starting values
        self.update_com_ports()
        
    
    # function that show and hide fir or iir widgets    
    def update_filter(self, text):
        if text == 'FIR':
            self.fir_configs.show()
            self.iir_configs.hide()
        else:
            self.iir_configs.show()
            self.fir_configs.hide()
            
                
    def update_com_ports(self):  # Updating com ports
        self.com_ports = [i.description for i in serial.tools.list_ports.comports()]
        selected = self.arduino_board.currentText()

        self.arduino_board.clear()
        self.arduino_board.addItems(self.com_ports)
        index_current = self.arduino_board.findText(selected)

        if index_current == -1:
            pass
        else:
            self.arduino_board.setCurrentIndex(index_current)
            
    def cauer_iir(self):
        self.fs = float(self.fs_iir_line.text())
        self.cutoff = float(self.fc_line.text())
        self.order = float(self.order_iir_line.text())
        self.rp = float(self.rp_line.text())
        self.rs = float(self.rs_line.text())
        
        # Generate a signal
        t = np.arange(0, 1.0, 1/self.fs)  
        x = 0.5 * np.sin(2 * np.pi * 50 * t) + 0.5 * np.sin(2 * np.pi * 200 * t)  

        # Euler Project
        b, a = ellip(self.order, self.rp, self.rs, self.cutoff/(0.5*self.fs), btype='low')

        
        y = filtfilt(b, a, x)

        
        plt.figure(figsize=(12, 10))

        plt.subplot(4, 1, 1)
        plt.plot(t, x)
        plt.title('Sinal Original')
        plt.xlabel('Tempo [s]')
        plt.ylabel('Amplitude')
        plt.grid()

        plt.subplot(4, 1, 2)
        plt.plot(t, y)
        plt.title('Sinal Filtrado')
        plt.xlabel('Tempo [s]')
        plt.ylabel('Amplitude')
        plt.grid()

        if self.yes_fr.isChecked():
            
            w, h = freqz(b, a, worN=8000)

            plt.subplot(4, 1, 3)
            plt.plot(0.5*self.fs*w/np.pi, abs(h), 'b')
            plt.title('Resposta em Frequência do Filtro - Magnitude')
            plt.xlabel('Frequência [Hz]')
            plt.ylabel('Magnitude [dB]')
            plt.grid()

            plt.subplot(4, 1, 4)
            plt.plot(0.5*self.fs*w/np.pi, np.unwrap(np.angle(h)), 'b')
            plt.title('Resposta em Frequência do Filtro - Fase')
            plt.xlabel('Frequência [Hz]')
            plt.ylabel('Fase [radianos]')
            plt.grid()

            plt.tight_layout()
            plt.show()
        else:
            pass