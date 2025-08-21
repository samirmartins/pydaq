# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'PyDAQ_get_model_NIDAQ_widgetFxqeZq.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtOpenGLWidgets import QOpenGLWidget
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QButtonGroup, QComboBox,
    QDoubleSpinBox, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QRadioButton,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_Arduino_GetModel_W(object):
    def setupUi(self, Arduino_GetModel_W):
        if not Arduino_GetModel_W.objectName():
            Arduino_GetModel_W.setObjectName(u"Arduino_GetModel_W")
        Arduino_GetModel_W.resize(650, 668)
        Arduino_GetModel_W.setStyleSheet(u"QComboBox QAbstractItemView {\n"
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
"QSpinBox{\n"
"	background-color: rgb(77, 77, 77);\n"
"	\n"
"	border-top: 1.5px solid rgb(46, 46, 46);\n"
"	border-left: 1.5px solid rgb(46, 46, 46);\n"
"\n"
"	border-bottom: 1.5px solid rgb(166, 166, 166);\n"
"	border-right: 1.5px solid rgb(166, 166, 166);\n"
"}\n"
"\n"
"QSpinBox::up-button{\n"
"    image: url(:/imgs/imgs/drop_up_arrow.png);\n"
"	width: 11px;\n"
"\n"
"	background-color: rgb(0, 79, 0);\n"
"	border-top: 1.5px solid rgb(127, 167, 127);\n"
"	border-left: 1.5px solid rgb(127, 167, 127);\n"
"\n"
"	border-b"
                        "ottom: 1.5px solid rgb(0, 0, 0);\n"
"	border-right: 1.5px solid rgb(0, 0, 0);\n"
"}\n"
"\n"
"QSpinBox::up-button:pressed{\n"
"	border: 2px solid rgb(255, 255, 255);\n"
"}\n"
"\n"
"QSpinBox::up-button:hover{\n"
"	background-color: rgb(0, 50, 0);\n"
"}\n"
"\n"
"QSpinBox::down-button{\n"
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
"QSpinBox::down-button:pressed{\n"
"	border: 2px solid rgb(255, 255, 255);\n"
"}\n"
"\n"
"QSpinBox::down-button:hover{\n"
"	background-color: rgb(0, 50, 0);\n"
"}\n"
"\n"
"QWidget#Arduino_GetModel_W{\n"
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
"	"
                        "border-left: 1.5px solid rgb(46, 46, 46);\n"
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
"	background-color: rgb(0, 79, 0);\n"
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
"	font: 12pt \"Helvetica\";\n"
"	text-align:center;\n"
"}\n"
"\n"
"QWidget{\n"
"	font:"
                        " 12pt \"Helvetica\";\n"
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
"	border-top: 1.5px solid rgb(46, 46, 46);\n"
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
"	image: url(:/imgs/imgs/reloa"
                        "d.png);\n"
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
"	font: 12pt \"Helvetica\";\n"
"	text-align:center;\n"
"}\n"
"\n"
"QPushButton#reload_devices:hover{\n"
"	background-color: rgb(0, 50, 0);\n"
"}\n"
"\n"
"QPushButton#reload_devices:pressed{\n"
"	border: 2px solid rgb(255, 255, 255);\n"
"}")
        self.verticalLayout = QVBoxLayout(Arduino_GetModel_W)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.widget = QWidget(Arduino_GetModel_W)
        self.widget.setObjectName(u"widget")
        self.widget.setMaximumSize(QSize(16777205, 16777205))
        self.gridLayout = QGridLayout(self.widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.widget_9 = QWidget(self.widget)
        self.widget_9.setObjectName(u"widget_9")
        self.horizontalLayout_3 = QHBoxLayout(self.widget_9)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.path_line_edit = QLineEdit(self.widget_9)
        self.path_line_edit.setObjectName(u"path_line_edit")
        self.path_line_edit.setMinimumSize(QSize(0, 22))
        self.path_line_edit.setMaximumSize(QSize(16777215, 22))

        self.horizontalLayout_3.addWidget(self.path_line_edit)

        self.path_folder_browse = QPushButton(self.widget_9)
        self.path_folder_browse.setObjectName(u"path_folder_browse")
        self.path_folder_browse.setMinimumSize(QSize(0, 30))
        self.path_folder_browse.setMaximumSize(QSize(16777215, 30))

        self.horizontalLayout_3.addWidget(self.path_folder_browse)


        self.gridLayout.addWidget(self.widget_9, 9, 2, 1, 1)

        self.widget_8 = QWidget(self.widget)
        self.widget_8.setObjectName(u"widget_8")
        self.gridLayout_5 = QGridLayout(self.widget_8)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.save_time_in = QDoubleSpinBox(self.widget_8)
        self.save_time_in.setObjectName(u"save_time_in")
        self.save_time_in.setMinimumSize(QSize(0, 22))
        self.save_time_in.setMaximumSize(QSize(16777215, 22))
        self.save_time_in.setMaximum(86000.000000000000000)

        self.gridLayout_5.addWidget(self.save_time_in, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.widget_8, 5, 2, 1, 1)

        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(0, 30))
        self.label_2.setMaximumSize(QSize(16777215, 30))

        self.gridLayout.addWidget(self.label_2, 10, 0, 1, 1)

        self.label_11 = QLabel(self.widget)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout.addWidget(self.label_11, 3, 0, 1, 1)

        self.widget_4 = QWidget(self.widget)
        self.widget_4.setObjectName(u"widget_4")
        self.gridLayout_2 = QGridLayout(self.widget_4)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.yes_rt_plot_radio = QRadioButton(self.widget_4)
        self.plot_radio_group = QButtonGroup(Arduino_GetModel_W)
        self.plot_radio_group.setObjectName(u"plot_radio_group")
        self.plot_radio_group.addButton(self.yes_rt_plot_radio)
        self.yes_rt_plot_radio.setObjectName(u"yes_rt_plot_radio")
        self.yes_rt_plot_radio.setChecked(False)

        self.gridLayout_2.addWidget(self.yes_rt_plot_radio, 0, 0, 1, 1)

        self.no_plot_radio = QRadioButton(self.widget_4)
        self.plot_radio_group.addButton(self.no_plot_radio)
        self.no_plot_radio.setObjectName(u"no_plot_radio")
        self.no_plot_radio.setChecked(True)

        self.gridLayout_2.addWidget(self.no_plot_radio, 0, 3, 1, 1)

        self.yes_ate_plot_radio = QRadioButton(self.widget_4)
        self.plot_radio_group.addButton(self.yes_ate_plot_radio)
        self.yes_ate_plot_radio.setObjectName(u"yes_ate_plot_radio")

        self.gridLayout_2.addWidget(self.yes_ate_plot_radio, 0, 2, 1, 1)

        self.label_warning = QLabel(self.widget_4)
        self.label_warning.setObjectName(u"label_warning")

        self.gridLayout_2.addWidget(self.label_warning, 0, 1, 1, 1)


        self.gridLayout.addWidget(self.widget_4, 7, 2, 1, 1, Qt.AlignmentFlag.AlignLeft)

        self.label_8 = QLabel(self.widget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMinimumSize(QSize(0, 30))
        self.label_8.setMaximumSize(QSize(16777215, 30))
        self.label_8.setBaseSize(QSize(0, 0))

        self.gridLayout.addWidget(self.label_8, 9, 0, 1, 1)

        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(0, 30))
        self.label.setMaximumSize(QSize(16777215, 30))

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setMinimumSize(QSize(0, 30))
        self.label_3.setMaximumSize(QSize(16777215, 30))

        self.gridLayout.addWidget(self.label_3, 11, 0, 1, 1)

        self.widget_7 = QWidget(self.widget)
        self.widget_7.setObjectName(u"widget_7")
        self.horizontalLayout = QHBoxLayout(self.widget_7)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.yes_save_radio = QRadioButton(self.widget_7)
        self.save_radio_group = QButtonGroup(Arduino_GetModel_W)
        self.save_radio_group.setObjectName(u"save_radio_group")
        self.save_radio_group.addButton(self.yes_save_radio)
        self.yes_save_radio.setObjectName(u"yes_save_radio")
        self.yes_save_radio.setChecked(True)

        self.horizontalLayout.addWidget(self.yes_save_radio)

        self.no_save_radio = QRadioButton(self.widget_7)
        self.save_radio_group.addButton(self.no_save_radio)
        self.no_save_radio.setObjectName(u"no_save_radio")

        self.horizontalLayout.addWidget(self.no_save_radio)


        self.gridLayout.addWidget(self.widget_7, 8, 2, 1, 1, Qt.AlignmentFlag.AlignLeft)

        self.widget_6 = QWidget(self.widget)
        self.widget_6.setObjectName(u"widget_6")
        self.gridLayout_7 = QGridLayout(self.widget_6)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.sesh_dur_in = QDoubleSpinBox(self.widget_6)
        self.sesh_dur_in.setObjectName(u"sesh_dur_in")
        self.sesh_dur_in.setMinimumSize(QSize(0, 22))
        self.sesh_dur_in.setMaximumSize(QSize(16777215, 22))
        self.sesh_dur_in.setBaseSize(QSize(0, 12))
        self.sesh_dur_in.setDecimals(2)
        self.sesh_dur_in.setMaximum(86400.000000000000000)
        self.sesh_dur_in.setSingleStep(0.010000000000000)
        self.sesh_dur_in.setStepType(QAbstractSpinBox.StepType.AdaptiveDecimalStepType)
        self.sesh_dur_in.setValue(150.000000000000000)

        self.gridLayout_7.addWidget(self.sesh_dur_in, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.widget_6, 6, 2, 1, 1)

        self.label_9 = QLabel(self.widget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMinimumSize(QSize(0, 30))
        self.label_9.setMaximumSize(QSize(16777215, 30))

        self.gridLayout.addWidget(self.label_9, 5, 0, 1, 1)

        self.label_6 = QLabel(self.widget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMinimumSize(QSize(0, 30))
        self.label_6.setMaximumSize(QSize(16777215, 30))

        self.gridLayout.addWidget(self.label_6, 7, 0, 1, 1)

        self.line = QFrame(self.widget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.VLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout.addWidget(self.line, 0, 1, 12, 1)

        self.widget_12 = QWidget(self.widget)
        self.widget_12.setObjectName(u"widget_12")
        self.gridLayout_10 = QGridLayout(self.widget_12)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.terminal_config_combo = QComboBox(self.widget_12)
        self.terminal_config_combo.setObjectName(u"terminal_config_combo")
        self.terminal_config_combo.setMinimumSize(QSize(0, 22))
        self.terminal_config_combo.setMaximumSize(QSize(16777215, 22))

        self.gridLayout_10.addWidget(self.terminal_config_combo, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.widget_12, 3, 2, 1, 1)

        self.label_7 = QLabel(self.widget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMinimumSize(QSize(0, 30))
        self.label_7.setMaximumSize(QSize(16777215, 30))

        self.gridLayout.addWidget(self.label_7, 8, 0, 1, 1)

        self.label_5 = QLabel(self.widget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(0, 30))
        self.label_5.setMaximumSize(QSize(16777215, 30))

        self.gridLayout.addWidget(self.label_5, 6, 0, 1, 1)

        self.widget_11 = QWidget(self.widget)
        self.widget_11.setObjectName(u"widget_11")
        self.gridLayout_9 = QGridLayout(self.widget_11)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.ai_channel_combo = QComboBox(self.widget_11)
        self.ai_channel_combo.setObjectName(u"ai_channel_combo")
        self.ai_channel_combo.setMinimumSize(QSize(0, 22))
        self.ai_channel_combo.setMaximumSize(QSize(16777215, 22))

        self.gridLayout_9.addWidget(self.ai_channel_combo, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.widget_11, 1, 2, 1, 1)

        self.label_10 = QLabel(self.widget)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout.addWidget(self.label_10, 1, 0, 1, 1)

        self.widget_10 = QWidget(self.widget)
        self.widget_10.setObjectName(u"widget_10")
        self.gridLayout_8 = QGridLayout(self.widget_10)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.system_settings_button = QPushButton(self.widget_10)
        self.system_settings_button.setObjectName(u"system_settings_button")

        self.gridLayout_8.addWidget(self.system_settings_button, 0, 0, 1, 1, Qt.AlignmentFlag.AlignHCenter)


        self.gridLayout.addWidget(self.widget_10, 11, 2, 1, 1)

        self.widget_2 = QWidget(self.widget)
        self.widget_2.setObjectName(u"widget_2")
        self.gridLayout_3 = QGridLayout(self.widget_2)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.device_combo = QComboBox(self.widget_2)
        self.device_combo.setObjectName(u"device_combo")
        self.device_combo.setMinimumSize(QSize(0, 22))
        self.device_combo.setMaximumSize(QSize(16777215, 22))

        self.gridLayout_3.addWidget(self.device_combo, 0, 0, 1, 1)

        self.openGLWidget = QOpenGLWidget(self.widget_2)
        self.openGLWidget.setObjectName(u"openGLWidget")

        self.gridLayout_3.addWidget(self.openGLWidget, 1, 0, 1, 1)

        self.reload_devices = QPushButton(self.widget_2)
        self.reload_devices.setObjectName(u"reload_devices")
        self.reload_devices.setMaximumSize(QSize(22, 22))

        self.gridLayout_3.addWidget(self.reload_devices, 0, 1, 1, 1)


        self.gridLayout.addWidget(self.widget_2, 0, 2, 1, 1)

        self.label_4 = QLabel(self.widget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(0, 30))
        self.label_4.setMaximumSize(QSize(16777215, 30))

        self.gridLayout.addWidget(self.label_4, 4, 0, 1, 1)

        self.widget_19 = QWidget(self.widget)
        self.widget_19.setObjectName(u"widget_19")
        self.horizontalLayout_2 = QHBoxLayout(self.widget_19)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.inp_signal_combo = QComboBox(self.widget_19)
        self.inp_signal_combo.setObjectName(u"inp_signal_combo")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.inp_signal_combo.sizePolicy().hasHeightForWidth())
        self.inp_signal_combo.setSizePolicy(sizePolicy1)
        self.inp_signal_combo.setMinimumSize(QSize(0, 22))
        self.inp_signal_combo.setMaximumSize(QSize(16777215, 22))
        self.inp_signal_combo.setSizeAdjustPolicy(QComboBox.SizeAdjustPolicy.AdjustToContentsOnFirstShow)

        self.horizontalLayout_2.addWidget(self.inp_signal_combo)

        self.config_signal_button = QPushButton(self.widget_19)
        self.config_signal_button.setObjectName(u"config_signal_button")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.config_signal_button.sizePolicy().hasHeightForWidth())
        self.config_signal_button.setSizePolicy(sizePolicy2)
        self.config_signal_button.setMinimumSize(QSize(0, 30))
        self.config_signal_button.setMaximumSize(QSize(16777215, 30))

        self.horizontalLayout_2.addWidget(self.config_signal_button, 0, Qt.AlignmentFlag.AlignRight)


        self.gridLayout.addWidget(self.widget_19, 10, 2, 1, 1)

        self.widget_5 = QWidget(self.widget)
        self.widget_5.setObjectName(u"widget_5")
        self.gridLayout_6 = QGridLayout(self.widget_5)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.Ts_in = QDoubleSpinBox(self.widget_5)
        self.Ts_in.setObjectName(u"Ts_in")
        self.Ts_in.setMinimumSize(QSize(0, 22))
        self.Ts_in.setMaximumSize(QSize(16777215, 22))
        self.Ts_in.setDecimals(2)
        self.Ts_in.setMinimum(0.010000000000000)
        self.Ts_in.setSingleStep(0.010000000000000)
        self.Ts_in.setStepType(QAbstractSpinBox.StepType.AdaptiveDecimalStepType)
        self.Ts_in.setValue(0.500000000000000)

        self.gridLayout_6.addWidget(self.Ts_in, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.widget_5, 4, 2, 1, 1)

        self.label_12 = QLabel(self.widget)
        self.label_12.setObjectName(u"label_12")

        self.gridLayout.addWidget(self.label_12, 2, 0, 1, 1)

        self.widget_13 = QWidget(self.widget)
        self.widget_13.setObjectName(u"widget_13")
        self.gridLayout_11 = QGridLayout(self.widget_13)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.ao_channel_combo = QComboBox(self.widget_13)
        self.ao_channel_combo.setObjectName(u"ao_channel_combo")
        self.ao_channel_combo.setMinimumSize(QSize(0, 22))
        self.ao_channel_combo.setMaximumSize(QSize(16777215, 22))

        self.gridLayout_11.addWidget(self.ao_channel_combo, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.widget_13, 2, 2, 1, 1)


        self.verticalLayout.addWidget(self.widget)

        self.line_3 = QFrame(Arduino_GetModel_W)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.Shape.HLine)
        self.line_3.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout.addWidget(self.line_3)

        self.widget_3 = QWidget(Arduino_GetModel_W)
        self.widget_3.setObjectName(u"widget_3")
        self.gridLayout_4 = QGridLayout(self.widget_3)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.start_get_model = QPushButton(self.widget_3)
        self.start_get_model.setObjectName(u"start_get_model")
        self.start_get_model.setMinimumSize(QSize(0, 30))
        self.start_get_model.setMaximumSize(QSize(16777215, 30))
        self.start_get_model.setStyleSheet(u"")

        self.gridLayout_4.addWidget(self.start_get_model, 0, 0, 1, 1, Qt.AlignmentFlag.AlignHCenter)


        self.verticalLayout.addWidget(self.widget_3)


        self.retranslateUi(Arduino_GetModel_W)

        QMetaObject.connectSlotsByName(Arduino_GetModel_W)
    # setupUi

    def retranslateUi(self, Arduino_GetModel_W):
        Arduino_GetModel_W.setWindowTitle(QCoreApplication.translate("Arduino_GetModel_W", u"Form", None))
        self.path_folder_browse.setText(QCoreApplication.translate("Arduino_GetModel_W", u" BROWSE ", None))
        self.label_2.setText(QCoreApplication.translate("Arduino_GetModel_W", u"Input signal:", None))
        self.label_11.setText(QCoreApplication.translate("Arduino_GetModel_W", u"Terminal Config.", None))
        self.yes_rt_plot_radio.setText(QCoreApplication.translate("Arduino_GetModel_W", u"Real time", None))
        self.no_plot_radio.setText(QCoreApplication.translate("Arduino_GetModel_W", u"No", None))
        self.yes_ate_plot_radio.setText(QCoreApplication.translate("Arduino_GetModel_W", u"At the end", None))
#if QT_CONFIG(tooltip)
        self.label_warning.setToolTip(QCoreApplication.translate("Arduino_GetModel_W", u"<html><head/><body><p><span style=\" font-size:16pt;\">Selecting Real Time may reduce your acquisition performance if you need to collect data at high frequencies ( sample period &lt; 0.05 s ). We suggest plotting at the end of the acquisition if you don't want to be affected.</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_warning.setText(QCoreApplication.translate("Arduino_GetModel_W", u"<html><head/><body><p><img src=\":/imgs/imgs/Warning_logo.png\"/></p></body></html>", None))
        self.label_8.setText(QCoreApplication.translate("Arduino_GetModel_W", u"Path:", None))
        self.label.setText(QCoreApplication.translate("Arduino_GetModel_W", u"Device:", None))
        self.label_3.setText(QCoreApplication.translate("Arduino_GetModel_W", u"System identification:", None))
        self.yes_save_radio.setText(QCoreApplication.translate("Arduino_GetModel_W", u"Yes", None))
        self.no_save_radio.setText(QCoreApplication.translate("Arduino_GetModel_W", u"No", None))
        self.label_9.setText(QCoreApplication.translate("Arduino_GetModel_W", u"Start saving data (s):", None))
        self.label_6.setText(QCoreApplication.translate("Arduino_GetModel_W", u"Plot data?", None))
        self.label_7.setText(QCoreApplication.translate("Arduino_GetModel_W", u"Save data?", None))
        self.label_5.setText(QCoreApplication.translate("Arduino_GetModel_W", u"Session duration (s):", None))
        self.label_10.setText(QCoreApplication.translate("Arduino_GetModel_W", u"Channel ai:", None))
        self.system_settings_button.setText(QCoreApplication.translate("Arduino_GetModel_W", u" ADVANCED SETTINGS ", None))
        self.reload_devices.setText("")
        self.label_4.setText(QCoreApplication.translate("Arduino_GetModel_W", u"Sample period (s):", None))
        self.config_signal_button.setText(QCoreApplication.translate("Arduino_GetModel_W", u" CONFIG SIGNAL ", None))
        self.label_12.setText(QCoreApplication.translate("Arduino_GetModel_W", u"Channel ao:", None))
        self.start_get_model.setText(QCoreApplication.translate("Arduino_GetModel_W", u" GET MODEL ", None))
    # retranslateUi

