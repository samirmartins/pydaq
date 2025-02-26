# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'PyDAQ_get_model_sysconfig_Arduino_widgetIkIyfu.ui'
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
    QButtonGroup,
    QComboBox,
    QFrame,
    QGridLayout,
    QHBoxLayout,
    QLabel,
    QRadioButton,
    QSizePolicy,
    QSpinBox,
    QVBoxLayout,
    QWidget,
)
from . import resources_1_rc


class Ui_Arduino_GetModel_W(object):
    def setupUi(self, Arduino_GetModel_W):
        if not Arduino_GetModel_W.objectName():
            Arduino_GetModel_W.setObjectName("Arduino_GetModel_W")
        Arduino_GetModel_W.resize(739, 407)
        Arduino_GetModel_W.setStyleSheet(
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
            "	b"
            "order-left: 1.5px solid rgb(46, 46, 46);\n"
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
            "	font: "
            '12pt "Helvetica";\n'
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
            "	image: url(:/imgs/imgs/reload"
            ".png);\n"
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
        self.verticalLayout = QVBoxLayout(Arduino_GetModel_W)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QWidget(Arduino_GetModel_W)
        self.widget.setObjectName("widget")
        self.widget.setMaximumSize(QSize(16777205, 16777205))
        self.gridLayout = QGridLayout(self.widget)
        self.gridLayout.setObjectName("gridLayout")
        self.label_5 = QLabel(self.widget)
        self.label_5.setObjectName("label_5")
        self.label_5.setMinimumSize(QSize(0, 30))
        self.label_5.setMaximumSize(QSize(16777215, 30))

        self.gridLayout.addWidget(self.label_5, 3, 0, 1, 1)

        self.label_6 = QLabel(self.widget)
        self.label_6.setObjectName("label_6")
        self.label_6.setMinimumSize(QSize(0, 30))
        self.label_6.setMaximumSize(QSize(16777215, 30))

        self.gridLayout.addWidget(self.label_6, 4, 0, 1, 1)

        self.widget_19 = QWidget(self.widget)
        self.widget_19.setObjectName("widget_19")
        self.horizontalLayout_2 = QHBoxLayout(self.widget_19)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.perc_data_val_in = QSpinBox(self.widget_19)
        self.perc_data_val_in.setObjectName("perc_data_val_in")
        self.perc_data_val_in.setMinimum(10)

        self.horizontalLayout_2.addWidget(self.perc_data_val_in)

        self.gridLayout.addWidget(self.widget_19, 7, 2, 1, 1)

        self.widget_6 = QWidget(self.widget)
        self.widget_6.setObjectName("widget_6")
        self.gridLayout_7 = QGridLayout(self.widget_6)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.inp_lag_sysid_in = QSpinBox(self.widget_6)
        self.inp_lag_sysid_in.setObjectName("inp_lag_sysid_in")
        self.inp_lag_sysid_in.setMinimumSize(QSize(0, 22))
        self.inp_lag_sysid_in.setMaximumSize(QSize(16777215, 22))
        self.inp_lag_sysid_in.setBaseSize(QSize(0, 12))
        self.inp_lag_sysid_in.setValue(3)

        self.gridLayout_7.addWidget(self.inp_lag_sysid_in, 0, 0, 1, 1)

        self.gridLayout.addWidget(self.widget_6, 3, 2, 1, 1)

        self.widget_8 = QWidget(self.widget)
        self.widget_8.setObjectName("widget_8")
        self.gridLayout_5 = QGridLayout(self.widget_8)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.out_lag_sysid_in = QSpinBox(self.widget_8)
        self.out_lag_sysid_in.setObjectName("out_lag_sysid_in")
        self.out_lag_sysid_in.setMinimumSize(QSize(0, 22))
        self.out_lag_sysid_in.setMaximumSize(QSize(16777215, 22))
        self.out_lag_sysid_in.setValue(3)

        self.gridLayout_5.addWidget(self.out_lag_sysid_in, 0, 0, 1, 1)

        self.gridLayout.addWidget(self.widget_8, 2, 2, 1, 1)

        self.label_4 = QLabel(self.widget)
        self.label_4.setObjectName("label_4")
        self.label_4.setMinimumSize(QSize(0, 30))
        self.label_4.setMaximumSize(QSize(16777215, 30))

        self.gridLayout.addWidget(self.label_4, 1, 0, 1, 1)

        self.widget_9 = QWidget(self.widget)
        self.widget_9.setObjectName("widget_9")
        self.horizontalLayout_3 = QHBoxLayout(self.widget_9)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.widget_18 = QWidget(self.widget_9)
        self.widget_18.setObjectName("widget_18")
        self.gridLayout_15 = QGridLayout(self.widget_18)
        self.gridLayout_15.setObjectName("gridLayout_15")
        self.true_ext_lsq = QRadioButton(self.widget_18)
        self.extended_lsq_radio_group = QButtonGroup(Arduino_GetModel_W)
        self.extended_lsq_radio_group.setObjectName("extended_lsq_radio_group")
        self.extended_lsq_radio_group.addButton(self.true_ext_lsq)
        self.true_ext_lsq.setObjectName("true_ext_lsq")
        self.true_ext_lsq.setChecked(True)

        self.gridLayout_15.addWidget(self.true_ext_lsq, 1, 0, 1, 1, Qt.AlignLeft)

        self.false_ext_lsq = QRadioButton(self.widget_18)
        self.extended_lsq_radio_group.addButton(self.false_ext_lsq)
        self.false_ext_lsq.setObjectName("false_ext_lsq")

        self.gridLayout_15.addWidget(self.false_ext_lsq, 1, 1, 1, 1)

        self.horizontalLayout_3.addWidget(self.widget_18, 0, Qt.AlignLeft)

        self.gridLayout.addWidget(self.widget_9, 6, 2, 1, 1)

        self.widget_5 = QWidget(self.widget)
        self.widget_5.setObjectName("widget_5")
        self.gridLayout_6 = QGridLayout(self.widget_5)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.degree_sysid_in = QSpinBox(self.widget_5)
        self.degree_sysid_in.setObjectName("degree_sysid_in")
        self.degree_sysid_in.setMinimumSize(QSize(0, 22))
        self.degree_sysid_in.setMaximumSize(QSize(16777215, 22))
        self.degree_sysid_in.setSingleStep(1)
        self.degree_sysid_in.setValue(2)

        self.gridLayout_6.addWidget(self.degree_sysid_in, 0, 0, 1, 1)

        self.gridLayout.addWidget(self.widget_5, 1, 2, 1, 1)

        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName("label_2")
        self.label_2.setMinimumSize(QSize(0, 30))
        self.label_2.setMaximumSize(QSize(16777215, 30))

        self.gridLayout.addWidget(self.label_2, 7, 0, 1, 1)

        self.label_8 = QLabel(self.widget)
        self.label_8.setObjectName("label_8")
        self.label_8.setMinimumSize(QSize(0, 30))
        self.label_8.setMaximumSize(QSize(16777215, 30))
        self.label_8.setBaseSize(QSize(0, 0))

        self.gridLayout.addWidget(self.label_8, 6, 0, 1, 1)

        self.label_7 = QLabel(self.widget)
        self.label_7.setObjectName("label_7")
        self.label_7.setMinimumSize(QSize(0, 30))
        self.label_7.setMaximumSize(QSize(16777215, 30))

        self.gridLayout.addWidget(self.label_7, 5, 0, 1, 1)

        self.label_9 = QLabel(self.widget)
        self.label_9.setObjectName("label_9")
        self.label_9.setMinimumSize(QSize(0, 30))
        self.label_9.setMaximumSize(QSize(16777215, 30))

        self.gridLayout.addWidget(self.label_9, 2, 0, 1, 1)

        self.label = QLabel(self.widget)
        self.label.setObjectName("label")
        self.label.setMinimumSize(QSize(0, 30))
        self.label.setMaximumSize(QSize(16777215, 30))

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.widget_2 = QWidget(self.widget)
        self.widget_2.setObjectName("widget_2")
        self.gridLayout_2 = QGridLayout(self.widget_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.num_inf_value_sysid_in = QSpinBox(self.widget_2)
        self.num_inf_value_sysid_in.setObjectName("num_inf_value_sysid_in")
        self.num_inf_value_sysid_in.setMinimumSize(QSize(0, 22))
        self.num_inf_value_sysid_in.setMaximumSize(QSize(16777215, 22))

        self.gridLayout_2.addWidget(self.num_inf_value_sysid_in, 0, 0, 1, 1)

        self.gridLayout.addWidget(self.widget_2, 4, 2, 1, 1)

        self.widget_4 = QWidget(self.widget)
        self.widget_4.setObjectName("widget_4")
        self.gridLayout_3 = QGridLayout(self.widget_4)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.esti_sysid_in = QComboBox(self.widget_4)
        self.esti_sysid_in.setObjectName("esti_sysid_in")
        self.esti_sysid_in.setMinimumSize(QSize(0, 22))
        self.esti_sysid_in.setMaximumSize(QSize(16777215, 22))

        self.gridLayout_3.addWidget(self.esti_sysid_in, 0, 0, 1, 1)

        self.gridLayout.addWidget(self.widget_4, 5, 2, 1, 1)

        self.line = QFrame(self.widget)
        self.line.setObjectName("line")
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line, 1, 1, 7, 1)

        self.verticalLayout.addWidget(self.widget)

        self.retranslateUi(Arduino_GetModel_W)

        QMetaObject.connectSlotsByName(Arduino_GetModel_W)

    # setupUi

    def retranslateUi(self, Arduino_GetModel_W):
        Arduino_GetModel_W.setWindowTitle(
            QCoreApplication.translate("Arduino_GetModel_W", "Form", None)
        )
        self.label_5.setText(
            QCoreApplication.translate("Arduino_GetModel_W", "Input Lag", None)
        )
        self.label_6.setText(
            QCoreApplication.translate(
                "Arduino_GetModel_W", "Number of information values", None
            )
        )
        self.label_4.setText(
            QCoreApplication.translate("Arduino_GetModel_W", "Degree", None)
        )
        self.true_ext_lsq.setText(
            QCoreApplication.translate("Arduino_GetModel_W", "True", None)
        )
        self.false_ext_lsq.setText(
            QCoreApplication.translate("Arduino_GetModel_W", "False", None)
        )
        self.label_2.setText(
            QCoreApplication.translate(
                "Arduino_GetModel_W", "Percentage of data for validation ", None
            )
        )
        self.label_8.setText(
            QCoreApplication.translate(
                "Arduino_GetModel_W", "Extended least squares algorithm", None
            )
        )
        self.label_7.setText(
            QCoreApplication.translate("Arduino_GetModel_W", "Estimator", None)
        )
        self.label_9.setText(
            QCoreApplication.translate("Arduino_GetModel_W", "Output Lag", None)
        )
        self.label.setText(
            QCoreApplication.translate(
                "Arduino_GetModel_W", "System Identification", None
            )
        )

    # retranslateUi
