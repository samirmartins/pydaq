from PySide6.QtCore import (
    QCoreApplication,
    QMetaObject,
    QSize,
)

from PySide6.QtWidgets import (
    QGridLayout,
    QPushButton,
    QSizePolicy,
    QSpacerItem,
)
from . import resources_1_rc


class Ui_error_window_dialog(object):
    def setupUi(self, error_window_dialog):
        if not error_window_dialog.objectName():
            error_window_dialog.setObjectName("error_window_dialog")
        error_window_dialog.resize(450, 150)
        error_window_dialog.setMinimumSize(QSize(450, 150))
        error_window_dialog.setMaximumSize(QSize(450, 150))
        error_window_dialog.setStyleSheet(
            "QDialog{\n"
            "	background-color: rgb(64, 64, 64);\n"
            "}\n"
            "\n"
            "QWidget{\n"
            "	color: rgb(255, 255, 255);\n"
            "}\n"
            "\n"
            "QPushButton{\n"
            "	background-color: rgb(0, 79, 0);\n"
            "\n"
            "	border-top: 1.5px solid rgb(127, 167, 127);\n"
            "	border-left: 1.5px solid rgb(127, 167, 127);\n"
            "\n"
            "	border-bottom: 1.5px solid rgb(0, 0, 0);\n"
            "	border-right: 1.5px solid rgb(0, 0, 0);\n"
            "\n"
            "	\n"
            '	font: 12pt "Helvetica";\n'
            "	text-align:center;\n"
            "}\n"
            "\n"
            "QWidget{\n"
            '	font: 12pt "Helvetica";\n'
            "}\n"
            "\n"
            "QPushButton:hover{\n"
            "	background-color: rgb(0, 50, 0);\n"
            "}\n"
            "\n"
            "QPushButton:pressed{\n"
            "	border: 2px solid rgb(255, 255, 255);\n"
            "}\n"
            ""
        )
        self.gridLayout = QGridLayout(error_window_dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.confirm = QPushButton(error_window_dialog)
        self.confirm.setObjectName("confirm")

        self.gridLayout.addWidget(self.confirm, 1, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(
            20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding
        )

        self.gridLayout.addItem(self.verticalSpacer, 0, 0, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(
            20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding
        )

        self.gridLayout.addItem(self.verticalSpacer_2, 2, 0, 1, 1)

        self.retranslateUi(error_window_dialog)

        QMetaObject.connectSlotsByName(error_window_dialog)

    # setupUi

    def retranslateUi(self, error_window_dialog):
        error_window_dialog.setWindowTitle(
            QCoreApplication.translate("error_window_dialog", "ERROR!", None)
        )
        self.confirm.setText(
            QCoreApplication.translate(
                "error_window_dialog",
                "Device, channel, path or data were not choosen properly!",
                None,
            )
        )

    # retranslateUi
