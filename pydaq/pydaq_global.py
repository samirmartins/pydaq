import sys

from PySide6 import QtWidgets
from .uis.ui_PyDAQ_Base import Ui_PydaqGlobal
import webbrowser


class PYDAQ_Global_GUI(QtWidgets.QMainWindow, Ui_PydaqGlobal):
    def __init__(self):
        super(PYDAQ_Global_GUI, self).__init__()
        self.setupUi(self)
        self.nidaq_tabs.setHidden(True)
        self.logo.released.connect(self.open_pydaq_website)

    def open_pydaq_website(self):
        url = "https://samirmartins.github.io/pydaq/"
        webbrowser.open(url)


def PYDAQ_GUI():
    app = QtWidgets.QApplication(sys.argv)
    window = PYDAQ_Global_GUI()
    window.show()

    sys.exit(app.exec())
