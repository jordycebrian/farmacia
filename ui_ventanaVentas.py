# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ventanaVentas.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_ventanaVentas(object):
    def setupUi(self, ventanaVentas):
        if not ventanaVentas.objectName():
            ventanaVentas.setObjectName(u"ventanaVentas")
        ventanaVentas.resize(762, 566)
        ventanaVentas.setCursor(QCursor(Qt.ArrowCursor))
        self.centralwidget = QWidget(ventanaVentas)
        self.centralwidget.setObjectName(u"centralwidget")
        self.txt_clave_producto = QLineEdit(self.centralwidget)
        self.txt_clave_producto.setObjectName(u"txt_clave_producto")
        self.txt_clave_producto.setGeometry(QRect(190, 130, 111, 31))
        self.txt_clave_producto.setStyleSheet(u"color: black;\n"
"font: 75 10pt \"Arial\";\n"
"border: 1px solid white;\n"
"border-radius: 5px;\n"
"background-color: white;")
        self.frame_content = QFrame(self.centralwidget)
        self.frame_content.setObjectName(u"frame_content")
        self.frame_content.setGeometry(QRect(-5, 0, 771, 81))
        self.frame_content.setStyleSheet(u"QObject{\n"
"	background-color: #555;\n"
"}")
        self.frame_content.setFrameShape(QFrame.StyledPanel)
        self.frame_content.setFrameShadow(QFrame.Raised)
        self.lbl_logo = QLabel(self.frame_content)
        self.lbl_logo.setObjectName(u"lbl_logo")
        self.lbl_logo.setGeometry(QRect(0, -50, 271, 151))
        self.lbl_logo.setPixmap(QPixmap(u"../../../Downloads/rocky-linux-icon.png"))
        self.lbl_titulo = QLabel(self.frame_content)
        self.lbl_titulo.setObjectName(u"lbl_titulo")
        self.lbl_titulo.setGeometry(QRect(280, 20, 311, 41))
        font = QFont()
        font.setFamily(u"Arial Black")
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(99)
        self.lbl_titulo.setFont(font)
        self.lbl_titulo.setStyleSheet(u"QObject{\n"
"	font: 900 18pt \"Arial Black\";\n"
"}")
        self.btn_back = QPushButton(self.frame_content)
        self.btn_back.setObjectName(u"btn_back")
        self.btn_back.setGeometry(QRect(680, 30, 71, 20))
        self.btn_back.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_back.setStyleSheet(u"QObject{\n"
"	color:White;\n"
"	background-color: #666;\n"
"	border-radius: 5px;\n"
"}\n"
"QObject:hover{\n"
"	background-color: #222;\n"
"}")
        icon = QIcon()
        icon.addFile(u"../../../Downloads/productos.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_back.setIcon(icon)
        self.tableWidget_ventas = QTableWidget(self.centralwidget)
        if (self.tableWidget_ventas.columnCount() < 5):
            self.tableWidget_ventas.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget_ventas.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget_ventas.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget_ventas.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget_ventas.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget_ventas.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.tableWidget_ventas.setObjectName(u"tableWidget_ventas")
        self.tableWidget_ventas.setGeometry(QRect(250, 220, 501, 241))
        self.lbl_clave_producto = QLabel(self.centralwidget)
        self.lbl_clave_producto.setObjectName(u"lbl_clave_producto")
        self.lbl_clave_producto.setGeometry(QRect(30, 130, 121, 31))
        self.lbl_clave_producto.setStyleSheet(u"font: 10pt \"Arial\";")
        self.lbl_cantidad = QLabel(self.centralwidget)
        self.lbl_cantidad.setObjectName(u"lbl_cantidad")
        self.lbl_cantidad.setGeometry(QRect(350, 130, 61, 31))
        self.lbl_cantidad.setStyleSheet(u"font: 10pt \"Arial\";")
        self.txt_cantidad = QLineEdit(self.centralwidget)
        self.txt_cantidad.setObjectName(u"txt_cantidad")
        self.txt_cantidad.setGeometry(QRect(450, 130, 151, 31))
        self.txt_cantidad.setStyleSheet(u"color: black;\n"
"font: 75 10pt \"Arial\";\n"
"border: 1px solid white;\n"
"border-radius: 5px;\n"
"background-color: white;")
        self.lbl_usuario = QLabel(self.centralwidget)
        self.lbl_usuario.setObjectName(u"lbl_usuario")
        self.lbl_usuario.setGeometry(QRect(30, 490, 61, 20))
        self.lbl_usuario.setStyleSheet(u"font: 10pt \"Arial\";")
        self.lbl_mostrarUsuario = QLabel(self.centralwidget)
        self.lbl_mostrarUsuario.setObjectName(u"lbl_mostrarUsuario")
        self.lbl_mostrarUsuario.setGeometry(QRect(90, 490, 61, 20))
        self.lbl_mostrarUsuario.setStyleSheet(u"font: 10pt \"Arial\";")
        self.lbl_hora = QLabel(self.centralwidget)
        self.lbl_hora.setObjectName(u"lbl_hora")
        self.lbl_hora.setGeometry(QRect(660, 490, 91, 20))
        self.lbl_hora.setStyleSheet(u"font: 10pt \"Arial\";")
        self.lbl_fecha = QLabel(self.centralwidget)
        self.lbl_fecha.setObjectName(u"lbl_fecha")
        self.lbl_fecha.setGeometry(QRect(660, 90, 91, 20))
        self.lbl_fecha.setStyleSheet(u"font: 10pt \"Arial\";")
        self.lbl_total = QLabel(self.centralwidget)
        self.lbl_total.setObjectName(u"lbl_total")
        self.lbl_total.setGeometry(QRect(10, 250, 71, 51))
        self.lbl_total.setStyleSheet(u"font: 20pt \"Arial\";")
        self.txt_total = QLineEdit(self.centralwidget)
        self.txt_total.setObjectName(u"txt_total")
        self.txt_total.setGeometry(QRect(110, 260, 131, 41))
        self.txt_total.setStyleSheet(u"color: black;\n"
"font: 75 10pt \"Arial\";\n"
"border: 1px solid white;\n"
"border-radius: 5px;\n"
"background-color: white;")
        self.lbl_pago = QLabel(self.centralwidget)
        self.lbl_pago.setObjectName(u"lbl_pago")
        self.lbl_pago.setGeometry(QRect(10, 320, 81, 41))
        self.lbl_pago.setStyleSheet(u"font: 20pt \"Arial\";")
        self.txt_pago = QLineEdit(self.centralwidget)
        self.txt_pago.setObjectName(u"txt_pago")
        self.txt_pago.setGeometry(QRect(110, 320, 131, 41))
        self.txt_pago.setStyleSheet(u"color: black;\n"
"font: 75 10pt \"Arial\";\n"
"border: 1px solid white;\n"
"border-radius: 5px;\n"
"background-color: white;")
        self.txt_cambio = QLineEdit(self.centralwidget)
        self.txt_cambio.setObjectName(u"txt_cambio")
        self.txt_cambio.setGeometry(QRect(110, 380, 131, 41))
        self.txt_cambio.setStyleSheet(u"color: black;\n"
"font: 75 10pt \"Arial\";\n"
"border: 1px solid white;\n"
"border-radius: 5px;\n"
"background-color: white;")
        self.lbl_cambio = QLabel(self.centralwidget)
        self.lbl_cambio.setObjectName(u"lbl_cambio")
        self.lbl_cambio.setGeometry(QRect(0, 380, 101, 41))
        self.lbl_cambio.setStyleSheet(u"font: 20pt \"Arial\";")
        self.btn_agregar_producto = QPushButton(self.centralwidget)
        self.btn_agregar_producto.setObjectName(u"btn_agregar_producto")
        self.btn_agregar_producto.setGeometry(QRect(620, 150, 121, 31))
        self.btn_agregar_producto.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_agregar_producto.setStyleSheet(u"QObject{\n"
"	color:White;\n"
"	background-color: #666;\n"
"	border-radius: 5px;\n"
"}\n"
"QObject:hover{\n"
"	background-color: #222;\n"
"}")
        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(0, 470, 761, 20))
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.line_2 = QFrame(self.centralwidget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setGeometry(QRect(0, 110, 761, 20))
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)
        self.txt_precio = QLineEdit(self.centralwidget)
        self.txt_precio.setObjectName(u"txt_precio")
        self.txt_precio.setGeometry(QRect(450, 170, 151, 31))
        self.txt_precio.setStyleSheet(u"color: black;\n"
"font: 75 10pt \"Arial\";\n"
"border: 1px solid white;\n"
"border-radius: 5px;\n"
"background-color: white;")
        self.lbl_precio = QLabel(self.centralwidget)
        self.lbl_precio.setObjectName(u"lbl_precio")
        self.lbl_precio.setGeometry(QRect(350, 170, 51, 31))
        self.lbl_precio.setStyleSheet(u"font: 10pt \"Arial\";")
        self.txt_nombre_producto = QLineEdit(self.centralwidget)
        self.txt_nombre_producto.setObjectName(u"txt_nombre_producto")
        self.txt_nombre_producto.setGeometry(QRect(190, 170, 111, 31))
        self.txt_nombre_producto.setStyleSheet(u"color: black;\n"
"font: 75 10pt \"Arial\";\n"
"border: 1px solid white;\n"
"border-radius: 5px;\n"
"background-color: white;")
        self.lbl_nombre_producto = QLabel(self.centralwidget)
        self.lbl_nombre_producto.setObjectName(u"lbl_nombre_producto")
        self.lbl_nombre_producto.setGeometry(QRect(30, 170, 121, 31))
        self.lbl_nombre_producto.setStyleSheet(u"font: 10pt \"Arial\";")
        self.btn_cobrar = QPushButton(self.centralwidget)
        self.btn_cobrar.setObjectName(u"btn_cobrar")
        self.btn_cobrar.setGeometry(QRect(70, 430, 121, 31))
        self.btn_cobrar.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_cobrar.setStyleSheet(u"QObject{\n"
"	color:White;\n"
"	background-color: #666;\n"
"	border-radius: 5px;\n"
"}\n"
"QObject:hover{\n"
"	background-color: #222;\n"
"}")
        ventanaVentas.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(ventanaVentas)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 762, 21))
        ventanaVentas.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(ventanaVentas)
        self.statusbar.setObjectName(u"statusbar")
        ventanaVentas.setStatusBar(self.statusbar)

        self.retranslateUi(ventanaVentas)

        QMetaObject.connectSlotsByName(ventanaVentas)
    # setupUi

    def retranslateUi(self, ventanaVentas):
        ventanaVentas.setWindowTitle(QCoreApplication.translate("ventanaVentas", u"Ventas", None))
        self.txt_clave_producto.setText("")
        self.lbl_logo.setText("")
        self.lbl_titulo.setText(QCoreApplication.translate("ventanaVentas", u"FarmaciaParacetamor", None))
        self.btn_back.setText("")
        ___qtablewidgetitem = self.tableWidget_ventas.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("ventanaVentas", u"Codigo", None));
        ___qtablewidgetitem1 = self.tableWidget_ventas.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("ventanaVentas", u"Producto", None));
        ___qtablewidgetitem2 = self.tableWidget_ventas.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("ventanaVentas", u"Precio", None));
        ___qtablewidgetitem3 = self.tableWidget_ventas.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("ventanaVentas", u"Cantidad", None));
        ___qtablewidgetitem4 = self.tableWidget_ventas.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("ventanaVentas", u"Total", None));
        self.lbl_clave_producto.setText(QCoreApplication.translate("ventanaVentas", u"Codigo de producto:", None))
        self.lbl_cantidad.setText(QCoreApplication.translate("ventanaVentas", u"Cantidad:", None))
        self.lbl_usuario.setText(QCoreApplication.translate("ventanaVentas", u"Usuario->", None))
        self.lbl_mostrarUsuario.setText(QCoreApplication.translate("ventanaVentas", u"Jordy", None))
        self.lbl_hora.setText("")
        self.lbl_fecha.setText("")
        self.lbl_total.setText(QCoreApplication.translate("ventanaVentas", u"Total:", None))
        self.lbl_pago.setText(QCoreApplication.translate("ventanaVentas", u"Pago:", None))
        self.txt_cambio.setText("")
        self.lbl_cambio.setText(QCoreApplication.translate("ventanaVentas", u"Cambio:", None))
        self.btn_agregar_producto.setText(QCoreApplication.translate("ventanaVentas", u"Agregar", None))
        self.txt_precio.setText("")
        self.lbl_precio.setText(QCoreApplication.translate("ventanaVentas", u"Precio:", None))
        self.txt_nombre_producto.setText("")
        self.lbl_nombre_producto.setText(QCoreApplication.translate("ventanaVentas", u"Nombre del Producto", None))
        self.btn_cobrar.setText(QCoreApplication.translate("ventanaVentas", u"Cobrar", None))
    # retranslateUi

