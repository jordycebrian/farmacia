# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ventanaFacturas.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_ventanaFacturas(object):
    def setupUi(self, ventanaFacturas):
        if not ventanaFacturas.objectName():
            ventanaFacturas.setObjectName(u"ventanaFacturas")
        ventanaFacturas.resize(760, 470)
        ventanaFacturas.setMaximumSize(QSize(760, 470))
        self.centralwidget = QWidget(ventanaFacturas)
        self.centralwidget.setObjectName(u"centralwidget")
        self.btn_eliminar_factura = QPushButton(self.centralwidget)
        self.btn_eliminar_factura.setObjectName(u"btn_eliminar_factura")
        self.btn_eliminar_factura.setGeometry(QRect(600, 110, 111, 31))
        self.btn_eliminar_factura.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_eliminar_factura.setStyleSheet(u"QObject{\n"
"	color: black;\n"
"	background-color: #ccc;\n"
"	border-radius: 5px;\n"
"	font: 75 10pt \"Arial\";\n"
"}\n"
"QObject:hover{\n"
"	background-color: yellow;\n"
"}")
        self.tableWidget_facturas = QTableWidget(self.centralwidget)
        if (self.tableWidget_facturas.columnCount() < 5):
            self.tableWidget_facturas.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setTextAlignment(Qt.AlignJustify|Qt.AlignTop);
        self.tableWidget_facturas.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget_facturas.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget_facturas.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget_facturas.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget_facturas.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.tableWidget_facturas.setObjectName(u"tableWidget_facturas")
        self.tableWidget_facturas.setGeometry(QRect(130, 170, 501, 231))
        self.tableWidget_facturas.setStyleSheet(u"font: 87 9pt \"Arial Black\";\n"
"border: 1px solid white;\n"
"background-color: white;\n"
"")
        self.btn_modificar_factura = QPushButton(self.centralwidget)
        self.btn_modificar_factura.setObjectName(u"btn_modificar_factura")
        self.btn_modificar_factura.setGeometry(QRect(420, 110, 111, 31))
        self.btn_modificar_factura.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_modificar_factura.setStyleSheet(u"QObject{\n"
"	color: black;\n"
"	background-color: #ccc;\n"
"	border-radius: 5px;\n"
"	font: 75 10pt \"Arial\";\n"
"}\n"
"QObject:hover{\n"
"	background-color: yellow;\n"
"}")
        self.btn_agregar_factura = QPushButton(self.centralwidget)
        self.btn_agregar_factura.setObjectName(u"btn_agregar_factura")
        self.btn_agregar_factura.setGeometry(QRect(240, 110, 111, 31))
        self.btn_agregar_factura.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_agregar_factura.setStyleSheet(u"QObject{\n"
"	color: black;\n"
"	background-color: #ccc;\n"
"	border-radius: 5px;\n"
"	font: 75 10pt \"Arial\";\n"
"}\n"
"QObject:hover{\n"
"	background-color: yellow;\n"
"}")
        self.lbl_error_buscador = QLabel(self.centralwidget)
        self.lbl_error_buscador.setObjectName(u"lbl_error_buscador")
        self.lbl_error_buscador.setGeometry(QRect(205, 150, 311, 20))
        self.lbl_error_buscador.setStyleSheet(u"font: 87 9pt \"Arial Black\";")
        self.frame_content = QFrame(self.centralwidget)
        self.frame_content.setObjectName(u"frame_content")
        self.frame_content.setGeometry(QRect(-10, 0, 771, 81))
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
        self.lbl_titulo_2.setGeometry(QRect(270, 0, 311, 41))
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
        self.btn_atras.setGeometry(QRect(680, 30, 71, 20))
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
        self.btn_mostrar_facturas = QPushButton(self.centralwidget)
        self.btn_mostrar_facturas.setObjectName(u"btn_mostrar_facturas")
        self.btn_mostrar_facturas.setGeometry(QRect(60, 110, 111, 31))
        self.btn_mostrar_facturas.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_mostrar_facturas.setStyleSheet(u"QObject{\n"
"	color: black;\n"
"	background-color: #ccc;\n"
"	border-radius: 5px;\n"
"	font: 75 10pt \"Arial\";\n"
"}\n"
"QObject:hover{\n"
"	background-color: yellow;\n"
"}")
        ventanaFacturas.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(ventanaFacturas)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 760, 21))
        ventanaFacturas.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(ventanaFacturas)
        self.statusbar.setObjectName(u"statusbar")
        ventanaFacturas.setStatusBar(self.statusbar)

        self.retranslateUi(ventanaFacturas)

        QMetaObject.connectSlotsByName(ventanaFacturas)
    # setupUi

    def retranslateUi(self, ventanaFacturas):
        ventanaFacturas.setWindowTitle(QCoreApplication.translate("ventanaFacturas", u"Facturas", None))
        self.btn_eliminar_factura.setText(QCoreApplication.translate("ventanaFacturas", u"Eliminar Factura", None))
        ___qtablewidgetitem = self.tableWidget_facturas.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("ventanaFacturas", u"Clave", None));
        ___qtablewidgetitem1 = self.tableWidget_facturas.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("ventanaFacturas", u"Empresa", None));
        ___qtablewidgetitem2 = self.tableWidget_facturas.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("ventanaFacturas", u"Cantidad_Producto", None));
        ___qtablewidgetitem3 = self.tableWidget_facturas.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("ventanaFacturas", u"Calle", None));
        ___qtablewidgetitem4 = self.tableWidget_facturas.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("ventanaFacturas", u"Colonia", None));
        self.btn_modificar_factura.setText(QCoreApplication.translate("ventanaFacturas", u"Modificar Factura", None))
        self.btn_agregar_factura.setText(QCoreApplication.translate("ventanaFacturas", u"Crear Factura", None))
        self.lbl_error_buscador.setText("")
        self.lbl_logo_2.setText("")
        self.lbl_titulo_2.setText(QCoreApplication.translate("ventanaFacturas", u"Generador de Facturas", None))
        self.btn_atras.setText("")
        self.btn_mostrar_facturas.setText(QCoreApplication.translate("ventanaFacturas", u"Mostrar Facturas", None))
    # retranslateUi

