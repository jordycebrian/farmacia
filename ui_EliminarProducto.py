# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'EliminarProducto.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_form_eliminar_producto(object):
    def setupUi(self, form_eliminar_producto):
        if not form_eliminar_producto.objectName():
            form_eliminar_producto.setObjectName(u"form_eliminar_producto")
        form_eliminar_producto.resize(320, 240)
        form_eliminar_producto.setMaximumSize(QSize(320, 240))
        form_eliminar_producto.setStyleSheet(u"background-color: #555;")
        self.label_manejo_error = QLabel(form_eliminar_producto)
        self.label_manejo_error.setObjectName(u"label_manejo_error")
        self.label_manejo_error.setGeometry(QRect(20, 120, 281, 21))
        self.label_manejo_error.setStyleSheet(u"font: 75 italic 10pt \"Arial\";")
        self.btn_borrar_producto = QPushButton(form_eliminar_producto)
        self.btn_borrar_producto.setObjectName(u"btn_borrar_producto")
        self.btn_borrar_producto.setGeometry(QRect(80, 150, 161, 31))
        self.btn_borrar_producto.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_borrar_producto.setStyleSheet(u"QObject{\n"
"	color:White;\n"
"	background-color: #666;\n"
"	border-radius: 5px;\n"
"}\n"
"QObject:hover{\n"
"	background-color: #222;\n"
"}")
        self.txt_borrar_producto = QLineEdit(form_eliminar_producto)
        self.txt_borrar_producto.setObjectName(u"txt_borrar_producto")
        self.txt_borrar_producto.setGeometry(QRect(70, 80, 181, 21))
        self.txt_borrar_producto.setStyleSheet(u"color: black;\n"
"font: 75 10pt \"Arial\";\n"
"border: 1px solid white;\n"
"border-radius: 5px;\n"
"background-color: white;")
        self.label_borrar = QLabel(form_eliminar_producto)
        self.label_borrar.setObjectName(u"label_borrar")
        self.label_borrar.setGeometry(QRect(10, 20, 291, 41))
        self.label_borrar.setStyleSheet(u"\n"
"font: 900 10pt \"Aria-black\";")

        self.retranslateUi(form_eliminar_producto)

        QMetaObject.connectSlotsByName(form_eliminar_producto)
    # setupUi

    def retranslateUi(self, form_eliminar_producto):
        form_eliminar_producto.setWindowTitle(QCoreApplication.translate("form_eliminar_producto", u"Eliminar Producto", None))
        self.label_manejo_error.setText("")
        self.btn_borrar_producto.setText(QCoreApplication.translate("form_eliminar_producto", u"Borrar", None))
        self.label_borrar.setText(QCoreApplication.translate("form_eliminar_producto", u"Introduce la clave para borrar el producto:", None))
    # retranslateUi

