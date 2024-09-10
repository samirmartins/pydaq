from PySide6.QtWidgets import QDialog

from ..uis.ui_PRBS_Info_widget import Ui_PRBS_Info
from ..utils import *


class PRBSConfig_W(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_PRBS_Info()
        self.ui.setupUi(self)

    def close_dialog(self):
        self.close()
