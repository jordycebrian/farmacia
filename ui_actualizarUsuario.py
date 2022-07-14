# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'actualizarUsuario.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Form_actualizar_usuario(object):
    def setupUi(self, Form_actualizar_usuario):
        if not Form_actualizar_usuario.objectName():
            Form_actualizar_usuario.setObjectName(u"Form_actualizar_usuario")
        Form_actualizar_usuario.resize(381, 322)
        Form_actualizar_usuario.setMaximumSize(QSize(381, 323))
        Form_actualizar_usuario.setStyleSheet(u"background-color: #555;")
        self.txt_email = QLineEdit(Form_actualizar_usuario)
        self.txt_email.setObjectName(u"txt_email")
        self.txt_email.setGeometry(QRect(150, 140, 211, 20))
        self.txt_email.setStyleSheet(u"color: black;\n"
"font: 75 10pt \"Arial\";\n"
"border: 1px solid white;\n"
"border-radius: 5px;\n"
"background-color: white;")
        self.lbl_descripcion = QLabel(Form_actualizar_usuario)
        self.lbl_descripcion.setObjectName(u"lbl_descripcion")
        self.lbl_descripcion.setGeometry(QRect(20, 220, 121, 21))
        self.lbl_descripcion.setStyleSheet(u"color: balck;\n"
"font: 900 12pt \"Arial\";")
        self.lbl_email = QLabel(Form_actualizar_usuario)
        self.lbl_email.setObjectName(u"lbl_email")
        self.lbl_email.setGeometry(QRect(20, 140, 61, 21))
        self.lbl_email.setStyleSheet(u"color: balck;\n"
"font: 900 12pt \"Arial\";")
        self.txt_clave = QLineEdit(Form_actualizar_usuario)
        self.txt_clave.setObjectName(u"txt_clave")
        self.txt_clave.setGeometry(QRect(150, 20, 211, 20))
        self.txt_clave.setStyleSheet(u"color: black;\n"
"font: 75 10pt \"Arial\";\n"
"border: 1px solid white;\n"
"border-radius: 5px;\n"
"background-color: white;")
        self.txt_contrasena = QLineEdit(Form_actualizar_usuario)
        self.txt_contrasena.setObjectName(u"txt_contrasena")
        self.txt_contrasena.setGeometry(QRect(150, 100, 211, 20))
        self.txt_contrasena.setStyleSheet(u"color: black;\n"
"font: 75 10pt \"Arial\";\n"
"border: 1px solid white;\n"
"border-radius: 5px;\n"
"background-color: white;")
        self.txt_contrasena.setEchoMode(QLineEdit.Password)
        self.txt_descripcion = QLineEdit(Form_actualizar_usuario)
        self.txt_descripcion.setObjectName(u"txt_descripcion")
        self.txt_descripcion.setGeometry(QRect(150, 220, 211, 20))
        self.txt_descripcion.setStyleSheet(u"color: black;\n"
"font: 75 10pt \"Arial\";\n"
"border: 1px solid white;\n"
"border-radius: 5px;\n"
"background-color: white;")
        self.txt_puesto = QLineEdit(Form_actualizar_usuario)
        self.txt_puesto.setObjectName(u"txt_puesto")
        self.txt_puesto.setGeometry(QRect(150, 180, 211, 20))
        self.txt_puesto.setStyleSheet(u"color: black;\n"
"font: 75 10pt \"Arial\";\n"
"border: 1px solid white;\n"
"border-radius: 5px;\n"
"background-color: white;")
        self.btn_actualizar_usuarios = QPushButton(Form_actualizar_usuario)
        self.btn_actualizar_usuarios.setObjectName(u"btn_actualizar_usuarios")
        self.btn_actualizar_usuarios.setGeometry(QRect(250, 260, 111, 31))
        self.btn_actualizar_usuarios.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_actualizar_usuarios.setStyleSheet(u"QObject{\n"
"	color:White;\n"
"	font: 900 12pt \"Arial\";\n"
"	background-color: #666;\n"
"	border-radius: 5px;\n"
"}\n"
"QObject:hover{\n"
"	background-color: #222;\n"
"}")
        self.lbl_contrasena = QLabel(Form_actualizar_usuario)
        self.lbl_contrasena.setObjectName(u"lbl_contrasena")
        self.lbl_contrasena.setGeometry(QRect(20, 100, 111, 21))
        self.lbl_contrasena.setStyleSheet(u"color: balck;\n"
"font: 900 12pt \"Arial\";")
        self.lbl_puesto = QLabel(Form_actualizar_usuario)
        self.lbl_puesto.setObjectName(u"lbl_puesto")
        self.lbl_puesto.setGeometry(QRect(20, 180, 71, 21))
        self.lbl_puesto.setStyleSheet(u"color: balck;\n"
"font: 900 12pt \"Arial\";")
        self.txt_nombre = QLineEdit(Form_actualizar_usuario)
        self.txt_nombre.setObjectName(u"txt_nombre")
        self.txt_nombre.setGeometry(QRect(150, 60, 211, 20))
        self.txt_nombre.setStyleSheet(u"color: black;\n"
"font: 75 10pt \"Arial\";\n"
"border: 1px solid white;\n"
"border-radius: 5px;\n"
"background-color: white;")
        self.lbl_clave = QLabel(Form_actualizar_usuario)
        self.lbl_clave.setObjectName(u"lbl_clave")
        self.lbl_clave.setGeometry(QRect(20, 20, 61, 21))
        self.lbl_clave.setStyleSheet(u"color: balck;\n"
"font: 900 12pt \"Arial\";")
        self.lbl_nombre = QLabel(Form_actualizar_usuario)
        self.lbl_nombre.setObjectName(u"lbl_nombre")
        self.lbl_nombre.setGeometry(QRect(20, 60, 81, 21))
        self.lbl_nombre.setStyleSheet(u"color: balck;\n"
"font: 900 12pt \"Arial\";")

        self.retranslateUi(Form_actualizar_usuario)

        QMetaObject.connectSlotsByName(Form_actualizar_usuario)
    # setupUi

    def retranslateUi(self, Form_actualizar_usuario):
        Form_actualizar_usuario.setWindowTitle(QCoreApplication.translate("Form_actualizar_usuario", u"Actualizar Usuario", None))
        self.txt_email.setText("")
        self.lbl_descripcion.setText(QCoreApplication.translate("Form_actualizar_usuario", u"Descripci\u00f3n:", None))
        self.lbl_email.setText(QCoreApplication.translate("Form_actualizar_usuario", u"Email:", None))
        self.txt_descripcion.setText("")
        self.btn_actualizar_usuarios.setText(QCoreApplication.translate("Form_actualizar_usuario", u"Actualizar", None))
        self.lbl_contrasena.setText(QCoreApplication.translate("Form_actualizar_usuario", u"Contrase\u00f1a:", None))
        self.lbl_puesto.setText(QCoreApplication.translate("Form_actualizar_usuario", u"Puesto:", None))
        self.txt_nombre.setText("")
        self.lbl_clave.setText(QCoreApplication.translate("Form_actualizar_usuario", u"Clave:", None))
        self.lbl_nombre.setText(QCoreApplication.translate("Form_actualizar_usuario", u"Nombre:", None))
    # retranslateUi

