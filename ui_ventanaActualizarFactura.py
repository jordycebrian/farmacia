# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ventanaActualizarFactura.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_ventanaModificarFactura(object):
    def setupUi(self, ventanaModificarFactura):
        if not ventanaModificarFactura.objectName():
            ventanaModificarFactura.setObjectName(u"ventanaModificarFactura")
        ventanaModificarFactura.resize(380, 300)
        ventanaModificarFactura.setMaximumSize(QSize(380, 300))
        ventanaModificarFactura.setStyleSheet(u"background-color:#555;")
        self.txt_clave = QLineEdit(ventanaModificarFactura)
        self.txt_clave.setObjectName(u"txt_clave")
        self.txt_clave.setGeometry(QRect(100, 20, 261, 20))
        self.txt_clave.setStyleSheet(u"color: black;\n"
"font: 75 10pt \"Arial\";\n"
"border: 1px solid white;\n"
"border-radius: 5px;\n"
"background-color: white;")
        self.lbl_calle = QLabel(ventanaModificarFactura)
        self.lbl_calle.setObjectName(u"lbl_calle")
        self.lbl_calle.setGeometry(QRect(10, 140, 81, 21))
        self.lbl_calle.setStyleSheet(u"color: balck;\n"
"font: 900 12pt \"Arial\";")
        self.txt_empresa = QLineEdit(ventanaModificarFactura)
        self.txt_empresa.setObjectName(u"txt_empresa")
        self.txt_empresa.setGeometry(QRect(100, 60, 261, 20))
        self.txt_empresa.setStyleSheet(u"color: black;\n"
"font: 75 10pt \"Arial\";\n"
"border: 1px solid white;\n"
"border-radius: 5px;\n"
"background-color: white;")
        self.lbl_colonia = QLabel(ventanaModificarFactura)
        self.lbl_colonia.setObjectName(u"lbl_colonia")
        self.lbl_colonia.setGeometry(QRect(10, 180, 81, 21))
        self.lbl_colonia.setStyleSheet(u"color: balck;\n"
"font: 900 12pt \"Arial\";")
        self.lbl_clave = QLabel(ventanaModificarFactura)
        self.lbl_clave.setObjectName(u"lbl_clave")
        self.lbl_clave.setGeometry(QRect(10, 20, 71, 21))
        self.lbl_clave.setStyleSheet(u"color: balck;\n"
"font: 900 12pt \"Arial\";")
        self.btn_modificar_factura = QPushButton(ventanaModificarFactura)
        self.btn_modificar_factura.setObjectName(u"btn_modificar_factura")
        self.btn_modificar_factura.setGeometry(QRect(250, 250, 111, 41))
        self.btn_modificar_factura.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_modificar_factura.setStyleSheet(u"QObject{\n"
"	color:White;\n"
"	font: 900 12pt \"Arial\";\n"
"	background-color: #666;\n"
"	border-radius: 5px;\n"
"}\n"
"QObject:hover{\n"
"	background-color: #222;\n"
"}")
        self.lbl_empresa = QLabel(ventanaModificarFactura)
        self.lbl_empresa.setObjectName(u"lbl_empresa")
        self.lbl_empresa.setGeometry(QRect(10, 60, 91, 21))
        self.lbl_empresa.setStyleSheet(u"color: balck;\n"
"font: 900 12pt \"Arial\";")
        self.txt_calle = QLineEdit(ventanaModificarFactura)
        self.txt_calle.setObjectName(u"txt_calle")
        self.txt_calle.setGeometry(QRect(100, 140, 261, 20))
        self.txt_calle.setStyleSheet(u"color: black;\n"
"font: 75 10pt \"Arial\";\n"
"border: 1px solid white;\n"
"border-radius: 5px;\n"
"background-color: white;")
        self.txt_cantidad = QLineEdit(ventanaModificarFactura)
        self.txt_cantidad.setObjectName(u"txt_cantidad")
        self.txt_cantidad.setGeometry(QRect(100, 100, 261, 20))
        self.txt_cantidad.setStyleSheet(u"color: black;\n"
"font: 75 10pt \"Arial\";\n"
"border: 1px solid white;\n"
"border-radius: 5px;\n"
"background-color: white;")
        self.txt_cantidad.setEchoMode(QLineEdit.Normal)
        self.txt_colonia = QLineEdit(ventanaModificarFactura)
        self.txt_colonia.setObjectName(u"txt_colonia")
        self.txt_colonia.setGeometry(QRect(100, 180, 261, 20))
        self.txt_colonia.setStyleSheet(u"color: black;\n"
"font: 75 10pt \"Arial\";\n"
"border: 1px solid white;\n"
"border-radius: 5px;\n"
"background-color: white;")
        self.lbl_cantidad = QLabel(ventanaModificarFactura)
        self.lbl_cantidad.setObjectName(u"lbl_cantidad")
        self.lbl_cantidad.setGeometry(QRect(10, 100, 91, 21))
        self.lbl_cantidad.setStyleSheet(u"color: balck;\n"
"font: 900 12pt \"Arial\";")

        self.retranslateUi(ventanaModificarFactura)

        QMetaObject.connectSlotsByName(ventanaModificarFactura)
    # setupUi

    def retranslateUi(self, ventanaModificarFactura):
        ventanaModificarFactura.setWindowTitle(QCoreApplication.translate("ventanaModificarFactura", u"Modificar Factura", None))
        self.lbl_calle.setText(QCoreApplication.translate("ventanaModificarFactura", u"Calle:", None))
        self.txt_empresa.setText("")
        self.lbl_colonia.setText(QCoreApplication.translate("ventanaModificarFactura", u"Colonia:", None))
        self.lbl_clave.setText(QCoreApplication.translate("ventanaModificarFactura", u"Clave:", None))
        self.btn_modificar_factura.setText(QCoreApplication.translate("ventanaModificarFactura", u"Modificar", None))
        self.lbl_empresa.setText(QCoreApplication.translate("ventanaModificarFactura", u"Empresa:", None))
        self.txt_calle.setText("")
        self.lbl_cantidad.setText(QCoreApplication.translate("ventanaModificarFactura", u"Cantidad:", None))
    # retranslateUi

