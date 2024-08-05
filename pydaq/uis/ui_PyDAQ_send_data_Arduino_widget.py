from PySide6.QtCore import (
    QCoreApplication,
    QMetaObject,
    QSize,
    Qt,
)

from PySide6.QtWidgets import (
    QAbstractSpinBox,
    QButtonGroup,
    QComboBox,
    QDoubleSpinBox,
    QFrame,
    QGridLayout,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QRadioButton,
    QWidget,
)
from . import resources_1_rc


class Ui_Arduino_SendData_W(object):
    def setupUi(self, Arduino_SendData_W):
        if not Arduino_SendData_W.objectName():
            Arduino_SendData_W.setObjectName("Arduino_SendData_W")
        Arduino_SendData_W.resize(354, 320)
        Arduino_SendData_W.setStyleSheet(
            "QComboBox QAbstractItemView {\n"
            "    background-color: rgb(77, 77, 77);\n"
            "}\n"
            "\n"
            "QComboBox QAbstractItemView::item:focus{\n"
            "    background-color: rgb(140, 140, 140);\n"
            "}\n"
            "\n"
            "QDoubleSpinBox{\n"
            "	background-color: rgb(77, 77, 77);\n"
            "	\n"
            "	border-top: 1.5px solid rgb(46, 46, 46);\n"
            "	border-left: 1.5px solid rgb(46, 46, 46);\n"
            "\n"
            "	border-bottom: 1.5px solid rgb(166, 166, 166);\n"
            "	border-right: 1.5px solid rgb(166, 166, 166);\n"
            "}\n"
            "\n"
            "QDoubleSpinBox::up-button{\n"
            "    image: url(:/imgs/imgs/drop_up_arrow.png);\n"
            "	width: 11px;\n"
            "\n"
            "	background-color: rgb(0, 79, 0);\n"
            "	border-top: 1.5px solid rgb(127, 167, 127);\n"
            "	border-left: 1.5px solid rgb(127, 167, 127);\n"
            "\n"
            "	border-bottom: 1.5px solid rgb(0, 0, 0);\n"
            "	border-right: 1.5px solid rgb(0, 0, 0);\n"
            "}\n"
            "\n"
            "QDoubleSpinBox::up-button:pressed{\n"
            "	border: 2px solid rgb(255, 255, 255);\n"
            "}\n"
            "\n"
            "QDoubleSpinBox::up-button:hover{\n"
            "	background-color: rgb(0, 50, 0);\n"
            "}\n"
            "\n"
            "QDoubleSpinBox::down-button{\n"
            ""
            "    image: url(:/imgs/imgs/drop_down_arrow.png);\n"
            "	width: 11px;\n"
            "\n"
            "	background-color: rgb(0, 79, 0);\n"
            "	border-top: 1.5px solid rgb(127, 167, 127);\n"
            "	border-left: 1.5px solid rgb(127, 167, 127);\n"
            "\n"
            "	border-bottom: 1.5px solid rgb(0, 0, 0);\n"
            "	border-right: 1.5px solid rgb(0, 0, 0);\n"
            "}\n"
            "\n"
            "QDoubleSpinBox::down-button:pressed{\n"
            "	border: 2px solid rgb(255, 255, 255);\n"
            "}\n"
            "\n"
            "QDoubleSpinBox::down-button:hover{\n"
            "	background-color: rgb(0, 50, 0);\n"
            "}\n"
            "\n"
            "QWidget#Arduino_SendData_W{\n"
            "	background-color: rgb(64, 64, 64);\n"
            "}\n"
            "\n"
            "QWidget{\n"
            "	color: rgb(255, 255, 255);\n"
            "}\n"
            "\n"
            "QComboBox{\n"
            "	background-color: rgb(77, 77, 77);\n"
            "	\n"
            "	border-top: 1.5px solid rgb(46, 46, 46);\n"
            "	border-left: 1.5px solid rgb(46, 46, 46);\n"
            "\n"
            "	border-bottom: 1.5px solid rgb(166, 166, 166);\n"
            "	border-right: 1.5px solid rgb(166, 166, 166);\n"
            "}\n"
            "\n"
            "\n"
            "QComboBox::drop-down{\n"
            "	image: url(:/imgs/imgs/drop_down_arrow.png);\n"
            "	width: 11px;\n"
            "\n"
            "	backg"
            "round-color: rgb(0, 79, 0);\n"
            "	border-top: 2px solid rgb(127, 167, 127);\n"
            "	border-left: 2px solid rgb(127, 167, 127);\n"
            "\n"
            "	border-bottom: 2px solid rgb(0, 0, 0);\n"
            "	border-right: 2px solid rgb(0, 0, 0);\n"
            "}\n"
            "\n"
            "QComboBox::drop-down:hover{\n"
            "	background-color: rgb(0, 50, 0);\n"
            "}\n"
            "\n"
            "QComboBox::drop-down:pressed{\n"
            "	border: 2px solid rgb(255, 255, 255);\n"
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
            "\n"
            "QLineEdit{\n"
            "	background-color: rgb(77, 77, 77);\n"
            "	border-top: 1.5px solid rgb(46, "
            "46, 46);\n"
            "	border-left: 1.5px solid rgb(46, 46, 46);\n"
            "\n"
            "	border-bottom: 1.5px solid rgb(166, 166, 166);\n"
            "	border-right: 1.5px solid rgb(166, 166, 166);\n"
            "}\n"
            "\n"
            "QRadioButton::indicator{\n"
            "	border-radius: 6px;\n"
            "	border-top: 1.5px solid rgb(0, 0, 0);\n"
            "	border-left: 1.5px solid rgb(0, 0, 0);\n"
            "\n"
            "	border-bottom: 1.5px solid rgb(160, 160, 160);\n"
            "	border-right: 1.5px solid rgb(160, 160, 160);\n"
            "}\n"
            "\n"
            "QRadioButton::indicator::checked{\n"
            "	background-color: white;\n"
            "}\n"
            "\n"
            "QRadioButton::indicator::unchecked:hover{\n"
            "	background-color: #9F9F9F;\n"
            "}\n"
            "\n"
            "QRadioButton::indicator::pressed{\n"
            "	border: 1.5px solid #505050\n"
            "}\n"
            "\n"
            "QPushButton#reload_devices{\n"
            "	image: url(:/imgs/imgs/reload.png);\n"
            "	width: 11px;\n"
            "	background-color: rgb(0, 79, 0);\n"
            "\n"
            "	border-top: 1.5px solid rgb(127, 167, 127);\n"
            "	border-left: 1.5px solid rgb(127, 167, 127);\n"
            "\n"
            "	border-bottom: 1.5px solid rgb(0, 0, 0);\n"
            "	border-right: 1.5px solid rgb(0, 0, 0);\n"
            "\n"
            "	\n"
            ""
            '	font: 12pt "Helvetica";\n'
            "	text-align:center;\n"
            "}\n"
            "\n"
            "QPushButton#reload_devices:hover{\n"
            "	background-color: rgb(0, 50, 0);\n"
            "}\n"
            "\n"
            "QPushButton#reload_devices:pressed{\n"
            "	border: 2px solid rgb(255, 255, 255);\n"
            "}"
        )
        self.gridLayout_3 = QGridLayout(Arduino_SendData_W)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.widget = QWidget(Arduino_SendData_W)
        self.widget.setObjectName("widget")
        self.gridLayout = QGridLayout(self.widget)
        self.gridLayout.setObjectName("gridLayout")
        self.widget_7 = QWidget(self.widget)
        self.widget_7.setObjectName("widget_7")
        self.horizontalLayout = QHBoxLayout(self.widget_7)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.yes_plot_radio = QRadioButton(self.widget_7)
        self.plot_radio_group = QButtonGroup(Arduino_SendData_W)
        self.plot_radio_group.setObjectName("plot_radio_group")
        self.plot_radio_group.addButton(self.yes_plot_radio)
        self.yes_plot_radio.setObjectName("yes_plot_radio")
        self.yes_plot_radio.setChecked(True)

        self.horizontalLayout.addWidget(self.yes_plot_radio)

        self.no_plot_radio = QRadioButton(self.widget_7)
        self.plot_radio_group.addButton(self.no_plot_radio)
        self.no_plot_radio.setObjectName("no_plot_radio")

        self.horizontalLayout.addWidget(self.no_plot_radio)

        self.gridLayout.addWidget(self.widget_7, 2, 2, 1, 1, Qt.AlignLeft)

        self.label_4 = QLabel(self.widget)
        self.label_4.setObjectName("label_4")
        self.label_4.setMinimumSize(QSize(0, 30))
        self.label_4.setMaximumSize(QSize(16777215, 30))

        self.gridLayout.addWidget(self.label_4, 1, 0, 1, 1)

        self.label_8 = QLabel(self.widget)
        self.label_8.setObjectName("label_8")
        self.label_8.setMinimumSize(QSize(0, 30))
        self.label_8.setMaximumSize(QSize(16777215, 30))

        self.gridLayout.addWidget(self.label_8, 4, 0, 1, 1)

        self.widget_9 = QWidget(self.widget)
        self.widget_9.setObjectName("widget_9")
        self.widget_9.setMinimumSize(QSize(0, 50))
        self.widget_9.setMaximumSize(QSize(16777215, 50))
        self.horizontalLayout_3 = QHBoxLayout(self.widget_9)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.path_line_edit = QLineEdit(self.widget_9)
        self.path_line_edit.setObjectName("path_line_edit")
        self.path_line_edit.setMinimumSize(QSize(0, 22))
        self.path_line_edit.setMaximumSize(QSize(16777215, 22))

        self.horizontalLayout_3.addWidget(self.path_line_edit, 0, Qt.AlignVCenter)

        self.path_folder_browse = QPushButton(self.widget_9)
        self.path_folder_browse.setObjectName("path_folder_browse")
        self.path_folder_browse.setMinimumSize(QSize(0, 30))
        self.path_folder_browse.setMaximumSize(QSize(16777215, 30))

        self.horizontalLayout_3.addWidget(self.path_folder_browse, 0, Qt.AlignVCenter)

        self.gridLayout.addWidget(self.widget_9, 4, 2, 1, 1)

        self.widget_2 = QWidget(self.widget)
        self.widget_2.setObjectName("widget_2")
        self.gridLayout_2 = QGridLayout(self.widget_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.device_combo = QComboBox(self.widget_2)
        self.device_combo.setObjectName("device_combo")
        self.device_combo.setMinimumSize(QSize(0, 22))
        self.device_combo.setMaximumSize(QSize(16777215, 22))

        self.gridLayout_2.addWidget(self.device_combo, 1, 0, 1, 1)

        self.reload_devices = QPushButton(self.widget_2)
        self.reload_devices.setObjectName("reload_devices")
        self.reload_devices.setMinimumSize(QSize(22, 22))
        self.reload_devices.setMaximumSize(QSize(22, 22))

        self.gridLayout_2.addWidget(self.reload_devices, 1, 1, 1, 1)

        self.gridLayout.addWidget(self.widget_2, 0, 2, 1, 1)

        self.label_6 = QLabel(self.widget)
        self.label_6.setObjectName("label_6")
        self.label_6.setMinimumSize(QSize(0, 30))
        self.label_6.setMaximumSize(QSize(16777215, 30))

        self.gridLayout.addWidget(self.label_6, 2, 0, 1, 1)

        self.label = QLabel(self.widget)
        self.label.setObjectName("label")
        self.label.setMinimumSize(QSize(0, 30))
        self.label.setMaximumSize(QSize(16777215, 30))

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.widget_5 = QWidget(self.widget)
        self.widget_5.setObjectName("widget_5")
        self.gridLayout_6 = QGridLayout(self.widget_5)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.Ts_in = QDoubleSpinBox(self.widget_5)
        self.Ts_in.setObjectName("Ts_in")
        self.Ts_in.setMinimumSize(QSize(0, 22))
        self.Ts_in.setMaximumSize(QSize(16777215, 22))
        self.Ts_in.setDecimals(4)
        self.Ts_in.setMaximum(999.990000000000009)
        self.Ts_in.setSingleStep(0.010000000000000)
        self.Ts_in.setStepType(QAbstractSpinBox.AdaptiveDecimalStepType)
        self.Ts_in.setValue(0.500000000000000)

        self.gridLayout_6.addWidget(self.Ts_in, 0, 0, 1, 1)

        self.gridLayout.addWidget(self.widget_5, 1, 2, 1, 1)

        self.line = QFrame(self.widget)
        self.line.setObjectName("line")
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line, 0, 1, 6, 1)

        self.gridLayout_3.addWidget(self.widget, 0, 0, 1, 1)

        self.line_3 = QFrame(Arduino_SendData_W)
        self.line_3.setObjectName("line_3")
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.gridLayout_3.addWidget(self.line_3, 1, 0, 1, 1)

        self.start_send_data = QPushButton(Arduino_SendData_W)
        self.start_send_data.setObjectName("start_send_data")
        self.start_send_data.setMinimumSize(QSize(100, 30))
        self.start_send_data.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_3.addWidget(self.start_send_data, 2, 0, 1, 1, Qt.AlignHCenter)

        self.retranslateUi(Arduino_SendData_W)

        QMetaObject.connectSlotsByName(Arduino_SendData_W)

    # setupUi

    def retranslateUi(self, Arduino_SendData_W):
        Arduino_SendData_W.setWindowTitle(
            QCoreApplication.translate("Arduino_SendData_W", "Form", None)
        )
        self.yes_plot_radio.setText(
            QCoreApplication.translate("Arduino_SendData_W", "Yes", None)
        )
        self.no_plot_radio.setText(
            QCoreApplication.translate("Arduino_SendData_W", "No", None)
        )
        self.label_4.setText(
            QCoreApplication.translate("Arduino_SendData_W", "Sample period (s)", None)
        )
        self.label_8.setText(
            QCoreApplication.translate("Arduino_SendData_W", "Data path", None)
        )
        self.path_folder_browse.setText(
            QCoreApplication.translate("Arduino_SendData_W", " Browse ", None)
        )
        # if QT_CONFIG(tooltip)
        self.reload_devices.setToolTip(
            QCoreApplication.translate(
                "Arduino_SendData_W",
                "<html><head/><body><p>Update COM ports</p></body></html>",
                None,
            )
        )
        # endif // QT_CONFIG(tooltip)
        self.reload_devices.setText("")
        self.label_6.setText(
            QCoreApplication.translate("Arduino_SendData_W", "Plot data?", None)
        )
        self.label.setText(
            QCoreApplication.translate(
                "Arduino_SendData_W", "Choose your arduino:", None
            )
        )
        self.start_send_data.setText(
            QCoreApplication.translate("Arduino_SendData_W", "SEND DATA", None)
        )

    # retranslateUi
