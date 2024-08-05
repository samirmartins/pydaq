from PySide6.QtWidgets import QDialog

from ..uis.ui_Error_window import Ui_error_window_dialog


class Error_window(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_error_window_dialog()
        self.ui.setupUi(self)

        self.ui.confirm.released.connect(self.close_dialog)

    def close_dialog(self):
        self.close()
