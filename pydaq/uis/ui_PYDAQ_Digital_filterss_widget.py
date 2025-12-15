# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'PYDAQ_Digital_filterss_widgetYwRNwM.ui'
##
## Created by: Qt User Interface Compiler version 6.7.1
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
from PySide6.QtWidgets import (QApplication, QButtonGroup, QCheckBox, QComboBox,
    QFrame, QGridLayout, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QWidget)

class Ui_Digitalfilters_arduino_widget(object):
    def setupUi(self, Digitalfilters_arduino_widget):
        if not Digitalfilters_arduino_widget.objectName():
            Digitalfilters_arduino_widget.setObjectName(u"Digitalfilters_arduino_widget")
        Digitalfilters_arduino_widget.resize(907, 617)
        Digitalfilters_arduino_widget.setStyleSheet(u"QWidget{\n"
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
"    image: url(:/imgs/drop_up_arrow.png);\n"
"	width: 11px;\n"
"\n"
"	background-color: rgb(0, 79, 0);\n"
"	border-top: 1.5px solid rgb(127, 167, 127);\n"
"	border-left: 1.5px solid rg"
                        "b(127, 167, 127);\n"
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
"    image: url(:/imgs/drop_down_arrow.png);\n"
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
"	background-color: rgb(77, 77, 77);\n"
""
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
"	font: 12pt \"Helvetica\";\n"
"	"
                        "text-align:center;\n"
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
"\n"
"QPushBut"
                        "ton#reload_devices{\n"
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
"")
        self.gridLayout = QGridLayout(Digitalfilters_arduino_widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.iir_configs = QWidget(Digitalfilters_arduino_widget)
        self.iir_configs.setObjectName(u"iir_configs")
        self.gridLayout_4 = QGridLayout(self.iir_configs)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.label_8 = QLabel(self.iir_configs)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_4.addWidget(self.label_8, 1, 0, 1, 1)

        self.label_11 = QLabel(self.iir_configs)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout_4.addWidget(self.label_11, 5, 0, 1, 1)

        self.order_iir_line = QLineEdit(self.iir_configs)
        self.order_iir_line.setObjectName(u"order_iir_line")

        self.gridLayout_4.addWidget(self.order_iir_line, 1, 1, 1, 1, Qt.AlignmentFlag.AlignRight)

        self.rp_line = QLineEdit(self.iir_configs)
        self.rp_line.setObjectName(u"rp_line")

        self.gridLayout_4.addWidget(self.rp_line, 4, 1, 1, 1, Qt.AlignmentFlag.AlignRight)

        self.label_9 = QLabel(self.iir_configs)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout_4.addWidget(self.label_9, 2, 0, 1, 1)

        self.rs_line = QLineEdit(self.iir_configs)
        self.rs_line.setObjectName(u"rs_line")

        self.gridLayout_4.addWidget(self.rs_line, 5, 1, 1, 1, Qt.AlignmentFlag.AlignRight)

        self.label_12 = QLabel(self.iir_configs)
        self.label_12.setObjectName(u"label_12")

        self.gridLayout_4.addWidget(self.label_12, 0, 0, 1, 1)

        self.fs_iir_line = QLineEdit(self.iir_configs)
        self.fs_iir_line.setObjectName(u"fs_iir_line")

        self.gridLayout_4.addWidget(self.fs_iir_line, 2, 1, 1, 1, Qt.AlignmentFlag.AlignRight)

        self.label_10 = QLabel(self.iir_configs)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout_4.addWidget(self.label_10, 4, 0, 1, 1)

        self.comboBox_4 = QComboBox(self.iir_configs)
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.setObjectName(u"comboBox_4")

        self.gridLayout_4.addWidget(self.comboBox_4, 0, 1, 1, 1)

        self.label_14 = QLabel(self.iir_configs)
        self.label_14.setObjectName(u"label_14")

        self.gridLayout_4.addWidget(self.label_14, 3, 0, 1, 1)

        self.fc_line = QLineEdit(self.iir_configs)
        self.fc_line.setObjectName(u"fc_line")

        self.gridLayout_4.addWidget(self.fc_line, 3, 1, 1, 1, Qt.AlignmentFlag.AlignRight)


        self.gridLayout.addWidget(self.iir_configs, 5, 0, 1, 1)

        self.line_2 = QFrame(Digitalfilters_arduino_widget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout.addWidget(self.line_2, 1, 0, 1, 1)

        self.frequency_response = QWidget(Digitalfilters_arduino_widget)
        self.frequency_response.setObjectName(u"frequency_response")
        self.gridLayout_5 = QGridLayout(self.frequency_response)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.no_fr = QCheckBox(self.frequency_response)
        self.buttonGroup = QButtonGroup(Digitalfilters_arduino_widget)
        self.buttonGroup.setObjectName(u"buttonGroup")
        self.buttonGroup.addButton(self.no_fr)
        self.no_fr.setObjectName(u"no_fr")
        self.no_fr.setMaximumSize(QSize(100, 16777215))

        self.gridLayout_5.addWidget(self.no_fr, 0, 2, 1, 1, Qt.AlignmentFlag.AlignRight)

        self.label_13 = QLabel(self.frequency_response)
        self.label_13.setObjectName(u"label_13")

        self.gridLayout_5.addWidget(self.label_13, 0, 0, 1, 1)

        self.yes_fr = QCheckBox(self.frequency_response)
        self.buttonGroup.addButton(self.yes_fr)
        self.yes_fr.setObjectName(u"yes_fr")
        self.yes_fr.setMaximumSize(QSize(100, 16777215))

        self.gridLayout_5.addWidget(self.yes_fr, 0, 1, 1, 1, Qt.AlignmentFlag.AlignRight)


        self.gridLayout.addWidget(self.frequency_response, 7, 0, 1, 1)

        self.line_3 = QFrame(Digitalfilters_arduino_widget)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.Shape.HLine)
        self.line_3.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout.addWidget(self.line_3, 6, 0, 1, 1)

        self.select_filter = QWidget(Digitalfilters_arduino_widget)
        self.select_filter.setObjectName(u"select_filter")
        self.horizontalLayout = QHBoxLayout(self.select_filter)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.select_filter)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.filter_combox = QComboBox(self.select_filter)
        self.filter_combox.addItem("")
        self.filter_combox.addItem("")
        self.filter_combox.setObjectName(u"filter_combox")

        self.horizontalLayout.addWidget(self.filter_combox)


        self.gridLayout.addWidget(self.select_filter, 2, 0, 1, 1)

        self.fir_configs = QWidget(Digitalfilters_arduino_widget)
        self.fir_configs.setObjectName(u"fir_configs")
        self.gridLayout_2 = QGridLayout(self.fir_configs)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.lineEdit_4 = QLineEdit(self.fir_configs)
        self.lineEdit_4.setObjectName(u"lineEdit_4")

        self.gridLayout_2.addWidget(self.lineEdit_4, 3, 1, 1, 1, Qt.AlignmentFlag.AlignRight)

        self.label_4 = QLabel(self.fir_configs)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_2.addWidget(self.label_4, 2, 0, 1, 1)

        self.lineEdit = QLineEdit(self.fir_configs)
        self.lineEdit.setObjectName(u"lineEdit")

        self.gridLayout_2.addWidget(self.lineEdit, 0, 1, 1, 1, Qt.AlignmentFlag.AlignRight)

        self.lineEdit_3 = QLineEdit(self.fir_configs)
        self.lineEdit_3.setObjectName(u"lineEdit_3")

        self.gridLayout_2.addWidget(self.lineEdit_3, 2, 1, 1, 1, Qt.AlignmentFlag.AlignRight)

        self.label_5 = QLabel(self.fir_configs)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_2.addWidget(self.label_5, 3, 0, 1, 1)

        self.label_2 = QLabel(self.fir_configs)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_2.addWidget(self.label_2, 0, 0, 1, 1)

        self.lineEdit_2 = QLineEdit(self.fir_configs)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.gridLayout_2.addWidget(self.lineEdit_2, 1, 1, 1, 1, Qt.AlignmentFlag.AlignRight)

        self.label_3 = QLabel(self.fir_configs)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_2.addWidget(self.label_3, 1, 0, 1, 1)

        self.label_6 = QLabel(self.fir_configs)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_2.addWidget(self.label_6, 4, 0, 1, 1)

        self.comboBox_2 = QComboBox(self.fir_configs)
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.setObjectName(u"comboBox_2")

        self.gridLayout_2.addWidget(self.comboBox_2, 4, 1, 1, 1)


        self.gridLayout.addWidget(self.fir_configs, 4, 0, 1, 1)

        self.arduino_selection = QWidget(Digitalfilters_arduino_widget)
        self.arduino_selection.setObjectName(u"arduino_selection")
        self.gridLayout_3 = QGridLayout(self.arduino_selection)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.arduino_board = QComboBox(self.arduino_selection)
        self.arduino_board.setObjectName(u"arduino_board")

        self.gridLayout_3.addWidget(self.arduino_board, 0, 1, 1, 1)

        self.label_7 = QLabel(self.arduino_selection)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_3.addWidget(self.label_7, 0, 0, 1, 1)

        self.reload_devices = QPushButton(self.arduino_selection)
        self.reload_devices.setObjectName(u"reload_devices")
        self.reload_devices.setMaximumSize(QSize(25, 16777215))

        self.gridLayout_3.addWidget(self.reload_devices, 0, 2, 1, 1)


        self.gridLayout.addWidget(self.arduino_selection, 0, 0, 1, 1)

        self.line = QFrame(Digitalfilters_arduino_widget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout.addWidget(self.line, 3, 0, 1, 1)

        self.bottom = QWidget(Digitalfilters_arduino_widget)
        self.bottom.setObjectName(u"bottom")
        self.gridLayout_6 = QGridLayout(self.bottom)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.Filter_button = QPushButton(self.bottom)
        self.Filter_button.setObjectName(u"Filter_button")
        self.Filter_button.setMinimumSize(QSize(50, 0))

        self.gridLayout_6.addWidget(self.Filter_button, 1, 0, 1, 1, Qt.AlignmentFlag.AlignHCenter)

        self.line_4 = QFrame(self.bottom)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.Shape.HLine)
        self.line_4.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_6.addWidget(self.line_4, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.bottom, 8, 0, 1, 1)


        self.retranslateUi(Digitalfilters_arduino_widget)
        self.filter_combox.currentTextChanged.connect(self.fir_configs.show)
        self.filter_combox.currentTextChanged.connect(self.iir_configs.hide)

        QMetaObject.connectSlotsByName(Digitalfilters_arduino_widget)
    # setupUi

    def retranslateUi(self, Digitalfilters_arduino_widget):
        Digitalfilters_arduino_widget.setWindowTitle(QCoreApplication.translate("Digitalfilters_arduino_widget", u"Form", None))
        self.label_8.setText(QCoreApplication.translate("Digitalfilters_arduino_widget", u"Filter order (N):", None))
        self.label_11.setText(QCoreApplication.translate("Digitalfilters_arduino_widget", u"rs:", None))
        self.order_iir_line.setText(QCoreApplication.translate("Digitalfilters_arduino_widget", u"10", None))
        self.rp_line.setText(QCoreApplication.translate("Digitalfilters_arduino_widget", u"1", None))
        self.label_9.setText(QCoreApplication.translate("Digitalfilters_arduino_widget", u"Fs:", None))
        self.rs_line.setText(QCoreApplication.translate("Digitalfilters_arduino_widget", u"10", None))
        self.label_12.setText(QCoreApplication.translate("Digitalfilters_arduino_widget", u"Type:", None))
        self.fs_iir_line.setText(QCoreApplication.translate("Digitalfilters_arduino_widget", u"1000", None))
        self.label_10.setText(QCoreApplication.translate("Digitalfilters_arduino_widget", u"rp:", None))
        self.comboBox_4.setItemText(0, QCoreApplication.translate("Digitalfilters_arduino_widget", u"BUTTERWORTH", None))
        self.comboBox_4.setItemText(1, QCoreApplication.translate("Digitalfilters_arduino_widget", u"CHEBYSHEV", None))
        self.comboBox_4.setItemText(2, QCoreApplication.translate("Digitalfilters_arduino_widget", u"CAUER", None))

#if QT_CONFIG(tooltip)
        self.label_14.setToolTip(QCoreApplication.translate("Digitalfilters_arduino_widget", u"<html><head/><body><p>Cutoff Frequency</p><p><br/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.label_14.setWhatsThis(QCoreApplication.translate("Digitalfilters_arduino_widget", u"<html><head/><body><p>Cutoff Frequency</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.label_14.setText(QCoreApplication.translate("Digitalfilters_arduino_widget", u"fc:", None))
        self.fc_line.setText(QCoreApplication.translate("Digitalfilters_arduino_widget", u"100", None))
        self.no_fr.setText(QCoreApplication.translate("Digitalfilters_arduino_widget", u"No", None))
        self.label_13.setText(QCoreApplication.translate("Digitalfilters_arduino_widget", u"Plot frequency response?", None))
        self.yes_fr.setText(QCoreApplication.translate("Digitalfilters_arduino_widget", u"Yes", None))
        self.label.setText(QCoreApplication.translate("Digitalfilters_arduino_widget", u"Filter:", None))
        self.filter_combox.setItemText(0, QCoreApplication.translate("Digitalfilters_arduino_widget", u"FIR", None))
        self.filter_combox.setItemText(1, QCoreApplication.translate("Digitalfilters_arduino_widget", u"IIR", None))

        self.label_4.setText(QCoreApplication.translate("Digitalfilters_arduino_widget", u"Low (Hz):", None))
        self.label_5.setText(QCoreApplication.translate("Digitalfilters_arduino_widget", u"High (Hz):", None))
        self.label_2.setText(QCoreApplication.translate("Digitalfilters_arduino_widget", u"Filter numtaps:", None))
        self.label_3.setText(QCoreApplication.translate("Digitalfilters_arduino_widget", u"Fs:", None))
        self.label_6.setText(QCoreApplication.translate("Digitalfilters_arduino_widget", u"Type:", None))
        self.comboBox_2.setItemText(0, QCoreApplication.translate("Digitalfilters_arduino_widget", u"HALF-BAND", None))
        self.comboBox_2.setItemText(1, QCoreApplication.translate("Digitalfilters_arduino_widget", u"HIGHPASS", None))
        self.comboBox_2.setItemText(2, QCoreApplication.translate("Digitalfilters_arduino_widget", u"BANDPASS", None))
        self.comboBox_2.setItemText(3, QCoreApplication.translate("Digitalfilters_arduino_widget", u"LOWPASS", None))

        self.label_7.setText(QCoreApplication.translate("Digitalfilters_arduino_widget", u"Device:", None))
        self.reload_devices.setText("")
        self.Filter_button.setText(QCoreApplication.translate("Digitalfilters_arduino_widget", u"FILTER", None))
    # retranslateUi

