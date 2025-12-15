# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'PyDAQ_send_data_Arduino_widgetZiJSNi.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
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
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QButtonGroup, QComboBox,
    QDoubleSpinBox, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QRadioButton,
    QSizePolicy, QWidget)


class Ui_Arduino_SendData_W(object):
    def setupUi(self, Arduino_SendData_W):
        if not Arduino_SendData_W.objectName():
            Arduino_SendData_W.setObjectName(u"Arduino_SendData_W")
        Arduino_SendData_W.resize(475, 320)
        Arduino_SendData_W.setStyleSheet(u"QComboBox QAbstractItemView {\n"
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
"	font: 12pt \"Helvetica\";\n"
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
        self.gridLayout_3 = QGridLayout(Arduino_SendData_W)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.widget = QWidget(Arduino_SendData_W)
        self.widget.setObjectName(u"widget")
        self.gridLayout = QGridLayout(self.widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.widget_7 = QWidget(self.widget)
        self.widget_7.setObjectName(u"widget_7")
        self.horizontalLayout = QHBoxLayout(self.widget_7)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.yes_rt_plot_radio = QRadioButton(self.widget_7)
        self.plot_radio_group = QButtonGroup(Arduino_SendData_W)
        self.plot_radio_group.setObjectName(u"plot_radio_group")
        self.plot_radio_group.addButton(self.yes_rt_plot_radio)
        self.yes_rt_plot_radio.setObjectName(u"yes_rt_plot_radio")
        self.yes_rt_plot_radio.setChecked(False)

        self.horizontalLayout.addWidget(self.yes_rt_plot_radio)

        self.label_warning = QLabel(self.widget_7)
        self.label_warning.setObjectName(u"label_warning")

        self.horizontalLayout.addWidget(self.label_warning)

        self.yes_ate_plot_radio = QRadioButton(self.widget_7)
        self.plot_radio_group.addButton(self.yes_ate_plot_radio)
        self.yes_ate_plot_radio.setObjectName(u"yes_ate_plot_radio")

        self.horizontalLayout.addWidget(self.yes_ate_plot_radio)

        self.no_plot_radio = QRadioButton(self.widget_7)
        self.plot_radio_group.addButton(self.no_plot_radio)
        self.no_plot_radio.setObjectName(u"no_plot_radio")
        self.no_plot_radio.setChecked(True)

        self.horizontalLayout.addWidget(self.no_plot_radio)


        self.gridLayout.addWidget(self.widget_7, 2, 2, 1, 1, Qt.AlignmentFlag.AlignLeft)

        self.label_4 = QLabel(self.widget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(0, 30))
        self.label_4.setMaximumSize(QSize(16777215, 30))

        self.gridLayout.addWidget(self.label_4, 1, 0, 1, 1)

        self.label_8 = QLabel(self.widget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMinimumSize(QSize(0, 30))
        self.label_8.setMaximumSize(QSize(16777215, 30))

        self.gridLayout.addWidget(self.label_8, 4, 0, 1, 1)

        self.widget_9 = QWidget(self.widget)
        self.widget_9.setObjectName(u"widget_9")
        self.widget_9.setMinimumSize(QSize(0, 50))
        self.widget_9.setMaximumSize(QSize(16777215, 50))
        self.horizontalLayout_3 = QHBoxLayout(self.widget_9)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.path_line_edit = QLineEdit(self.widget_9)
        self.path_line_edit.setObjectName(u"path_line_edit")
        self.path_line_edit.setMinimumSize(QSize(0, 22))
        self.path_line_edit.setMaximumSize(QSize(16777215, 22))

        self.horizontalLayout_3.addWidget(self.path_line_edit, 0, Qt.AlignmentFlag.AlignVCenter)

        self.path_folder_browse = QPushButton(self.widget_9)
        self.path_folder_browse.setObjectName(u"path_folder_browse")
        self.path_folder_browse.setMinimumSize(QSize(0, 30))
        self.path_folder_browse.setMaximumSize(QSize(16777215, 30))

        self.horizontalLayout_3.addWidget(self.path_folder_browse, 0, Qt.AlignmentFlag.AlignVCenter)


        self.gridLayout.addWidget(self.widget_9, 4, 2, 1, 1)

        self.widget_2 = QWidget(self.widget)
        self.widget_2.setObjectName(u"widget_2")
        self.gridLayout_2 = QGridLayout(self.widget_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.device_combo = QComboBox(self.widget_2)
        self.device_combo.setObjectName(u"device_combo")
        self.device_combo.setMinimumSize(QSize(0, 22))
        self.device_combo.setMaximumSize(QSize(16777215, 22))

        self.gridLayout_2.addWidget(self.device_combo, 1, 0, 1, 1)

        self.reload_devices = QPushButton(self.widget_2)
        self.reload_devices.setObjectName(u"reload_devices")
        self.reload_devices.setMinimumSize(QSize(22, 22))
        self.reload_devices.setMaximumSize(QSize(22, 22))

        self.gridLayout_2.addWidget(self.reload_devices, 1, 1, 1, 1)


        self.gridLayout.addWidget(self.widget_2, 0, 2, 1, 1)

        self.label_6 = QLabel(self.widget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMinimumSize(QSize(0, 30))
        self.label_6.setMaximumSize(QSize(16777215, 30))

        self.gridLayout.addWidget(self.label_6, 2, 0, 1, 1)

        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(0, 30))
        self.label.setMaximumSize(QSize(16777215, 30))

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.widget_5 = QWidget(self.widget)
        self.widget_5.setObjectName(u"widget_5")
        self.gridLayout_6 = QGridLayout(self.widget_5)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.Ts_in = QDoubleSpinBox(self.widget_5)
        self.Ts_in.setObjectName(u"Ts_in")
        self.Ts_in.setMinimumSize(QSize(0, 22))
        self.Ts_in.setMaximumSize(QSize(16777215, 22))
        self.Ts_in.setDecimals(6)
        self.Ts_in.setMaximum(999999999999.000000000000000)
        self.Ts_in.setSingleStep(0.010000000000000)
        self.Ts_in.setStepType(QAbstractSpinBox.StepType.AdaptiveDecimalStepType)
        self.Ts_in.setValue(1.000000000000000)

        self.gridLayout_6.addWidget(self.Ts_in, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.widget_5, 1, 2, 1, 1)

        self.line = QFrame(self.widget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.VLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout.addWidget(self.line, 0, 1, 6, 1)


        self.gridLayout_3.addWidget(self.widget, 0, 0, 1, 1)

        self.line_3 = QFrame(Arduino_SendData_W)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.Shape.HLine)
        self.line_3.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_3.addWidget(self.line_3, 1, 0, 1, 1)

        self.start_send_data = QPushButton(Arduino_SendData_W)
        self.start_send_data.setObjectName(u"start_send_data")
        self.start_send_data.setMinimumSize(QSize(100, 30))
        self.start_send_data.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_3.addWidget(self.start_send_data, 2, 0, 1, 1, Qt.AlignmentFlag.AlignHCenter)


        self.retranslateUi(Arduino_SendData_W)

        QMetaObject.connectSlotsByName(Arduino_SendData_W)
    # setupUi

    def retranslateUi(self, Arduino_SendData_W):
        Arduino_SendData_W.setWindowTitle(QCoreApplication.translate("Arduino_SendData_W", u"Form", None))
        self.yes_rt_plot_radio.setText(QCoreApplication.translate("Arduino_SendData_W", u"Real time", None))
#if QT_CONFIG(tooltip)
        self.label_warning.setToolTip(QCoreApplication.translate("Arduino_SendData_W", u"<html><head/><body><p><span style=\" font-size:16pt;\">Selecting Real Time may reduce your acquisition performance if you need to collect data at high frequencies ( sample period &lt; 0.05 s ). We suggest plotting at the end of the acquisition if you don't want to be affected.</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_warning.setText(QCoreApplication.translate("Arduino_SendData_W", u"<html><head/><body><p><img src=\":/imgs/imgs/Warning_logo.png\"/></p></body></html>", None))
        self.yes_ate_plot_radio.setText(QCoreApplication.translate("Arduino_SendData_W", u"At the end", None))
        self.no_plot_radio.setText(QCoreApplication.translate("Arduino_SendData_W", u"No", None))
        self.label_4.setText(QCoreApplication.translate("Arduino_SendData_W", u"Sample period (s):", None))
        self.label_8.setText(QCoreApplication.translate("Arduino_SendData_W", u"Path:", None))
        self.path_folder_browse.setText(QCoreApplication.translate("Arduino_SendData_W", u" BROWSE ", None))
#if QT_CONFIG(tooltip)
        self.reload_devices.setToolTip(QCoreApplication.translate("Arduino_SendData_W", u"<html><head/><body><p>Update COM ports</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.reload_devices.setText("")
        self.label_6.setText(QCoreApplication.translate("Arduino_SendData_W", u"Plot data?", None))
        self.label.setText(QCoreApplication.translate("Arduino_SendData_W", u"Device:", None))
        self.start_send_data.setText(QCoreApplication.translate("Arduino_SendData_W", u"SEND DATA", None))
    # retranslateUi

