# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'PyDAQ_get_data_NIDAQ_widgetumSpsv.ui'
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
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QButtonGroup, QComboBox,
    QDoubleSpinBox, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QRadioButton,
    QSizePolicy, QWidget)

class Ui_NIDAQ_GetData_W(object):
    def setupUi(self, NIDAQ_GetData_W):
        if not NIDAQ_GetData_W.objectName():
            NIDAQ_GetData_W.setObjectName(u"NIDAQ_GetData_W")
        NIDAQ_GetData_W.resize(526, 527)
        NIDAQ_GetData_W.setStyleSheet(u"QComboBox QAbstractItemView {\n"
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
"QWidget#NIDAQ_GetData_W{\n"
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
"	backgrou"
                        "nd-color: rgb(0, 79, 0);\n"
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
"	border-top: 1.5px solid rgb(46, 46,"
                        " 46);\n"
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
        self.gridLayout_2 = QGridLayout(NIDAQ_GetData_W)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.line_2 = QFrame(NIDAQ_GetData_W)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_2.addWidget(self.line_2, 1, 0, 1, 1)

        self.widget_11 = QWidget(NIDAQ_GetData_W)
        self.widget_11.setObjectName(u"widget_11")
        self.gridLayout_8 = QGridLayout(self.widget_11)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.start_get_data = QPushButton(self.widget_11)
        self.start_get_data.setObjectName(u"start_get_data")
        self.start_get_data.setMinimumSize(QSize(0, 30))
        self.start_get_data.setMaximumSize(QSize(100, 30))
        self.start_get_data.setStyleSheet(u"")

        self.gridLayout_8.addWidget(self.start_get_data, 0, 0, 1, 1)


        self.gridLayout_2.addWidget(self.widget_11, 2, 0, 1, 1)

        self.widget = QWidget(NIDAQ_GetData_W)
        self.widget.setObjectName(u"widget")
        self.gridLayout = QGridLayout(self.widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.line = QFrame(self.widget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.VLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout.addWidget(self.line, 0, 1, 9, 1)

        self.widget_3 = QWidget(self.widget)
        self.widget_3.setObjectName(u"widget_3")
        self.gridLayout_4 = QGridLayout(self.widget_3)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.channel_combo = QComboBox(self.widget_3)
        self.channel_combo.setObjectName(u"channel_combo")
        self.channel_combo.setMinimumSize(QSize(0, 22))
        self.channel_combo.setMaximumSize(QSize(16777215, 22))

        self.gridLayout_4.addWidget(self.channel_combo, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.widget_3, 1, 2, 1, 1)

        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(0, 30))
        self.label.setMaximumSize(QSize(16777215, 30))

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.widget_10 = QWidget(self.widget)
        self.widget_10.setObjectName(u"widget_10")
        self.horizontalLayout_4 = QHBoxLayout(self.widget_10)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.yes_radio = QRadioButton(self.widget_10)
        self.filter_radio_group = QButtonGroup(NIDAQ_GetData_W)
        self.filter_radio_group.setObjectName(u"filter_radio_group")
        self.filter_radio_group.addButton(self.yes_radio)
        self.yes_radio.setObjectName(u"yes_radio")
        self.yes_radio.setChecked(False)

        self.horizontalLayout_4.addWidget(self.yes_radio)

        self.No_radio = QRadioButton(self.widget_10)
        self.filter_radio_group.addButton(self.No_radio)
        self.No_radio.setObjectName(u"No_radio")
        self.No_radio.setChecked(True)

        self.horizontalLayout_4.addWidget(self.No_radio)


        self.gridLayout.addWidget(self.widget_10, 5, 2, 1, 1, Qt.AlignmentFlag.AlignLeft)

        self.label_9 = QLabel(self.widget)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout.addWidget(self.label_9, 5, 0, 1, 1)

        self.widget_8 = QWidget(self.widget)
        self.widget_8.setObjectName(u"widget_8")
        self.horizontalLayout_2 = QHBoxLayout(self.widget_8)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.yes_save_radio = QRadioButton(self.widget_8)
        self.save_radio_group = QButtonGroup(NIDAQ_GetData_W)
        self.save_radio_group.setObjectName(u"save_radio_group")
        self.save_radio_group.addButton(self.yes_save_radio)
        self.yes_save_radio.setObjectName(u"yes_save_radio")
        self.yes_save_radio.setChecked(True)

        self.horizontalLayout_2.addWidget(self.yes_save_radio)

        self.no_save_radio = QRadioButton(self.widget_8)
        self.save_radio_group.addButton(self.no_save_radio)
        self.no_save_radio.setObjectName(u"no_save_radio")

        self.horizontalLayout_2.addWidget(self.no_save_radio)


        self.gridLayout.addWidget(self.widget_8, 7, 2, 1, 1, Qt.AlignmentFlag.AlignLeft)

        self.widget_6 = QWidget(self.widget)
        self.widget_6.setObjectName(u"widget_6")
        self.gridLayout_7 = QGridLayout(self.widget_6)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.sesh_dur_in = QDoubleSpinBox(self.widget_6)
        self.sesh_dur_in.setObjectName(u"sesh_dur_in")
        self.sesh_dur_in.setMinimumSize(QSize(0, 22))
        self.sesh_dur_in.setMaximumSize(QSize(16777215, 22))
        self.sesh_dur_in.setDecimals(4)
        self.sesh_dur_in.setMaximum(86400.000000000000000)
        self.sesh_dur_in.setSingleStep(0.010000000000000)
        self.sesh_dur_in.setStepType(QAbstractSpinBox.StepType.AdaptiveDecimalStepType)
        self.sesh_dur_in.setValue(10.000000000000000)

        self.gridLayout_7.addWidget(self.sesh_dur_in, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.widget_6, 4, 2, 1, 1)

        self.label_5 = QLabel(self.widget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(0, 30))
        self.label_5.setMaximumSize(QSize(16777215, 30))

        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)

        self.label_6 = QLabel(self.widget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMinimumSize(QSize(0, 30))
        self.label_6.setMaximumSize(QSize(16777215, 30))

        self.gridLayout.addWidget(self.label_6, 6, 0, 1, 1)

        self.widget_9 = QWidget(self.widget)
        self.widget_9.setObjectName(u"widget_9")
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


        self.gridLayout.addWidget(self.widget_9, 8, 2, 1, 1)

        self.widget_2 = QWidget(self.widget)
        self.widget_2.setObjectName(u"widget_2")
        self.gridLayout_3 = QGridLayout(self.widget_2)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.device_combo = QComboBox(self.widget_2)
        self.device_combo.setObjectName(u"device_combo")
        self.device_combo.setMinimumSize(QSize(0, 22))
        self.device_combo.setMaximumSize(QSize(16777215, 22))

        self.gridLayout_3.addWidget(self.device_combo, 0, 0, 1, 1)

        self.reload_devices = QPushButton(self.widget_2)
        self.reload_devices.setObjectName(u"reload_devices")
        self.reload_devices.setMinimumSize(QSize(22, 22))
        self.reload_devices.setMaximumSize(QSize(22, 22))

        self.gridLayout_3.addWidget(self.reload_devices, 0, 1, 1, 1)


        self.gridLayout.addWidget(self.widget_2, 0, 2, 1, 1)

        self.label_7 = QLabel(self.widget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMinimumSize(QSize(0, 30))
        self.label_7.setMaximumSize(QSize(16777215, 30))

        self.gridLayout.addWidget(self.label_7, 7, 0, 1, 1)

        self.label_8 = QLabel(self.widget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMinimumSize(QSize(0, 30))
        self.label_8.setMaximumSize(QSize(16777215, 30))

        self.gridLayout.addWidget(self.label_8, 8, 0, 1, 1, Qt.AlignmentFlag.AlignVCenter)

        self.widget_7 = QWidget(self.widget)
        self.widget_7.setObjectName(u"widget_7")
        self.horizontalLayout = QHBoxLayout(self.widget_7)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.yes_rt_plot_radio = QRadioButton(self.widget_7)
        self.plot_radio_group = QButtonGroup(NIDAQ_GetData_W)
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
        self.no_plot_radio.setEnabled(True)
        self.no_plot_radio.setAutoFillBackground(False)
        self.no_plot_radio.setChecked(True)

        self.horizontalLayout.addWidget(self.no_plot_radio)


        self.gridLayout.addWidget(self.widget_7, 6, 2, 1, 1, Qt.AlignmentFlag.AlignLeft)

        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(0, 30))
        self.label_2.setMaximumSize(QSize(16777215, 30))

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.widget_4 = QWidget(self.widget)
        self.widget_4.setObjectName(u"widget_4")
        self.gridLayout_5 = QGridLayout(self.widget_4)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.terminal_config_combo = QComboBox(self.widget_4)
        self.terminal_config_combo.setObjectName(u"terminal_config_combo")
        self.terminal_config_combo.setMinimumSize(QSize(0, 22))
        self.terminal_config_combo.setMaximumSize(QSize(16777215, 22))

        self.gridLayout_5.addWidget(self.terminal_config_combo, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.widget_4, 2, 2, 1, 1)

        self.widget_5 = QWidget(self.widget)
        self.widget_5.setObjectName(u"widget_5")
        self.gridLayout_6 = QGridLayout(self.widget_5)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.Ts_in = QDoubleSpinBox(self.widget_5)
        self.Ts_in.setObjectName(u"Ts_in")
        self.Ts_in.setMinimumSize(QSize(0, 22))
        self.Ts_in.setMaximumSize(QSize(16777215, 22))
        self.Ts_in.setDecimals(4)
        self.Ts_in.setMaximum(999.990000000000009)
        self.Ts_in.setSingleStep(0.010000000000000)
        self.Ts_in.setStepType(QAbstractSpinBox.StepType.AdaptiveDecimalStepType)
        self.Ts_in.setValue(0.500000000000000)

        self.gridLayout_6.addWidget(self.Ts_in, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.widget_5, 3, 2, 1, 1)

        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(0, 30))
        self.label_3.setMaximumSize(QSize(16777215, 30))

        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)

        self.label_4 = QLabel(self.widget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(0, 30))
        self.label_4.setMaximumSize(QSize(16777215, 30))

        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)


        self.gridLayout_2.addWidget(self.widget, 0, 0, 1, 1)


        self.retranslateUi(NIDAQ_GetData_W)

        QMetaObject.connectSlotsByName(NIDAQ_GetData_W)
    # setupUi

    def retranslateUi(self, NIDAQ_GetData_W):
        NIDAQ_GetData_W.setWindowTitle(QCoreApplication.translate("NIDAQ_GetData_W", u"Form", None))
        self.start_get_data.setText(QCoreApplication.translate("NIDAQ_GetData_W", u" GET DATA ", None))
        self.label.setText(QCoreApplication.translate("NIDAQ_GetData_W", u"Device:", None))
        self.yes_radio.setText(QCoreApplication.translate("NIDAQ_GetData_W", u"Yes", None))
        self.No_radio.setText(QCoreApplication.translate("NIDAQ_GetData_W", u"No", None))
        self.label_9.setText(QCoreApplication.translate("NIDAQ_GetData_W", u"Digital filter?", None))
        self.yes_save_radio.setText(QCoreApplication.translate("NIDAQ_GetData_W", u"Yes", None))
        self.no_save_radio.setText(QCoreApplication.translate("NIDAQ_GetData_W", u"No", None))
        self.label_5.setText(QCoreApplication.translate("NIDAQ_GetData_W", u"Session duration (s):", None))
        self.label_6.setText(QCoreApplication.translate("NIDAQ_GetData_W", u"Plot data?", None))
        self.path_folder_browse.setText(QCoreApplication.translate("NIDAQ_GetData_W", u" BROWSE ", None))
        self.reload_devices.setText("")
        self.label_7.setText(QCoreApplication.translate("NIDAQ_GetData_W", u"Save data?", None))
        self.label_8.setText(QCoreApplication.translate("NIDAQ_GetData_W", u"Path:", None))
        self.yes_rt_plot_radio.setText(QCoreApplication.translate("NIDAQ_GetData_W", u"Real time", None))
#if QT_CONFIG(tooltip)
        self.label_warning.setToolTip(QCoreApplication.translate("NIDAQ_GetData_W", u"<html><head/><body><p><span style=\" font-size:16pt;\">Selecting Real Time may reduce your acquisition performance if you need to collect data at high frequencies ( sample period &lt; 0.05 s). We suggest plotting at the end of the acquisition if you don't want to be affected.</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.label_warning.setWhatsThis(QCoreApplication.translate("NIDAQ_GetData_W", u"<html><head/><body><p><br/></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.label_warning.setText(QCoreApplication.translate("NIDAQ_GetData_W", u"<html><head/><body><p><img src=\":/imgs/imgs/Warning_logo.png\"/></p></body></html>", None))
        self.yes_ate_plot_radio.setText(QCoreApplication.translate("NIDAQ_GetData_W", u"At the end", None))
        self.no_plot_radio.setText(QCoreApplication.translate("NIDAQ_GetData_W", u"No", None))
        self.label_2.setText(QCoreApplication.translate("NIDAQ_GetData_W", u"Channel:", None))
        self.label_3.setText(QCoreApplication.translate("NIDAQ_GetData_W", u"Terminal Config.", None))
        self.label_4.setText(QCoreApplication.translate("NIDAQ_GetData_W", u"Sample period (s):", None))
    # retranslateUi

