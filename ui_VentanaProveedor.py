# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'VentanaProveedor.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Ventana_Proveedores(object):
    def setupUi(self, Ventana_Proveedores):
        if not Ventana_Proveedores.objectName():
            Ventana_Proveedores.setObjectName(u"Ventana_Proveedores")
        Ventana_Proveedores.resize(760, 470)
        Ventana_Proveedores.setMaximumSize(QSize(760, 470))
        self.centralwidget = QWidget(Ventana_Proveedores)
        self.centralwidget.setObjectName(u"centralwidget")
        self.txt_nombre_proveedor = QLineEdit(self.centralwidget)
        self.txt_nombre_proveedor.setObjectName(u"txt_nombre_proveedor")
        self.txt_nombre_proveedor.setGeometry(QRect(280, 120, 311, 21))
        self.txt_nombre_proveedor.setStyleSheet(u"color: black;\n"
"font: 75 10pt \"Arial\";\n"
"border: 1px solid white;\n"
"border-radius: 5px;\n"
"background-color: white;")
        self.btn_agregar_proveedor = QPushButton(self.centralwidget)
        self.btn_agregar_proveedor.setObjectName(u"btn_agregar_proveedor")
        self.btn_agregar_proveedor.setGeometry(QRect(30, 240, 111, 31))
        self.btn_agregar_proveedor.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_agregar_proveedor.setStyleSheet(u"QObject{\n"
"	color:White;\n"
"	background-color: #666;\n"
"	border-radius: 5px;\n"
"}\n"
"QObject:hover{\n"
"	background-color: #222;\n"
"}")
        self.lbl_ingrese_nombre = QLabel(self.centralwidget)
        self.lbl_ingrese_nombre.setObjectName(u"lbl_ingrese_nombre")
        self.lbl_ingrese_nombre.setGeometry(QRect(190, 120, 81, 20))
        self.btn_actualizar_proveedor = QPushButton(self.centralwidget)
        self.btn_actualizar_proveedor.setObjectName(u"btn_actualizar_proveedor")
        self.btn_actualizar_proveedor.setGeometry(QRect(30, 310, 111, 31))
        self.btn_actualizar_proveedor.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_actualizar_proveedor.setStyleSheet(u"QObject{\n"
"	color:White;\n"
"	background-color: #666;\n"
"	border-radius: 5px;\n"
"}\n"
"QObject:hover{\n"
"	background-color: #222;\n"
"}")
        self.btn_buscar_proveedor = QPushButton(self.centralwidget)
        self.btn_buscar_proveedor.setObjectName(u"btn_buscar_proveedor")
        self.btn_buscar_proveedor.setGeometry(QRect(600, 120, 91, 23))
        self.btn_buscar_proveedor.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_buscar_proveedor.setStyleSheet(u"QObject{\n"
"	color:White;\n"
"	background-color: #666;\n"
"	border-radius: 5px;\n"
"}\n"
"QObject:hover{\n"
"	background-color: #222;\n"
"}")
        self.frame_content = QFrame(self.centralwidget)
        self.frame_content.setObjectName(u"frame_content")
        self.frame_content.setGeometry(QRect(-5, 0, 771, 81))
        self.frame_content.setStyleSheet(u"QObject{\n"
"	background-color: #555;\n"
"}")
        self.frame_content.setFrameShape(QFrame.StyledPanel)
        self.frame_content.setFrameShadow(QFrame.Raised)
        self.lbl_logo_2 = QLabel(self.frame_content)
        self.lbl_logo_2.setObjectName(u"lbl_logo_2")
        self.lbl_logo_2.setGeometry(QRect(0, -50, 271, 151))
        self.lbl_logo_2.setPixmap(QPixmap(u"../../../Downloads/rocky-linux-icon.png"))
        self.lbl_titulo_2 = QLabel(self.frame_content)
        self.lbl_titulo_2.setObjectName(u"lbl_titulo_2")
        self.lbl_titulo_2.setGeometry(QRect(300, 20, 331, 41))
        font = QFont()
        font.setFamily(u"Arial Black")
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(99)
        self.lbl_titulo_2.setFont(font)
        self.lbl_titulo_2.setStyleSheet(u"QObject{\n"
"	font: 900 18pt \"Arial Black\";\n"
"}")
        self.btn_atras = QPushButton(self.frame_content)
        self.btn_atras.setObjectName(u"btn_atras")
        self.btn_atras.setGeometry(QRect(680, 30, 71, 20))
        self.btn_atras.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_atras.setStyleSheet(u"QObject{\n"
"	color:White;\n"
"	background-color: #666;\n"
"	border-radius: 5px;\n"
"}\n"
"QObject:hover{\n"
"	background-color: #222;\n"
"}")
        icon = QIcon()
        icon.addFile(u"../../../Downloads/productos.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_atras.setIcon(icon)
        self.lbl_error_buscador = QLabel(self.centralwidget)
        self.lbl_error_buscador.setObjectName(u"lbl_error_buscador")
        self.lbl_error_buscador.setGeometry(QRect(205, 150, 311, 20))
        self.lbl_error_buscador.setStyleSheet(u"font: 87 9pt \"Arial Black\";")
        self.btn_eliminar_proveedor = QPushButton(self.centralwidget)
        self.btn_eliminar_proveedor.setObjectName(u"btn_eliminar_proveedor")
        self.btn_eliminar_proveedor.setGeometry(QRect(30, 370, 111, 31))
        self.btn_eliminar_proveedor.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_eliminar_proveedor.setStyleSheet(u"QObject{\n"
"	color:White;\n"
"	background-color: #666;\n"
"	border-radius: 5px;\n"
"}\n"
"QObject:hover{\n"
"	background-color: #222;\n"
"}")
        self.btn_mostrar_proveedor = QPushButton(self.centralwidget)
        self.btn_mostrar_proveedor.setObjectName(u"btn_mostrar_proveedor")
        self.btn_mostrar_proveedor.setGeometry(QRect(30, 180, 111, 31))
        self.btn_mostrar_proveedor.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_mostrar_proveedor.setStyleSheet(u"QObject{\n"
"	color:White;\n"
"	background-color: #666;\n"
"	border-radius: 5px;\n"
"}\n"
"QObject:hover{\n"
"	background-color: #222;\n"
"}")
        self.tableWidget_proveedores = QTableWidget(self.centralwidget)
        if (self.tableWidget_proveedores.columnCount() < 5):
            self.tableWidget_proveedores.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget_proveedores.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget_proveedores.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget_proveedores.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget_proveedores.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget_proveedores.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.tableWidget_proveedores.setObjectName(u"tableWidget_proveedores")
        self.tableWidget_proveedores.setGeometry(QRect(190, 180, 501, 231))
        self.btn_facturar = QPushButton(self.centralwidget)
        self.btn_facturar.setObjectName(u"btn_facturar")
        self.btn_facturar.setGeometry(QRect(30, 120, 111, 31))
        self.btn_facturar.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_facturar.setStyleSheet(u"QObject{\n"
"	color: black;\n"
"	background-color: #ccc;\n"
"	border-radius: 5px;\n"
"}\n"
"QObject:hover{\n"
"	background-color: yellow;\n"
"}")
        Ventana_Proveedores.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(Ventana_Proveedores)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 760, 21))
        Ventana_Proveedores.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(Ventana_Proveedores)
        self.statusbar.setObjectName(u"statusbar")
        Ventana_Proveedores.setStatusBar(self.statusbar)

        self.retranslateUi(Ventana_Proveedores)

        QMetaObject.connectSlotsByName(Ventana_Proveedores)
    # setupUi

    def retranslateUi(self, Ventana_Proveedores):
        Ventana_Proveedores.setWindowTitle(QCoreApplication.translate("Ventana_Proveedores", u"Ventana Proveedores", None))
        self.btn_agregar_proveedor.setText(QCoreApplication.translate("Ventana_Proveedores", u"Agregar Proveedor", None))
        self.lbl_ingrese_nombre.setText(QCoreApplication.translate("Ventana_Proveedores", u"Buscar Proveedor", None))
        self.btn_actualizar_proveedor.setText(QCoreApplication.translate("Ventana_Proveedores", u"Actualizar Proveedor", None))
        self.btn_buscar_proveedor.setText(QCoreApplication.translate("Ventana_Proveedores", u"Buscar", None))
        self.lbl_logo_2.setText("")
        self.lbl_titulo_2.setText(QCoreApplication.translate("Ventana_Proveedores", u"Proveedores", None))
        self.btn_atras.setText("")
        self.lbl_error_buscador.setText("")
        self.btn_eliminar_proveedor.setText(QCoreApplication.translate("Ventana_Proveedores", u"Eliminar Proveedor", None))
        self.btn_mostrar_proveedor.setText(QCoreApplication.translate("Ventana_Proveedores", u"Mostrar Proveedor", None))
        ___qtablewidgetitem = self.tableWidget_proveedores.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Ventana_Proveedores", u"Codigo", None));
        ___qtablewidgetitem1 = self.tableWidget_proveedores.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Ventana_Proveedores", u"Empresa", None));
        ___qtablewidgetitem2 = self.tableWidget_proveedores.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Ventana_Proveedores", u"NombrePoveedor", None));
        ___qtablewidgetitem3 = self.tableWidget_proveedores.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Ventana_Proveedores", u"Telefono", None));
        ___qtablewidgetitem4 = self.tableWidget_proveedores.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Ventana_Proveedores", u"Correo", None));
        self.btn_facturar.setText(QCoreApplication.translate("Ventana_Proveedores", u"Generar Factura", None))
    # retranslateUi

