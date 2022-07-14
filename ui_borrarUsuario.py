# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'borrarUsuario.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Form_Eliminar(object):
    def setupUi(self, Form_Eliminar):
        if not Form_Eliminar.objectName():
            Form_Eliminar.setObjectName(u"Form_Eliminar")
        Form_Eliminar.resize(320, 240)
        Form_Eliminar.setMaximumSize(QSize(320, 240))
        Form_Eliminar.setStyleSheet(u"background-color:#555;")
        self.label_borrar = QLabel(Form_Eliminar)
        self.label_borrar.setObjectName(u"label_borrar")
        self.label_borrar.setGeometry(QRect(30, 40, 261, 41))
        self.label_borrar.setStyleSheet(u"\n"
"font: 900 10pt \"Aria-black\";")
        self.txt_borrar_usuario = QLineEdit(Form_Eliminar)
        self.txt_borrar_usuario.setObjectName(u"txt_borrar_usuario")
        self.txt_borrar_usuario.setGeometry(QRect(70, 100, 181, 21))
        self.txt_borrar_usuario.setStyleSheet(u"color: black;\n"
"font: 75 10pt \"Arial\";\n"
"border: 1px solid white;\n"
"border-radius: 5px;\n"
"background-color: white;")
        self.btn_borrar_usuario = QPushButton(Form_Eliminar)
        self.btn_borrar_usuario.setObjectName(u"btn_borrar_usuario")
        self.btn_borrar_usuario.setGeometry(QRect(80, 170, 161, 31))
        self.btn_borrar_usuario.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_borrar_usuario.setStyleSheet(u"QObject{\n"
"	color:White;\n"
"	background-color: #666;\n"
"	border-radius: 5px;\n"
"}\n"
"QObject:hover{\n"
"	background-color: #222;\n"
"}")
        self.label_manejo_error = QLabel(Form_Eliminar)
        self.label_manejo_error.setObjectName(u"label_manejo_error")
        self.label_manejo_error.setGeometry(QRect(20, 140, 281, 21))
        self.label_manejo_error.setStyleSheet(u"font: 75 italic 10pt \"Arial\";")

        self.retranslateUi(Form_Eliminar)

        QMetaObject.connectSlotsByName(Form_Eliminar)
    # setupUi

    def retranslateUi(self, Form_Eliminar):
        Form_Eliminar.setWindowTitle(QCoreApplication.translate("Form_Eliminar", u"Eliminar Usuario", None))
        self.label_borrar.setText(QCoreApplication.translate("Form_Eliminar", u"Introduce la clave para borrar el usurio:", None))
        self.btn_borrar_usuario.setText(QCoreApplication.translate("Form_Eliminar", u"Borrar", None))
        self.label_manejo_error.setText("")
    # retranslateUi

