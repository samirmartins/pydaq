# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'PyDAQ_pid_control_NIDAQ_widgetLGKsQT.ui'
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
from PySide6.QtWidgets import (QApplication, QButtonGroup, QComboBox, QDoubleSpinBox,
    QFrame, QGridLayout, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QRadioButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_NIDAQ_PID_Control(object):
    def setupUi(self, NIDAQ_PID_Control):
        if not NIDAQ_PID_Control.objectName():
            NIDAQ_PID_Control.setObjectName(u"NIDAQ_PID_Control")
        NIDAQ_PID_Control.resize(597, 1031)
        NIDAQ_PID_Control.setStyleSheet(u"QWidget{\n"
"	background-color: rgb(64, 64, 64);\n"
"}\n"
"\n"
"QTabWidget::pane { \n"
"   border: 1px solid rgb(166, 166, 166);\n"
"}\n"
"\n"
"QTabBar::tab {\n"
"  	background-color: rgb(77, 77, 77);\n"
" }\n"
"\n"
" QTabBar::tab:selected {\n"
"  	background-color: rgb(140, 140, 140);\n"
"	padding-top: 2px;\n"
"	padding-bottom: 2px;\n"
"	padding-left: 12px;\n"
"	padding-right: 12px;\n"
" }\n"
"\n"
" QTabBar::tab:selected:hover {\n"
"  	background-color: rgb(140, 140, 140);\n"
"	padding-top: 2px;\n"
"	padding-bottom: 2px;\n"
"	padding-left: 12px;\n"
"	padding-right: 12px;\n"
" }\n"
"\n"
" QTabBar::tab:hover {\n"
"  	background-color: rgb(109, 109, 109);\n"
"	padding-top: 2px;\n"
"	padding-bottom: 2px;\n"
"	padding-left: 12px;\n"
"	padding-right: 12px;\n"
" }\n"
"\n"
" QTabBar::tab:middle {\n"
"	border-right: 1px dashed rgb(166, 166, 166);\n"
"	border-left: 1px dashed rgb(166, 166, 166);\n"
"	padding-top: 2px;\n"
"	padding-bottom: 2px;\n"
"	padding-left: 12px;\n"
"	padding-right: 12px;\n"
" }\n"
"\n"
" QTabBar:"
                        ":tab:last {\n"
"	border-top-right-radius: 10px;\n"
"	padding-top: 2px;\n"
"	padding-bottom: 2px;\n"
"	padding-left: 12px;\n"
"	padding-right: 12px;\n"
" }\n"
"\n"
" QTabBar::tab:first {\n"
"	border-top-left-radius: 10px;\n"
"	padding-top: 2px;\n"
"	padding-bottom: 2px;\n"
"	padding-left: 12px;\n"
"	padding-right: 12px;\n"
" }\n"
"\n"
"\n"
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
"	border-left: 1.5px sol"
                        "id rgb(127, 167, 127);\n"
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
"QWidget#centralwidget{\n"
"	background-color: rgb(64, 64, 64);\n"
"}\n"
"\n"
"QWidget{\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QComboBox{\n"
"	background-color: rgb(77, "
                        "77, 77);\n"
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
"	font: 12pt \"Helve"
                        "tica\";\n"
"	text-align:center;\n"
"}\n"
"\n"
"QWidget{\n"
"	font: 12pt \"Helvetica\";\n"
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
""
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
"}\n"
"\n"
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
"	border"
                        "-top: 1.5px solid rgb(127, 167, 127);\n"
"	border-left: 1.5px solid rgb(127, 167, 127);\n"
"\n"
"	border-bottom: 1.5px solid rgb(0, 0, 0);\n"
"	border-right: 1.5px solid rgb(0, 0, 0);\n"
"}\n"
"\n"
"QDoubleSpinBox:disabled {\n"
"    background-color: rgb(50, 50, 50);\n"
"    \n"
"    border-top: 1.5px solid rgb(30, 30, 30);\n"
"    border-left: 1.5px solid rgb(30, 30, 30);\n"
"    \n"
"    border-bottom: 1.5px solid rgb(100, 100, 100);\n"
"    border-right: 1.5px solid rgb(100, 100, 100);\n"
"    \n"
"    color: rgb(150, 150, 150);\n"
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
"    image: url(:/imgs/imgs/drop_down_arrow.png);\n"
"	width: 11px;\n"
"\n"
"	background-color: rgb(0, 79, 0);\n"
"	border-top: 1.5px solid rgb(127, 167, 127);\n"
"	border-left: 1.5px solid rgb(127, 167, 127);\n"
"\n"
"	border-bottom: 1.5px solid rgb(0, 0, 0);\n"
""
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
"")
        self.gridLayout = QGridLayout(NIDAQ_PID_Control)
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame_equation = QFrame(NIDAQ_PID_Control)
        self.frame_equation.setObjectName(u"frame_equation")
        self.frame_equation.setMinimumSize(QSize(400, 120))
        self.frame_equation.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_equation.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_5 = QGridLayout(self.frame_equation)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.widget_image = QWidget(self.frame_equation)
        self.widget_image.setObjectName(u"widget_image")
        self.widget_image.setMinimumSize(QSize(0, 100))
        self.image_layout = QVBoxLayout(self.widget_image)
        self.image_layout.setObjectName(u"image_layout")

        self.gridLayout_5.addWidget(self.widget_image, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.frame_equation, 3, 0, 1, 1)

        self.widget_top = QWidget(NIDAQ_PID_Control)
        self.widget_top.setObjectName(u"widget_top")
        self.gridLayout_2 = QGridLayout(self.widget_top)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_terminal = QLabel(self.widget_top)
        self.label_terminal.setObjectName(u"label_terminal")

        self.gridLayout_2.addWidget(self.label_terminal, 6, 0, 1, 1)

        self.line = QFrame(self.widget_top)
        self.line.setObjectName(u"line")
        self.line.setMinimumSize(QSize(0, 0))
        self.line.setFrameShape(QFrame.Shape.VLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_2.addWidget(self.line, 0, 2, 20, 1)

        self.label_setpoint = QLabel(self.widget_top)
        self.label_setpoint.setObjectName(u"label_setpoint")
        self.label_setpoint.setMinimumSize(QSize(0, 30))

        self.gridLayout_2.addWidget(self.label_setpoint, 7, 0, 1, 1)

        self.pushButton_confirm = QPushButton(self.widget_top)
        self.pushButton_confirm.setObjectName(u"pushButton_confirm")
        self.pushButton_confirm.setMinimumSize(QSize(80, 30))
        self.pushButton_confirm.setMaximumSize(QSize(100, 16777215))

        self.gridLayout_2.addWidget(self.pushButton_confirm, 18, 3, 1, 1, Qt.AlignmentFlag.AlignHCenter)

        self.widget_path = QWidget(self.widget_top)
        self.widget_path.setObjectName(u"widget_path")
        self.horizontalLayout_10 = QHBoxLayout(self.widget_path)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.path_line_edit = QLineEdit(self.widget_path)
        self.path_line_edit.setObjectName(u"path_line_edit")
        self.path_line_edit.setMinimumSize(QSize(0, 22))

        self.horizontalLayout_10.addWidget(self.path_line_edit)

        self.path_folder_browse = QPushButton(self.widget_path)
        self.path_folder_browse.setObjectName(u"path_folder_browse")
        self.path_folder_browse.setMinimumSize(QSize(70, 30))

        self.horizontalLayout_10.addWidget(self.path_folder_browse)


        self.gridLayout_2.addWidget(self.widget_path, 17, 3, 1, 1, Qt.AlignmentFlag.AlignVCenter)

        self.label_kd = QLabel(self.widget_top)
        self.label_kd.setObjectName(u"label_kd")
        self.label_kd.setMinimumSize(QSize(0, 30))

        self.gridLayout_2.addWidget(self.label_kd, 15, 0, 1, 1)

        self.label_save = QLabel(self.widget_top)
        self.label_save.setObjectName(u"label_save")

        self.gridLayout_2.addWidget(self.label_save, 16, 0, 1, 1)

        self.widget_period = QWidget(self.widget_top)
        self.widget_period.setObjectName(u"widget_period")
        self.horizontalLayout_8 = QHBoxLayout(self.widget_period)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.doubleSpinBox_period = QDoubleSpinBox(self.widget_period)
        self.doubleSpinBox_period.setObjectName(u"doubleSpinBox_period")
        self.doubleSpinBox_period.setDecimals(6)
        self.doubleSpinBox_period.setMaximum(9999999.000000000000000)
        self.doubleSpinBox_period.setSingleStep(0.100000000000000)
        self.doubleSpinBox_period.setValue(1.000000000000000)

        self.horizontalLayout_8.addWidget(self.doubleSpinBox_period)


        self.gridLayout_2.addWidget(self.widget_period, 11, 3, 1, 1)

        self.label_i_equation = QLabel(self.widget_top)
        self.label_i_equation.setObjectName(u"label_i_equation")

        self.gridLayout_2.addWidget(self.label_i_equation, 9, 1, 1, 1, Qt.AlignmentFlag.AlignRight)

        self.widget_kp = QWidget(self.widget_top)
        self.widget_kp.setObjectName(u"widget_kp")
        self.horizontalLayout_6 = QHBoxLayout(self.widget_kp)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.doubleSpinBox_kp = QDoubleSpinBox(self.widget_kp)
        self.doubleSpinBox_kp.setObjectName(u"doubleSpinBox_kp")
        self.doubleSpinBox_kp.setMaximum(999999.000000000000000)
        self.doubleSpinBox_kp.setSingleStep(0.100000000000000)
        self.doubleSpinBox_kp.setValue(1.000000000000000)

        self.horizontalLayout_6.addWidget(self.doubleSpinBox_kp)


        self.gridLayout_2.addWidget(self.widget_kp, 13, 3, 1, 1)

        self.widget_nidaq = QWidget(self.widget_top)
        self.widget_nidaq.setObjectName(u"widget_nidaq")
        self.horizontalLayout_2 = QHBoxLayout(self.widget_nidaq)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.device_combo = QComboBox(self.widget_nidaq)
        self.device_combo.setObjectName(u"device_combo")
        self.device_combo.setMinimumSize(QSize(0, 0))
        self.device_combo.setMaximumSize(QSize(9000000, 16777215))

        self.horizontalLayout_2.addWidget(self.device_combo)

        self.reload_devices = QPushButton(self.widget_nidaq)
        self.reload_devices.setObjectName(u"reload_devices")
        self.reload_devices.setMinimumSize(QSize(22, 22))
        self.reload_devices.setMaximumSize(QSize(22, 22))

        self.horizontalLayout_2.addWidget(self.reload_devices)


        self.gridLayout_2.addWidget(self.widget_nidaq, 3, 3, 1, 1)

        self.widget_ki = QWidget(self.widget_top)
        self.widget_ki.setObjectName(u"widget_ki")
        self.horizontalLayout_4 = QHBoxLayout(self.widget_ki)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.doubleSpinBox_ki = QDoubleSpinBox(self.widget_ki)
        self.doubleSpinBox_ki.setObjectName(u"doubleSpinBox_ki")
        self.doubleSpinBox_ki.setMaximum(999999.000000000000000)
        self.doubleSpinBox_ki.setSingleStep(0.100000000000000)

        self.horizontalLayout_4.addWidget(self.doubleSpinBox_ki)


        self.gridLayout_2.addWidget(self.widget_ki, 14, 3, 1, 1)

        self.widget_unit = QWidget(self.widget_top)
        self.widget_unit.setObjectName(u"widget_unit")
        self.horizontalLayout = QHBoxLayout(self.widget_unit)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lineEdit_unit = QLineEdit(self.widget_unit)
        self.lineEdit_unit.setObjectName(u"lineEdit_unit")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(10)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_unit.sizePolicy().hasHeightForWidth())
        self.lineEdit_unit.setSizePolicy(sizePolicy)
        self.lineEdit_unit.setMaximumSize(QSize(9999999, 16777215))

        self.horizontalLayout.addWidget(self.lineEdit_unit)


        self.gridLayout_2.addWidget(self.widget_unit, 8, 3, 1, 1, Qt.AlignmentFlag.AlignVCenter)

        self.label_periody = QLabel(self.widget_top)
        self.label_periody.setObjectName(u"label_periody")
        self.label_periody.setMinimumSize(QSize(0, 30))

        self.gridLayout_2.addWidget(self.label_periody, 11, 0, 1, 1)

        self.widget_type = QWidget(self.widget_top)
        self.widget_type.setObjectName(u"widget_type")
        self.widget_type.setMinimumSize(QSize(100, 0))
        self.horizontalLayout_7 = QHBoxLayout(self.widget_type)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.comboBox_type = QComboBox(self.widget_type)
        self.comboBox_type.addItem("")
        self.comboBox_type.addItem("")
        self.comboBox_type.addItem("")
        self.comboBox_type.addItem("")
        self.comboBox_type.setObjectName(u"comboBox_type")
        self.comboBox_type.setMinimumSize(QSize(0, 25))
        self.comboBox_type.setMaximumSize(QSize(9000000, 16777215))

        self.horizontalLayout_7.addWidget(self.comboBox_type)


        self.gridLayout_2.addWidget(self.widget_type, 12, 3, 1, 1)

        self.widget_ai_channel = QWidget(self.widget_top)
        self.widget_ai_channel.setObjectName(u"widget_ai_channel")
        self.horizontalLayout_13 = QHBoxLayout(self.widget_ai_channel)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.ai_channel_combo = QComboBox(self.widget_ai_channel)
        self.ai_channel_combo.setObjectName(u"ai_channel_combo")

        self.horizontalLayout_13.addWidget(self.ai_channel_combo)


        self.gridLayout_2.addWidget(self.widget_ai_channel, 4, 3, 1, 1)

        self.label_type = QLabel(self.widget_top)
        self.label_type.setObjectName(u"label_type")
        self.label_type.setMinimumSize(QSize(0, 30))

        self.gridLayout_2.addWidget(self.label_type, 12, 0, 1, 1)

        self.label_unit = QLabel(self.widget_top)
        self.label_unit.setObjectName(u"label_unit")
        self.label_unit.setMinimumSize(QSize(0, 30))

        self.gridLayout_2.addWidget(self.label_unit, 8, 0, 1, 1)

        self.label_i_type = QLabel(self.widget_top)
        self.label_i_type.setObjectName(u"label_i_type")

        self.gridLayout_2.addWidget(self.label_i_type, 12, 1, 1, 1)

        self.widget_6 = QWidget(self.widget_top)
        self.widget_6.setObjectName(u"widget_6")
        self.horizontalLayout_9 = QHBoxLayout(self.widget_6)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.yes_simulate_radio = QRadioButton(self.widget_6)
        self.simulate_radio_group = QButtonGroup(NIDAQ_PID_Control)
        self.simulate_radio_group.setObjectName(u"simulate_radio_group")
        self.simulate_radio_group.addButton(self.yes_simulate_radio)
        self.yes_simulate_radio.setObjectName(u"yes_simulate_radio")

        self.horizontalLayout_9.addWidget(self.yes_simulate_radio)

        self.no_simulate_radio = QRadioButton(self.widget_6)
        self.simulate_radio_group.addButton(self.no_simulate_radio)
        self.no_simulate_radio.setObjectName(u"no_simulate_radio")
        self.no_simulate_radio.setChecked(True)

        self.horizontalLayout_9.addWidget(self.no_simulate_radio)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_2)


        self.gridLayout_2.addWidget(self.widget_6, 1, 3, 1, 1)

        self.label_simulate = QLabel(self.widget_top)
        self.label_simulate.setObjectName(u"label_simulate")

        self.gridLayout_2.addWidget(self.label_simulate, 1, 0, 1, 1)

        self.widget_3 = QWidget(self.widget_top)
        self.widget_3.setObjectName(u"widget_3")
        self.horizontalLayout_12 = QHBoxLayout(self.widget_3)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.yes_save_radio = QRadioButton(self.widget_3)
        self.save_radio_group = QButtonGroup(NIDAQ_PID_Control)
        self.save_radio_group.setObjectName(u"save_radio_group")
        self.save_radio_group.addButton(self.yes_save_radio)
        self.yes_save_radio.setObjectName(u"yes_save_radio")
        self.yes_save_radio.setAutoFillBackground(False)
        self.yes_save_radio.setChecked(True)

        self.horizontalLayout_12.addWidget(self.yes_save_radio)

        self.no_save_radio = QRadioButton(self.widget_3)
        self.save_radio_group.addButton(self.no_save_radio)
        self.no_save_radio.setObjectName(u"no_save_radio")

        self.horizontalLayout_12.addWidget(self.no_save_radio)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer)


        self.gridLayout_2.addWidget(self.widget_3, 16, 3, 1, 1)

        self.label_path = QLabel(self.widget_top)
        self.label_path.setObjectName(u"label_path")

        self.gridLayout_2.addWidget(self.label_path, 17, 0, 1, 1)

        self.widget_kd = QWidget(self.widget_top)
        self.widget_kd.setObjectName(u"widget_kd")
        self.horizontalLayout_5 = QHBoxLayout(self.widget_kd)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.doubleSpinBox_kd = QDoubleSpinBox(self.widget_kd)
        self.doubleSpinBox_kd.setObjectName(u"doubleSpinBox_kd")
        self.doubleSpinBox_kd.setMaximum(9999999.000000000000000)
        self.doubleSpinBox_kd.setSingleStep(0.100000000000000)

        self.horizontalLayout_5.addWidget(self.doubleSpinBox_kd)


        self.gridLayout_2.addWidget(self.widget_kd, 15, 3, 1, 1, Qt.AlignmentFlag.AlignVCenter)

        self.label_ai_channel = QLabel(self.widget_top)
        self.label_ai_channel.setObjectName(u"label_ai_channel")

        self.gridLayout_2.addWidget(self.label_ai_channel, 4, 0, 1, 1)

        self.widget_terminal_config = QWidget(self.widget_top)
        self.widget_terminal_config.setObjectName(u"widget_terminal_config")
        self.horizontalLayout_11 = QHBoxLayout(self.widget_terminal_config)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.terminal_config_combo = QComboBox(self.widget_terminal_config)
        self.terminal_config_combo.setObjectName(u"terminal_config_combo")

        self.horizontalLayout_11.addWidget(self.terminal_config_combo)


        self.gridLayout_2.addWidget(self.widget_terminal_config, 6, 3, 1, 1)

        self.widget_setpoint = QWidget(self.widget_top)
        self.widget_setpoint.setObjectName(u"widget_setpoint")
        self.horizontalLayout_3 = QHBoxLayout(self.widget_setpoint)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.doubleSpinBox_setpoint = QDoubleSpinBox(self.widget_setpoint)
        self.doubleSpinBox_setpoint.setObjectName(u"doubleSpinBox_setpoint")
        self.doubleSpinBox_setpoint.setMaximumSize(QSize(100, 16777215))
        self.doubleSpinBox_setpoint.setMaximum(9999999.000000000000000)
        self.doubleSpinBox_setpoint.setSingleStep(0.100000000000000)
        self.doubleSpinBox_setpoint.setValue(5.000000000000000)

        self.horizontalLayout_3.addWidget(self.doubleSpinBox_setpoint)

        self.comboBox_setpoint = QComboBox(self.widget_setpoint)
        self.comboBox_setpoint.addItem("")
        self.comboBox_setpoint.addItem("")
        self.comboBox_setpoint.addItem("")
        self.comboBox_setpoint.setObjectName(u"comboBox_setpoint")
        self.comboBox_setpoint.setMinimumSize(QSize(190, 0))
        self.comboBox_setpoint.setMaximumSize(QSize(9000000, 16777215))

        self.horizontalLayout_3.addWidget(self.comboBox_setpoint)


        self.gridLayout_2.addWidget(self.widget_setpoint, 7, 3, 1, 1)

        self.label_ki = QLabel(self.widget_top)
        self.label_ki.setObjectName(u"label_ki")
        self.label_ki.setMinimumSize(QSize(0, 30))

        self.gridLayout_2.addWidget(self.label_ki, 14, 0, 1, 1)

        self.label_nidaq = QLabel(self.widget_top)
        self.label_nidaq.setObjectName(u"label_nidaq")
        self.label_nidaq.setMinimumSize(QSize(154, 30))
        self.label_nidaq.setMaximumSize(QSize(160, 16777215))

        self.gridLayout_2.addWidget(self.label_nidaq, 3, 0, 1, 1)

        self.label_equation = QLabel(self.widget_top)
        self.label_equation.setObjectName(u"label_equation")
        self.label_equation.setMinimumSize(QSize(0, 30))

        self.gridLayout_2.addWidget(self.label_equation, 9, 0, 1, 1)

        self.label_ao_channel = QLabel(self.widget_top)
        self.label_ao_channel.setObjectName(u"label_ao_channel")

        self.gridLayout_2.addWidget(self.label_ao_channel, 5, 0, 1, 1)

        self.label_kp = QLabel(self.widget_top)
        self.label_kp.setObjectName(u"label_kp")
        self.label_kp.setMinimumSize(QSize(0, 30))

        self.gridLayout_2.addWidget(self.label_kp, 13, 0, 1, 1)

        self.widget_ao_channel = QWidget(self.widget_top)
        self.widget_ao_channel.setObjectName(u"widget_ao_channel")
        self.horizontalLayout_14 = QHBoxLayout(self.widget_ao_channel)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.ao_channel_combo = QComboBox(self.widget_ao_channel)
        self.ao_channel_combo.setObjectName(u"ao_channel_combo")

        self.horizontalLayout_14.addWidget(self.ao_channel_combo)


        self.gridLayout_2.addWidget(self.widget_ao_channel, 5, 3, 1, 1)

        self.widget_equation = QWidget(self.widget_top)
        self.widget_equation.setObjectName(u"widget_equation")
        self.horizontalLayout_15 = QHBoxLayout(self.widget_equation)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.label_vunit = QLabel(self.widget_equation)
        self.label_vunit.setObjectName(u"label_vunit")

        self.horizontalLayout_15.addWidget(self.label_vunit)

        self.lineEdit_equationvu = QLineEdit(self.widget_equation)
        self.lineEdit_equationvu.setObjectName(u"lineEdit_equationvu")

        self.horizontalLayout_15.addWidget(self.lineEdit_equationvu)

        self.label_unitv = QLabel(self.widget_equation)
        self.label_unitv.setObjectName(u"label_unitv")

        self.horizontalLayout_15.addWidget(self.label_unitv)

        self.lineEdit_equationuv = QLineEdit(self.widget_equation)
        self.lineEdit_equationuv.setObjectName(u"lineEdit_equationuv")

        self.horizontalLayout_15.addWidget(self.lineEdit_equationuv)


        self.gridLayout_2.addWidget(self.widget_equation, 9, 3, 1, 1)

        self.label_system_equation = QLabel(self.widget_top)
        self.label_system_equation.setObjectName(u"label_system_equation")

        self.gridLayout_2.addWidget(self.label_system_equation, 2, 0, 1, 1)

        self.label_i_polinomial = QLabel(self.widget_top)
        self.label_i_polinomial.setObjectName(u"label_i_polinomial")

        self.gridLayout_2.addWidget(self.label_i_polinomial, 2, 1, 1, 1)

        self.widget_polynomial = QWidget(self.widget_top)
        self.widget_polynomial.setObjectName(u"widget_polynomial")
        self.horizontalLayout_16 = QHBoxLayout(self.widget_polynomial)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.label_numerator = QLabel(self.widget_polynomial)
        self.label_numerator.setObjectName(u"label_numerator")

        self.horizontalLayout_16.addWidget(self.label_numerator)

        self.lineEdit_numerator = QLineEdit(self.widget_polynomial)
        self.lineEdit_numerator.setObjectName(u"lineEdit_numerator")

        self.horizontalLayout_16.addWidget(self.lineEdit_numerator)

        self.label_denominator = QLabel(self.widget_polynomial)
        self.label_denominator.setObjectName(u"label_denominator")

        self.horizontalLayout_16.addWidget(self.label_denominator)

        self.lineEdit_denominator = QLineEdit(self.widget_polynomial)
        self.lineEdit_denominator.setObjectName(u"lineEdit_denominator")

        self.horizontalLayout_16.addWidget(self.lineEdit_denominator)


        self.gridLayout_2.addWidget(self.widget_polynomial, 2, 3, 1, 1)


        self.gridLayout.addWidget(self.widget_top, 2, 0, 1, 1)

        self.line_2 = QFrame(NIDAQ_PID_Control)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setMinimumSize(QSize(0, 0))
        self.line_2.setFrameShape(QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout.addWidget(self.line_2, 1, 0, 1, 1)

        self.line_3 = QFrame(NIDAQ_PID_Control)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setMinimumSize(QSize(0, 0))
        self.line_3.setFrameShape(QFrame.Shape.HLine)
        self.line_3.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout.addWidget(self.line_3, 4, 0, 1, 1)

        self.pushButton_start = QPushButton(NIDAQ_PID_Control)
        self.pushButton_start.setObjectName(u"pushButton_start")
        self.pushButton_start.setMinimumSize(QSize(120, 30))
        self.pushButton_start.setMaximumSize(QSize(150, 30))

        self.gridLayout.addWidget(self.pushButton_start, 5, 0, 1, 1, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)


        self.retranslateUi(NIDAQ_PID_Control)

        QMetaObject.connectSlotsByName(NIDAQ_PID_Control)
    # setupUi

    def retranslateUi(self, NIDAQ_PID_Control):
        NIDAQ_PID_Control.setWindowTitle(QCoreApplication.translate("NIDAQ_PID_Control", u"Form", None))
        self.label_terminal.setText(QCoreApplication.translate("NIDAQ_PID_Control", u"Terminal config.:", None))
        self.label_setpoint.setText(QCoreApplication.translate("NIDAQ_PID_Control", u"Setpoint:", None))
        self.pushButton_confirm.setText(QCoreApplication.translate("NIDAQ_PID_Control", u"Confirm", None))
        self.path_folder_browse.setText(QCoreApplication.translate("NIDAQ_PID_Control", u"Browse", None))
        self.label_kd.setText(QCoreApplication.translate("NIDAQ_PID_Control", u"Kd:", None))
        self.label_save.setText(QCoreApplication.translate("NIDAQ_PID_Control", u"Save Data?", None))
#if QT_CONFIG(tooltip)
        self.label_i_equation.setToolTip(QCoreApplication.translate("NIDAQ_PID_Control", u"<html><head/><body><p><span style=\" font-size:14pt;\">The equation should be written in the form: Ax\u00b2+Bx+C</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_i_equation.setText(QCoreApplication.translate("NIDAQ_PID_Control", u"<html><head/><body><p><img src=\":/imgs/imgs/inform.png\"/></p></body></html>", None))
        self.reload_devices.setText("")
        self.lineEdit_unit.setText(QCoreApplication.translate("NIDAQ_PID_Control", u"Current (A)", None))
        self.label_periody.setText(QCoreApplication.translate("NIDAQ_PID_Control", u"Sampling period (s):", None))
        self.comboBox_type.setItemText(0, QCoreApplication.translate("NIDAQ_PID_Control", u"P", None))
        self.comboBox_type.setItemText(1, QCoreApplication.translate("NIDAQ_PID_Control", u"PI", None))
        self.comboBox_type.setItemText(2, QCoreApplication.translate("NIDAQ_PID_Control", u"PD", None))
        self.comboBox_type.setItemText(3, QCoreApplication.translate("NIDAQ_PID_Control", u"PID", None))

#if QT_CONFIG(tooltip)
        self.label_type.setToolTip(QCoreApplication.translate("NIDAQ_PID_Control", u"<html><head/><body><p><img src=\":/imgs/imgs/PID_Flow.png\"/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_type.setText(QCoreApplication.translate("NIDAQ_PID_Control", u"Controler type?", None))
        self.label_unit.setText(QCoreApplication.translate("NIDAQ_PID_Control", u"Unit:", None))
#if QT_CONFIG(tooltip)
        self.label_i_type.setToolTip(QCoreApplication.translate("NIDAQ_PID_Control", u"<html><head/><body><p><img src=\":/imgs/imgs/PID_Flow.png\"/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_i_type.setText(QCoreApplication.translate("NIDAQ_PID_Control", u"<html><head/><body><p><img src=\":/imgs/imgs/inform.png\"/></p></body></html>", None))
        self.yes_simulate_radio.setText(QCoreApplication.translate("NIDAQ_PID_Control", u"Yes", None))
        self.no_simulate_radio.setText(QCoreApplication.translate("NIDAQ_PID_Control", u"No", None))
        self.label_simulate.setText(QCoreApplication.translate("NIDAQ_PID_Control", u"Simulate?", None))
        self.yes_save_radio.setText(QCoreApplication.translate("NIDAQ_PID_Control", u"Yes", None))
        self.no_save_radio.setText(QCoreApplication.translate("NIDAQ_PID_Control", u"No", None))
        self.label_path.setText(QCoreApplication.translate("NIDAQ_PID_Control", u"Data path:", None))
        self.label_ai_channel.setText(QCoreApplication.translate("NIDAQ_PID_Control", u"AI channel:", None))
        self.comboBox_setpoint.setItemText(0, QCoreApplication.translate("NIDAQ_PID_Control", u"Voltage (V)", None))
        self.comboBox_setpoint.setItemText(1, QCoreApplication.translate("NIDAQ_PID_Control", u"Temperature (C\u00b0)", None))
        self.comboBox_setpoint.setItemText(2, QCoreApplication.translate("NIDAQ_PID_Control", u"Other", None))

        self.label_ki.setText(QCoreApplication.translate("NIDAQ_PID_Control", u"Ki:", None))
        self.label_nidaq.setText(QCoreApplication.translate("NIDAQ_PID_Control", u"Device:", None))
#if QT_CONFIG(tooltip)
        self.label_equation.setToolTip(QCoreApplication.translate("NIDAQ_PID_Control", u"<html><head/><body><p><span style=\" font-size:14pt;\">The equation should be written in the form: Ax\u00b2+Bx+C</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_equation.setText(QCoreApplication.translate("NIDAQ_PID_Control", u"Calibration equation:", None))
        self.label_ao_channel.setText(QCoreApplication.translate("NIDAQ_PID_Control", u"AO channel:", None))
        self.label_kp.setText(QCoreApplication.translate("NIDAQ_PID_Control", u"Kp:", None))
        self.label_vunit.setText(QCoreApplication.translate("NIDAQ_PID_Control", u"V(Unit)", None))
        self.lineEdit_equationvu.setText(QCoreApplication.translate("NIDAQ_PID_Control", u"1*x", None))
        self.label_unitv.setText(QCoreApplication.translate("NIDAQ_PID_Control", u"Unit(V)", None))
        self.lineEdit_equationuv.setText(QCoreApplication.translate("NIDAQ_PID_Control", u"1*x", None))
        self.label_system_equation.setText(QCoreApplication.translate("NIDAQ_PID_Control", u"System Equation:", None))
#if QT_CONFIG(tooltip)
        self.label_i_polinomial.setToolTip(QCoreApplication.translate("NIDAQ_PID_Control", u"<html><head/><body><p><span style=\" font-size:14pt;\">Transfer function of a polynomial system G(s) = N(s) / D(s), where N(s) and D(s) are polynomials in s.</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_i_polinomial.setText(QCoreApplication.translate("NIDAQ_PID_Control", u"<html><head/><body><p><img src=\":/imgs/imgs/inform.png\"/></p></body></html>", None))
        self.label_numerator.setText(QCoreApplication.translate("NIDAQ_PID_Control", u"Numerator:", None))
        self.lineEdit_numerator.setText(QCoreApplication.translate("NIDAQ_PID_Control", u"1", None))
        self.label_denominator.setText(QCoreApplication.translate("NIDAQ_PID_Control", u"Denominator:", None))
        self.lineEdit_denominator.setText(QCoreApplication.translate("NIDAQ_PID_Control", u"1*s+0.2", None))
        self.pushButton_start.setText(QCoreApplication.translate("NIDAQ_PID_Control", u"PID CONTROL", None))
    # retranslateUi

