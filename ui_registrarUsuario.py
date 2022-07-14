# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'registrarUsuario.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Form_agregar_usuario(object):
    def setupUi(self, Form_agregar_usuario):
        if not Form_agregar_usuario.objectName():
            Form_agregar_usuario.setObjectName(u"Form_agregar_usuario")
        Form_agregar_usuario.resize(381, 323)
        Form_agregar_usuario.setMaximumSize(QSize(381, 323))
        Form_agregar_usuario.setStyleSheet(u"background-color: #555;")
        self.lbl_clave = QLabel(Form_agregar_usuario)
        self.lbl_clave.setObjectName(u"lbl_clave")
        self.lbl_clave.setGeometry(QRect(10, 40, 61, 21))
        self.lbl_clave.setStyleSheet(u"color: balck;\n"
"font: 900 12pt \"Arial\";")
        self.txt_clave = QLineEdit(Form_agregar_usuario)
        self.txt_clave.setObjectName(u"txt_clave")
        self.txt_clave.setGeometry(QRect(140, 40, 211, 20))
        self.txt_clave.setStyleSheet(u"color: black;\n"
"font: 75 10pt \"Arial\";\n"
"border: 1px solid white;\n"
"border-radius: 5px;\n"
"background-color: white;")
        self.txt_nombre = QLineEdit(Form_agregar_usuario)
        self.txt_nombre.setObjectName(u"txt_nombre")
        self.txt_nombre.setGeometry(QRect(140, 80, 211, 20))
        self.txt_nombre.setStyleSheet(u"color: black;\n"
"font: 75 10pt \"Arial\";\n"
"border: 1px solid white;\n"
"border-radius: 5px;\n"
"background-color: white;")
        self.lbl_nombre = QLabel(Form_agregar_usuario)
        self.lbl_nombre.setObjectName(u"lbl_nombre")
        self.lbl_nombre.setGeometry(QRect(10, 80, 81, 21))
        self.lbl_nombre.setStyleSheet(u"color: balck;\n"
"font: 900 12pt \"Arial\";")
        self.txt_contrasena = QLineEdit(Form_agregar_usuario)
        self.txt_contrasena.setObjectName(u"txt_contrasena")
        self.txt_contrasena.setGeometry(QRect(140, 120, 211, 20))
        self.txt_contrasena.setStyleSheet(u"color: black;\n"
"font: 75 10pt \"Arial\";\n"
"border: 1px solid white;\n"
"border-radius: 5px;\n"
"background-color: white;")
        self.txt_contrasena.setEchoMode(QLineEdit.Password)
        self.lbl_contrasena = QLabel(Form_agregar_usuario)
        self.lbl_contrasena.setObjectName(u"lbl_contrasena")
        self.lbl_contrasena.setGeometry(QRect(10, 120, 111, 21))
        self.lbl_contrasena.setStyleSheet(u"color: balck;\n"
"font: 900 12pt \"Arial\";")
        self.txt_email = QLineEdit(Form_agregar_usuario)
        self.txt_email.setObjectName(u"txt_email")
        self.txt_email.setGeometry(QRect(140, 160, 211, 20))
        self.txt_email.setStyleSheet(u"color: black;\n"
"font: 75 10pt \"Arial\";\n"
"border: 1px solid white;\n"
"border-radius: 5px;\n"
"background-color: white;")
        self.lbl_email = QLabel(Form_agregar_usuario)
        self.lbl_email.setObjectName(u"lbl_email")
        self.lbl_email.setGeometry(QRect(10, 160, 61, 21))
        self.lbl_email.setStyleSheet(u"color: balck;\n"
"font: 900 12pt \"Arial\";")
        self.txt_puesto = QLineEdit(Form_agregar_usuario)
        self.txt_puesto.setObjectName(u"txt_puesto")
        self.txt_puesto.setGeometry(QRect(140, 200, 211, 20))
        self.txt_puesto.setStyleSheet(u"color: black;\n"
"font: 75 10pt \"Arial\";\n"
"border: 1px solid white;\n"
"border-radius: 5px;\n"
"background-color: white;")
        self.lbl_puesto = QLabel(Form_agregar_usuario)
        self.lbl_puesto.setObjectName(u"lbl_puesto")
        self.lbl_puesto.setGeometry(QRect(10, 200, 71, 21))
        self.lbl_puesto.setStyleSheet(u"color: balck;\n"
"font: 900 12pt \"Arial\";")
        self.txt_descripcion = QLineEdit(Form_agregar_usuario)
        self.txt_descripcion.setObjectName(u"txt_descripcion")
        self.txt_descripcion.setGeometry(QRect(140, 240, 211, 20))
        self.txt_descripcion.setStyleSheet(u"color: black;\n"
"font: 75 10pt \"Arial\";\n"
"border: 1px solid white;\n"
"border-radius: 5px;\n"
"background-color: white;")
        self.lbl_descripcion = QLabel(Form_agregar_usuario)
        self.lbl_descripcion.setObjectName(u"lbl_descripcion")
        self.lbl_descripcion.setGeometry(QRect(10, 240, 121, 21))
        self.lbl_descripcion.setStyleSheet(u"color: balck;\n"
"font: 900 12pt \"Arial\";")
        self.btn_agregar_usuarios = QPushButton(Form_agregar_usuario)
        self.btn_agregar_usuarios.setObjectName(u"btn_agregar_usuarios")
        self.btn_agregar_usuarios.setGeometry(QRect(240, 280, 111, 31))
        self.btn_agregar_usuarios.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_agregar_usuarios.setStyleSheet(u"QObject{\n"
"	color:White;\n"
"	font: 900 12pt \"Arial\";\n"
"	background-color: #666;\n"
"	border-radius: 5px;\n"
"}\n"
"QObject:hover{\n"
"	background-color: #222;\n"
"}")

        self.retranslateUi(Form_agregar_usuario)

        QMetaObject.connectSlotsByName(Form_agregar_usuario)
    # setupUi

    def retranslateUi(self, Form_agregar_usuario):
        Form_agregar_usuario.setWindowTitle(QCoreApplication.translate("Form_agregar_usuario", u"Agregar Usuario", None))
        self.lbl_clave.setText(QCoreApplication.translate("Form_agregar_usuario", u"Clave:", None))
        self.txt_nombre.setText("")
        self.lbl_nombre.setText(QCoreApplication.translate("Form_agregar_usuario", u"Nombre:", None))
        self.lbl_contrasena.setText(QCoreApplication.translate("Form_agregar_usuario", u"Contrase\u00f1a:", None))
        self.txt_email.setText("")
        self.lbl_email.setText(QCoreApplication.translate("Form_agregar_usuario", u"Email:", None))
        self.lbl_puesto.setText(QCoreApplication.translate("Form_agregar_usuario", u"Puesto:", None))
        self.txt_descripcion.setText("")
        self.lbl_descripcion.setText(QCoreApplication.translate("Form_agregar_usuario", u"Descripci\u00f3n:", None))
        self.btn_agregar_usuarios.setText(QCoreApplication.translate("Form_agregar_usuario", u"Registrar", None))
    # retranslateUi

