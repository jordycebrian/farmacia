# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'RegistrarProveedor.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_RegistrarProveedor(object):
    def setupUi(self, RegistrarProveedor):
        if not RegistrarProveedor.objectName():
            RegistrarProveedor.setObjectName(u"RegistrarProveedor")
        RegistrarProveedor.resize(380, 320)
        RegistrarProveedor.setMaximumSize(QSize(380, 320))
        RegistrarProveedor.setStyleSheet(u"background-color: #555;")
        self.lbl_email = QLabel(RegistrarProveedor)
        self.lbl_email.setObjectName(u"lbl_email")
        self.lbl_email.setGeometry(QRect(10, 190, 61, 21))
        self.lbl_email.setStyleSheet(u"color: balck;\n"
"font: 900 12pt \"Arial\";")
        self.txt_empresa = QLineEdit(RegistrarProveedor)
        self.txt_empresa.setObjectName(u"txt_empresa")
        self.txt_empresa.setGeometry(QRect(100, 70, 261, 20))
        self.txt_empresa.setStyleSheet(u"color: black;\n"
"font: 75 10pt \"Arial\";\n"
"border: 1px solid white;\n"
"border-radius: 5px;\n"
"background-color: white;")
        self.txt_email = QLineEdit(RegistrarProveedor)
        self.txt_email.setObjectName(u"txt_email")
        self.txt_email.setGeometry(QRect(100, 190, 261, 20))
        self.txt_email.setStyleSheet(u"color: black;\n"
"font: 75 10pt \"Arial\";\n"
"border: 1px solid white;\n"
"border-radius: 5px;\n"
"background-color: white;")
        self.lbl_empresa = QLabel(RegistrarProveedor)
        self.lbl_empresa.setObjectName(u"lbl_empresa")
        self.lbl_empresa.setGeometry(QRect(10, 70, 91, 21))
        self.lbl_empresa.setStyleSheet(u"color: balck;\n"
"font: 900 12pt \"Arial\";")
        self.lbl_nombre = QLabel(RegistrarProveedor)
        self.lbl_nombre.setObjectName(u"lbl_nombre")
        self.lbl_nombre.setGeometry(QRect(10, 110, 91, 21))
        self.lbl_nombre.setStyleSheet(u"color: balck;\n"
"font: 900 12pt \"Arial\";")
        self.txt_telefono = QLineEdit(RegistrarProveedor)
        self.txt_telefono.setObjectName(u"txt_telefono")
        self.txt_telefono.setGeometry(QRect(100, 150, 261, 20))
        self.txt_telefono.setStyleSheet(u"color: black;\n"
"font: 75 10pt \"Arial\";\n"
"border: 1px solid white;\n"
"border-radius: 5px;\n"
"background-color: white;")
        self.lbl_telefono = QLabel(RegistrarProveedor)
        self.lbl_telefono.setObjectName(u"lbl_telefono")
        self.lbl_telefono.setGeometry(QRect(10, 150, 81, 21))
        self.lbl_telefono.setStyleSheet(u"color: balck;\n"
"font: 900 12pt \"Arial\";")
        self.txt_clave = QLineEdit(RegistrarProveedor)
        self.txt_clave.setObjectName(u"txt_clave")
        self.txt_clave.setGeometry(QRect(100, 30, 261, 20))
        self.txt_clave.setStyleSheet(u"color: black;\n"
"font: 75 10pt \"Arial\";\n"
"border: 1px solid white;\n"
"border-radius: 5px;\n"
"background-color: white;")
        self.lbl_clave = QLabel(RegistrarProveedor)
        self.lbl_clave.setObjectName(u"lbl_clave")
        self.lbl_clave.setGeometry(QRect(10, 30, 71, 21))
        self.lbl_clave.setStyleSheet(u"color: balck;\n"
"font: 900 12pt \"Arial\";")
        self.txt_nombre = QLineEdit(RegistrarProveedor)
        self.txt_nombre.setObjectName(u"txt_nombre")
        self.txt_nombre.setGeometry(QRect(100, 110, 261, 20))
        self.txt_nombre.setStyleSheet(u"color: black;\n"
"font: 75 10pt \"Arial\";\n"
"border: 1px solid white;\n"
"border-radius: 5px;\n"
"background-color: white;")
        self.txt_nombre.setEchoMode(QLineEdit.Normal)
        self.btn_agregar_proveedor = QPushButton(RegistrarProveedor)
        self.btn_agregar_proveedor.setObjectName(u"btn_agregar_proveedor")
        self.btn_agregar_proveedor.setGeometry(QRect(250, 260, 111, 41))
        self.btn_agregar_proveedor.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_agregar_proveedor.setStyleSheet(u"QObject{\n"
"	color:White;\n"
"	font: 900 12pt \"Arial\";\n"
"	background-color: #666;\n"
"	border-radius: 5px;\n"
"}\n"
"QObject:hover{\n"
"	background-color: #222;\n"
"}")

        self.retranslateUi(RegistrarProveedor)

        QMetaObject.connectSlotsByName(RegistrarProveedor)
    # setupUi

    def retranslateUi(self, RegistrarProveedor):
        RegistrarProveedor.setWindowTitle(QCoreApplication.translate("RegistrarProveedor", u"Registrar Proveedor", None))
        self.lbl_email.setText(QCoreApplication.translate("RegistrarProveedor", u"Email:", None))
        self.txt_empresa.setText("")
        self.lbl_empresa.setText(QCoreApplication.translate("RegistrarProveedor", u"Empresa:", None))
        self.lbl_nombre.setText(QCoreApplication.translate("RegistrarProveedor", u"Nombre:", None))
        self.txt_telefono.setText("")
        self.lbl_telefono.setText(QCoreApplication.translate("RegistrarProveedor", u"Telefono:", None))
        self.lbl_clave.setText(QCoreApplication.translate("RegistrarProveedor", u"Clave:", None))
        self.btn_agregar_proveedor.setText(QCoreApplication.translate("RegistrarProveedor", u"Registrar", None))
    # retranslateUi

