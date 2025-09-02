import nidaqmx
import os
import matplotlib.pyplot as plt
import numpy as np

from ..uis.ui_PYDAQ_Digital_filterss_NIDAQ_widget import Ui_Digitalfilters_NIDAQ_widget


from PySide6.QtWidgets import QFileDialog, QWidget

from ..get_data import GetData
from .error_window_gui import Error_window

from pydaq.utils.signals import GuiSignals
from PySide6.QtCore import Signal
from PySide6 import QtWidgets

class Digital_Filters_NIDAQ_Widget(QWidget, Ui_Digitalfilters_NIDAQ_widget):
    dataEntered = Signal(dict)
    def __init__(self, *args):
        super(Digital_Filters_NIDAQ_Widget, self).__init__()
        self.setupUi(self)
        
        self.signals = GuiSignals()
        self.iir_widget.hide()
        self.fir_widget.show()
        self.bd_widget.hide()
        self.fc_widget.hide()
        
        # Signals 
        self.type_filter.currentTextChanged.connect(self.check_filter)
        self.type_box.currentTextChanged.connect(self.bandstop_ui)
        self.save_button.clicked.connect(self.send_data)
        
    # Function to send the variables to get data window
    def send_data(self):
        data = {
            "numtaps_fir": self.order_fir.text(),
            "Cutoff": self.cutoff_fir.text(),
            "design": self.design_box.currentText(),
            "fr": self.yes_fr.isChecked(),
            "type": self.type_box.currentText(),
            "numtaps_iir": self.order_iir.text(),
            "Cutoff_iir": self.cutoff_iir.text(),
            "design_iir": self.designbox_iir.currentText(),
            "type_iir": self.typebox_iir.currentText(),
            "filter": self.type_filter.currentText(),
            'rp': self.rp.text(),
            'rs': self.rs.text(),
            'Fc1': self.fc1_line.text(),
            'Fc2': self.fc2_line.text(),
        }
        
        self.dataEntered.emit(data)
        self.close()
    
    def s_fr(self):
        if self.yes_fr.isChecked():
            self.dataEntered.emit()
            
        
    def check_filter(self, text):
        if text == 'FIR':
            self.fir_widget.show()
            self.iir_widget.hide()
            
        if text == 'IIR':
            self.iir_widget.show()
            self.fir_widget.hide()
            
    def bandstop_ui(self, text):
        if text == 'bandstop' or text == 'bandpass':
            self.bd_widget.show()
            self.fc_widget.show()
            self.cof_widget.hide()
            self.cutoff_widget.hide()
        else:
            self.cof_widget.show()
            self.cutoff_widget.show()
            self.bd_widget.hide()
            self.fc_widget.hide()
            
            
            
    

    
            

