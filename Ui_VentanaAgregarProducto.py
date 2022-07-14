# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'VentanaAgregarProducto.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_AgregarProducto(object):
    def setupUi(self, AgregarProducto):
        if not AgregarProducto.objectName():
            AgregarProducto.setObjectName(u"AgregarProducto")
        AgregarProducto.resize(600, 350)
        AgregarProducto.setMaximumSize(QSize(600, 350))
        AgregarProducto.setStyleSheet(u"background-color:#555;")
        self.lbl_codigo = QLabel(AgregarProducto)
        self.lbl_codigo.setObjectName(u"lbl_codigo")
        self.lbl_codigo.setGeometry(QRect(20, 30, 61, 21))
        self.lbl_codigo.setStyleSheet(u"color: balck;\n"
"font: 900 12pt \"Arial\";")
        self.txt_nombre = QLineEdit(AgregarProducto)
        self.txt_nombre.setObjectName(u"txt_nombre")
        self.txt_nombre.setGeometry(QRect(150, 110, 211, 20))
        self.txt_nombre.setStyleSheet(u"color: black;\n"
"font: 75 10pt \"Arial\";\n"
"border: 1px solid white;\n"
"border-radius: 5px;\n"
"background-color: white;")
        self.txt_nombre.setEchoMode(QLineEdit.Normal)
        self.txt_caducidad = QLineEdit(AgregarProducto)
        self.txt_caducidad.setObjectName(u"txt_caducidad")
        self.txt_caducidad.setGeometry(QRect(150, 190, 211, 20))
        self.txt_caducidad.setStyleSheet(u"color: black;\n"
"font: 75 10pt \"Arial\";\n"
"border: 1px solid white;\n"
"border-radius: 5px;\n"
"background-color: white;")
        self.txt_clave = QLineEdit(AgregarProducto)
        self.txt_clave.setObjectName(u"txt_clave")
        self.txt_clave.setGeometry(QRect(150, 30, 211, 20))
        self.txt_clave.setStyleSheet(u"color: black;\n"
"font: 75 10pt \"Arial\";\n"
"border: 1px solid white;\n"
"border-radius: 5px;\n"
"background-color: white;")
        self.lbl_caducidad = QLabel(AgregarProducto)
        self.lbl_caducidad.setObjectName(u"lbl_caducidad")
        self.lbl_caducidad.setGeometry(QRect(20, 190, 131, 21))
        self.lbl_caducidad.setStyleSheet(u"color: balck;\n"
"font: 900 12pt \"Arial\";")
        self.lbl_lote = QLabel(AgregarProducto)
        self.lbl_lote.setObjectName(u"lbl_lote")
        self.lbl_lote.setGeometry(QRect(20, 230, 121, 21))
        self.lbl_lote.setStyleSheet(u"color: balck;\n"
"font: 900 12pt \"Arial\";")
        self.lbl_precio = QLabel(AgregarProducto)
        self.lbl_precio.setObjectName(u"lbl_precio")
        self.lbl_precio.setGeometry(QRect(20, 150, 61, 21))
        self.lbl_precio.setStyleSheet(u"color: balck;\n"
"font: 900 12pt \"Arial\";")
        self.txt_lote = QLineEdit(AgregarProducto)
        self.txt_lote.setObjectName(u"txt_lote")
        self.txt_lote.setGeometry(QRect(150, 230, 211, 20))
        self.txt_lote.setStyleSheet(u"color: black;\n"
"font: 75 10pt \"Arial\";\n"
"border: 1px solid white;\n"
"border-radius: 5px;\n"
"background-color: white;")
        self.btn_agregar_producto = QPushButton(AgregarProducto)
        self.btn_agregar_producto.setObjectName(u"btn_agregar_producto")
        self.btn_agregar_producto.setGeometry(QRect(260, 310, 111, 31))
        self.btn_agregar_producto.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_agregar_producto.setStyleSheet(u"QObject{\n"
"	color:White;\n"
"	font: 900 12pt \"Arial\";\n"
"	background-color: #666;\n"
"	border-radius: 5px;\n"
"}\n"
"QObject:hover{\n"
"	background-color: #222;\n"
"}")
        self.lbl_tipo = QLabel(AgregarProducto)
        self.lbl_tipo.setObjectName(u"lbl_tipo")
        self.lbl_tipo.setGeometry(QRect(20, 70, 81, 21))
        self.lbl_tipo.setStyleSheet(u"color: balck;\n"
"font: 900 12pt \"Arial\";")
        self.txt_precio = QLineEdit(AgregarProducto)
        self.txt_precio.setObjectName(u"txt_precio")
        self.txt_precio.setGeometry(QRect(150, 150, 211, 20))
        self.txt_precio.setStyleSheet(u"color: black;\n"
"font: 75 10pt \"Arial\";\n"
"border: 1px solid white;\n"
"border-radius: 5px;\n"
"background-color: white;")
        self.lbl_nombre = QLabel(AgregarProducto)
        self.lbl_nombre.setObjectName(u"lbl_nombre")
        self.lbl_nombre.setGeometry(QRect(20, 110, 111, 21))
        self.lbl_nombre.setStyleSheet(u"color: balck;\n"
"font: 900 12pt \"Arial\";")
        self.txt_tipo = QLineEdit(AgregarProducto)
        self.txt_tipo.setObjectName(u"txt_tipo")
        self.txt_tipo.setGeometry(QRect(150, 70, 211, 20))
        self.txt_tipo.setStyleSheet(u"color: black;\n"
"font: 75 10pt \"Arial\";\n"
"border: 1px solid white;\n"
"border-radius: 5px;\n"
"background-color: white;")
        self.lbl_cantidad = QLabel(AgregarProducto)
        self.lbl_cantidad.setObjectName(u"lbl_cantidad")
        self.lbl_cantidad.setGeometry(QRect(20, 270, 121, 21))
        self.lbl_cantidad.setStyleSheet(u"color: balck;\n"
"font: 900 12pt \"Arial\";")
        self.txt_cantidad = QLineEdit(AgregarProducto)
        self.txt_cantidad.setObjectName(u"txt_cantidad")
        self.txt_cantidad.setGeometry(QRect(150, 270, 211, 20))
        self.txt_cantidad.setStyleSheet(u"color: black;\n"
"font: 75 10pt \"Arial\";\n"
"border: 1px solid white;\n"
"border-radius: 5px;\n"
"background-color: white;")
        self.lbl_imagen = QLabel(AgregarProducto)
        self.lbl_imagen.setObjectName(u"lbl_imagen")
        self.lbl_imagen.setGeometry(QRect(400, 80, 181, 181))
        self.lbl_imagen.setStyleSheet(u"border-radius:5px;\n"
"border: 3px solid white;")
        self.btn_insertar_imagen = QPushButton(AgregarProducto)
        self.btn_insertar_imagen.setObjectName(u"btn_insertar_imagen")
        self.btn_insertar_imagen.setGeometry(QRect(400, 30, 181, 31))
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

        self.retranslateUi(AgregarProducto)

        QMetaObject.connectSlotsByName(AgregarProducto)
    # setupUi

    def retranslateUi(self, AgregarProducto):
        AgregarProducto.setWindowTitle(QCoreApplication.translate("AgregarProducto", u"Agregar Poroducto", None))
        self.lbl_codigo.setText(QCoreApplication.translate("AgregarProducto", u"Codigo:", None))
        self.lbl_caducidad.setText(QCoreApplication.translate("AgregarProducto", u"Caducidadad:", None))
        self.lbl_lote.setText(QCoreApplication.translate("AgregarProducto", u"Lote:", None))
        self.lbl_precio.setText(QCoreApplication.translate("AgregarProducto", u"Precio:", None))
        self.txt_lote.setText("")
        self.btn_agregar_producto.setText(QCoreApplication.translate("AgregarProducto", u"Registrar", None))
        self.lbl_tipo.setText(QCoreApplication.translate("AgregarProducto", u"Tipo:", None))
        self.txt_precio.setText("")
        self.lbl_nombre.setText(QCoreApplication.translate("AgregarProducto", u"Nombre:", None))
        self.txt_tipo.setText("")
        self.lbl_cantidad.setText(QCoreApplication.translate("AgregarProducto", u"Cantidad:", None))
        self.txt_cantidad.setText("")
        self.lbl_imagen.setText("")
        self.btn_insertar_imagen.setText(QCoreApplication.translate("AgregarProducto", u"Insertar Imagen", None))
    # retranslateUi

