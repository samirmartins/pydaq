# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'PRBS_Info_widgetSRReWZ.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (
    QCoreApplication,
    QDate,
    QDateTime,
    QLocale,
    QMetaObject,
    QObject,
    QPoint,
    QRect,
    QSize,
    QTime,
    QUrl,
    Qt,
)
from PySide6.QtGui import (
    QBrush,
    QColor,
    QConicalGradient,
    QCursor,
    QFont,
    QFontDatabase,
    QGradient,
    QIcon,
    QImage,
    QKeySequence,
    QLinearGradient,
    QPainter,
    QPalette,
    QPixmap,
    QRadialGradient,
    QTransform,
)
from PySide6.QtWidgets import (
    QApplication,
    QFrame,
    QGridLayout,
    QLabel,
    QLineEdit,
    QSizePolicy,
    QSpinBox,
    QWidget,
)
from . import resources_1_rc


class Ui_PRBS_Info(object):
    def setupUi(self, PRBS_Info):
        if not PRBS_Info.objectName():
            PRBS_Info.setObjectName("PRBS_Info")
        PRBS_Info.resize(318, 294)
        sizePolicy = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(PRBS_Info.sizePolicy().hasHeightForWidth())
        PRBS_Info.setSizePolicy(sizePolicy)
        PRBS_Info.setMinimumSize(QSize(0, 0))
        PRBS_Info.setMaximumSize(QSize(16777215, 16777215))
        PRBS_Info.setStyleSheet(
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
            "QWidget#PRBS_Info{\n"
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
            "	border-le"
            "ft: 1.5px solid rgb(46, 46, 46);\n"
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
            '	font: 12pt "Helvetica";\n'
            "	text-align:center;\n"
            "}\n"
            "\n"
            "QWidget{\n"
            '	font: 12pt "H'
            'elvetica";\n'
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
            "	image: url(:/imgs/imgs/reload.png);\n"
            ""
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
            "}"
        )
        self.gridLayout = QGridLayout(PRBS_Info)
        self.gridLayout.setObjectName("gridLayout")
        self.widget = QWidget(PRBS_Info)
        self.widget.setObjectName("widget")
        self.gridLayout_2 = QGridLayout(self.widget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label = QLabel(self.widget)
        self.label.setObjectName("label")

        self.gridLayout_2.addWidget(self.label, 2, 0, 1, 1)

        self.prbs_bits_in = QSpinBox(self.widget)
        self.prbs_bits_in.setObjectName("prbs_bits_in")
        sizePolicy1 = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(
            self.prbs_bits_in.sizePolicy().hasHeightForWidth()
        )
        self.prbs_bits_in.setSizePolicy(sizePolicy1)
        self.prbs_bits_in.setMinimumSize(QSize(0, 22))
        self.prbs_bits_in.setMaximumSize(QSize(16777215, 22))
        self.prbs_bits_in.setMinimum(1)
        self.prbs_bits_in.setValue(6)

        self.gridLayout_2.addWidget(self.prbs_bits_in, 3, 0, 1, 1)

        self.prbs_seed_in = QLineEdit(self.widget)
        self.prbs_seed_in.setObjectName("prbs_seed_in")

        self.gridLayout_2.addWidget(self.prbs_seed_in, 5, 0, 1, 1)

        self.label_4 = QLabel(self.widget)
        self.label_4.setObjectName("label_4")

        self.gridLayout_2.addWidget(self.label_4, 6, 0, 1, 1)

        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName("label_2")

        self.gridLayout_2.addWidget(self.label_2, 0, 0, 1, 1)

        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName("label_3")

        self.gridLayout_2.addWidget(self.label_3, 4, 0, 1, 1)

        self.prbs_tb_var_in = QSpinBox(self.widget)
        self.prbs_tb_var_in.setObjectName("prbs_tb_var_in")
        self.prbs_tb_var_in.setMinimum(1)

        self.gridLayout_2.addWidget(self.prbs_tb_var_in, 7, 0, 1, 1)

        self.line = QFrame(self.widget)
        self.line.setObjectName("line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.gridLayout_2.addWidget(self.line, 1, 0, 1, 1)

        self.gridLayout.addWidget(self.widget, 1, 0, 1, 1)

        self.retranslateUi(PRBS_Info)

        QMetaObject.connectSlotsByName(PRBS_Info)

    # setupUi

    def retranslateUi(self, PRBS_Info):
        PRBS_Info.setWindowTitle(
            QCoreApplication.translate("PRBS_Info", "PRBS Signal Configuration", None)
        )
        self.label.setText(QCoreApplication.translate("PRBS_Info", "Bits", None))
        self.prbs_seed_in.setInputMask(
            QCoreApplication.translate("PRBS_Info", "BBBBBBBBBBBBBBB", None)
        )
        self.prbs_seed_in.setText(QCoreApplication.translate("PRBS_Info", "101", None))
        self.label_4.setText(QCoreApplication.translate("PRBS_Info", "Tb_var", None))
        self.label_2.setText(
            QCoreApplication.translate("PRBS_Info", "PRBS - Input Informations", None)
        )
        self.label_3.setText(QCoreApplication.translate("PRBS_Info", "Seed", None))

    # retranslateUi
