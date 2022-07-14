# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ventanaActualizarProveedor.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_ActualizarProveedor(object):
    def setupUi(self, ActualizarProveedor):
        if not ActualizarProveedor.objectName():
            ActualizarProveedor.setObjectName(u"ActualizarProveedor")
        ActualizarProveedor.resize(400, 300)
        ActualizarProveedor.setMaximumSize(QSize(400, 300))
        ActualizarProveedor.setStyleSheet(u"background-color: #555;")
        self.lbl_nombre = QLabel(ActualizarProveedor)
        self.lbl_nombre.setObjectName(u"lbl_nombre")
        self.lbl_nombre.setGeometry(QRect(30, 100, 91, 21))
        self.lbl_nombre.setStyleSheet(u"color: balck;\n"
"font: 900 12pt \"Arial\";")
        self.lbl_telefono = QLabel(ActualizarProveedor)
        self.lbl_telefono.setObjectName(u"lbl_telefono")
        self.lbl_telefono.setGeometry(QRect(30, 140, 81, 21))
        self.lbl_telefono.setStyleSheet(u"color: balck;\n"
"font: 900 12pt \"Arial\";")
        self.lbl_empresa = QLabel(ActualizarProveedor)
        self.lbl_empresa.setObjectName(u"lbl_empresa")
        self.lbl_empresa.setGeometry(QRect(30, 60, 91, 21))
        self.lbl_empresa.setStyleSheet(u"color: balck;\n"
"font: 900 12pt \"Arial\";")
        self.txt_telefono = QLineEdit(ActualizarProveedor)
        self.txt_telefono.setObjectName(u"txt_telefono")
        self.txt_telefono.setGeometry(QRect(120, 140, 261, 20))
        self.txt_telefono.setStyleSheet(u"color: black;\n"
"font: 75 10pt \"Arial\";\n"
"border: 1px solid white;\n"
"border-radius: 5px;\n"
"background-color: white;")
        self.lbl_email = QLabel(ActualizarProveedor)
        self.lbl_email.setObjectName(u"lbl_email")
        self.lbl_email.setGeometry(QRect(30, 180, 61, 21))
        self.lbl_email.setStyleSheet(u"color: balck;\n"
"font: 900 12pt \"Arial\";")
        self.txt_empresa = QLineEdit(ActualizarProveedor)
        self.txt_empresa.setObjectName(u"txt_empresa")
        self.txt_empresa.setGeometry(QRect(120, 60, 261, 20))
        self.txt_empresa.setStyleSheet(u"color: black;\n"
"font: 75 10pt \"Arial\";\n"
"border: 1px solid white;\n"
"border-radius: 5px;\n"
"background-color: white;")
        self.txt_email = QLineEdit(ActualizarProveedor)
        self.txt_email.setObjectName(u"txt_email")
        self.txt_email.setGeometry(QRect(120, 180, 261, 20))
        self.txt_email.setStyleSheet(u"color: black;\n"
"font: 75 10pt \"Arial\";\n"
"border: 1px solid white;\n"
"border-radius: 5px;\n"
"background-color: white;")
        self.lbl_clave = QLabel(ActualizarProveedor)
        self.lbl_clave.setObjectName(u"lbl_clave")
        self.lbl_clave.setGeometry(QRect(30, 20, 71, 21))
        self.lbl_clave.setStyleSheet(u"color: balck;\n"
"font: 900 12pt \"Arial\";")
        self.txt_clave = QLineEdit(ActualizarProveedor)
        self.txt_clave.setObjectName(u"txt_clave")
        self.txt_clave.setGeometry(QRect(120, 20, 261, 20))
        self.txt_clave.setStyleSheet(u"color: black;\n"
"font: 75 10pt \"Arial\";\n"
"border: 1px solid white;\n"
"border-radius: 5px;\n"
"background-color: white;")
        self.txt_nombre = QLineEdit(ActualizarProveedor)
        self.txt_nombre.setObjectName(u"txt_nombre")
        self.txt_nombre.setGeometry(QRect(120, 100, 261, 20))
        self.txt_nombre.setStyleSheet(u"color: black;\n"
"font: 75 10pt \"Arial\";\n"
"border: 1px solid white;\n"
"border-radius: 5px;\n"
"background-color: white;")
        self.txt_nombre.setEchoMode(QLineEdit.Normal)
        self.btn_actualizar_proveedor = QPushButton(ActualizarProveedor)
        self.btn_actualizar_proveedor.setObjectName(u"btn_actualizar_proveedor")
        self.btn_actualizar_proveedor.setGeometry(QRect(270, 250, 111, 41))
        self.btn_actualizar_proveedor.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_actualizar_proveedor.setStyleSheet(u"QObject{\n"
"	color:White;\n"
"	font: 900 12pt \"Arial\";\n"
"	background-color: #666;\n"
"	border-radius: 5px;\n"
"}\n"
"QObject:hover{\n"
"	background-color: #222;\n"
"}")

        self.retranslateUi(ActualizarProveedor)

        QMetaObject.connectSlotsByName(ActualizarProveedor)
    # setupUi

    def retranslateUi(self, ActualizarProveedor):
        ActualizarProveedor.setWindowTitle(QCoreApplication.translate("ActualizarProveedor", u"Actualizar Proveedor", None))
        self.lbl_nombre.setText(QCoreApplication.translate("ActualizarProveedor", u"Nombre:", None))
        self.lbl_telefono.setText(QCoreApplication.translate("ActualizarProveedor", u"Telefono:", None))
        self.lbl_empresa.setText(QCoreApplication.translate("ActualizarProveedor", u"Empresa:", None))
        self.txt_telefono.setText("")
        self.lbl_email.setText(QCoreApplication.translate("ActualizarProveedor", u"Email:", None))
        self.txt_empresa.setText("")
        self.lbl_clave.setText(QCoreApplication.translate("ActualizarProveedor", u"Clave:", None))
        self.btn_actualizar_proveedor.setText(QCoreApplication.translate("ActualizarProveedor", u"Actualizar", None))
    # retranslateUi

