# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ventanaUsuarios.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindowUsers(object):
    def setupUi(self, MainWindowUsers):
        if not MainWindowUsers.objectName():
            MainWindowUsers.setObjectName(u"MainWindowUsers")
        MainWindowUsers.resize(661, 381)
        MainWindowUsers.setMaximumSize(QSize(661, 381))
        MainWindowUsers.setStyleSheet(u"background-color: #555;")
        self.centralwidget = QWidget(MainWindowUsers)
        self.centralwidget.setObjectName(u"centralwidget")
        self.btn_incio = QPushButton(self.centralwidget)
        self.btn_incio.setObjectName(u"btn_incio")
        self.btn_incio.setGeometry(QRect(20, 10, 71, 20))
        self.btn_incio.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_incio.setStyleSheet(u"QObject{\n"
"	color:White;\n"
"	background-color: #666;\n"
"	border-radius: 5px;\n"
"}\n"
"QObject:hover{\n"
"	background-color: #222;\n"
"}")
        icon = QIcon()
        icon.addFile(u"../../../Downloads/productos.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_incio.setIcon(icon)
        self.btn_contenido = QPushButton(self.centralwidget)
        self.btn_contenido.setObjectName(u"btn_contenido")
        self.btn_contenido.setGeometry(QRect(570, 10, 71, 20))
        self.btn_contenido.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_contenido.setStyleSheet(u"QObject{\n"
"	color:White;\n"
"	background-color: #666;\n"
"	border-radius: 5px;\n"
"}\n"
"QObject:hover{\n"
"	background-color: #222;\n"
"}")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(120, 0, 421, 41))
        self.label.setStyleSheet(u"font:  26pt \"Arial Black\";")
        self.btn_agregar_usuario = QPushButton(self.centralwidget)
        self.btn_agregar_usuario.setObjectName(u"btn_agregar_usuario")
        self.btn_agregar_usuario.setGeometry(QRect(20, 160, 111, 31))
        self.btn_agregar_usuario.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_agregar_usuario.setStyleSheet(u"QObject{\n"
"	color:White;\n"
"	background-color: #666;\n"
"	border-radius: 5px;\n"
"}\n"
"QObject:hover{\n"
"	background-color: #222;\n"
"}")
        self.btn_actualizar_usuario = QPushButton(self.centralwidget)
        self.btn_actualizar_usuario.setObjectName(u"btn_actualizar_usuario")
        self.btn_actualizar_usuario.setGeometry(QRect(20, 210, 111, 31))
        self.btn_actualizar_usuario.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_actualizar_usuario.setStyleSheet(u"QObject{\n"
"	color:White;\n"
"	background-color: #666;\n"
"	border-radius: 5px;\n"
"}\n"
"QObject:hover{\n"
"	background-color: #222;\n"
"}")
        self.btn_eliminar_usuario = QPushButton(self.centralwidget)
        self.btn_eliminar_usuario.setObjectName(u"btn_eliminar_usuario")
        self.btn_eliminar_usuario.setGeometry(QRect(20, 260, 111, 31))
        self.btn_eliminar_usuario.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_eliminar_usuario.setStyleSheet(u"QObject{\n"
"	color:White;\n"
"	background-color: #666;\n"
"	border-radius: 5px;\n"
"}\n"
"QObject:hover{\n"
"	background-color: #222;\n"
"}")
        self.tableWidget_users = QTableWidget(self.centralwidget)
        if (self.tableWidget_users.columnCount() < 6):
            self.tableWidget_users.setColumnCount(6)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget_users.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget_users.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget_users.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget_users.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget_users.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget_users.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        self.tableWidget_users.setObjectName(u"tableWidget_users")
        self.tableWidget_users.setGeometry(QRect(145, 110, 501, 221))
        self.txt_clave_usuario = QLineEdit(self.centralwidget)
        self.txt_clave_usuario.setObjectName(u"txt_clave_usuario")
        self.txt_clave_usuario.setGeometry(QRect(330, 80, 231, 21))
        self.txt_clave_usuario.setStyleSheet(u"color: black;\n"
"font: 75 10pt \"Arial\";\n"
"border: 1px solid white;\n"
"border-radius: 5px;\n"
"background-color: white;")
        self.btn_buscar_usuario = QPushButton(self.centralwidget)
        self.btn_buscar_usuario.setObjectName(u"btn_buscar_usuario")
        self.btn_buscar_usuario.setGeometry(QRect(570, 80, 71, 23))
        self.btn_buscar_usuario.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_buscar_usuario.setStyleSheet(u"QObject{\n"
"	color:White;\n"
"	background-color: #666;\n"
"	border-radius: 5px;\n"
"}\n"
"QObject:hover{\n"
"	background-color: #222;\n"
"}")
        self.btn_mostrar_usuarios = QPushButton(self.centralwidget)
        self.btn_mostrar_usuarios.setObjectName(u"btn_mostrar_usuarios")
        self.btn_mostrar_usuarios.setGeometry(QRect(20, 110, 111, 31))
        self.btn_mostrar_usuarios.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_mostrar_usuarios.setStyleSheet(u"QObject{\n"
"	color:White;\n"
"	background-color: #666;\n"
"	border-radius: 5px;\n"
"}\n"
"QObject:hover{\n"
"	background-color: #222;\n"
"}")
        self.lbl_ingrese_nombre = QLabel(self.centralwidget)
        self.lbl_ingrese_nombre.setObjectName(u"lbl_ingrese_nombre")
        self.lbl_ingrese_nombre.setGeometry(QRect(330, 60, 181, 20))
        MainWindowUsers.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindowUsers)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 661, 21))
        MainWindowUsers.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindowUsers)
        self.statusbar.setObjectName(u"statusbar")
        MainWindowUsers.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindowUsers)

        QMetaObject.connectSlotsByName(MainWindowUsers)
    # setupUi

    def retranslateUi(self, MainWindowUsers):
        MainWindowUsers.setWindowTitle(QCoreApplication.translate("MainWindowUsers", u"MainWindow", None))
        self.btn_incio.setText("")
        self.btn_contenido.setText(QCoreApplication.translate("MainWindowUsers", u"Contenido", None))
        self.label.setText(QCoreApplication.translate("MainWindowUsers", u"Usuarios Registrados", None))
        self.btn_agregar_usuario.setText(QCoreApplication.translate("MainWindowUsers", u"Agregar Usuario", None))
        self.btn_actualizar_usuario.setText(QCoreApplication.translate("MainWindowUsers", u"Actualizar Usuario", None))
        self.btn_eliminar_usuario.setText(QCoreApplication.translate("MainWindowUsers", u"Eliminar Usuario", None))
        ___qtablewidgetitem = self.tableWidget_users.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindowUsers", u"Clave", None));
        ___qtablewidgetitem1 = self.tableWidget_users.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindowUsers", u"Nombre", None));
        ___qtablewidgetitem2 = self.tableWidget_users.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindowUsers", u"Contrase\u00f1a", None));
        ___qtablewidgetitem3 = self.tableWidget_users.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindowUsers", u"Email", None));
        ___qtablewidgetitem4 = self.tableWidget_users.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindowUsers", u"Puesto", None));
        ___qtablewidgetitem5 = self.tableWidget_users.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindowUsers", u"Descripci\u00f3n", None));
        self.btn_buscar_usuario.setText(QCoreApplication.translate("MainWindowUsers", u"Buscar", None))
        self.btn_mostrar_usuarios.setText(QCoreApplication.translate("MainWindowUsers", u"Mostrar Usuarios", None))
        self.lbl_ingrese_nombre.setText(QCoreApplication.translate("MainWindowUsers", u"Ingrese Nombre", None))
    # retranslateUi

