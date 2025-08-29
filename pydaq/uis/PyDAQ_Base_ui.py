# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'PyDAQ_Base.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QButtonGroup, QGridLayout, QHBoxLayout,
    QMainWindow, QMenu, QMenuBar, QPushButton,
    QRadioButton, QScrollArea, QSizePolicy, QStatusBar,
    QTabWidget, QVBoxLayout, QWidget)

from ..guis.getdata_arduino_widget import GetData_Arduino_Widget
from ..guis.getdata_nidaq_widget import GetData_NIDAQ_Widget
from ..guis.getmodel_arduino_widget import GetModel_Arduino_Widget
from ..guis.getmodel_nidaq_widget import GetModel_Nidaq_Widget
from ..guis.pid_control_arduino_widget import PID_Control_Arduino_Widget
from ..guis.pid_control_nidaq_widget import PID_Control_NIDAQ_Widget
from ..guis.senddata_arduino_widget import SendData_Arduino_Widget
from ..guis.senddata_nidaq_widget import SendData_NIDAQ_Widget
from ..guis.stepresponse_arduino_widget import StepResponse_Arduino_Widget
from ..guis.stepresponse_nidaq_widget import StepResponse_NIDAQ_Widget
import resources_1_rc

class Ui_PydaqGlobal(object):
    def setupUi(self, PydaqGlobal):
        if not PydaqGlobal.objectName():
            PydaqGlobal.setObjectName(u"PydaqGlobal")
        PydaqGlobal.resize(1097, 665)
        PydaqGlobal.setMinimumSize(QSize(750, 0))
        icon = QIcon()
        icon.addFile(u":/imgs/imgs/favicon.ico", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        PydaqGlobal.setWindowIcon(icon)
        PydaqGlobal.setIconSize(QSize(24, 24))
        PydaqGlobal.setTabShape(QTabWidget.TabShape.Rounded)
        self.actionArduino = QAction(PydaqGlobal)
        self.actionArduino.setObjectName(u"actionArduino")
        self.actionNIDAQ = QAction(PydaqGlobal)
        self.actionNIDAQ.setObjectName(u"actionNIDAQ")
        self.actionAbout_PYDAQ = QAction(PydaqGlobal)
        self.actionAbout_PYDAQ.setObjectName(u"actionAbout_PYDAQ")
        self.actionArduino_2 = QAction(PydaqGlobal)
        self.actionArduino_2.setObjectName(u"actionArduino_2")
        self.actionNIDAQ_2 = QAction(PydaqGlobal)
        self.actionNIDAQ_2.setObjectName(u"actionNIDAQ_2")
        self.actionAbout = QAction(PydaqGlobal)
        self.actionAbout.setObjectName(u"actionAbout")
        self.actionDocumentation = QAction(PydaqGlobal)
        self.actionDocumentation.setObjectName(u"actionDocumentation")
        self.actionArduino_3 = QAction(PydaqGlobal)
        self.actionArduino_3.setObjectName(u"actionArduino_3")
        self.actionNIDAQ_3 = QAction(PydaqGlobal)
        self.actionNIDAQ_3.setObjectName(u"actionNIDAQ_3")
        self.centralwidget = QWidget(PydaqGlobal)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"QWidget{\n"
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
"QPushButton#logo{\n"
"	background-color: rgb(64, 64, 64);\n"
"	border: 0px;\n"
"}\n"
"\n"
"QPushButton#logo:hover{\n"
"	background-color: rgb(166, 166, 166);\n"
"	border: 1px solid rgb(190, 190, 190) ;\n"
"}\n"
"\n"
"QPushButton#logo:pressed{\n"
"	background-color: rgb(166, 166, 166);\n"
"	border: 1px solid rgb(255, 255, 255) ;\n"
"}\n"
"\n"
"QScrollBar:vertical {\n"
"     border: 1px solid rgb(140, 140, 140);\n"
"     background"
                        ": rgb(140, 140, 140);\n"
"     width: 17px;\n"
"     margin: 17px 0 17px 0;\n"
" }\n"
"QScrollBar::handle:vertical {\n"
"     background: rgb(0, 79, 0);\n"
"     min-height: 20px;\n"
" }\n"
"QScrollBar::add-line:vertical {\n"
"	image: url(:/imgs/imgs/drop_down_arrow.png);\n"
"     border: 1px solid rgb(140, 140, 140);\n"
"     background: rgb(0, 79, 0);\n"
"     height: 15px;\n"
"     subcontrol-position: bottom;\n"
"     subcontrol-origin: margin;\n"
" }\n"
"\n"
"QScrollBar::sub-line:vertical {\n"
"	image: url(:/imgs/imgs/drop_up_arrow.png);\n"
"     border: 1px solid rgb(140, 140, 140);\n"
"     background: rgb(0, 79, 0);\n"
"     height: 15px;\n"
"     subcontrol-position: top;\n"
"     subcontrol-origin: margin;\n"
" }\n"
"\n"
"QScrollBar::add-line:vertical:pressed {\n"
"    border: 1px solid rgb(255, 255, 255);\n"
"	background: rgb(0, 79, 0)\n"
" }\n"
"\n"
"QScrollBar::sub-line:vertical:pressed {\n"
"	border: 1px solid rgb(255, 255, 255);\n"
"	background: rgb(0, 79, 0)\n"
" }\n"
"\n"
"QScrollBar::add-line"
                        ":vertical:hover {\n"
"     background-color: rgb(0, 50, 0);\n"
" }\n"
"\n"
"QScrollBar::sub-line:vertical:hover {\n"
"    background-color: rgb(0, 50, 0);\n"
" }\n"
"\n"
"QScrollBar::handle:vertical:pressed {\n"
"    border: 1px solid rgb(255, 255, 255);\n"
"	background: rgb(0, 79, 0)\n"
" }\n"
"\n"
"QScrollBar::handle:vertical:hover {\n"
"    background-color: rgb(0, 50, 0);\n"
" }\n"
"\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
"QScrollArea{\n"
"	border: none;\n"
"}\n"
"")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.logo = QPushButton(self.centralwidget)
        self.logo.setObjectName(u"logo")
        self.logo.setMinimumSize(QSize(186, 147))
        self.logo.setMaximumSize(QSize(186, 147))
        self.logo.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/imgs/imgs/logo.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.logo.setIcon(icon1)
        self.logo.setIconSize(QSize(182, 143))

        self.verticalLayout.addWidget(self.logo, 0, Qt.AlignmentFlag.AlignHCenter)

        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setStyleSheet(u"")
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.radioButton = QRadioButton(self.widget)
        self.interface_radio = QButtonGroup(PydaqGlobal)
        self.interface_radio.setObjectName(u"interface_radio")
        self.interface_radio.addButton(self.radioButton)
        self.radioButton.setObjectName(u"radioButton")
        self.radioButton.setChecked(True)

        self.horizontalLayout.addWidget(self.radioButton)

        self.radioButton_2 = QRadioButton(self.widget)
        self.interface_radio.addButton(self.radioButton_2)
        self.radioButton_2.setObjectName(u"radioButton_2")
        self.radioButton_2.setChecked(False)

        self.horizontalLayout.addWidget(self.radioButton_2)


        self.verticalLayout.addWidget(self.widget)

        self.widget_2 = QWidget(self.centralwidget)
        self.widget_2.setObjectName(u"widget_2")
        self.gridLayout = QGridLayout(self.widget_2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.nidaq_tabs = QTabWidget(self.widget_2)
        self.nidaq_tabs.setObjectName(u"nidaq_tabs")
        self.nidaq_tabs.setTabPosition(QTabWidget.TabPosition.North)
        self.nidaq_tabs.setDocumentMode(False)
        self.nidaq_tabs.setTabsClosable(False)
        self.nidaq_tabs.setMovable(False)
        self.nidaq_tabs.setTabBarAutoHide(False)
        self.get_data_nidaq = QWidget()
        self.get_data_nidaq.setObjectName(u"get_data_nidaq")
        self.gridLayout_3 = QGridLayout(self.get_data_nidaq)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.scrollArea_2 = QScrollArea(self.get_data_nidaq)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_4 = QWidget()
        self.scrollAreaWidgetContents_4.setObjectName(u"scrollAreaWidgetContents_4")
        self.scrollAreaWidgetContents_4.setGeometry(QRect(0, 0, 507, 335))
        self.gridLayout_8 = QGridLayout(self.scrollAreaWidgetContents_4)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.get_nidaq_placeholder = GetData_NIDAQ_Widget(self.scrollAreaWidgetContents_4)
        self.get_nidaq_placeholder.setObjectName(u"get_nidaq_placeholder")

        self.gridLayout_8.addWidget(self.get_nidaq_placeholder, 0, 0, 1, 1)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_4)

        self.gridLayout_3.addWidget(self.scrollArea_2, 0, 0, 1, 1)

        self.nidaq_tabs.addTab(self.get_data_nidaq, "")
        self.send_data_nidaq_tab = QWidget()
        self.send_data_nidaq_tab.setObjectName(u"send_data_nidaq_tab")
        self.gridLayout_7 = QGridLayout(self.send_data_nidaq_tab)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.scrollArea_3 = QScrollArea(self.send_data_nidaq_tab)
        self.scrollArea_3.setObjectName(u"scrollArea_3")
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollAreaWidgetContents_5 = QWidget()
        self.scrollAreaWidgetContents_5.setObjectName(u"scrollAreaWidgetContents_5")
        self.scrollAreaWidgetContents_5.setGeometry(QRect(0, 0, 82, 28))
        self.gridLayout_10 = QGridLayout(self.scrollAreaWidgetContents_5)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.send_nidaq_placeholder = SendData_NIDAQ_Widget(self.scrollAreaWidgetContents_5)
        self.send_nidaq_placeholder.setObjectName(u"send_nidaq_placeholder")

        self.gridLayout_10.addWidget(self.send_nidaq_placeholder, 0, 0, 1, 1)

        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_5)

        self.gridLayout_7.addWidget(self.scrollArea_3, 0, 0, 1, 1)

        self.nidaq_tabs.addTab(self.send_data_nidaq_tab, "")
        self.step_response_nidaq_tab = QWidget()
        self.step_response_nidaq_tab.setObjectName(u"step_response_nidaq_tab")
        self.gridLayout_6 = QGridLayout(self.step_response_nidaq_tab)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.scrollArea = QScrollArea(self.step_response_nidaq_tab)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents_3 = QWidget()
        self.scrollAreaWidgetContents_3.setObjectName(u"scrollAreaWidgetContents_3")
        self.scrollAreaWidgetContents_3.setGeometry(QRect(0, 0, 82, 28))
        self.gridLayout_9 = QGridLayout(self.scrollAreaWidgetContents_3)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.step_nidaq_placeholder = StepResponse_NIDAQ_Widget(self.scrollAreaWidgetContents_3)
        self.step_nidaq_placeholder.setObjectName(u"step_nidaq_placeholder")

        self.gridLayout_9.addWidget(self.step_nidaq_placeholder, 0, 0, 1, 1)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents_3)

        self.gridLayout_6.addWidget(self.scrollArea, 0, 0, 1, 1)

        self.nidaq_tabs.addTab(self.step_response_nidaq_tab, "")
        self.get_model_nidaq_tab = QWidget()
        self.get_model_nidaq_tab.setObjectName(u"get_model_nidaq_tab")
        self.gridLayout_13 = QGridLayout(self.get_model_nidaq_tab)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.scrollArea_7 = QScrollArea(self.get_model_nidaq_tab)
        self.scrollArea_7.setObjectName(u"scrollArea_7")
        self.scrollArea_7.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 82, 28))
        self.gridLayout_15 = QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.getm_nidaq_placeholder = GetModel_Nidaq_Widget(self.scrollAreaWidgetContents)
        self.getm_nidaq_placeholder.setObjectName(u"getm_nidaq_placeholder")

        self.gridLayout_15.addWidget(self.getm_nidaq_placeholder, 0, 0, 1, 1)

        self.scrollArea_7.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout_13.addWidget(self.scrollArea_7, 0, 0, 1, 1)

        self.nidaq_tabs.addTab(self.get_model_nidaq_tab, "")
        self.pid_control_nidaq_tab = QWidget()
        self.pid_control_nidaq_tab.setObjectName(u"pid_control_nidaq_tab")
        self.gridLayout_20 = QGridLayout(self.pid_control_nidaq_tab)
        self.gridLayout_20.setObjectName(u"gridLayout_20")
        self.scrollArea_10 = QScrollArea(self.pid_control_nidaq_tab)
        self.scrollArea_10.setObjectName(u"scrollArea_10")
        self.scrollArea_10.setWidgetResizable(True)
        self.scrollAreaWidgetContents_9 = QWidget()
        self.scrollAreaWidgetContents_9.setObjectName(u"scrollAreaWidgetContents_9")
        self.scrollAreaWidgetContents_9.setGeometry(QRect(0, 0, 82, 28))
        self.gridLayout_21 = QGridLayout(self.scrollAreaWidgetContents_9)
        self.gridLayout_21.setObjectName(u"gridLayout_21")
        self.widget_4 = PID_Control_NIDAQ_Widget(self.scrollAreaWidgetContents_9)
        self.widget_4.setObjectName(u"widget_4")

        self.gridLayout_21.addWidget(self.widget_4, 0, 0, 1, 1)

        self.scrollArea_10.setWidget(self.scrollAreaWidgetContents_9)

        self.gridLayout_20.addWidget(self.scrollArea_10, 0, 0, 1, 1)

        self.nidaq_tabs.addTab(self.pid_control_nidaq_tab, "")

        self.gridLayout.addWidget(self.nidaq_tabs, 0, 1, 1, 1)

        self.arduino_tabs = QTabWidget(self.widget_2)
        self.arduino_tabs.setObjectName(u"arduino_tabs")
        self.arduino_tabs.setStyleSheet(u"")
        self.arduino_tabs.setTabShape(QTabWidget.TabShape.Rounded)
        self.arduino_tabs.setElideMode(Qt.TextElideMode.ElideNone)
        self.get_data_arduino_tab = QWidget()
        self.get_data_arduino_tab.setObjectName(u"get_data_arduino_tab")
        self.gridLayout_2 = QGridLayout(self.get_data_arduino_tab)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.scrollArea_4 = QScrollArea(self.get_data_arduino_tab)
        self.scrollArea_4.setObjectName(u"scrollArea_4")
        self.scrollArea_4.setWidgetResizable(True)
        self.scrollAreaWidgetContents_6 = QWidget()
        self.scrollAreaWidgetContents_6.setObjectName(u"scrollAreaWidgetContents_6")
        self.scrollAreaWidgetContents_6.setGeometry(QRect(0, 0, 508, 335))
        self.gridLayout_11 = QGridLayout(self.scrollAreaWidgetContents_6)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.get_ino_placeholder = GetData_Arduino_Widget(self.scrollAreaWidgetContents_6)
        self.get_ino_placeholder.setObjectName(u"get_ino_placeholder")

        self.gridLayout_11.addWidget(self.get_ino_placeholder, 0, 0, 1, 1)

        self.scrollArea_4.setWidget(self.scrollAreaWidgetContents_6)

        self.gridLayout_2.addWidget(self.scrollArea_4, 0, 0, 1, 1)

        self.arduino_tabs.addTab(self.get_data_arduino_tab, "")
        self.send_data_arduino_tab = QWidget()
        self.send_data_arduino_tab.setObjectName(u"send_data_arduino_tab")
        self.gridLayout_4 = QGridLayout(self.send_data_arduino_tab)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.scrollArea_5 = QScrollArea(self.send_data_arduino_tab)
        self.scrollArea_5.setObjectName(u"scrollArea_5")
        self.scrollArea_5.setWidgetResizable(True)
        self.scrollAreaWidgetContents_7 = QWidget()
        self.scrollAreaWidgetContents_7.setObjectName(u"scrollAreaWidgetContents_7")
        self.scrollAreaWidgetContents_7.setGeometry(QRect(0, 0, 65, 28))
        self.gridLayout_12 = QGridLayout(self.scrollAreaWidgetContents_7)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.send_ino_placeholder = SendData_Arduino_Widget(self.scrollAreaWidgetContents_7)
        self.send_ino_placeholder.setObjectName(u"send_ino_placeholder")

        self.gridLayout_12.addWidget(self.send_ino_placeholder, 0, 0, 1, 1)

        self.scrollArea_5.setWidget(self.scrollAreaWidgetContents_7)

        self.gridLayout_4.addWidget(self.scrollArea_5, 0, 0, 1, 1)

        self.arduino_tabs.addTab(self.send_data_arduino_tab, "")
        self.step_response_arduino_tab = QWidget()
        self.step_response_arduino_tab.setObjectName(u"step_response_arduino_tab")
        self.gridLayout_5 = QGridLayout(self.step_response_arduino_tab)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.scrollArea_6 = QScrollArea(self.step_response_arduino_tab)
        self.scrollArea_6.setObjectName(u"scrollArea_6")
        self.scrollArea_6.setWidgetResizable(True)
        self.scrollAreaWidgetContents_11 = QWidget()
        self.scrollAreaWidgetContents_11.setObjectName(u"scrollAreaWidgetContents_11")
        self.scrollAreaWidgetContents_11.setGeometry(QRect(0, 0, 65, 28))
        self.gridLayout_14 = QGridLayout(self.scrollAreaWidgetContents_11)
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.step_ino_placeholder = StepResponse_Arduino_Widget(self.scrollAreaWidgetContents_11)
        self.step_ino_placeholder.setObjectName(u"step_ino_placeholder")

        self.gridLayout_14.addWidget(self.step_ino_placeholder, 0, 0, 1, 1)

        self.scrollArea_6.setWidget(self.scrollAreaWidgetContents_11)

        self.gridLayout_5.addWidget(self.scrollArea_6, 0, 0, 1, 1)

        self.arduino_tabs.addTab(self.step_response_arduino_tab, "")
        self.get_model_arduino_tab = QWidget()
        self.get_model_arduino_tab.setObjectName(u"get_model_arduino_tab")
        self.gridLayout_16 = QGridLayout(self.get_model_arduino_tab)
        self.gridLayout_16.setObjectName(u"gridLayout_16")
        self.scrollArea_8 = QScrollArea(self.get_model_arduino_tab)
        self.scrollArea_8.setObjectName(u"scrollArea_8")
        self.scrollArea_8.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 65, 28))
        self.gridLayout_17 = QGridLayout(self.scrollAreaWidgetContents_2)
        self.gridLayout_17.setObjectName(u"gridLayout_17")
        self.getm_arduino_placeholder = GetModel_Arduino_Widget(self.scrollAreaWidgetContents_2)
        self.getm_arduino_placeholder.setObjectName(u"getm_arduino_placeholder")

        self.gridLayout_17.addWidget(self.getm_arduino_placeholder, 0, 0, 1, 1)

        self.scrollArea_8.setWidget(self.scrollAreaWidgetContents_2)

        self.gridLayout_16.addWidget(self.scrollArea_8, 0, 0, 1, 1)

        self.arduino_tabs.addTab(self.get_model_arduino_tab, "")
        self.pid_control_arduino_tab = QWidget()
        self.pid_control_arduino_tab.setObjectName(u"pid_control_arduino_tab")
        self.gridLayout_18 = QGridLayout(self.pid_control_arduino_tab)
        self.gridLayout_18.setObjectName(u"gridLayout_18")
        self.scrollArea_9 = QScrollArea(self.pid_control_arduino_tab)
        self.scrollArea_9.setObjectName(u"scrollArea_9")
        self.scrollArea_9.setWidgetResizable(True)
        self.scrollAreaWidgetContents_8 = QWidget()
        self.scrollAreaWidgetContents_8.setObjectName(u"scrollAreaWidgetContents_8")
        self.scrollAreaWidgetContents_8.setGeometry(QRect(0, 0, 65, 28))
        self.gridLayout_19 = QGridLayout(self.scrollAreaWidgetContents_8)
        self.gridLayout_19.setObjectName(u"gridLayout_19")
        self.widget_3 = PID_Control_Arduino_Widget(self.scrollAreaWidgetContents_8)
        self.widget_3.setObjectName(u"widget_3")

        self.gridLayout_19.addWidget(self.widget_3, 0, 1, 1, 1)

        self.scrollArea_9.setWidget(self.scrollAreaWidgetContents_8)

        self.gridLayout_18.addWidget(self.scrollArea_9, 0, 0, 1, 1)

        self.arduino_tabs.addTab(self.pid_control_arduino_tab, "")

        self.gridLayout.addWidget(self.arduino_tabs, 0, 0, 1, 1)


        self.verticalLayout.addWidget(self.widget_2)

        PydaqGlobal.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(PydaqGlobal)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1097, 33))
        self.menuBeenchmarking = QMenu(self.menubar)
        self.menuBeenchmarking.setObjectName(u"menuBeenchmarking")
        self.menuAbout = QMenu(self.menubar)
        self.menuAbout.setObjectName(u"menuAbout")
        PydaqGlobal.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(PydaqGlobal)
        self.statusbar.setObjectName(u"statusbar")
        PydaqGlobal.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuBeenchmarking.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())
        self.menuBeenchmarking.addAction(self.actionArduino_3)
        self.menuBeenchmarking.addAction(self.actionNIDAQ_3)
        self.menuAbout.addAction(self.actionDocumentation)

        self.retranslateUi(PydaqGlobal)
        self.radioButton.toggled.connect(self.arduino_tabs.show)
        self.radioButton.toggled.connect(self.nidaq_tabs.hide)
        self.radioButton_2.toggled.connect(self.arduino_tabs.hide)
        self.radioButton_2.toggled.connect(self.nidaq_tabs.show)

        self.nidaq_tabs.setCurrentIndex(0)
        self.arduino_tabs.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(PydaqGlobal)
    # setupUi

    def retranslateUi(self, PydaqGlobal):
        PydaqGlobal.setWindowTitle(QCoreApplication.translate("PydaqGlobal", u"PYDAQ Global", None))
        self.actionArduino.setText(QCoreApplication.translate("PydaqGlobal", u"Arduino", None))
        self.actionNIDAQ.setText(QCoreApplication.translate("PydaqGlobal", u"NIDAQ", None))
        self.actionAbout_PYDAQ.setText(QCoreApplication.translate("PydaqGlobal", u"About PYDAQ", None))
        self.actionArduino_2.setText(QCoreApplication.translate("PydaqGlobal", u"Arduino", None))
        self.actionNIDAQ_2.setText(QCoreApplication.translate("PydaqGlobal", u"NIDAQ", None))
        self.actionAbout.setText(QCoreApplication.translate("PydaqGlobal", u"About", None))
        self.actionDocumentation.setText(QCoreApplication.translate("PydaqGlobal", u"Documentation", None))
        self.actionArduino_3.setText(QCoreApplication.translate("PydaqGlobal", u"Arduino", None))
        self.actionNIDAQ_3.setText(QCoreApplication.translate("PydaqGlobal", u"NIDAQ", None))
#if QT_CONFIG(tooltip)
        self.logo.setToolTip(QCoreApplication.translate("PydaqGlobal", u"Go to PYDAQ Documentation", None))
#endif // QT_CONFIG(tooltip)
        self.logo.setText("")
        self.radioButton.setText(QCoreApplication.translate("PydaqGlobal", u"Arduino", None))
        self.radioButton_2.setText(QCoreApplication.translate("PydaqGlobal", u"NIDAQ", None))
        self.nidaq_tabs.setTabText(self.nidaq_tabs.indexOf(self.get_data_nidaq), QCoreApplication.translate("PydaqGlobal", u"Get Data", None))
        self.nidaq_tabs.setTabText(self.nidaq_tabs.indexOf(self.send_data_nidaq_tab), QCoreApplication.translate("PydaqGlobal", u"Send Data", None))
        self.nidaq_tabs.setTabText(self.nidaq_tabs.indexOf(self.step_response_nidaq_tab), QCoreApplication.translate("PydaqGlobal", u"Step Response", None))
        self.nidaq_tabs.setTabText(self.nidaq_tabs.indexOf(self.get_model_nidaq_tab), QCoreApplication.translate("PydaqGlobal", u"Get Model", None))
        self.nidaq_tabs.setTabText(self.nidaq_tabs.indexOf(self.pid_control_nidaq_tab), QCoreApplication.translate("PydaqGlobal", u"PID Control", None))
        self.arduino_tabs.setTabText(self.arduino_tabs.indexOf(self.get_data_arduino_tab), QCoreApplication.translate("PydaqGlobal", u"Get Data", None))
        self.arduino_tabs.setTabText(self.arduino_tabs.indexOf(self.send_data_arduino_tab), QCoreApplication.translate("PydaqGlobal", u"Send Data", None))
        self.arduino_tabs.setTabText(self.arduino_tabs.indexOf(self.step_response_arduino_tab), QCoreApplication.translate("PydaqGlobal", u"Step Response", None))
        self.arduino_tabs.setTabText(self.arduino_tabs.indexOf(self.get_model_arduino_tab), QCoreApplication.translate("PydaqGlobal", u"Get Model", None))
        self.arduino_tabs.setTabText(self.arduino_tabs.indexOf(self.pid_control_arduino_tab), QCoreApplication.translate("PydaqGlobal", u"PID Control", None))
        self.menuBeenchmarking.setTitle(QCoreApplication.translate("PydaqGlobal", u"Beenchmarking", None))
        self.menuAbout.setTitle(QCoreApplication.translate("PydaqGlobal", u"About", None))
    # retranslateUi

