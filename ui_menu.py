# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'menu.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(641, 391)
        MainWindow.setMinimumSize(QSize(0, 0))
        MainWindow.setMaximumSize(QSize(641, 391))
        MainWindow.setBaseSize(QSize(0, 0))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setEnabled(True)
        self.frame.setGeometry(QRect(-20, -10, 661, 381))
        self.frame.setMinimumSize(QSize(661, 381))
        self.frame.setMaximumSize(QSize(661, 381))
        self.frame.setStyleSheet(u"QObject{\n"
"	background-color: #555;\n"
"}")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 10, 311, 381))
        self.label.setStyleSheet(u"QObject{\n"
"	background-color: white;\n"
"}")
        self.label.setPixmap(QPixmap(u"../../../Downloads/rocky-linux-icon.png"))
        self.lbl_titulo = QLabel(self.frame)
        self.lbl_titulo.setObjectName(u"lbl_titulo")
        self.lbl_titulo.setGeometry(QRect(420, 40, 151, 41))
        self.lbl_titulo.setStyleSheet(u"QObject{\n"
"	color: white;\n"
"	font: 900 19pt \"Arial\";\n"
"	\n"
"}")
        self.lbl_description = QLabel(self.frame)
        self.lbl_description.setObjectName(u"lbl_description")
        self.lbl_description.setGeometry(QRect(390, 90, 211, 31))
        self.lbl_description.setStyleSheet(u"color: white;\n"
"font: 700 10pt \"Arial\";")
        self.txt_user = QLineEdit(self.frame)
        self.txt_user.setObjectName(u"txt_user")
        self.txt_user.setGeometry(QRect(390, 180, 211, 20))
        self.txt_user.setStyleSheet(u"color: black;\n"
"font: 75 10pt \"Arial\";\n"
"background-color: white;\n"
"border-radius: 5px;\n"
"")
        self.lbl_user = QLabel(self.frame)
        self.lbl_user.setObjectName(u"lbl_user")
        self.lbl_user.setGeometry(QRect(390, 145, 51, 21))
        self.lbl_user.setStyleSheet(u"color:White;\n"
"font: 75 10pt \"Arial\";")
        self.lbl_password = QLabel(self.frame)
        self.lbl_password.setObjectName(u"lbl_password")
        self.lbl_password.setGeometry(QRect(390, 220, 71, 31))
        self.lbl_password.setStyleSheet(u"color:White;\n"
"font: 75 10pt \"Arial\";")
        self.txt_password = QLineEdit(self.frame)
        self.txt_password.setObjectName(u"txt_password")
        self.txt_password.setGeometry(QRect(390, 260, 211, 20))
        self.txt_password.setStyleSheet(u"color: black;\n"
"font: 75 10pt \"Arial\";\n"
"background-color: white;\n"
"border-radius: 5px;\n"
"")
        self.txt_password.setEchoMode(QLineEdit.Password)
        self.btn_login = QPushButton(self.frame)
        self.btn_login.setObjectName(u"btn_login")
        self.btn_login.setGeometry(QRect(390, 310, 75, 23))
        self.btn_login.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_login.setStyleSheet(u"QObject{\n"
"	color:White;\n"
"	background-color: #666;\n"
"	border-radius: 5px;\n"
"}\n"
"QObject:hover{\n"
"	background-color: #222;\n"
"}")
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(390, 290, 211, 16))
        self.label_2.setStyleSheet(u"color:White;\n"
"font: 75 10pt \"Arial\";")
        self.lbl_titulo_menu = QLabel(self.frame)
        self.lbl_titulo_menu.setObjectName(u"lbl_titulo_menu")
        self.lbl_titulo_menu.setGeometry(QRect(40, 30, 261, 31))
        font = QFont()
        font.setFamily(u"Arial Black")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(99)
        self.lbl_titulo_menu.setFont(font)
        self.lbl_titulo_menu.setStyleSheet(u"QObject{\n"
"	background-color: white;\n"
"	font: 900 14pt \"Arial Black\";\n"
"}")
        self.btn_registrar = QPushButton(self.frame)
        self.btn_registrar.setObjectName(u"btn_registrar")
        self.btn_registrar.setGeometry(QRect(520, 310, 81, 23))
        self.btn_registrar.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_registrar.setStyleSheet(u"QObject{\n"
"	color:White;\n"
"	background-color: #666;\n"
"	border-radius: 5px;\n"
"}\n"
"QObject:hover{\n"
"	background-color: #222;\n"
"}")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 641, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Men\u00fa", None))
        self.label.setText("")
        self.lbl_titulo.setText(QCoreApplication.translate("MainWindow", u"Bienvenido", None))
        self.lbl_description.setText(QCoreApplication.translate("MainWindow", u"Ingresa los datos para iniciar", None))
        self.lbl_user.setText(QCoreApplication.translate("MainWindow", u"Usuario", None))
        self.lbl_password.setText(QCoreApplication.translate("MainWindow", u"Contrase\u00f1a", None))
        self.txt_password.setText("")
        self.btn_login.setText(QCoreApplication.translate("MainWindow", u"LOGIN", None))
        self.label_2.setText("")
        self.lbl_titulo_menu.setText(QCoreApplication.translate("MainWindow", u"Farmacia ParacetaAmor", None))
        self.btn_registrar.setText(QCoreApplication.translate("MainWindow", u"REGISTRARSE", None))
    # retranslateUi

