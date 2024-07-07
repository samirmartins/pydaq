# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'PyDAQ_BasejBQLOt.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (
    QCoreApplication,
    QMetaObject,
    QRect,
    QSize,
    Qt,
)
from PySide6.QtGui import (
    QCursor,
    QIcon,
)
from PySide6.QtWidgets import (
    QButtonGroup,
    QGridLayout,
    QHBoxLayout,
    QMenuBar,
    QPushButton,
    QRadioButton,
    QScrollArea,
    QStatusBar,
    QTabWidget,
    QVBoxLayout,
    QWidget,
)

from ..guis.getdata_arduino_widget import GetData_Arduino_Widget
from ..guis.getdata_nidaq_widget import GetData_NIDAQ_Widget
from ..guis.senddata_arduino_widget import SendData_Arduino_Widget
from ..guis.senddata_nidaq_widget import SendData_NIDAQ_Widget
from ..guis.stepresponse_arduino_widget import StepResponse_Arduino_Widget
from ..guis.stepresponse_nidaq_widget import StepResponse_NIDAQ_Widget
from . import resources_1_rc


class Ui_PydaqGlobal(object):
    def setupUi(self, PydaqGlobal):
        if not PydaqGlobal.objectName():
            PydaqGlobal.setObjectName("PydaqGlobal")
        PydaqGlobal.resize(1280, 720)
        PydaqGlobal.setMinimumSize(QSize(1280, 720))
        PydaqGlobal.setMaximumSize(QSize(16777215, 16777215))
        icon = QIcon()
        icon.addFile(":/imgs/imgs/favicon.ico", QSize(), QIcon.Normal, QIcon.Off)
        PydaqGlobal.setWindowIcon(icon)
        PydaqGlobal.setIconSize(QSize(24, 24))
        PydaqGlobal.setTabShape(QTabWidget.Rounded)
        self.centralwidget = QWidget(PydaqGlobal)
        self.centralwidget.setObjectName("centralwidget")
        self.centralwidget.setStyleSheet(
            "QWidget{\n"
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
            '	font: 12pt "Helve'
            'tica";\n'
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
            ""
        )
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.logo = QPushButton(self.centralwidget)
        self.logo.setObjectName("logo")
        self.logo.setMinimumSize(QSize(186, 147))
        self.logo.setMaximumSize(QSize(186, 147))
        self.logo.setCursor(QCursor(Qt.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(":/imgs/imgs/logo.png", QSize(), QIcon.Normal, QIcon.Off)
        self.logo.setIcon(icon1)
        self.logo.setIconSize(QSize(182, 143))

        self.verticalLayout.addWidget(self.logo, 0, Qt.AlignHCenter)

        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName("widget")
        self.widget.setStyleSheet("")
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.radioButton = QRadioButton(self.widget)
        self.interface_radio = QButtonGroup(PydaqGlobal)
        self.interface_radio.setObjectName("interface_radio")
        self.interface_radio.addButton(self.radioButton)
        self.radioButton.setObjectName("radioButton")
        self.radioButton.setChecked(True)

        self.horizontalLayout.addWidget(self.radioButton)

        self.radioButton_2 = QRadioButton(self.widget)
        self.interface_radio.addButton(self.radioButton_2)
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton_2.setChecked(False)

        self.horizontalLayout.addWidget(self.radioButton_2)

        self.verticalLayout.addWidget(self.widget)

        self.widget_2 = QWidget(self.centralwidget)
        self.widget_2.setObjectName("widget_2")
        self.gridLayout = QGridLayout(self.widget_2)
        self.gridLayout.setObjectName("gridLayout")
        self.nidaq_tabs = QTabWidget(self.widget_2)
        self.nidaq_tabs.setObjectName("nidaq_tabs")
        self.nidaq_tabs.setTabPosition(QTabWidget.North)
        self.nidaq_tabs.setDocumentMode(False)
        self.nidaq_tabs.setTabsClosable(False)
        self.nidaq_tabs.setMovable(False)
        self.nidaq_tabs.setTabBarAutoHide(False)
        self.get_data_nidaq = QWidget()
        self.get_data_nidaq.setObjectName("get_data_nidaq")
        self.gridLayout_3 = QGridLayout(self.get_data_nidaq)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.scrollArea_2 = QScrollArea(self.get_data_nidaq)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_4 = QWidget()
        self.scrollAreaWidgetContents_4.setObjectName("scrollAreaWidgetContents_4")
        self.scrollAreaWidgetContents_4.setGeometry(QRect(0, 0, 599, 402))
        self.gridLayout_8 = QGridLayout(self.scrollAreaWidgetContents_4)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.get_nidaq_placeholder = GetData_NIDAQ_Widget(
            self.scrollAreaWidgetContents_4
        )
        self.get_nidaq_placeholder.setObjectName("get_nidaq_placeholder")

        self.gridLayout_8.addWidget(self.get_nidaq_placeholder, 0, 0, 1, 1)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_4)

        self.gridLayout_3.addWidget(self.scrollArea_2, 0, 0, 1, 1)

        self.nidaq_tabs.addTab(self.get_data_nidaq, "")
        self.send_data_nidaq_tab = QWidget()
        self.send_data_nidaq_tab.setObjectName("send_data_nidaq_tab")
        self.gridLayout_7 = QGridLayout(self.send_data_nidaq_tab)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.scrollArea_3 = QScrollArea(self.send_data_nidaq_tab)
        self.scrollArea_3.setObjectName("scrollArea_3")
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollAreaWidgetContents_5 = QWidget()
        self.scrollAreaWidgetContents_5.setObjectName("scrollAreaWidgetContents_5")
        self.scrollAreaWidgetContents_5.setGeometry(QRect(0, 0, 599, 402))
        self.gridLayout_10 = QGridLayout(self.scrollAreaWidgetContents_5)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.send_nidaq_placeholder = SendData_NIDAQ_Widget(
            self.scrollAreaWidgetContents_5
        )
        self.send_nidaq_placeholder.setObjectName("send_nidaq_placeholder")

        self.gridLayout_10.addWidget(self.send_nidaq_placeholder, 0, 0, 1, 1)

        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_5)

        self.gridLayout_7.addWidget(self.scrollArea_3, 0, 0, 1, 1)

        self.nidaq_tabs.addTab(self.send_data_nidaq_tab, "")
        self.step_response_nidaq_tab = QWidget()
        self.step_response_nidaq_tab.setObjectName("step_response_nidaq_tab")
        self.gridLayout_6 = QGridLayout(self.step_response_nidaq_tab)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.scrollArea = QScrollArea(self.step_response_nidaq_tab)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents_3 = QWidget()
        self.scrollAreaWidgetContents_3.setObjectName("scrollAreaWidgetContents_3")
        self.scrollAreaWidgetContents_3.setGeometry(QRect(0, 0, 599, 402))
        self.gridLayout_9 = QGridLayout(self.scrollAreaWidgetContents_3)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.step_nidaq_placeholder = StepResponse_NIDAQ_Widget(
            self.scrollAreaWidgetContents_3
        )
        self.step_nidaq_placeholder.setObjectName("step_nidaq_placeholder")

        self.gridLayout_9.addWidget(self.step_nidaq_placeholder, 0, 0, 1, 1)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents_3)

        self.gridLayout_6.addWidget(self.scrollArea, 0, 0, 1, 1)

        self.nidaq_tabs.addTab(self.step_response_nidaq_tab, "")

        self.gridLayout.addWidget(self.nidaq_tabs, 0, 1, 1, 1)

        self.arduino_tabs = QTabWidget(self.widget_2)
        self.arduino_tabs.setObjectName("arduino_tabs")
        self.arduino_tabs.setStyleSheet("")
        self.arduino_tabs.setTabShape(QTabWidget.Rounded)
        self.arduino_tabs.setElideMode(Qt.ElideNone)
        self.get_data_arduino_tab = QWidget()
        self.get_data_arduino_tab.setObjectName("get_data_arduino_tab")
        self.gridLayout_2 = QGridLayout(self.get_data_arduino_tab)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.scrollArea_4 = QScrollArea(self.get_data_arduino_tab)
        self.scrollArea_4.setObjectName("scrollArea_4")
        self.scrollArea_4.setWidgetResizable(True)
        self.scrollAreaWidgetContents_6 = QWidget()
        self.scrollAreaWidgetContents_6.setObjectName("scrollAreaWidgetContents_6")
        self.scrollAreaWidgetContents_6.setGeometry(QRect(0, 0, 599, 402))
        self.gridLayout_11 = QGridLayout(self.scrollAreaWidgetContents_6)
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.get_ino_placeholder = GetData_Arduino_Widget(
            self.scrollAreaWidgetContents_6
        )
        self.get_ino_placeholder.setObjectName("get_ino_placeholder")

        self.gridLayout_11.addWidget(self.get_ino_placeholder, 0, 0, 1, 1)

        self.scrollArea_4.setWidget(self.scrollAreaWidgetContents_6)

        self.gridLayout_2.addWidget(self.scrollArea_4, 0, 0, 1, 1)

        self.arduino_tabs.addTab(self.get_data_arduino_tab, "")
        self.send_data_arduino_tab = QWidget()
        self.send_data_arduino_tab.setObjectName("send_data_arduino_tab")
        self.gridLayout_4 = QGridLayout(self.send_data_arduino_tab)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.scrollArea_5 = QScrollArea(self.send_data_arduino_tab)
        self.scrollArea_5.setObjectName("scrollArea_5")
        self.scrollArea_5.setWidgetResizable(True)
        self.scrollAreaWidgetContents_7 = QWidget()
        self.scrollAreaWidgetContents_7.setObjectName("scrollAreaWidgetContents_7")
        self.scrollAreaWidgetContents_7.setGeometry(QRect(0, 0, 599, 402))
        self.gridLayout_12 = QGridLayout(self.scrollAreaWidgetContents_7)
        self.gridLayout_12.setObjectName("gridLayout_12")
        self.send_ino_placeholder = SendData_Arduino_Widget(
            self.scrollAreaWidgetContents_7
        )
        self.send_ino_placeholder.setObjectName("send_ino_placeholder")

        self.gridLayout_12.addWidget(self.send_ino_placeholder, 0, 0, 1, 1)

        self.scrollArea_5.setWidget(self.scrollAreaWidgetContents_7)

        self.gridLayout_4.addWidget(self.scrollArea_5, 0, 0, 1, 1)

        self.arduino_tabs.addTab(self.send_data_arduino_tab, "")
        self.step_response_arduino_tab = QWidget()
        self.step_response_arduino_tab.setObjectName("step_response_arduino_tab")
        self.gridLayout_5 = QGridLayout(self.step_response_arduino_tab)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.scrollArea_6 = QScrollArea(self.step_response_arduino_tab)
        self.scrollArea_6.setObjectName("scrollArea_6")
        self.scrollArea_6.setWidgetResizable(True)
        self.scrollAreaWidgetContents_11 = QWidget()
        self.scrollAreaWidgetContents_11.setObjectName("scrollAreaWidgetContents_11")
        self.scrollAreaWidgetContents_11.setGeometry(QRect(0, 0, 599, 402))
        self.gridLayout_14 = QGridLayout(self.scrollAreaWidgetContents_11)
        self.gridLayout_14.setObjectName("gridLayout_14")
        self.step_ino_placeholder = StepResponse_Arduino_Widget(
            self.scrollAreaWidgetContents_11
        )
        self.step_ino_placeholder.setObjectName("step_ino_placeholder")

        self.gridLayout_14.addWidget(self.step_ino_placeholder, 0, 0, 1, 1)

        self.scrollArea_6.setWidget(self.scrollAreaWidgetContents_11)

        self.gridLayout_5.addWidget(self.scrollArea_6, 0, 0, 1, 1)

        self.arduino_tabs.addTab(self.step_response_arduino_tab, "")

        self.gridLayout.addWidget(self.arduino_tabs, 0, 0, 1, 1)

        self.verticalLayout.addWidget(self.widget_2)

        PydaqGlobal.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(PydaqGlobal)
        self.menubar.setObjectName("menubar")
        self.menubar.setGeometry(QRect(0, 0, 1280, 22))
        PydaqGlobal.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(PydaqGlobal)
        self.statusbar.setObjectName("statusbar")
        PydaqGlobal.setStatusBar(self.statusbar)

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
        PydaqGlobal.setWindowTitle(
            QCoreApplication.translate("PydaqGlobal", "PYDAQ Global", None)
        )
        # if QT_CONFIG(tooltip)
        self.logo.setToolTip(
            QCoreApplication.translate("PydaqGlobal", "Go to PYDAQ Documentation", None)
        )
        # endif // QT_CONFIG(tooltip)
        self.logo.setText("")
        self.radioButton.setText(
            QCoreApplication.translate("PydaqGlobal", "Arduino", None)
        )
        self.radioButton_2.setText(
            QCoreApplication.translate("PydaqGlobal", "NIDAQ", None)
        )
        self.nidaq_tabs.setTabText(
            self.nidaq_tabs.indexOf(self.get_data_nidaq),
            QCoreApplication.translate("PydaqGlobal", "Get Data", None),
        )
        self.nidaq_tabs.setTabText(
            self.nidaq_tabs.indexOf(self.send_data_nidaq_tab),
            QCoreApplication.translate("PydaqGlobal", "Send Data", None),
        )
        self.nidaq_tabs.setTabText(
            self.nidaq_tabs.indexOf(self.step_response_nidaq_tab),
            QCoreApplication.translate("PydaqGlobal", "Step Response", None),
        )
        self.arduino_tabs.setTabText(
            self.arduino_tabs.indexOf(self.get_data_arduino_tab),
            QCoreApplication.translate("PydaqGlobal", "Get Data", None),
        )
        self.arduino_tabs.setTabText(
            self.arduino_tabs.indexOf(self.send_data_arduino_tab),
            QCoreApplication.translate("PydaqGlobal", "Send Data", None),
        )
        self.arduino_tabs.setTabText(
            self.arduino_tabs.indexOf(self.step_response_arduino_tab),
            QCoreApplication.translate("PydaqGlobal", "Step Response", None),
        )

    # retranslateUi
