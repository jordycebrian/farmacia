# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ventanaEliminarFactura.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_VenatanaEliminarFactura(object):
    def setupUi(self, VenatanaEliminarFactura):
        if not VenatanaEliminarFactura.objectName():
            VenatanaEliminarFactura.setObjectName(u"VenatanaEliminarFactura")
        VenatanaEliminarFactura.resize(299, 179)
        VenatanaEliminarFactura.setStyleSheet(u"background-color:#555;")
        self.btn_borrar_factura = QPushButton(VenatanaEliminarFactura)
        self.btn_borrar_factura.setObjectName(u"btn_borrar_factura")
        self.btn_borrar_factura.setGeometry(QRect(70, 130, 161, 31))
        self.btn_borrar_factura.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_borrar_factura.setStyleSheet(u"QObject{\n"
"	color:White;\n"
"	background-color: #666;\n"
"	border-radius: 5px;\n"
"}\n"
"QObject:hover{\n"
"	background-color: #222;\n"
"}")
        self.txt_borrar_factura = QLineEdit(VenatanaEliminarFactura)
        self.txt_borrar_factura.setObjectName(u"txt_borrar_factura")
        self.txt_borrar_factura.setGeometry(QRect(60, 60, 181, 21))
        self.txt_borrar_factura.setStyleSheet(u"color: black;\n"
"font: 75 10pt \"Arial\";\n"
"border: 1px solid white;\n"
"border-radius: 5px;\n"
"background-color: white;")
        self.label_manejo_error = QLabel(VenatanaEliminarFactura)
        self.label_manejo_error.setObjectName(u"label_manejo_error")
        self.label_manejo_error.setGeometry(QRect(10, 100, 281, 21))
        self.label_manejo_error.setStyleSheet(u"font: 75 italic 10pt \"Arial\";")
        self.label_borrar = QLabel(VenatanaEliminarFactura)
        self.label_borrar.setObjectName(u"label_borrar")
        self.label_borrar.setGeometry(QRect(20, 0, 261, 41))
        self.label_borrar.setStyleSheet(u"\n"
"font: 900 10pt \"Aria-black\";")

        self.retranslateUi(VenatanaEliminarFactura)

        QMetaObject.connectSlotsByName(VenatanaEliminarFactura)
    # setupUi

    def retranslateUi(self, VenatanaEliminarFactura):
        VenatanaEliminarFactura.setWindowTitle(QCoreApplication.translate("VenatanaEliminarFactura", u"Eliminar Factura", None))
        self.btn_borrar_factura.setText(QCoreApplication.translate("VenatanaEliminarFactura", u"Borrar", None))
        self.label_manejo_error.setText("")
        self.label_borrar.setText(QCoreApplication.translate("VenatanaEliminarFactura", u"Introduce la clave para borrar el usurio:", None))
    # retranslateUi

