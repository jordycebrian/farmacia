# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'contenido.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(761, 481)
        Form.setMinimumSize(QSize(761, 481))
        Form.setMaximumSize(QSize(761, 481))
        Form.setSizeIncrement(QSize(0, 0))
        Form.setStyleSheet(u"QObject{\n"
"	background-color: #ccc;\n"
"}")
        self.frame_content = QFrame(Form)
        self.frame_content.setObjectName(u"frame_content")
        self.frame_content.setGeometry(QRect(0, 0, 771, 81))
        self.frame_content.setStyleSheet(u"QObject{\n"
"	background-color: #555;\n"
"}")
        self.frame_content.setFrameShape(QFrame.StyledPanel)
        self.frame_content.setFrameShadow(QFrame.Raised)
        self.btn_back = QPushButton(self.frame_content)
        self.btn_back.setObjectName(u"btn_back")
        self.btn_back.setGeometry(QRect(720, 0, 51, 21))
        self.btn_back.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_back.setStyleSheet(u"QObject{\n"
"	background-color: #fff;\n"
"}")
        icon = QIcon()
        icon.addFile(u"../../../Downloads/productos.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_back.setIcon(icon)
        self.lbl_logo = QLabel(self.frame_content)
        self.lbl_logo.setObjectName(u"lbl_logo")
        self.lbl_logo.setGeometry(QRect(0, -50, 271, 151))
        self.lbl_logo.setPixmap(QPixmap(u"../../../Downloads/rocky-linux-icon.png"))
        self.lbl_titulo = QLabel(self.frame_content)
        self.lbl_titulo.setObjectName(u"lbl_titulo")
        self.lbl_titulo.setGeometry(QRect(300, 20, 261, 31))
        font = QFont()
        font.setFamily(u"Arial Black")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.lbl_titulo.setFont(font)
        self.lbl_titulo.setStyleSheet(u"QObject{\n"
"+\n"
"	font: 900 14pt \"Arial Black\";\n"
"}")
        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(10, 130, 161, 291))
        self.frame.setStyleSheet(u"QObject{\n"
"	background-color: #555;\n"
"	border: 1px solid white;\n"
"	border-radius:5px;\n"
"}")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.lbl_ventas = QLabel(self.frame)
        self.lbl_ventas.setObjectName(u"lbl_ventas")
        self.lbl_ventas.setGeometry(QRect(10, 20, 101, 21))
        self.lbl_ventas.setStyleSheet(u"QObject{\n"
"	color: white;\n"
"	font: 87 12pt \"Arial Black\";\n"
"	border: 1px solid #555;\n"
"}")
        self.btn_ventas = QPushButton(self.frame)
        self.btn_ventas.setObjectName(u"btn_ventas")
        self.btn_ventas.setGeometry(QRect(10, 50, 141, 141))
        self.btn_ventas.setCursor(QCursor(Qt.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u"img/ventas.jpg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_ventas.setIcon(icon1)
        self.btn_ventas.setIconSize(QSize(220, 220))
        self.frame_3 = QFrame(Form)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(390, 130, 161, 291))
        self.frame_3.setStyleSheet(u"QObject{\n"
"	background-color: #555;\n"
"	border: 1px solid white;\n"
"	border-radius:5px;\n"
"}")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.lbl_provedor = QLabel(self.frame_3)
        self.lbl_provedor.setObjectName(u"lbl_provedor")
        self.lbl_provedor.setGeometry(QRect(10, 20, 111, 21))
        self.lbl_provedor.setStyleSheet(u"QObject{\n"
"	color: white;\n"
"	font: 87 12pt \"Arial Black\";\n"
"	border: 1px solid #555;\n"
"}")
        self.btn_provedores = QPushButton(self.frame_3)
        self.btn_provedores.setObjectName(u"btn_provedores")
        self.btn_provedores.setGeometry(QRect(10, 60, 141, 141))
        self.btn_provedores.setCursor(QCursor(Qt.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u"img/provedores.jpg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_provedores.setIcon(icon2)
        self.btn_provedores.setIconSize(QSize(220, 220))
        self.frame_4 = QFrame(Form)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setGeometry(QRect(580, 130, 161, 291))
        self.frame_4.setStyleSheet(u"QObject{\n"
"	background-color: #555;\n"
"	border: 1px solid white;\n"
"	border-radius:5px;\n"
"}")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.lbl_invercion = QLabel(self.frame_4)
        self.lbl_invercion.setObjectName(u"lbl_invercion")
        self.lbl_invercion.setGeometry(QRect(10, 20, 111, 21))
        self.lbl_invercion.setStyleSheet(u"QObject{\n"
"	color: white;\n"
"	font: 87 12pt \"Arial Black\";\n"
"	border: 1px solid #555;\n"
"}")
        self.btn_invercion = QPushButton(self.frame_4)
        self.btn_invercion.setObjectName(u"btn_invercion")
        self.btn_invercion.setGeometry(QRect(10, 60, 141, 141))
        self.btn_invercion.setCursor(QCursor(Qt.PointingHandCursor))
        icon3 = QIcon()
        icon3.addFile(u"img/invercion.jpg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_invercion.setIcon(icon3)
        self.btn_invercion.setIconSize(QSize(220, 220))
        self.frame_2 = QFrame(Form)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(200, 130, 161, 291))
        self.frame_2.setStyleSheet(u"QObject{\n"
"	background-color: #555;\n"
"	border: 1px solid white;\n"
"	border-radius:5px;\n"
"}")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.lbl_productos = QLabel(self.frame_2)
        self.lbl_productos.setObjectName(u"lbl_productos")
        self.lbl_productos.setGeometry(QRect(10, 20, 101, 21))
        self.lbl_productos.setStyleSheet(u"QObject{\n"
"	color: white;\n"
"	font: 87 12pt \"Arial Black\";\n"
"	border: 1px solid #555;\n"
"}")
        self.brn_productos = QPushButton(self.frame_2)
        self.brn_productos.setObjectName(u"brn_productos")
        self.brn_productos.setGeometry(QRect(10, 60, 141, 141))
        self.brn_productos.setCursor(QCursor(Qt.PointingHandCursor))
        icon4 = QIcon()
        icon4.addFile(u"img/products.jpg", QSize(), QIcon.Normal, QIcon.Off)
        self.brn_productos.setIcon(icon4)
        self.brn_productos.setIconSize(QSize(220, 220))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Contenido", None))
        self.btn_back.setText("")
        self.lbl_logo.setText("")
        self.lbl_titulo.setText(QCoreApplication.translate("Form", u"Farmacia ParacetaAmor", None))
        self.lbl_ventas.setText(QCoreApplication.translate("Form", u"Ventas", None))
        self.btn_ventas.setText("")
        self.lbl_provedor.setText(QCoreApplication.translate("Form", u"Provedores", None))
        self.btn_provedores.setText("")
        self.lbl_invercion.setText(QCoreApplication.translate("Form", u"Inverci\u00f3n", None))
        self.btn_invercion.setText("")
        self.lbl_productos.setText(QCoreApplication.translate("Form", u"Productos", None))
        self.brn_productos.setText("")
    # retranslateUi

