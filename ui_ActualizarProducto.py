# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ventanaactualizarproducto.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_VentanaActualizarProducto(object):
    def setupUi(self, VentanaActualizarProducto):
        if not VentanaActualizarProducto.objectName():
            VentanaActualizarProducto.setObjectName(u"VentanaActualizarProducto")
        VentanaActualizarProducto.resize(600, 350)
        VentanaActualizarProducto.setMaximumSize(QSize(600, 350))
        VentanaActualizarProducto.setStyleSheet(u"background-color:#555;")
        self.txt_lote = QLineEdit(VentanaActualizarProducto)
        self.txt_lote.setObjectName(u"txt_lote")
        self.txt_lote.setGeometry(QRect(150, 220, 211, 20))
        self.txt_lote.setStyleSheet(u"color: black;\n"
"font: 75 10pt \"Arial\";\n"
"border: 1px solid white;\n"
"border-radius: 5px;\n"
"background-color: white;")
        self.lbl_nombre = QLabel(VentanaActualizarProducto)
        self.lbl_nombre.setObjectName(u"lbl_nombre")
        self.lbl_nombre.setGeometry(QRect(20, 100, 111, 21))
        self.lbl_nombre.setStyleSheet(u"color: balck;\n"
"font: 900 12pt \"Arial\";")
        self.btn_insertar_imagen = QPushButton(VentanaActualizarProducto)
        self.btn_insertar_imagen.setObjectName(u"btn_insertar_imagen")
        self.btn_insertar_imagen.setGeometry(QRect(400, 20, 181, 31))
        self.btn_insertar_imagen.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_insertar_imagen.setStyleSheet(u"QObject{\n"
"	color:White;\n"
"	font: 900 12pt \"Arial\";\n"
"	background-color: #666;\n"
"	border-radius: 5px;\n"
"}\n"
"QObject:hover{\n"
"	background-color: #222;\n"
"}")
        self.lbl_lote = QLabel(VentanaActualizarProducto)
        self.lbl_lote.setObjectName(u"lbl_lote")
        self.lbl_lote.setGeometry(QRect(20, 220, 121, 21))
        self.lbl_lote.setStyleSheet(u"color: balck;\n"
"font: 900 12pt \"Arial\";")
        self.txt_clave = QLineEdit(VentanaActualizarProducto)
        self.txt_clave.setObjectName(u"txt_clave")
        self.txt_clave.setGeometry(QRect(150, 20, 211, 20))
        self.txt_clave.setStyleSheet(u"color: black;\n"
"font: 75 10pt \"Arial\";\n"
"border: 1px solid white;\n"
"border-radius: 5px;\n"
"background-color: white;")
        self.lbl_cantidad = QLabel(VentanaActualizarProducto)
        self.lbl_cantidad.setObjectName(u"lbl_cantidad")
        self.lbl_cantidad.setGeometry(QRect(20, 260, 121, 21))
        self.lbl_cantidad.setStyleSheet(u"color: balck;\n"
"font: 900 12pt \"Arial\";")
        self.txt_cantidad = QLineEdit(VentanaActualizarProducto)
        self.txt_cantidad.setObjectName(u"txt_cantidad")
        self.txt_cantidad.setGeometry(QRect(150, 260, 211, 20))
        self.txt_cantidad.setStyleSheet(u"color: black;\n"
"font: 75 10pt \"Arial\";\n"
"border: 1px solid white;\n"
"border-radius: 5px;\n"
"background-color: white;")
        self.lbl_codigo = QLabel(VentanaActualizarProducto)
        self.lbl_codigo.setObjectName(u"lbl_codigo")
        self.lbl_codigo.setGeometry(QRect(20, 20, 61, 21))
        self.lbl_codigo.setStyleSheet(u"color: balck;\n"
"font: 900 12pt \"Arial\";")
        self.lbl_precio = QLabel(VentanaActualizarProducto)
        self.lbl_precio.setObjectName(u"lbl_precio")
        self.lbl_precio.setGeometry(QRect(20, 140, 61, 21))
        self.lbl_precio.setStyleSheet(u"color: balck;\n"
"font: 900 12pt \"Arial\";")
        self.lbl_tipo = QLabel(VentanaActualizarProducto)
        self.lbl_tipo.setObjectName(u"lbl_tipo")
        self.lbl_tipo.setGeometry(QRect(20, 60, 81, 21))
        self.lbl_tipo.setStyleSheet(u"color: balck;\n"
"font: 900 12pt \"Arial\";")
        self.lbl_imagen = QLabel(VentanaActualizarProducto)
        self.lbl_imagen.setObjectName(u"lbl_imagen")
        self.lbl_imagen.setGeometry(QRect(400, 70, 181, 181))
        self.lbl_imagen.setStyleSheet(u"border-radius:5px;\n"
"border: 3px solid white;")
        self.txt_nombre = QLineEdit(VentanaActualizarProducto)
        self.txt_nombre.setObjectName(u"txt_nombre")
        self.txt_nombre.setGeometry(QRect(150, 100, 211, 20))
        self.txt_nombre.setStyleSheet(u"color: black;\n"
"font: 75 10pt \"Arial\";\n"
"border: 1px solid white;\n"
"border-radius: 5px;\n"
"background-color: white;")
        self.txt_nombre.setEchoMode(QLineEdit.Normal)
        self.btn_actualizar_producto = QPushButton(VentanaActualizarProducto)
        self.btn_actualizar_producto.setObjectName(u"btn_actualizar_producto")
        self.btn_actualizar_producto.setGeometry(QRect(260, 300, 111, 31))
        self.btn_actualizar_producto.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_actualizar_producto.setStyleSheet(u"QObject{\n"
"	color:White;\n"
"	font: 900 12pt \"Arial\";\n"
"	background-color: #666;\n"
"	border-radius: 5px;\n"
"}\n"
"QObject:hover{\n"
"	background-color: #222;\n"
"}")
        self.txt_caducidad = QLineEdit(VentanaActualizarProducto)
        self.txt_caducidad.setObjectName(u"txt_caducidad")
        self.txt_caducidad.setGeometry(QRect(150, 180, 211, 20))
        self.txt_caducidad.setStyleSheet(u"color: black;\n"
"font: 75 10pt \"Arial\";\n"
"border: 1px solid white;\n"
"border-radius: 5px;\n"
"background-color: white;")
        self.lbl_caducidad = QLabel(VentanaActualizarProducto)
        self.lbl_caducidad.setObjectName(u"lbl_caducidad")
        self.lbl_caducidad.setGeometry(QRect(20, 180, 131, 21))
        self.lbl_caducidad.setStyleSheet(u"color: balck;\n"
"font: 900 12pt \"Arial\";")
        self.txt_precio = QLineEdit(VentanaActualizarProducto)
        self.txt_precio.setObjectName(u"txt_precio")
        self.txt_precio.setGeometry(QRect(150, 140, 211, 20))
        self.txt_precio.setStyleSheet(u"color: black;\n"
"font: 75 10pt \"Arial\";\n"
"border: 1px solid white;\n"
"border-radius: 5px;\n"
"background-color: white;")
        self.txt_tipo = QLineEdit(VentanaActualizarProducto)
        self.txt_tipo.setObjectName(u"txt_tipo")
        self.txt_tipo.setGeometry(QRect(150, 60, 211, 20))
        self.txt_tipo.setStyleSheet(u"color: black;\n"
"font: 75 10pt \"Arial\";\n"
"border: 1px solid white;\n"
"border-radius: 5px;\n"
"background-color: white;")

        self.retranslateUi(VentanaActualizarProducto)

        QMetaObject.connectSlotsByName(VentanaActualizarProducto)
    # setupUi

    def retranslateUi(self, VentanaActualizarProducto):
        VentanaActualizarProducto.setWindowTitle(QCoreApplication.translate("VentanaActualizarProducto", u"ActualizarProducto", None))
        self.txt_lote.setText("")
        self.lbl_nombre.setText(QCoreApplication.translate("VentanaActualizarProducto", u"Nombre:", None))
        self.btn_insertar_imagen.setText(QCoreApplication.translate("VentanaActualizarProducto", u"Insertar Imagen", None))
        self.lbl_lote.setText(QCoreApplication.translate("VentanaActualizarProducto", u"Lote:", None))
        self.lbl_cantidad.setText(QCoreApplication.translate("VentanaActualizarProducto", u"Cantidad:", None))
        self.txt_cantidad.setText("")
        self.lbl_codigo.setText(QCoreApplication.translate("VentanaActualizarProducto", u"Codigo:", None))
        self.lbl_precio.setText(QCoreApplication.translate("VentanaActualizarProducto", u"Precio:", None))
        self.lbl_tipo.setText(QCoreApplication.translate("VentanaActualizarProducto", u"Tipo:", None))
        self.lbl_imagen.setText("")
        self.btn_actualizar_producto.setText(QCoreApplication.translate("VentanaActualizarProducto", u"Actualizar", None))
        self.lbl_caducidad.setText(QCoreApplication.translate("VentanaActualizarProducto", u"Caducidadad:", None))
        self.txt_precio.setText("")
        self.txt_tipo.setText("")
    # retranslateUi

