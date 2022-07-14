# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'registro.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Form_Registro(object):
    def setupUi(self, Form_Registro):
        if not Form_Registro.objectName():
            Form_Registro.setObjectName(u"Form_Registro")
        Form_Registro.resize(320, 222)
        Form_Registro.setMaximumSize(QSize(320, 222))
        Form_Registro.setStyleSheet(u"background-color: #555;")
        self.btn_login_registro = QPushButton(Form_Registro)
        self.btn_login_registro.setObjectName(u"btn_login_registro")
        self.btn_login_registro.setGeometry(QRect(70, 170, 181, 21))
        self.btn_login_registro.setStyleSheet(u"QObject{\n"
"	color:White;\n"
"	background-color: #666;\n"
"	border-radius: 5px;\n"
"}\n"
"QObject:hover{\n"
"	background-color: #222;\n"
"}")
        self.lbl_user_registro = QLabel(Form_Registro)
        self.lbl_user_registro.setObjectName(u"lbl_user_registro")
        self.lbl_user_registro.setGeometry(QRect(10, 50, 71, 21))
        self.lbl_user_registro.setStyleSheet(u"color:White;\n"
"font: 75 10pt \"Arial\";")
        self.txt_user_regsitro = QLineEdit(Form_Registro)
        self.txt_user_regsitro.setObjectName(u"txt_user_regsitro")
        self.txt_user_regsitro.setGeometry(QRect(90, 50, 211, 20))
        self.txt_user_regsitro.setStyleSheet(u"color: black;\n"
"font: 75 10pt \"Arial\";\n"
"border: 1px solid white;\n"
"border-radius: 5px;\n"
"background-color: white;")
        self.lbl_password_registro = QLabel(Form_Registro)
        self.lbl_password_registro.setObjectName(u"lbl_password_registro")
        self.lbl_password_registro.setGeometry(QRect(10, 90, 71, 31))
        self.lbl_password_registro.setStyleSheet(u"color:White;\n"
"font: 75 10pt \"Arial\";")
        self.txt_password_registro = QLineEdit(Form_Registro)
        self.txt_password_registro.setObjectName(u"txt_password_registro")
        self.txt_password_registro.setGeometry(QRect(90, 100, 211, 20))
        self.txt_password_registro.setStyleSheet(u"color: black;\n"
"font: 75 10pt \"Arial\";\n"
"border: 1px solid white;\n"
"border-radius: 5px;\n"
"background-color: white;")
        self.txt_password_registro.setEchoMode(QLineEdit.Password)
        self.btn_incio = QPushButton(Form_Registro)
        self.btn_incio.setObjectName(u"btn_incio")
        self.btn_incio.setGeometry(QRect(250, 10, 61, 20))
        self.btn_incio.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_incio.setStyleSheet(u"QObject{\n"
"	color:White;\n"
"	background-color: #666;\n"
"	border-radius: 5px;\n"
"}\n"
"QObject:hover{\n"
"	background-color: #222;\n"
"}")
        self.label_error = QLabel(Form_Registro)
        self.label_error.setObjectName(u"label_error")
        self.label_error.setGeometry(QRect(40, 140, 261, 20))
        self.label_error.setStyleSheet(u"color: black;")

        self.retranslateUi(Form_Registro)

        QMetaObject.connectSlotsByName(Form_Registro)
    # setupUi

    def retranslateUi(self, Form_Registro):
        Form_Registro.setWindowTitle(QCoreApplication.translate("Form_Registro", u"Registro", None))
        self.btn_login_registro.setText(QCoreApplication.translate("Form_Registro", u"LOGIN", None))
        self.lbl_user_registro.setText(QCoreApplication.translate("Form_Registro", u"Usuario", None))
        self.lbl_password_registro.setText(QCoreApplication.translate("Form_Registro", u"Contrase\u00f1a", None))
        self.txt_password_registro.setText("")
        self.btn_incio.setText(QCoreApplication.translate("Form_Registro", u"Inicio", None))
        self.label_error.setText("")
    # retranslateUi

