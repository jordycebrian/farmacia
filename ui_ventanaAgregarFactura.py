# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ventanaAgregarFactura.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_ventanaAgregarFactura(object):
    def setupUi(self, ventanaAgregarFactura):
        if not ventanaAgregarFactura.objectName():
            ventanaAgregarFactura.setObjectName(u"ventanaAgregarFactura")
        ventanaAgregarFactura.resize(380, 320)
        ventanaAgregarFactura.setMaximumSize(QSize(380, 320))
        ventanaAgregarFactura.setStyleSheet(u"background-color:#555;")
        self.btn_agregar_factura = QPushButton(ventanaAgregarFactura)
        self.btn_agregar_factura.setObjectName(u"btn_agregar_factura")
        self.btn_agregar_factura.setGeometry(QRect(250, 260, 111, 41))
        self.btn_agregar_factura.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_agregar_factura.setStyleSheet(u"QObject{\n"
"	color:White;\n"
"	font: 900 12pt \"Arial\";\n"
"	background-color: #666;\n"
"	border-radius: 5px;\n"
"}\n"
"QObject:hover{\n"
"	background-color: #222;\n"
"}")
        self.lbl_clave = QLabel(ventanaAgregarFactura)
        self.lbl_clave.setObjectName(u"lbl_clave")
        self.lbl_clave.setGeometry(QRect(10, 30, 71, 21))
        self.lbl_clave.setStyleSheet(u"color: balck;\n"
"font: 900 12pt \"Arial\";")
        self.txt_empresa = QLineEdit(ventanaAgregarFactura)
        self.txt_empresa.setObjectName(u"txt_empresa")
        self.txt_empresa.setGeometry(QRect(100, 70, 261, 20))
        self.txt_empresa.setStyleSheet(u"color: black;\n"
"font: 75 10pt \"Arial\";\n"
"border: 1px solid white;\n"
"border-radius: 5px;\n"
"background-color: white;")
        self.lbl_calle = QLabel(ventanaAgregarFactura)
        self.lbl_calle.setObjectName(u"lbl_calle")
        self.lbl_calle.setGeometry(QRect(10, 150, 81, 21))
        self.lbl_calle.setStyleSheet(u"color: balck;\n"
"font: 900 12pt \"Arial\";")
        self.lbl_cantidad = QLabel(ventanaAgregarFactura)
        self.lbl_cantidad.setObjectName(u"lbl_cantidad")
        self.lbl_cantidad.setGeometry(QRect(10, 110, 91, 21))
        self.lbl_cantidad.setStyleSheet(u"color: balck;\n"
"font: 900 12pt \"Arial\";")
        self.txt_cantidad = QLineEdit(ventanaAgregarFactura)
        self.txt_cantidad.setObjectName(u"txt_cantidad")
        self.txt_cantidad.setGeometry(QRect(100, 110, 261, 20))
        self.txt_cantidad.setStyleSheet(u"color: black;\n"
"font: 75 10pt \"Arial\";\n"
"border: 1px solid white;\n"
"border-radius: 5px;\n"
"background-color: white;")
        self.txt_cantidad.setEchoMode(QLineEdit.Normal)
        self.lbl_colonia = QLabel(ventanaAgregarFactura)
        self.lbl_colonia.setObjectName(u"lbl_colonia")
        self.lbl_colonia.setGeometry(QRect(10, 190, 81, 21))
        self.lbl_colonia.setStyleSheet(u"color: balck;\n"
"font: 900 12pt \"Arial\";")
        self.txt_colonia = QLineEdit(ventanaAgregarFactura)
        self.txt_colonia.setObjectName(u"txt_colonia")
        self.txt_colonia.setGeometry(QRect(100, 190, 261, 20))
        self.txt_colonia.setStyleSheet(u"color: black;\n"
"font: 75 10pt \"Arial\";\n"
"border: 1px solid white;\n"
"border-radius: 5px;\n"
"background-color: white;")
        self.lbl_empresa = QLabel(ventanaAgregarFactura)
        self.lbl_empresa.setObjectName(u"lbl_empresa")
        self.lbl_empresa.setGeometry(QRect(10, 70, 91, 21))
        self.lbl_empresa.setStyleSheet(u"color: balck;\n"
"font: 900 12pt \"Arial\";")
        self.txt_calle = QLineEdit(ventanaAgregarFactura)
        self.txt_calle.setObjectName(u"txt_calle")
        self.txt_calle.setGeometry(QRect(100, 150, 261, 20))
        self.txt_calle.setStyleSheet(u"color: black;\n"
"font: 75 10pt \"Arial\";\n"
"border: 1px solid white;\n"
"border-radius: 5px;\n"
"background-color: white;")
        self.txt_clave = QLineEdit(ventanaAgregarFactura)
        self.txt_clave.setObjectName(u"txt_clave")
        self.txt_clave.setGeometry(QRect(100, 30, 261, 20))
        self.txt_clave.setStyleSheet(u"color: black;\n"
"font: 75 10pt \"Arial\";\n"
"border: 1px solid white;\n"
"border-radius: 5px;\n"
"background-color: white;")

        self.retranslateUi(ventanaAgregarFactura)

        QMetaObject.connectSlotsByName(ventanaAgregarFactura)
    # setupUi

    def retranslateUi(self, ventanaAgregarFactura):
        ventanaAgregarFactura.setWindowTitle(QCoreApplication.translate("ventanaAgregarFactura", u"Agregar Factura", None))
        self.btn_agregar_factura.setText(QCoreApplication.translate("ventanaAgregarFactura", u"Registrar", None))
        self.lbl_clave.setText(QCoreApplication.translate("ventanaAgregarFactura", u"Clave:", None))
        self.txt_empresa.setText("")
        self.lbl_calle.setText(QCoreApplication.translate("ventanaAgregarFactura", u"Calle:", None))
        self.lbl_cantidad.setText(QCoreApplication.translate("ventanaAgregarFactura", u"Cantidad:", None))
        self.lbl_colonia.setText(QCoreApplication.translate("ventanaAgregarFactura", u"Colonia:", None))
        self.lbl_empresa.setText(QCoreApplication.translate("ventanaAgregarFactura", u"Empresa:", None))
        self.txt_calle.setText("")
    # retranslateUi

