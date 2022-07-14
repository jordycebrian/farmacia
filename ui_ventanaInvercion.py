# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ventanaInvercion.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_invercion(object):
    def setupUi(self, invercion):
        if not invercion.objectName():
            invercion.setObjectName(u"invercion")
        invercion.resize(618, 510)
        self.centralwidget = QWidget(invercion)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame_content = QFrame(self.centralwidget)
        self.frame_content.setObjectName(u"frame_content")
        self.frame_content.setGeometry(QRect(0, 0, 781, 81))
        self.frame_content.setStyleSheet(u"QObject{\n"
"	background-color: #555;\n"
"}")
        self.frame_content.setFrameShape(QFrame.StyledPanel)
        self.frame_content.setFrameShadow(QFrame.Raised)
        self.lbl_logo_2 = QLabel(self.frame_content)
        self.lbl_logo_2.setObjectName(u"lbl_logo_2")
        self.lbl_logo_2.setGeometry(QRect(10, 0, 271, 81))
        self.lbl_logo_2.setPixmap(QPixmap(u"../../../Downloads/rocky-linux-icon.png"))
        self.lbl_titulo_2 = QLabel(self.frame_content)
        self.lbl_titulo_2.setObjectName(u"lbl_titulo_2")
        self.lbl_titulo_2.setGeometry(QRect(280, 20, 131, 41))
        font = QFont()
        font.setFamily(u"Arial Black")
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(99)
        self.lbl_titulo_2.setFont(font)
        self.lbl_titulo_2.setStyleSheet(u"QObject{\n"
"	font: 900 18pt \"Arial Black\";\n"
"}")
        self.btn_atras = QPushButton(self.frame_content)
        self.btn_atras.setObjectName(u"btn_atras")
        self.btn_atras.setGeometry(QRect(520, 30, 71, 20))
        self.btn_atras.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_atras.setStyleSheet(u"QObject{\n"
"	color:White;\n"
"	background-color: #666;\n"
"	border-radius: 5px;\n"
"}\n"
"QObject:hover{\n"
"	background-color: #222;\n"
"}")
        icon = QIcon()
        icon.addFile(u"../../../Downloads/productos.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_atras.setIcon(icon)
        self.tableWidget_invercion = QTableWidget(self.centralwidget)
        if (self.tableWidget_invercion.columnCount() < 4):
            self.tableWidget_invercion.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_invercion.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_invercion.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_invercion.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_invercion.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.tableWidget_invercion.setObjectName(u"tableWidget_invercion")
        self.tableWidget_invercion.setGeometry(QRect(110, 150, 401, 261))
        self.tableWidget_invercion.setAutoFillBackground(False)
        self.tableWidget_invercion.setStyleSheet(u"font: 87 9pt \"Arial Black\";\n"
"border: 1px solid white;\n"
"background-color: white;\n"
"")
        self.tableWidget_invercion.horizontalHeader().setCascadingSectionResizes(False)
        self.label_total = QLabel(self.centralwidget)
        self.label_total.setObjectName(u"label_total")
        self.label_total.setGeometry(QRect(220, 430, 151, 21))
        self.label_total.setStyleSheet(u"font: 15pt \"Arial\";")
        self.txt_total_invercion = QLineEdit(self.centralwidget)
        self.txt_total_invercion.setObjectName(u"txt_total_invercion")
        self.txt_total_invercion.setGeometry(QRect(370, 430, 141, 21))
        self.txt_total_invercion.setStyleSheet(u"color: black;\n"
"font: 75 10pt \"Arial\";\n"
"border: 1px solid white;\n"
"border-radius: 5px;\n"
"background-color: white;")
        self.btn_limpiar_ventas = QPushButton(self.centralwidget)
        self.btn_limpiar_ventas.setObjectName(u"btn_limpiar_ventas")
        self.btn_limpiar_ventas.setGeometry(QRect(350, 110, 161, 21))
        self.btn_limpiar_ventas.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_limpiar_ventas.setStyleSheet(u"QObject{\n"
"	color:White;\n"
"	background-color: #666;\n"
"	border-radius: 5px;\n"
"}\n"
"QObject:hover{\n"
"	background-color: #222;\n"
"}")
        invercion.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(invercion)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 618, 21))
        invercion.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(invercion)
        self.statusbar.setObjectName(u"statusbar")
        invercion.setStatusBar(self.statusbar)

        self.retranslateUi(invercion)

        QMetaObject.connectSlotsByName(invercion)
    # setupUi

    def retranslateUi(self, invercion):
        invercion.setWindowTitle(QCoreApplication.translate("invercion", u"MainWindow", None))
        self.lbl_logo_2.setText("")
        self.lbl_titulo_2.setText(QCoreApplication.translate("invercion", u"Invercion", None))
        self.btn_atras.setText("")
        ___qtablewidgetitem = self.tableWidget_invercion.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("invercion", u"Codigo Barras", None));
        ___qtablewidgetitem1 = self.tableWidget_invercion.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("invercion", u"Fecha", None));
        ___qtablewidgetitem2 = self.tableWidget_invercion.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("invercion", u"Cantidad", None));
        ___qtablewidgetitem3 = self.tableWidget_invercion.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("invercion", u"Total", None));
        self.label_total.setText(QCoreApplication.translate("invercion", u"Total Generado:", None))
        self.btn_limpiar_ventas.setText(QCoreApplication.translate("invercion", u"Limpiar Ventas", None))
    # retranslateUi

