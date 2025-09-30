# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'PYDAQ_Digital_filterss_NIDAQ_widget.ui'
##
## Created by: Qt User Interface Compiler version 6.9.2
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
from PySide6.QtWidgets import (QApplication, QButtonGroup, QComboBox, QFrame,
    QGridLayout, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QRadioButton, QSizePolicy, QWidget)
import resources_1_rc

class Ui_Digitalfilters_NIDAQ_widget(object):
    def setupUi(self, Digitalfilters_NIDAQ_widget):
        if not Digitalfilters_NIDAQ_widget.objectName():
            Digitalfilters_NIDAQ_widget.setObjectName(u"Digitalfilters_NIDAQ_widget")
        Digitalfilters_NIDAQ_widget.resize(537, 520)
        Digitalfilters_NIDAQ_widget.setMinimumSize(QSize(537, 520))
        Digitalfilters_NIDAQ_widget.setMaximumSize(QSize(537, 800))
        Digitalfilters_NIDAQ_widget.setStyleSheet(u"QWidget{\n"
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
"QDou"
                        "bleSpinBox::up-button:hover{\n"
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
"")
        self.gridLayout = QGridLayout(Digitalfilters_NIDAQ_widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.line_2 = QFrame(Digitalfilters_NIDAQ_widget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout.addWidget(self.line_2, 4, 0, 1, 1)

        self.left_side = QWidget(Digitalfilters_NIDAQ_widget)
        self.left_side.setObjectName(u"left_side")
        self.left_side.setMinimumSize(QSize(483, 108))
        self.left_side.setMaximumSize(QSize(600, 108))
        self.gridLayout_2 = QGridLayout(self.left_side)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.widget_5 = QWidget(self.left_side)
        self.widget_5.setObjectName(u"widget_5")
        self.horizontalLayout = QHBoxLayout(self.widget_5)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.yes_fr = QRadioButton(self.widget_5)
        self.ratio_fr = QButtonGroup(Digitalfilters_NIDAQ_widget)
        self.ratio_fr.setObjectName(u"ratio_fr")
        self.ratio_fr.addButton(self.yes_fr)
        self.yes_fr.setObjectName(u"yes_fr")
        self.yes_fr.setChecked(True)

        self.horizontalLayout.addWidget(self.yes_fr)

        self.no_fr = QRadioButton(self.widget_5)
        self.ratio_fr.addButton(self.no_fr)
        self.no_fr.setObjectName(u"no_fr")

        self.horizontalLayout.addWidget(self.no_fr)


        self.gridLayout_2.addWidget(self.widget_5, 3, 2, 1, 1, Qt.AlignmentFlag.AlignLeft)

        self.line_7 = QFrame(self.left_side)
        self.line_7.setObjectName(u"line_7")
        self.line_7.setFrameShape(QFrame.Shape.VLine)
        self.line_7.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_2.addWidget(self.line_7, 0, 1, 5, 1)

        self.label_5 = QLabel(self.left_side)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(0, 30))
        self.label_5.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_2.addWidget(self.label_5, 3, 0, 1, 1)

        self.label_4 = QLabel(self.left_side)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(0, 30))
        self.label_4.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_2.addWidget(self.label_4, 1, 0, 1, 1)

        self.widget_4 = QWidget(self.left_side)
        self.widget_4.setObjectName(u"widget_4")
        self.gridLayout_6 = QGridLayout(self.widget_4)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.type_filter = QComboBox(self.widget_4)
        self.type_filter.addItem("")
        self.type_filter.addItem("")
        self.type_filter.setObjectName(u"type_filter")
        self.type_filter.setMinimumSize(QSize(0, 22))
        self.type_filter.setMaximumSize(QSize(16777215, 22))

        self.gridLayout_6.addWidget(self.type_filter, 0, 0, 1, 1)


        self.gridLayout_2.addWidget(self.widget_4, 1, 2, 1, 1)


        self.gridLayout.addWidget(self.left_side, 3, 0, 1, 1)

        self.widget_6 = QWidget(Digitalfilters_NIDAQ_widget)
        self.widget_6.setObjectName(u"widget_6")
        self.widget_6.setMinimumSize(QSize(0, 40))
        self.widget_6.setMaximumSize(QSize(560, 40))
        self.gridLayout_7 = QGridLayout(self.widget_6)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.save_button = QPushButton(self.widget_6)
        self.save_button.setObjectName(u"save_button")
        self.save_button.setMinimumSize(QSize(0, 30))
        self.save_button.setMaximumSize(QSize(100, 30))

        self.gridLayout_7.addWidget(self.save_button, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.widget_6, 8, 0, 1, 1)

        self.iir_widget = QWidget(Digitalfilters_NIDAQ_widget)
        self.iir_widget.setObjectName(u"iir_widget")
        self.iir_widget.setMinimumSize(QSize(519, 259))
        self.iir_widget.setMaximumSize(QSize(550, 300))
        self.gridLayout_9 = QGridLayout(self.iir_widget)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.label_12 = QLabel(self.iir_widget)
        self.label_12.setObjectName(u"label_12")

        self.gridLayout_9.addWidget(self.label_12, 4, 0, 1, 1)

        self.widget_11 = QWidget(self.iir_widget)
        self.widget_11.setObjectName(u"widget_11")
        self.widget_11.setMinimumSize(QSize(0, 50))
        self.widget_11.setMaximumSize(QSize(16777215, 60))
        self.gridLayout_14 = QGridLayout(self.widget_11)
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.designbox_iir = QComboBox(self.widget_11)
        self.designbox_iir.addItem("")
        self.designbox_iir.addItem("")
        self.designbox_iir.addItem("")
        self.designbox_iir.addItem("")
        self.designbox_iir.setObjectName(u"designbox_iir")
        self.designbox_iir.setMinimumSize(QSize(160, 0))

        self.gridLayout_14.addWidget(self.designbox_iir, 0, 0, 1, 1)


        self.gridLayout_9.addWidget(self.widget_11, 2, 2, 1, 1, Qt.AlignmentFlag.AlignRight)

        self.cutoff1_label = QLabel(self.iir_widget)
        self.cutoff1_label.setObjectName(u"cutoff1_label")

        self.gridLayout_9.addWidget(self.cutoff1_label, 6, 0, 1, 1)

        self.line_4 = QFrame(self.iir_widget)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.Shape.VLine)
        self.line_4.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_9.addWidget(self.line_4, 0, 1, 7, 1)

        self.widget_12 = QWidget(self.iir_widget)
        self.widget_12.setObjectName(u"widget_12")
        self.widget_12.setMinimumSize(QSize(0, 50))
        self.gridLayout_15 = QGridLayout(self.widget_12)
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.typebox_iir = QComboBox(self.widget_12)
        self.typebox_iir.addItem("")
        self.typebox_iir.addItem("")
        self.typebox_iir.addItem("")
        self.typebox_iir.addItem("")
        self.typebox_iir.setObjectName(u"typebox_iir")
        self.typebox_iir.setMinimumSize(QSize(160, 0))

        self.gridLayout_15.addWidget(self.typebox_iir, 0, 0, 1, 1)


        self.gridLayout_9.addWidget(self.widget_12, 5, 2, 1, 1, Qt.AlignmentFlag.AlignRight)

        self.widget_14 = QWidget(self.iir_widget)
        self.widget_14.setObjectName(u"widget_14")
        self.widget_14.setMinimumSize(QSize(0, 50))
        self.gridLayout_17 = QGridLayout(self.widget_14)
        self.gridLayout_17.setObjectName(u"gridLayout_17")
        self.rs = QLineEdit(self.widget_14)
        self.rs.setObjectName(u"rs")
        self.rs.setEnabled(True)
        self.rs.setMinimumSize(QSize(160, 0))
        self.rs.setMaxLength(999999999)

        self.gridLayout_17.addWidget(self.rs, 0, 0, 1, 1)


        self.gridLayout_9.addWidget(self.widget_14, 4, 2, 1, 1, Qt.AlignmentFlag.AlignRight)

        self.cutoff1_widget = QWidget(self.iir_widget)
        self.cutoff1_widget.setObjectName(u"cutoff1_widget")
        self.cutoff1_widget.setMinimumSize(QSize(0, 50))
        self.gridLayout_13 = QGridLayout(self.cutoff1_widget)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.cutoff_iir = QLineEdit(self.cutoff1_widget)
        self.cutoff_iir.setObjectName(u"cutoff_iir")
        self.cutoff_iir.setMinimumSize(QSize(160, 0))
        self.cutoff_iir.setMaxLength(999999999)

        self.gridLayout_13.addWidget(self.cutoff_iir, 0, 0, 1, 1)


        self.gridLayout_9.addWidget(self.cutoff1_widget, 6, 2, 1, 1, Qt.AlignmentFlag.AlignRight)

        self.label_9 = QLabel(self.iir_widget)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout_9.addWidget(self.label_9, 2, 0, 1, 1)

        self.widget_9 = QWidget(self.iir_widget)
        self.widget_9.setObjectName(u"widget_9")
        self.widget_9.setMinimumSize(QSize(0, 50))
        self.widget_9.setMaximumSize(QSize(16777215, 16777215))
        self.gridLayout_12 = QGridLayout(self.widget_9)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.order_iir = QLineEdit(self.widget_9)
        self.order_iir.setObjectName(u"order_iir")
        self.order_iir.setMinimumSize(QSize(160, 0))
        self.order_iir.setMaxLength(999999999)

        self.gridLayout_12.addWidget(self.order_iir, 0, 0, 1, 1, Qt.AlignmentFlag.AlignRight)


        self.gridLayout_9.addWidget(self.widget_9, 0, 2, 1, 1, Qt.AlignmentFlag.AlignRight)

        self.label_11 = QLabel(self.iir_widget)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout_9.addWidget(self.label_11, 3, 0, 1, 1)

        self.widget_13 = QWidget(self.iir_widget)
        self.widget_13.setObjectName(u"widget_13")
        self.widget_13.setMinimumSize(QSize(0, 50))
        self.gridLayout_16 = QGridLayout(self.widget_13)
        self.gridLayout_16.setObjectName(u"gridLayout_16")
        self.rp = QLineEdit(self.widget_13)
        self.rp.setObjectName(u"rp")
        self.rp.setMinimumSize(QSize(160, 0))
        self.rp.setMaxLength(999999999)

        self.gridLayout_16.addWidget(self.rp, 0, 0, 1, 1)


        self.gridLayout_9.addWidget(self.widget_13, 3, 2, 1, 1, Qt.AlignmentFlag.AlignRight)

        self.cutoff2_label = QLabel(self.iir_widget)
        self.cutoff2_label.setObjectName(u"cutoff2_label")

        self.gridLayout_9.addWidget(self.cutoff2_label, 7, 0, 1, 1)

        self.label_10 = QLabel(self.iir_widget)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout_9.addWidget(self.label_10, 5, 0, 1, 1)

        self.label_6 = QLabel(self.iir_widget)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_9.addWidget(self.label_6, 0, 0, 1, 1, Qt.AlignmentFlag.AlignLeft)

        self.fc_widget_2 = QWidget(self.iir_widget)
        self.fc_widget_2.setObjectName(u"fc_widget_2")
        self.fc_widget_2.setMinimumSize(QSize(0, 50))
        self.gridLayout_24 = QGridLayout(self.fc_widget_2)
        self.gridLayout_24.setObjectName(u"gridLayout_24")
        self.fc1_line_iir = QLineEdit(self.fc_widget_2)
        self.fc1_line_iir.setObjectName(u"fc1_line_iir")
        self.fc1_line_iir.setMaximumSize(QSize(60, 16777215))

        self.gridLayout_24.addWidget(self.fc1_line_iir, 0, 0, 1, 1)

        self.label_16 = QLabel(self.fc_widget_2)
        self.label_16.setObjectName(u"label_16")

        self.gridLayout_24.addWidget(self.label_16, 0, 1, 1, 1)

        self.fc2_line_iir = QLineEdit(self.fc_widget_2)
        self.fc2_line_iir.setObjectName(u"fc2_line_iir")
        self.fc2_line_iir.setMaximumSize(QSize(60, 16777215))

        self.gridLayout_24.addWidget(self.fc2_line_iir, 0, 2, 1, 1)


        self.gridLayout_9.addWidget(self.fc_widget_2, 7, 2, 1, 1, Qt.AlignmentFlag.AlignRight)


        self.gridLayout.addWidget(self.iir_widget, 7, 0, 1, 1)

        self.line = QFrame(Digitalfilters_NIDAQ_widget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout.addWidget(self.line, 6, 0, 1, 1)

        self.fir_widget = QWidget(Digitalfilters_NIDAQ_widget)
        self.fir_widget.setObjectName(u"fir_widget")
        self.fir_widget.setMinimumSize(QSize(519, 289))
        self.fir_widget.setMaximumSize(QSize(519, 289))
        self.fir_widget.setAutoFillBackground(False)
        self.gridLayout_3 = QGridLayout(self.fir_widget)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.widget_8 = QWidget(self.fir_widget)
        self.widget_8.setObjectName(u"widget_8")
        self.gridLayout_11 = QGridLayout(self.widget_8)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.type_box = QComboBox(self.widget_8)
        self.type_box.addItem("")
        self.type_box.addItem("")
        self.type_box.addItem("")
        self.type_box.addItem("")
        self.type_box.setObjectName(u"type_box")
        self.type_box.setMinimumSize(QSize(145, 0))
        self.type_box.setMaximumSize(QSize(145, 16777215))

        self.gridLayout_11.addWidget(self.type_box, 0, 0, 1, 1)


        self.gridLayout_3.addWidget(self.widget_8, 3, 2, 1, 1, Qt.AlignmentFlag.AlignRight)

        self.widget_3 = QWidget(self.fir_widget)
        self.widget_3.setObjectName(u"widget_3")
        self.gridLayout_5 = QGridLayout(self.widget_3)
        self.gridLayout_5.setObjectName(u"gridLayout_5")

        self.gridLayout_3.addWidget(self.widget_3, 6, 2, 1, 1, Qt.AlignmentFlag.AlignRight)

        self.cutoff_widget = QWidget(self.fir_widget)
        self.cutoff_widget.setObjectName(u"cutoff_widget")
        self.gridLayout_8 = QGridLayout(self.cutoff_widget)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.cutoff_fir = QLineEdit(self.cutoff_widget)
        self.cutoff_fir.setObjectName(u"cutoff_fir")
        self.cutoff_fir.setMaxLength(999999999)

        self.gridLayout_8.addWidget(self.cutoff_fir, 0, 0, 1, 1)


        self.gridLayout_3.addWidget(self.cutoff_widget, 4, 2, 1, 1, Qt.AlignmentFlag.AlignRight)

        self.widget_2 = QWidget(self.fir_widget)
        self.widget_2.setObjectName(u"widget_2")
        self.gridLayout_4 = QGridLayout(self.widget_2)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.order_fir = QLineEdit(self.widget_2)
        self.order_fir.setObjectName(u"order_fir")
        font = QFont()
        font.setFamilies([u"Helvetica"])
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        self.order_fir.setFont(font)
        self.order_fir.setMaxLength(999999999)

        self.gridLayout_4.addWidget(self.order_fir, 0, 0, 1, 1, Qt.AlignmentFlag.AlignRight)


        self.gridLayout_3.addWidget(self.widget_2, 2, 2, 1, 1, Qt.AlignmentFlag.AlignRight)

        self.line_3 = QFrame(self.fir_widget)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.Shape.VLine)
        self.line_3.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_3.addWidget(self.line_3, 0, 1, 6, 1)

        self.widget = QWidget(self.fir_widget)
        self.widget.setObjectName(u"widget")
        self.gridLayout_10 = QGridLayout(self.widget)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.design_box = QComboBox(self.widget)
        self.design_box.addItem("")
        self.design_box.addItem("")
        self.design_box.addItem("")
        self.design_box.addItem("")
        self.design_box.addItem("")
        self.design_box.addItem("")
        self.design_box.setObjectName(u"design_box")
        self.design_box.setMinimumSize(QSize(145, 0))
        self.design_box.setMaximumSize(QSize(300, 16777215))

        self.gridLayout_10.addWidget(self.design_box, 1, 0, 1, 1, Qt.AlignmentFlag.AlignRight)


        self.gridLayout_3.addWidget(self.widget, 1, 2, 1, 1, Qt.AlignmentFlag.AlignRight)

        self.fc_widget = QWidget(self.fir_widget)
        self.fc_widget.setObjectName(u"fc_widget")
        self.gridLayout_18 = QGridLayout(self.fc_widget)
        self.gridLayout_18.setObjectName(u"gridLayout_18")
        self.fc1_line = QLineEdit(self.fc_widget)
        self.fc1_line.setObjectName(u"fc1_line")
        self.fc1_line.setEnabled(True)
        self.fc1_line.setMinimumSize(QSize(60, 0))
        self.fc1_line.setMaximumSize(QSize(25, 16777215))
        self.fc1_line.setMaxLength(999999999)

        self.gridLayout_18.addWidget(self.fc1_line, 0, 0, 1, 1, Qt.AlignmentFlag.AlignRight)

        self.label_13 = QLabel(self.fc_widget)
        self.label_13.setObjectName(u"label_13")

        self.gridLayout_18.addWidget(self.label_13, 0, 1, 1, 1)

        self.fc2_line = QLineEdit(self.fc_widget)
        self.fc2_line.setObjectName(u"fc2_line")
        self.fc2_line.setMinimumSize(QSize(60, 0))
        self.fc2_line.setMaximumSize(QSize(60, 16777215))
        self.fc2_line.setMaxLength(999999999)

        self.gridLayout_18.addWidget(self.fc2_line, 0, 2, 1, 1)


        self.gridLayout_3.addWidget(self.fc_widget, 5, 2, 1, 1, Qt.AlignmentFlag.AlignRight)

        self.bd_widget = QWidget(self.fir_widget)
        self.bd_widget.setObjectName(u"bd_widget")
        self.gridLayout_19 = QGridLayout(self.bd_widget)
        self.gridLayout_19.setObjectName(u"gridLayout_19")
        self.label_3 = QLabel(self.bd_widget)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_19.addWidget(self.label_3, 0, 0, 1, 1)


        self.gridLayout_3.addWidget(self.bd_widget, 5, 0, 1, 1, Qt.AlignmentFlag.AlignLeft)

        self.cof_widget = QWidget(self.fir_widget)
        self.cof_widget.setObjectName(u"cof_widget")
        self.gridLayout_20 = QGridLayout(self.cof_widget)
        self.gridLayout_20.setObjectName(u"gridLayout_20")
        self.label_14 = QLabel(self.cof_widget)
        self.label_14.setObjectName(u"label_14")

        self.gridLayout_20.addWidget(self.label_14, 0, 0, 1, 1)


        self.gridLayout_3.addWidget(self.cof_widget, 4, 0, 1, 1, Qt.AlignmentFlag.AlignLeft)

        self.widget_16 = QWidget(self.fir_widget)
        self.widget_16.setObjectName(u"widget_16")
        self.gridLayout_21 = QGridLayout(self.widget_16)
        self.gridLayout_21.setObjectName(u"gridLayout_21")
        self.label_2 = QLabel(self.widget_16)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_21.addWidget(self.label_2, 0, 0, 1, 1)


        self.gridLayout_3.addWidget(self.widget_16, 3, 0, 1, 1, Qt.AlignmentFlag.AlignLeft)

        self.widget_17 = QWidget(self.fir_widget)
        self.widget_17.setObjectName(u"widget_17")
        self.gridLayout_22 = QGridLayout(self.widget_17)
        self.gridLayout_22.setObjectName(u"gridLayout_22")
        self.label = QLabel(self.widget_17)
        self.label.setObjectName(u"label")

        self.gridLayout_22.addWidget(self.label, 0, 0, 1, 1)


        self.gridLayout_3.addWidget(self.widget_17, 2, 0, 1, 1, Qt.AlignmentFlag.AlignLeft)

        self.widget_18 = QWidget(self.fir_widget)
        self.widget_18.setObjectName(u"widget_18")
        self.gridLayout_23 = QGridLayout(self.widget_18)
        self.gridLayout_23.setObjectName(u"gridLayout_23")
        self.label_7 = QLabel(self.widget_18)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_23.addWidget(self.label_7, 0, 0, 1, 1)


        self.gridLayout_3.addWidget(self.widget_18, 1, 0, 1, 1, Qt.AlignmentFlag.AlignLeft)


        self.gridLayout.addWidget(self.fir_widget, 5, 0, 1, 1)


        self.retranslateUi(Digitalfilters_NIDAQ_widget)

        QMetaObject.connectSlotsByName(Digitalfilters_NIDAQ_widget)
    # setupUi

    def retranslateUi(self, Digitalfilters_NIDAQ_widget):
        Digitalfilters_NIDAQ_widget.setWindowTitle(QCoreApplication.translate("Digitalfilters_NIDAQ_widget", u"Digital Filters", None))
        self.yes_fr.setText(QCoreApplication.translate("Digitalfilters_NIDAQ_widget", u"Yes", None))
        self.no_fr.setText(QCoreApplication.translate("Digitalfilters_NIDAQ_widget", u"No", None))
        self.label_5.setText(QCoreApplication.translate("Digitalfilters_NIDAQ_widget", u"Plot frequency response?", None))
        self.label_4.setText(QCoreApplication.translate("Digitalfilters_NIDAQ_widget", u"Fillter:", None))
        self.type_filter.setItemText(0, QCoreApplication.translate("Digitalfilters_NIDAQ_widget", u"FIR", None))
        self.type_filter.setItemText(1, QCoreApplication.translate("Digitalfilters_NIDAQ_widget", u"IIR", None))

        self.save_button.setText(QCoreApplication.translate("Digitalfilters_NIDAQ_widget", u"SAVE", None))
        self.label_12.setText(QCoreApplication.translate("Digitalfilters_NIDAQ_widget", u"Stopband attenuation (dB):", None))
        self.designbox_iir.setItemText(0, QCoreApplication.translate("Digitalfilters_NIDAQ_widget", u"Chebyshev Type I", None))
        self.designbox_iir.setItemText(1, QCoreApplication.translate("Digitalfilters_NIDAQ_widget", u"Chebyshev Type II", None))
        self.designbox_iir.setItemText(2, QCoreApplication.translate("Digitalfilters_NIDAQ_widget", u"Butterworth", None))
        self.designbox_iir.setItemText(3, QCoreApplication.translate("Digitalfilters_NIDAQ_widget", u"Elliptic", None))

        self.cutoff1_label.setText(QCoreApplication.translate("Digitalfilters_NIDAQ_widget", u"Cutoff:", None))
        self.typebox_iir.setItemText(0, QCoreApplication.translate("Digitalfilters_NIDAQ_widget", u"lowpass", None))
        self.typebox_iir.setItemText(1, QCoreApplication.translate("Digitalfilters_NIDAQ_widget", u"highpass", None))
        self.typebox_iir.setItemText(2, QCoreApplication.translate("Digitalfilters_NIDAQ_widget", u"bandpass", None))
        self.typebox_iir.setItemText(3, QCoreApplication.translate("Digitalfilters_NIDAQ_widget", u"bandstop", None))

        self.rs.setText(QCoreApplication.translate("Digitalfilters_NIDAQ_widget", u"1", None))
        self.cutoff_iir.setText(QCoreApplication.translate("Digitalfilters_NIDAQ_widget", u"0.1", None))
        self.label_9.setText(QCoreApplication.translate("Digitalfilters_NIDAQ_widget", u"Filter design:", None))
        self.order_iir.setText(QCoreApplication.translate("Digitalfilters_NIDAQ_widget", u"2", None))
        self.label_11.setText(QCoreApplication.translate("Digitalfilters_NIDAQ_widget", u"Passband ripple (dB):", None))
        self.rp.setText(QCoreApplication.translate("Digitalfilters_NIDAQ_widget", u"2", None))
        self.cutoff2_label.setText(QCoreApplication.translate("Digitalfilters_NIDAQ_widget", u"Cutoff:", None))
        self.label_10.setText(QCoreApplication.translate("Digitalfilters_NIDAQ_widget", u"Type:", None))
        self.label_6.setText(QCoreApplication.translate("Digitalfilters_NIDAQ_widget", u"Order:", None))
        self.fc1_line_iir.setText(QCoreApplication.translate("Digitalfilters_NIDAQ_widget", u"0.1", None))
        self.label_16.setText(QCoreApplication.translate("Digitalfilters_NIDAQ_widget", u"to", None))
        self.fc2_line_iir.setText(QCoreApplication.translate("Digitalfilters_NIDAQ_widget", u"0.2", None))
        self.type_box.setItemText(0, QCoreApplication.translate("Digitalfilters_NIDAQ_widget", u"lowpass", None))
        self.type_box.setItemText(1, QCoreApplication.translate("Digitalfilters_NIDAQ_widget", u"highpass", None))
        self.type_box.setItemText(2, QCoreApplication.translate("Digitalfilters_NIDAQ_widget", u"bandpass", None))
        self.type_box.setItemText(3, QCoreApplication.translate("Digitalfilters_NIDAQ_widget", u"bandstop", None))

        self.cutoff_fir.setText(QCoreApplication.translate("Digitalfilters_NIDAQ_widget", u"0.1", None))
        self.order_fir.setText(QCoreApplication.translate("Digitalfilters_NIDAQ_widget", u"10", None))
        self.design_box.setItemText(0, QCoreApplication.translate("Digitalfilters_NIDAQ_widget", u"Hamming", None))
        self.design_box.setItemText(1, QCoreApplication.translate("Digitalfilters_NIDAQ_widget", u"Hann", None))
        self.design_box.setItemText(2, QCoreApplication.translate("Digitalfilters_NIDAQ_widget", u"Bartlett-Hann", None))
        self.design_box.setItemText(3, QCoreApplication.translate("Digitalfilters_NIDAQ_widget", u"Blackman", None))
        self.design_box.setItemText(4, QCoreApplication.translate("Digitalfilters_NIDAQ_widget", u"Gauss", None))
        self.design_box.setItemText(5, QCoreApplication.translate("Digitalfilters_NIDAQ_widget", u"Kaiser", None))

        self.fc1_line.setText(QCoreApplication.translate("Digitalfilters_NIDAQ_widget", u"0.1", None))
        self.label_13.setText(QCoreApplication.translate("Digitalfilters_NIDAQ_widget", u"to", None))
        self.fc2_line.setText(QCoreApplication.translate("Digitalfilters_NIDAQ_widget", u"0.2", None))
        self.label_3.setText(QCoreApplication.translate("Digitalfilters_NIDAQ_widget", u"Cutoff (Hz):", None))
        self.label_14.setText(QCoreApplication.translate("Digitalfilters_NIDAQ_widget", u"Cutoff (Hz):", None))
        self.label_2.setText(QCoreApplication.translate("Digitalfilters_NIDAQ_widget", u"Type:", None))
        self.label.setText(QCoreApplication.translate("Digitalfilters_NIDAQ_widget", u"Order:", None))
        self.label_7.setText(QCoreApplication.translate("Digitalfilters_NIDAQ_widget", u"Filter design:", None))
    # retranslateUi

