# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ventanaBorrarProveedor.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_ventanaBorrarProveedor(object):
    def setupUi(self, ventanaBorrarProveedor):
        if not ventanaBorrarProveedor.objectName():
            ventanaBorrarProveedor.setObjectName(u"ventanaBorrarProveedor")
        ventanaBorrarProveedor.resize(320, 240)
        ventanaBorrarProveedor.setMaximumSize(QSize(320, 240))
        ventanaBorrarProveedor.setStyleSheet(u"background-color:#555;")
        self.btn_borrar_proveedor = QPushButton(ventanaBorrarProveedor)
        self.btn_borrar_proveedor.setObjectName(u"btn_borrar_proveedor")
        self.btn_borrar_proveedor.setGeometry(QRect(80, 150, 161, 31))
        self.btn_borrar_proveedor.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_borrar_proveedor.setStyleSheet(u"QObject{\n"
"	color:White;\n"
"	background-color: #666;\n"
"	border-radius: 5px;\n"
"}\n"
"QObject:hover{\n"
"	background-color: #222;\n"
"}")
        self.label_manejo_error = QLabel(ventanaBorrarProveedor)
        self.label_manejo_error.setObjectName(u"label_manejo_error")
        self.label_manejo_error.setGeometry(QRect(20, 120, 281, 21))
        self.label_manejo_error.setStyleSheet(u"font: 75 italic 10pt \"Arial\";")
        self.label_borrar = QLabel(ventanaBorrarProveedor)
        self.label_borrar.setObjectName(u"label_borrar")
        self.label_borrar.setGeometry(QRect(10, 20, 291, 41))
        self.label_borrar.setStyleSheet(u"\n"
"font: 900 10pt \"Aria-black\";")
        self.txt_borrar_proveedor = QLineEdit(ventanaBorrarProveedor)
        self.txt_borrar_proveedor.setObjectName(u"txt_borrar_proveedor")
        self.txt_borrar_proveedor.setGeometry(QRect(70, 80, 181, 21))
        self.txt_borrar_proveedor.setStyleSheet(u"color: black;\n"
"font: 75 10pt \"Arial\";\n"
"border: 1px solid white;\n"
"border-radius: 5px;\n"
"background-color: white;")

        self.retranslateUi(ventanaBorrarProveedor)

        QMetaObject.connectSlotsByName(ventanaBorrarProveedor)
    # setupUi

    def retranslateUi(self, ventanaBorrarProveedor):
        ventanaBorrarProveedor.setWindowTitle(QCoreApplication.translate("ventanaBorrarProveedor", u"Borrar Proveedor", None))
        self.btn_borrar_proveedor.setText(QCoreApplication.translate("ventanaBorrarProveedor", u"Borrar", None))
        self.label_manejo_error.setText("")
        self.label_borrar.setText(QCoreApplication.translate("ventanaBorrarProveedor", u"Introduce la clave para borrar el proveedor:", None))
    # retranslateUi

