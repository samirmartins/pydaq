import sys

from PySide6 import QtWidgets
from .uis.ui_PyDAQ_Base import Ui_PydaqGlobal
from pydaq.guis.benchmarking_widget import BenchmarkingWidget
import webbrowser


class PYDAQ_Global_GUI(QtWidgets.QMainWindow, Ui_PydaqGlobal):
    def __init__(self):
        super(PYDAQ_Global_GUI, self).__init__()
        self.setupUi(self)
        self.nidaq_tabs.setHidden(True)
        self.logo.released.connect(self.open_pydaq_website)
        #self.benchmarking_button.released.connect(self.open_benchmarking)

        # Connecting Signals to access data
        self.fetched_object = None

        self.get_ino_placeholder.signals.returned.connect(self.fetch_object)
        self.get_nidaq_placeholder.signals.returned.connect(self.fetch_object)
        self.send_ino_placeholder.signals.returned.connect(self.fetch_object)
        self.send_nidaq_placeholder.signals.returned.connect(self.fetch_object)
        self.step_ino_placeholder.signals.returned.connect(self.fetch_object)
        self.step_nidaq_placeholder.signals.returned.connect(self.fetch_object)
        self.actionArduino.triggered.connect(self.open_benchmarking)
        self.actionNIDAQ.triggered.connect(self.open_benchmarking)
        self.actionAbout_PYDAQ.triggered.connect(self.open_pydaq_website)
    
    def fetch_object(self, fetched_obj):
        self.fetched_object = fetched_obj

    def open_pydaq_website(self):
        url = "https://samirmartins.github.io/pydaq/"
        webbrowser.open(url)

    def open_benchmarking(self):
        self.benchmarking = BenchmarkingWidget()
        self.benchmarking.show()


def PydaqGui():
    if not QtWidgets.QApplication.instance():
        app = QtWidgets.QApplication(sys.argv)
    else:
        app = QtWidgets.QApplication.instance()
    window = PYDAQ_Global_GUI()
    window.show()

    try:
        app.exec()
        return window.fetched_object
    except SystemExit:
        print("")
