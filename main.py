
from PySide2.QtWidgets import QMainWindow, QMessageBox, QFileDialog
from PySide2 import QtGui
from PySide2.QtGui import QImage
from PySide2.QtCore import Slot, QTime,QTimer
from PySide2 import QtWidgets
#ventanas de formato python 
from ui_menu import Ui_MainWindow
from ui_contenido import Ui_Form
from ui_registro import Ui_Form_Registro
from ui_ventanaUsuarios import Ui_MainWindowUsers
from ui_registrarUsuario import Ui_Form_agregar_usuario
from ui_actualizarUsuario import Ui_Form_actualizar_usuario
from ui_borrarUsuario import Ui_Form_Eliminar
from ui_ventanaProductos import Ui_Ventana_Productos
from Ui_VentanaAgregarProducto import Ui_AgregarProducto
from ui_ActualizarProducto import Ui_VentanaActualizarProducto
from ui_EliminarProducto import Ui_form_eliminar_producto
from ui_VentanaProveedor import Ui_Ventana_Proveedores
from ui_RegistrarProveedor import Ui_RegistrarProveedor
from ui_ventanaActualizarProveedor import Ui_ActualizarProveedor
from Ui_ventanaBorrarProveedor import Ui_ventanaBorrarProveedor
from ui_ventanaFacturas import Ui_ventanaFacturas
from ui_ventanaAgregarFactura import Ui_ventanaAgregarFactura
from ui_ventanaActualizarFactura import Ui_ventanaModificarFactura
from ui_ventanaEliminarFactura import Ui_VenatanaEliminarFactura
from ui_ventanaVentas import Ui_ventanaVentas
from ui_ventanaInvercion import Ui_invercion
#fin ventanas python

#Importando control base de datos
from database import ConexionBaseDatos

#libreiras manejo de imagen y fehcas
from datetime import datetime
import cv2
import imutils
imagen = None
#algunas variables para usos variados
ruta = None
usuario = None
fecha = None

"""
##########################
CONTORL VENTANA INICIO SECION
##########################
"""
class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.main = Ui_MainWindow()
        self.main.setupUi(self)
        #eventos de ventana
        self.main.btn_login.clicked.connect(self.validacionLogin)
        self.main.btn_registrar.clicked.connect(self.ValidacionEntrarRegistro)


    @Slot()
    def validacionLogin(self):
        global usuario
        self.database = ConexionBaseDatos()#clase database y creacion de objeto
        try:
            #validando el usuario y la contraseña de cajas de texto y lazando pestaña de contenido
            if self.database.ValidacionDeUsuario(self.main.txt_password.text(),self.main.txt_user.text()):
                usuario = self.main.txt_user.text()
                self.hide()
                contentwindow = ContentWindow(self)
                contentwindow.show()
            else:
                #mostrando errores de usuario y contraseña
                return self.main.label_2.setText('Usuario o Contraseña incorrectos')
        except TypeError as t:
            return self.main.label_2.setText('Algo salio mal'+t)
    
    #mostrando ventana de validacion de ingreso a registro
    @Slot()
    def ValidacionEntrarRegistro(self):
        self.hide()
        ventanaRegistro = VentanaIngresarRegistro(self)
        ventanaRegistro.show()


"""
##########################
CONTORL VENTANA CONTENIDO
##########################
"""


class ContentWindow(QMainWindow):
    def __init__(self, parent=None):
        super(ContentWindow, self).__init__(parent)
        self.content = Ui_Form()
        self.content.setupUi(self)
        #eventos de ventana
        self.content.btn_back.clicked.connect(self.RegresarAlInicio)
        self.content.brn_productos.clicked.connect(self.MostrarVentanaProductos)
        self.content.btn_provedores.clicked.connect(self.MostrarVentanaProveedores)
        self.content.btn_ventas.clicked.connect(self.MostrarVentanaVentas)
        self.content.btn_invercion.clicked.connect(self.MostrarVentanaInvercion)


    @Slot()
    def MostrarVentanaProductos(self):
        self.hide()
        self.productos = VentanasProductos(self)
        self.productos.show()    

    @Slot()
    def MostrarVentanaProveedores(self):
        self.hide()
        self.proveedores = VentanaProveedores(self)
        self.proveedores.show()


    @Slot()
    def MostrarVentanaVentas(self):
        self.hide()
        self.ventas = VentanaVentas(self)
        self.ventas.show()

    @Slot()
    def MostrarVentanaInvercion(self):
        self.hide()
        self.invercion = VentanaInvercion(self)
        self.invercion.show()

    @Slot()
    def RegresarAlInicio(self):
        #boton regresando ventana atras
        self.hide()
        self.parent().show()
        self.close()

"""
##########################
CONTORL VENTANA USUARIOS
##########################
"""


#login para ingresar a la ventana de usuarios, metodo de seguridad  
class VentanaIngresarRegistro(QMainWindow):
    def __init__(self, parent=None) -> None:
        super(VentanaIngresarRegistro, self).__init__(parent)
        self.registro = Ui_Form_Registro()
        self.registro.setupUi(self)
        self.registro.btn_incio.clicked.connect(self.RegresarAlInicio)
        self.registro.btn_login_registro.clicked.connect(self.validacionLoginRegistro)

    @Slot()
    def validacionLoginRegistro(self):
        self.database = ConexionBaseDatos()#clase database y creacion de objeto
        try:
            #validando el usuario y la contraseña de cajas de texto y lazando pestaña de contenido
            if self.database.ValidacionDeUsuario(self.registro.txt_password_registro.text(),self.registro.txt_user_regsitro.text()):
                self.hide()
                contenUsersWindow = VentanaUsuarios(self)
                contenUsersWindow.show()
            else:
                #mostrando errores
                return self.registro.label_error.setText('Usuario o Contraseña incorrectos')
        except TypeError as t:
            return self.registro.label_error.setText('Algo salio mal'+t)

    @Slot()
    def RegresarAlInicio(self):
        #boton regresando al inicio de secion
        self.hide()
        self.parent().show()
        self.close()





class VentanaUsuarios(QMainWindow):
    def __init__(self, parent: None):
        super(VentanaUsuarios, self).__init__(parent)
        self.usuarios = Ui_MainWindowUsers()
        self.usuarios.setupUi(self)
        self.usuarios.btn_incio.clicked.connect(self.RegresarAlInicio)
        self.usuarios.btn_contenido.clicked.connect(self.IrAContenidoPrincipal)
        self.usuarios.btn_mostrar_usuarios.clicked.connect(self.MostrarUsuariosTable)
        self.usuarios.btn_agregar_usuario.clicked.connect(self.MostrarVentanaAgregarUsuario)
        self.usuarios.btn_actualizar_usuario.clicked.connect(self.MostrarVentanaActualizarUsuario)
        self.usuarios.btn_eliminar_usuario.clicked.connect(self.MostrarEliminarVentana)
        self.usuarios.btn_buscar_usuario.clicked.connect(self.MostrarUsuarioEnTabla)
    

    #Mostar Usuarios en Tabla
    @Slot()
    def MostrarUsuariosTable(self):
        basedatos = ConexionBaseDatos()
        usuarios = basedatos.MostarUsuarios()
        self.usuarios.tableWidget_users.setRowCount(0)
        for row_number, row_data in enumerate(usuarios):
            self.usuarios.tableWidget_users.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.usuarios.tableWidget_users.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
    
    @Slot()
    #mostrando usuario buscado por nombre
    def MostrarUsuarioEnTabla(self):
        nombre = self.usuarios.txt_clave_usuario.text()
        #objeto base
        basedatos = ConexionBaseDatos()
        usuario = basedatos.MostrarUsuario(nombre)
        #mostrando en tabla
        self.usuarios.tableWidget_users.setRowCount(0)
        for row_number, row_data in enumerate(usuario):
            self.usuarios.tableWidget_users.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.usuarios.tableWidget_users.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))


    @Slot()
    #mostrando ventana eliminar
    def MostrarEliminarVentana(self):
        self.ventanaeliminar = VentanaEliminarUsuario(self)
        self.ventanaeliminar.show()

    @Slot()
    def MostrarVentanaActualizarUsuario(self):
        self.ventanUpdateUser = VentanaActualizarUsuario(self)
        self.ventanUpdateUser.show()
    
    @Slot()
    def MostrarVentanaAgregarUsuario(self):
        self.ventanaRegistro = VentanaAgregarUsuario(self)
        self.ventanaRegistro.show()

    @Slot()
    def IrAContenidoPrincipal(self):
        self.hide()
        self.contenidoPrincipal = ContentWindow(self)
        self.contenidoPrincipal.show()


    @Slot()
    def RegresarAlInicio(self):
        #boton regresando al inicio de secion
        self.hide()
        self.parent().show()
        self.close()

#agregar nuevo usuario a la base
class VentanaAgregarUsuario(QMainWindow):
    def __init__(self, parent:None):
        super(VentanaAgregarUsuario,self).__init__(parent)
        self.AgregarUsuario = Ui_Form_agregar_usuario()
        self.AgregarUsuario.setupUi(self)
        self.AgregarUsuario.btn_agregar_usuarios.clicked.connect(self.AgregandoUsuario)

    @Slot()
    def AgregandoUsuario(self):
        #tomando parametros
        clave = self.AgregarUsuario.txt_clave.text()
        nombre = self.AgregarUsuario.txt_nombre.text()
        contrasena = self.AgregarUsuario.txt_contrasena.text()
        email = self.AgregarUsuario.txt_email.text()
        puesto = self.AgregarUsuario.txt_puesto.text()
        descripcion = self.AgregarUsuario.txt_descripcion.text()

        #registrando usuario
        BaseDatos = ConexionBaseDatos()
        try:
            BaseDatos.AgregandoUsuario(clave,nombre,contrasena,email,puesto,descripcion)
            QMessageBox.information(self,"Exito","Usuario Registrado Correctamente")
        except:
            QMessageBox.Critical(self,"Error","Fallo de Registor")


#ventana actualizar usuario
class VentanaActualizarUsuario(QMainWindow):
    def __init__(self, parent:None):
        super(VentanaActualizarUsuario,self).__init__(parent)
        self.actualizarUsuario = Ui_Form_actualizar_usuario()
        self.actualizarUsuario.setupUi(self)
        self.actualizarUsuario.btn_actualizar_usuarios.clicked.connect(self.ejecutarActualizarUsuario)

    @Slot()
    def ejecutarActualizarUsuario(self):
        clave = self.actualizarUsuario.txt_clave.text()
        nombre = self.actualizarUsuario.txt_nombre.text()
        contrasena = self.actualizarUsuario.txt_contrasena.text()
        email = self.actualizarUsuario.txt_email.text()
        puesto = self.actualizarUsuario.txt_puesto.text()
        descripcion = self.actualizarUsuario.txt_descripcion.text()

        BaseDatos = ConexionBaseDatos()
        try:
            BaseDatos.ActualizarUsuario(clave,nombre,contrasena,email,puesto,descripcion)
            QMessageBox.information(self,"Exito","Usuario Actualizado Correctamente")
        except:
            QMessageBox.Critical(self,"Error","Fallo al Actualizar")


#eliminando usuario de base de datos
class VentanaEliminarUsuario(QMainWindow):
    def __init__(self, parent:None):
        super(VentanaEliminarUsuario, self).__init__(parent)
        self.eliminar = Ui_Form_Eliminar()
        self.eliminar.setupUi(self)
        self.eliminar.btn_borrar_usuario.clicked.connect(self.eliminarUsuario)

    def  eliminarUsuario(self):
        clave = self.eliminar.txt_borrar_usuario.text()

        try:
            baseDatos = ConexionBaseDatos()
            baseDatos.eliminandoUsuario(clave)
            QMessageBox.information(self,"Exito","Usuario Eliminado Correctamente")
        except:
            return self.eliminar.label_manejo_error.setText("Error Clave No Existe")



"""
##########################
CONTORL VENTANA PRODUCTOS
##########################
"""

class VentanasProductos(QMainWindow):
    def __init__(self, parent=None):
        super(VentanasProductos, self).__init__(parent)
        self.productos = Ui_Ventana_Productos()
        self.productos.setupUi(self)
        self.productos.btn_back.clicked.connect(self.RegresarAlInicio)
        self.productos.btn_mostrar_productos.clicked.connect(self.MostrarProductos)
        self.productos.btn_agregar_producto.clicked.connect(self.MostrarVentanaAgregarProducto)
        self.productos.btn_actualizar_prodcuto.clicked.connect(self.MostrarVentanaActualizarPorducto)
        self.productos.btn_eliminar_prodcuto.clicked.connect(self.MostrarVentanaEliminarProducto)
        self.productos.btn_buscar_producto.clicked.connect(self.MostrarProductoEnTabla)
    
    @Slot()
    def MostrarProductos(self):
        # funcion Mostrando prodcutos en la tabla de la ventana
        basedatos = ConexionBaseDatos()
        productos = basedatos.MostarProductos()

        self.productos.tableWidget_producto.setRowCount(0)
        for row_number, row_data in enumerate(productos):
            self.productos.tableWidget_producto.insertRow(row_number)
            for column_number,data in enumerate(row_data):
                #comprobando lugar de imagen y convertirla de bite a imagen
                if column_number == 7:
                    item = self.getImageLabel(data)
                    self.productos.tableWidget_producto.setCellWidget(row_number,column_number,item)
                # fin proceso imagen
                else:
                    #los otros datos de la tabla
                    self.productos.tableWidget_producto.setItem(row_number,column_number,QtWidgets.QTableWidgetItem(str(data)))

    @Slot()
    #mostrando producto buscado por nombre
    def MostrarProductoEnTabla(self):
        
        id = self.productos.txt_clave_producto.text()
        #objeto base
        basedatos = ConexionBaseDatos()

        #manejo error producto no existe
        if basedatos.ProductoExiste(id): 
            producto = basedatos.MostrarProducto(id)
            
            
            self.productos.lbl_error_buscador.clear()#limpiando label error

            #mostrando producto buscado en tabla
            self.productos.tableWidget_producto.setRowCount(0)
            for row_number, row_data in enumerate(producto):
                self.productos.tableWidget_producto.insertRow(row_number)
                for column_number,data in enumerate(row_data):
                    #comprobando lugar de imagen y convertirla de bite a imagen y
                    if column_number == 7:
                        item = self.getImageLabel(data)
                        self.productos.tableWidget_producto.setCellWidget(row_number,column_number,item)
                    # fin proceso imagen
                    elif column_number != 7:
                        # mostrando los otros datos de la tabla diferente de imagen
                        self.productos.tableWidget_producto.setItem(row_number,column_number,QtWidgets.QTableWidgetItem(str(data)))
        else:
            self.productos.lbl_error_buscador.setText("Producto No existe")
    @Slot()
    # indicar el label de la imagen y cargar la imagen ahí
    def getImageLabel(self,image):
        imageLabel = QtWidgets.QLabel(self.productos.centralwidget)
        imageLabel.setText("")
        imageLabel.setScaledContents(True)
        pixmap = QtGui.QPixmap()
        pixmap.loadFromData(image,'jpg')
        imageLabel.setPixmap(pixmap)
        return imageLabel

    @Slot()
    def MostrarVentanaActualizarPorducto(self):
        self.updatepro = VentanaActualizarProducto(self)
        self.updatepro.show()

    @Slot()
    def MostrarVentanaAgregarProducto(self):
        self.mostraraddproduct = VentanaAgregarProducto(self)
        self.mostraraddproduct.show()

    @Slot()
    def MostrarVentanaEliminarProducto(self):
        self.mostrardeleteproduct = VentanaEliminarProducto(self)
        self.mostrardeleteproduct.show()

    
    @Slot()
    def RegresarAlInicio(self):
        #boton regresando una ventana atras
        self.hide()
        self.parent().show()
        self.close()


class VentanaAgregarProducto(QMainWindow):
    def __init__(self, parent=None) -> None:
        super(VentanaAgregarProducto,self).__init__(parent)
        self.addproduct = Ui_AgregarProducto()
        self.addproduct.setupUi(self)
        self.addproduct.btn_agregar_producto.clicked.connect(self.agregarProducto)
        self.addproduct.btn_insertar_imagen.clicked.connect(self.rutaImagen)
    

    #imagen a seleccionar para el producto y cargando en lebel para visualizarla
    def rutaImagen(self):
        global ruta
        ruta = QFileDialog.getOpenFileName(self,'Abrir','*.*')[0]

        if len(ruta) > 0:
            global imagen

            #read the image input and resize image
            imagen = cv2.imread(ruta)
            imagen = imutils.resize(imagen, height=300)
            imageShow = imutils.resize(imagen, width=280)
            #to bgr
            imageShow = cv2.cvtColor(imageShow, cv2.COLOR_BGR2RGB)


            #show image in label
            im = QImage(imageShow, imageShow.shape[1], imageShow.shape[0], imageShow.strides[0], QImage.Format_RGB888)
            self.addproduct.lbl_imagen.setPixmap(QtGui.QPixmap.fromImage(im))



    def agregarProducto(self):
        global ruta
        codigo = self.addproduct.txt_clave.text()
        tipo = self.addproduct.txt_tipo.text()
        nombre = self.addproduct.txt_nombre.text()
        precio = self.addproduct.txt_precio.text()
        caducidad = self.addproduct.txt_caducidad.text()
        lote = self.addproduct.txt_lote.text()
        cantidad = self.addproduct.txt_cantidad.text()

        #convirtuendo la imagen a bite para guardarla en base de datos
        with open(ruta, 'rb') as i:
            im = i.read()
        imagen = im
        #fin proceso 

        
        database = ConexionBaseDatos()
        try:
            database.AgregandoProducto(codigo,tipo,nombre,precio,caducidad,lote,cantidad,imagen)
            QMessageBox.information(self,"Exito","Producto Registrado")
            self.addproduct.txt_clave.clear()
            self.addproduct.txt_tipo.clear()
            self.addproduct.txt_nombre.clear()
            self.addproduct.txt_precio.clear()
            self.addproduct.txt_caducidad.clear()
            self.addproduct.txt_lote.clear()
            self.addproduct.txt_cantidad.clear()
            self.addproduct.lbl_imagen.clear()
        except:
            return QMessageBox.Critical(self,"Error","Algo salio mal :(")

class VentanaActualizarProducto(QMainWindow):
    def __init__(self, parent:None) -> None:
        super().__init__(parent)
        self.updateproduct = Ui_VentanaActualizarProducto()
        self.updateproduct.setupUi(self)
        self.updateproduct.btn_actualizar_producto.clicked.connect(self.actualizarProducto)
        self.updateproduct.btn_insertar_imagen.clicked.connect(self.CargarImagen)
        
    def CargarImagen(self):
        global ruta
        ruta = QFileDialog.getOpenFileName(self,'Abrir','*.*')[0]

        if len(ruta) > 0:
            global imagen

            #read the image input and resize image
            imagen = cv2.imread(ruta)
            imagen = imutils.resize(imagen, height=300)
            imageShow = imutils.resize(imagen, width=280)
            #to bgr
            imageShow = cv2.cvtColor(imageShow, cv2.COLOR_BGR2RGB)


            #show image in label
            im = QImage(imageShow, imageShow.shape[1], imageShow.shape[0], imageShow.strides[0], QImage.Format_RGB888)
            self.updateproduct.lbl_imagen.setPixmap(QtGui.QPixmap.fromImage(im))

    def actualizarProducto(self):
        global ruta
        codigo = self.updateproduct.txt_clave.text()
        tipo = self.updateproduct.txt_tipo.text()
        nombre = self.updateproduct.txt_nombre.text()
        precio = self.updateproduct.txt_precio.text()
        caducidad = self.updateproduct.txt_caducidad.text()
        lote = self.updateproduct.txt_lote.text()
        cantidad = self.updateproduct.txt_cantidad.text()

        #convirtuendo la imagen a bite para guardarla en base de datos
        with open(ruta, 'rb') as i:
            im = i.read()
        imagen = im
        #fin proceso 

        
        database = ConexionBaseDatos()
        try:
            database.ActualizarProducto(codigo,tipo,nombre,precio,caducidad,lote,cantidad,imagen)
            QMessageBox.information(self,"Exito","Producto Actualizado")
            self.updateproduct.txt_clave.clear()
            self.updateproduct.txt_tipo.clear()
            self.updateproduct.txt_nombre.clear()
            self.updateproduct.txt_precio.clear()
            self.updateproduct.txt_caducidad.clear()
            self.updateproduct.txt_lote.clear()
            self.updateproduct.txt_cantidad.clear()
            self.updateproduct.lbl_imagen.clear()
        except:
            return QMessageBox.Critical(self,"Error","Algo salio mal :(")


class VentanaEliminarProducto(QMainWindow):
    def __init__(self, parent:None) -> None:
        super().__init__(parent)
        self.deleteproduct = Ui_form_eliminar_producto()
        self.deleteproduct.setupUi(self)
        self.deleteproduct.btn_borrar_producto.clicked.connect(self.eliminandoProdcuto)

    def eliminandoProdcuto(self):
        clave = self.deleteproduct.txt_borrar_producto.text()

        try:
            baseDatos = ConexionBaseDatos()
            baseDatos.eliminandoProducto(clave)
            QMessageBox.information(self,"Exito","Producto Eliminado Correctamente")
            self.deleteproduct.txt_borrar_producto.clear()
        except:
            return self.eliminar.label_manejo_error.setText("Error Clave No Existe")


"""
##########################
CONTORL VENTANA PROVEEDORES
##########################
"""

class VentanaProveedores(QMainWindow):
    def __init__(self, parent:None) -> None:
        super().__init__(parent)
        self.provewindow = Ui_Ventana_Proveedores()
        self.provewindow.setupUi(self)
        self.provewindow.btn_atras.clicked.connect(self.RegresarAtras)
        self.provewindow.btn_mostrar_proveedor.clicked.connect(self.MostrarProveedores)
        self.provewindow.btn_agregar_proveedor.clicked.connect(self.LanzarVentanaRegistrarProveedor)
        self.provewindow.btn_actualizar_proveedor.clicked.connect(self.MostrarVentanaActualizarProveedor)
        self.provewindow.btn_eliminar_proveedor.clicked.connect(self.MostrarVentanaBorrarProveedor)
        self.provewindow.btn_buscar_proveedor.clicked.connect(self.MostrarProvedor)
        self.provewindow.btn_facturar.clicked.connect(self.MostrandoVentanaFacturas)

    @Slot()
    def MostrarProveedores(self):
        basedatos = ConexionBaseDatos()
        proveedores = basedatos.MostarProveedores()
        self.provewindow.tableWidget_proveedores.setRowCount(0)
        for row_number, row_data in enumerate(proveedores):
            self.provewindow.tableWidget_proveedores.insertRow(row_number)
            for column_number,data in enumerate(row_data):
                self.provewindow.tableWidget_proveedores.setItem(row_number,column_number, QtWidgets.QTableWidgetItem(str(data)))
    
    @Slot()
    def MostrarProvedor(self):
        id = self.provewindow.txt_nombre_proveedor.text()
        #objeto base
        basedatos = ConexionBaseDatos()

        #manejo error producto no existe
        if basedatos.ProveedorExiste(id): 
            proveedor = basedatos.MostrarProveedor(id)
            
            
            self.provewindow.lbl_error_buscador.clear()#limpiando label error

            #mostrando producto buscado en tabla
            self.provewindow.tableWidget_proveedores.setRowCount(0)
            for row_number, row_data in enumerate(proveedor):
                self.provewindow.tableWidget_proveedores.insertRow(row_number)
                for column_number,data in enumerate(row_data):
                    self.provewindow.tableWidget_proveedores.setItem(row_number,column_number, QtWidgets.QTableWidgetItem(str(data)))
        else:
            self.productos.lbl_error_buscador.setText("Proveedor No existe")

    @Slot()
    def LanzarVentanaRegistrarProveedor(self):
        self.windowaddpro = VentanaAgregarProveedor(self)
        self.windowaddpro.show()

    @Slot()
    def MostrarVentanaActualizarProveedor(self):
        self.mostrarupdate = VentanaActualizarProveedor(self)
        self.mostrarupdate.show()

    @Slot()
    def MostrarVentanaBorrarProveedor(self):
        self.deleteprov = VentanaEliminarProveedor(self)
        self.deleteprov.show()

    @Slot()
    def MostrandoVentanaFacturas(self):
        self.facturas = VentanaFacturas(self)
        self.facturas.show()

    @Slot()
    def RegresarAtras(self):
        #boton regresando una ventana atras
        self.hide()
        self.parent().show()
        self.close()

class VentanaAgregarProveedor(QMainWindow):
    def __init__(self, parent:None):
        super().__init__(parent)
        self.windowaddproveedor = Ui_RegistrarProveedor()
        self.windowaddproveedor.setupUi(self)
        self.windowaddproveedor.btn_agregar_proveedor.clicked.connect(self.registrarProveedor)
    
    def limpiarCampos(self):
        self.windowaddproveedor.txt_clave.clear()
        self.windowaddproveedor.txt_empresa.clear()
        self.windowaddproveedor.txt_nombre.clear()
        self.windowaddproveedor.txt_telefono.clear()
        self.windowaddproveedor.txt_email.clear()


    def registrarProveedor(self):
        clave = self.windowaddproveedor.txt_clave.text()
        empresa = self.windowaddproveedor.txt_empresa.text()
        nombre = self.windowaddproveedor.txt_nombre.text()
        telefono = self.windowaddproveedor.txt_telefono.text()
        email = self.windowaddproveedor.txt_email.text()
        try:
            basedatos = ConexionBaseDatos()
            basedatos.AgregandoProveedor(clave,empresa,nombre,telefono,email)
            QMessageBox.information(self,"Exito","Proveedor Agregado!")
            self.limpiarCampos()
        except:
            QMessageBox.Abort(self,"Error","Fallo en Agregar Poveedor")


class VentanaActualizarProveedor(QMainWindow):
    def __init__(self, parent:None) -> None:
        super().__init__(parent)
        self.updateproveedor = Ui_ActualizarProveedor()
        self.updateproveedor.setupUi(self)
        self.updateproveedor.btn_actualizar_proveedor.clicked.connect(self.ActualizarProveedor)

    @Slot()
    def limpiarCampos(self):
        self.updateproveedor.txt_clave.clear()
        self.updateproveedor.txt_empresa.clear()
        self.updateproveedor.txt_nombre.clear()
        self.updateproveedor.txt_telefono.clear()
        self.updateproveedor.txt_email.clear()
    
    @Slot()
    def ActualizarProveedor(self):
        clave = self.updateproveedor.txt_clave.text()
        empresa = self.updateproveedor.txt_empresa.text()
        nombre = self.updateproveedor.txt_nombre.text()
        telefono = self.updateproveedor.txt_telefono.text()
        email = self.updateproveedor.txt_email.text()
        try:
            basedatos = ConexionBaseDatos()
            basedatos.ActualizarProveedor(clave,empresa,nombre,telefono,email)
            QMessageBox.information(self,"Exito","Proveedor Agregado!")
            self.limpiarCampos()
        except:
            QMessageBox.Abort(self,"Error","Fallo en Agregar Poveedor")


class VentanaEliminarProveedor(QMainWindow):
    def __init__(self, parent:None) -> None:
        super().__init__(parent)
        self.deleteproveedor = Ui_ventanaBorrarProveedor()
        self.deleteproveedor.setupUi(self)
        self.deleteproveedor.btn_borrar_proveedor.clicked.connect(self.BorrarProveedor)

    @Slot()
    def BorrarProveedor(self):
        clave = self.deleteproveedor.txt_borrar_proveedor.text()

        try:
            basedatos = ConexionBaseDatos()
            basedatos.eliminandoProveedor(clave)
            QMessageBox.information(self,"Exito","Proveedor Eliminado!")
        except:
            self.deleteproveedor.label_manejo_error.setText("No existe la clave")


"""
##########################
CONTORL VENTANA FACTURAS
##########################
"""

class VentanaFacturas(QMainWindow):
    def __init__(self, parent:None) -> None:
        super().__init__(parent)   
        self.facturas = Ui_ventanaFacturas()
        self.facturas.setupUi(self)
        self.facturas.btn_atras.clicked.connect(self.RegresarAtras)
        self.facturas.btn_mostrar_facturas.clicked.connect(self.MostrarFacturas)
        self.facturas.btn_agregar_factura.clicked.connect(self.MostrarVentanaAgregarFactura)
        self.facturas.btn_modificar_factura.clicked.connect(self.MostrarVentanaModificarFactura)
        self.facturas.btn_eliminar_factura.clicked.connect(self.MostrarVentanaEliminarFactura)
    
    def MostrarFacturas(self):
        basedatos = ConexionBaseDatos()
        facturas = basedatos.MostarFacturas()
        self.facturas.tableWidget_facturas.setRowCount(0)
        for row_number, row_data in enumerate(facturas):
            self.facturas.tableWidget_facturas.insertRow(row_number)
            for column_number,data in enumerate(row_data):
                self.facturas.tableWidget_facturas.setItem(row_number,column_number, QtWidgets.QTableWidgetItem(str(data)))

    def MostrarVentanaAgregarFactura(self):
        self.agregarFactura = ventanaAgregarFactura(self)
        self.agregarFactura.show()
    
    def MostrarVentanaModificarFactura(self):
        self.modifFactura = VentanaModificarFactura(self)
        self.modifFactura.show()

    def MostrarVentanaEliminarFactura(self):
        self.deletefactura = VentanaEliminarFactura(self)
        self.deletefactura.show()
    
    def RegresarAtras(self):
        #boton regresando una ventana atras
        self.hide()
        self.parent().show()
        self.close()

class ventanaAgregarFactura(QMainWindow):
    def __init__(self, parent: None) -> None:
        super().__init__(parent)
        self.addfactura = Ui_ventanaAgregarFactura()
        self.addfactura.setupUi(self)
        self.addfactura.btn_agregar_factura.clicked.connect(self.AgregandoFactura)


    def limpiarTextos(self):
        self.addfactura.txt_clave.clear()
        self.addfactura.txt_empresa.clear()
        self.addfactura.txt_cantidad.clear()
        self.addfactura.txt_calle.clear()
        self.addfactura.txt_colonia.clear()

    def AgregandoFactura(self):
        clave = self.addfactura.txt_clave.text()
        empresa = self.addfactura.txt_empresa.text()
        cantidad = self.addfactura.txt_cantidad.text()
        calle = self.addfactura.txt_calle.text()
        colonia = self.addfactura.txt_colonia.text()

        try:
            basedatos = ConexionBaseDatos()
            basedatos.AgregandoFactura(clave,empresa,cantidad,calle,colonia)
            QMessageBox.information(self,"Exito","Proveedor Agregado!")
            self.limpiarTextos()
        except:
            QMessageBox.Abort(self,"Error","Algo Fallo")

class VentanaModificarFactura(QMainWindow):
    def __init__(self, parent: None) -> None:
        super().__init__(parent)
        self.updatafactura = Ui_ventanaModificarFactura()
        self.updatafactura.setupUi(self)
        self.updatafactura.btn_modificar_factura.clicked.connect(self.ModificandoFactura)

    def limpiarTextos(self):
        self.updatafactura.txt_clave.clear()
        self.updatafactura.txt_empresa.clear()
        self.updatafactura.txt_cantidad.clear()
        self.updatafactura.txt_calle.clear()
        self.updatafactura.txt_colonia.clear()
    
    def ModificandoFactura(self):
        clave = self.updatafactura.txt_clave.text()
        empresa = self.updatafactura.txt_empresa.text()
        cantidad = self.updatafactura.txt_cantidad.text()
        calle = self.updatafactura.txt_calle.text()
        colonia = self.updatafactura.txt_colonia.text()

        try:
            basedatos = ConexionBaseDatos()
            basedatos.EditarFactura(clave,empresa,cantidad,calle,colonia)
            QMessageBox.information(self,"Exito","Proveedor Editado!")
            self.limpiarTextos()
        except:
            QMessageBox.Abort(self,"Error","Algo Fallo")

class VentanaEliminarFactura(QMainWindow):
    def __init__(self, parent:None) -> None:
        super().__init__(parent)
        self.deletefactura = Ui_VenatanaEliminarFactura()
        self.deletefactura.setupUi(self)
        self.deletefactura.btn_borrar_factura.clicked.connect(self.EliminarFactura)

    def EliminarFactura(self):
        clave = self.deletefactura.txt_borrar_factura.text()

        try:
            basedatos = ConexionBaseDatos()
            basedatos.eliminandoFactura(clave)
            QMessageBox.information(self,"Exito","Proveedor Eliminado!")
            self.deletefactura.txt_borrar_factura.clear()
        except:
            self.deletefactura.label_manejo_error.setText("Clave No existe")

"""
##########################
CONTORL VENTANA VENTAS
##########################
"""

class VentanaVentas(QMainWindow):
    def __init__(self, parent:None) -> None:
        super().__init__(parent)
        self.ventas = Ui_ventanaVentas()
        self.ventas.setupUi(self)
        self.ventas.btn_back.clicked.connect(self.RegresarAtras)
        self.ventas.btn_agregar_producto.clicked.connect(self.MostarDatos)
        self.ventas.btn_cobrar.clicked.connect(self.LimpiarVenta)

        #libreira para contador tiempo
        timer = QTimer(self)
        timer.timeout.connect(self.MostrarTiempo)
        timer.start(1000)

        #Mostrando fecha con datetime
        fechaCompleta = str(datetime.now())
        datos = fechaCompleta.split()
        global fecha
        fecha = str(datos[0])
        self.ventas.lbl_fecha.setText(str(fecha))

        #Mostrar usuario
        global usuario
        self.ventas.lbl_mostrarUsuario.setText(str(usuario))

    def MostrarTiempo(self):
        horaActual = QTime.currentTime()
        tiempo = horaActual.toString('hh:mm:ss ap')
        self.ventas.lbl_hora.setText(tiempo)
    
    def limpiarCampos(self):
        self.ventas.txt_clave_producto.clear()
        self.ventas.txt_nombre_producto.clear()
        self.ventas.txt_precio.clear()
        self.ventas.txt_cantidad.clear()
    
    @Slot()
    def MostarDatos(self):
        global fecha
        #tomando datos de cajas
        
        codigo = self.ventas.txt_clave_producto.text()
        producto = self.ventas.txt_nombre_producto.text()
        precio = self.ventas.txt_precio.text()
        cantidad = self.ventas.txt_cantidad.text()
        total = int(precio)*int(cantidad)
        

        #gurardandolos para su uso en tabla
        basedatos = ConexionBaseDatos()
        #guardanod en base de datos ventas
        ventas = basedatos.insertarVenta(codigo,producto,precio,cantidad,total)
        #guardanod en base de datos invercion
        invercion = basedatos.insertarInvercion(codigo,fecha,cantidad,total)
        
        #mostrando datos en tabla
        seleccionar = basedatos.MostarVentas()
        suma = 0
        self.ventas.tableWidget_ventas.setRowCount(0)
        for row_number,row_data in enumerate(seleccionar):
            self.ventas.tableWidget_ventas.insertRow(row_number)
            for column_number,data in enumerate(row_data):
                #sumando la columna para el total general
                if column_number == 4:
                    suma+=data
                #mostrando datos en tabla
                self.ventas.tableWidget_ventas.setItem(row_number,column_number,QtWidgets.QTableWidgetItem(str(data)))
            #mostrando la suma en la caja de texto
            self.ventas.txt_total.setText(str(suma))     
        self.limpiarCampos()

    @Slot()
    def LimpiarVenta(self):
        

        #vaciando tabla de base de datos
        basedatos = ConexionBaseDatos()
        basedatos.eliminandoVenta()

        #vaciando tabla de la ventana
        self.ventas.tableWidget_ventas.clearContents()
        self.ventas.tableWidget_ventas.setRowCount(0)

        #operacion para el cambio
        total = self.ventas.txt_total.text()
        pago  = self.ventas.txt_pago.text()

        total = int(total)
        pago = int(pago)

        if total > 0 and pago > 0:
            cambio = pago-total
            self.ventas.txt_cambio.setText(str(cambio))

        #mensaje de confirmacion
        self.ventas.txt_total.clear()
        self.ventas.txt_pago.clear()
        QMessageBox.information(self,"Exito","Gracias Por Su Compra")


    @Slot()
    def RegresarAtras(self): 
        #boton regresando una ventana atras
        self.hide()
        self.parent().show()
        self.close()



"""
##########################
CONTORL VENTANA INVERCION
##########################
"""


class VentanaInvercion(QMainWindow):
    def __init__(self, parent:None) -> None:
        super().__init__(parent)
        self.invercion = Ui_invercion()
        self.invercion.setupUi(self)
        self.invercion.btn_atras.clicked.connect(self.RegresarAtras)
        self.invercion.btn_limpiar_ventas.clicked.connect(self.BorrarInvercion)

        #mostrando datos en tabla
        basedatos = ConexionBaseDatos()
        inverciones = basedatos.MostrarInvercion()
        sumaTotal=0
        self.invercion.tableWidget_invercion.setRowCount(0)
        for row_number, row_data in enumerate(inverciones):
            self.invercion.tableWidget_invercion.insertRow(row_number)
            for column_number,data in enumerate(row_data):
                #sumando columna para sacarl el total
                if column_number == 3:
                    sumaTotal+=data
                #mostrando datos en campos de tabla
                self.invercion.tableWidget_invercion.setItem(row_number,column_number, QtWidgets.QTableWidgetItem(str(data)))
        
        #mostrando suma
        self.invercion.txt_total_invercion.setText(str(sumaTotal))

    @Slot()
    def BorrarInvercion(self):

        try:
            basedatos = ConexionBaseDatos()
            basedatos.eliminandoInvercion()
            QMessageBox.information(self,"Exito","Todo se Elimino!")
            self.invercion.txt_total_invercion.clear()
        except:
            QMessageBox.information(self,"Error","Algo Salio Mal")

    @Slot()
    def RegresarAtras(self): 
        #boton regresando una ventana atras
        self.hide()
        self.parent().show()
        self.close()
    
    
