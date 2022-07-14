# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ventanaProductos.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Ventana_Productos(object):
    def setupUi(self, Ventana_Productos):
        if not Ventana_Productos.objectName():
            Ventana_Productos.setObjectName(u"Ventana_Productos")
        Ventana_Productos.resize(759, 476)
        Ventana_Productos.setMaximumSize(QSize(759, 479))
        Ventana_Productos.setStyleSheet(u"")
        self.centralwidget = QWidget(Ventana_Productos)
        self.centralwidget.setObjectName(u"centralwidget")
        self.btn_mostrar_productos = QPushButton(self.centralwidget)
        self.btn_mostrar_productos.setObjectName(u"btn_mostrar_productos")
        self.btn_mostrar_productos.setGeometry(QRect(10, 160, 111, 31))
        self.btn_mostrar_productos.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_mostrar_productos.setStyleSheet(u"QObject{\n"
"	color:White;\n"
"	background-color: #666;\n"
"	border-radius: 5px;\n"
"}\n"
"QObject:hover{\n"
"	background-color: #222;\n"
"}")
        self.btn_agregar_producto = QPushButton(self.centralwidget)
        self.btn_agregar_producto.setObjectName(u"btn_agregar_producto")
        self.btn_agregar_producto.setGeometry(QRect(10, 220, 111, 31))
        self.btn_agregar_producto.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_agregar_producto.setStyleSheet(u"QObject{\n"
"	color:White;\n"
"	background-color: #666;\n"
"	border-radius: 5px;\n"
"}\n"
"QObject:hover{\n"
"	background-color: #222;\n"
"}")
        self.txt_clave_producto = QLineEdit(self.centralwidget)
        self.txt_clave_producto.setObjectName(u"txt_clave_producto")
        self.txt_clave_producto.setGeometry(QRect(210, 100, 321, 21))
        self.txt_clave_producto.setStyleSheet(u"color: black;\n"
"font: 75 10pt \"Arial\";\n"
"border: 1px solid white;\n"
"border-radius: 5px;\n"
"background-color: white;")
        self.btn_actualizar_prodcuto = QPushButton(self.centralwidget)
        self.btn_actualizar_prodcuto.setObjectName(u"btn_actualizar_prodcuto")
        self.btn_actualizar_prodcuto.setGeometry(QRect(10, 290, 111, 31))
        self.btn_actualizar_prodcuto.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_actualizar_prodcuto.setStyleSheet(u"QObject{\n"
"	color:White;\n"
"	background-color: #666;\n"
"	border-radius: 5px;\n"
"}\n"
"QObject:hover{\n"
"	background-color: #222;\n"
"}")
        self.lbl_ingrese_nombre = QLabel(self.centralwidget)
        self.lbl_ingrese_nombre.setObjectName(u"lbl_ingrese_nombre")
        self.lbl_ingrese_nombre.setGeometry(QRect(210, 80, 211, 20))
        self.tableWidget_producto = QTableWidget(self.centralwidget)
        if (self.tableWidget_producto.columnCount() < 8):
            self.tableWidget_producto.setColumnCount(8)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget_producto.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget_producto.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget_producto.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget_producto.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget_producto.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget_producto.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget_producto.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget_producto.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        self.tableWidget_producto.setObjectName(u"tableWidget_producto")
        self.tableWidget_producto.setGeometry(QRect(135, 160, 601, 271))
        self.btn_buscar_producto = QPushButton(self.centralwidget)
        self.btn_buscar_producto.setObjectName(u"btn_buscar_producto")
        self.btn_buscar_producto.setGeometry(QRect(540, 100, 91, 23))
        self.btn_buscar_producto.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_buscar_producto.setStyleSheet(u"QObject{\n"
"	color:White;\n"
"	background-color: #666;\n"
"	border-radius: 5px;\n"
"}\n"
"QObject:hover{\n"
"	background-color: #222;\n"
"}")
        self.btn_eliminar_prodcuto = QPushButton(self.centralwidget)
        self.btn_eliminar_prodcuto.setObjectName(u"btn_eliminar_prodcuto")
        self.btn_eliminar_prodcuto.setGeometry(QRect(10, 360, 111, 31))
        self.btn_eliminar_prodcuto.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_eliminar_prodcuto.setStyleSheet(u"QObject{\n"
"	color:White;\n"
"	background-color: #666;\n"
"	border-radius: 5px;\n"
"}\n"
"QObject:hover{\n"
"	background-color: #222;\n"
"}")
        self.frame_content = QFrame(self.centralwidget)
        self.frame_content.setObjectName(u"frame_content")
        self.frame_content.setGeometry(QRect(0, -20, 771, 81))
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
        self.lbl_titulo.setGeometry(QRect(400, 30, 141, 41))
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
        self.lbl_error_buscador = QLabel(self.centralwidget)
        self.lbl_error_buscador.setObjectName(u"lbl_error_buscador")
        self.lbl_error_buscador.setGeometry(QRect(210, 130, 311, 20))
        self.lbl_error_buscador.setStyleSheet(u"font: 87 9pt \"Arial Black\";")
        Ventana_Productos.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(Ventana_Productos)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 759, 21))
        Ventana_Productos.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(Ventana_Productos)
        self.statusbar.setObjectName(u"statusbar")
        Ventana_Productos.setStatusBar(self.statusbar)

        self.retranslateUi(Ventana_Productos)

        QMetaObject.connectSlotsByName(Ventana_Productos)
    # setupUi

    def retranslateUi(self, Ventana_Productos):
        Ventana_Productos.setWindowTitle(QCoreApplication.translate("Ventana_Productos", u"Productos", None))
        self.btn_mostrar_productos.setText(QCoreApplication.translate("Ventana_Productos", u"Mostrar Productos", None))
        self.btn_agregar_producto.setText(QCoreApplication.translate("Ventana_Productos", u"Agregar Producto", None))
        self.btn_actualizar_prodcuto.setText(QCoreApplication.translate("Ventana_Productos", u"Actualizar Producto", None))
        self.lbl_ingrese_nombre.setText(QCoreApplication.translate("Ventana_Productos", u"Buscar Producto", None))
        ___qtablewidgetitem = self.tableWidget_producto.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Ventana_Productos", u"Codigo", None));
        ___qtablewidgetitem1 = self.tableWidget_producto.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Ventana_Productos", u"Tipo", None));
        ___qtablewidgetitem2 = self.tableWidget_producto.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Ventana_Productos", u"Nombre", None));
        ___qtablewidgetitem3 = self.tableWidget_producto.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Ventana_Productos", u"Precio", None));
        ___qtablewidgetitem4 = self.tableWidget_producto.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Ventana_Productos", u"Caducidad", None));
        ___qtablewidgetitem5 = self.tableWidget_producto.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Ventana_Productos", u"Lote", None));
        ___qtablewidgetitem6 = self.tableWidget_producto.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("Ventana_Productos", u"Cantidad", None));
        ___qtablewidgetitem7 = self.tableWidget_producto.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("Ventana_Productos", u"Imagen", None));
        self.btn_buscar_producto.setText(QCoreApplication.translate("Ventana_Productos", u"Buscar", None))
        self.btn_eliminar_prodcuto.setText(QCoreApplication.translate("Ventana_Productos", u"Eliminar Producto", None))
        self.lbl_logo.setText("")
        self.lbl_titulo.setText(QCoreApplication.translate("Ventana_Productos", u"Productos", None))
        self.btn_back.setText("")
        self.lbl_error_buscador.setText("")
    # retranslateUi

