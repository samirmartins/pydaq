from PySide6.QtWidgets import QDialog

from ..uis.ui_PyDAQ_get_model_sysconfig_Arduino_widget import Ui_Arduino_GetModel_W
from ..utils import *


class SysIdentConfig_W(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Arduino_GetModel_W()
        self.ui.setupUi(self)

    def close_dialog(self):
        self.close()
