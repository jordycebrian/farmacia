import pyodbc

class ConexionBaseDatos():
    def __init__(self):

        """Conexion database"""
        conn = pyodbc.connect('Driver={ODBC Driver 17 for Sql Server};'
        'Server=DESKTOP-H2RJN7F;'
        'Database=farmacia;'
        'UID=sa;'
        'PWD=cero41;')

        self.cursor = conn.cursor()
        """FIN database"""

    """
    ###########################
    Manejo de Usuarios
    ###########################
    """
    #mostrando usuarios en tabla de usuarios
    def MostarUsuarios(self):
        query = 'SELECT * FROM usuarios'
        return self.cursor.execute(query)
        
    def MostrarUsuario(self,nombre):
        try:
            query = 'SELECT * FROM usuarios WHERE nombre = ?'
            return self.cursor.execute(query,[nombre])
            
        except:
            return("Error en la base")

    """Usando datos de base para logear"""
    def ValidacionDeUsuario(self,contra,user):
        #agarrando los datos usuario y contrasena de la base
        query = ('SELECT nombre,contrasena FROM usuarios')
        self.cursor.execute(query)
        #lista de elementos en el query
        cadena = [el for el in self.cursor]
        

        #buscando usuario y contrasena en base de datos y validando con elemntos en caja de texto usuario y password
        for elemento in range(len(cadena)):
            if cadena[elemento][0] == user and cadena[elemento][1] == contra:
                return True
    
    def AgregandoUsuario(self,clave,nombre,contrasena,email,puesto,descripion):
        try:
            query = ('INSERT INTO usuarios(id_usuario,nombre,contrasena,email,puesto,descripcion)VALUES(?,?,?,?,?,?)')
            self.cursor.execute(query,[clave,nombre,contrasena,email,puesto,descripion])
            self.cursor.commit()
        except:
            return "FALLO EN LA BASE DE DATOS"

    def ActualizarUsuario(self,clave,nombre,contrasena,email,puesto,descripion):
        try:
            query = ('UPDATE usuarios SET id_usuario=?,nombre=?,contrasena=?,email=?,puesto=?,descripcion=? WHERE id_usuario=?')
            self.cursor.execute(query,[clave,nombre,contrasena,email,puesto,descripion,clave])
            self.cursor.commit()
        except:
            return "FALLO EN LA BASE DE DATOS"

    def eliminandoUsuario(self,clave):
        try:
            query = ('DELETE FROM usuarios WHERE id_usuario=?')
            self.cursor.execute(query,[clave])
            self.cursor.commit()
        except:
            return "fallo la consulta"

    """
    ###########################################
    Manejo de la base de datos de los productos
    ###########################################
    """
    def MostarProductos(self):
        query = 'SELECT * FROM productos'
        return self.cursor.execute(query)
        
    def MostrarProducto(self,id):
        try:
            query = 'SELECT * FROM productos WHERE id_producto = ?'
            return self.cursor.execute(query,[id])
            
        except:
            return("Error en la base")

    
    """Usando datos de base para logear"""
    def ProductoExiste(self,id_producto):
        #agarrando los datos usuario y contrasena de la base
        query = ('SELECT id_producto FROM productos')
        self.cursor.execute(query)
        #lista de elementos en el query
        cadena = [el for el in self.cursor]
        

        #buscando usuario y contrasena en base de datos y validando con elemntos en caja de texto usuario y password
        for elemento in range(len(cadena)):
            if cadena[elemento][0] == id_producto:
                return True

    
    def AgregandoProducto(self,clave,tipo,nombre,precio,caducidad,lote,cantidad,imagen):
        try:
            query = ('INSERT INTO productos(id_producto,tipo,nombre,precio,caducidad,lote,cantidad,imagen)VALUES(?,?,?,?,?,?,?,?)')
            self.cursor.execute(query,[clave,tipo,nombre,precio,caducidad,lote,cantidad,imagen])
            self.cursor.commit()
        except:
            return "FALLO EN LA BASE DE DATOS"

    def ActualizarProducto(self,clave,tipo,nombre,precio,caducidad,lote,cantidad,imagen):
        try:
            query = ('UPDATE productos SET id_producto=?,tipo=?,nombre=?,precio=?,caducidad=?,lote=?,cantidad=?,imagen=? WHERE id_producto=?')
            self.cursor.execute(query,[clave,tipo,nombre,precio,caducidad,lote,cantidad,imagen,clave])
            self.cursor.commit()
        except:
            return "FALLO EN LA BASE DE DATOS"

    def eliminandoProducto(self,clave):
        try:
            query = ('DELETE FROM productos WHERE id_producto=?')
            self.cursor.execute(query,[clave])
            self.cursor.commit()
        except:
            return "fallo la consulta"

    def MostrarProductoVentas(self,id):
        try:
            query = 'SELECT id_producto,nombre,precio,cantidad,imagen FROM productos WHERE id_producto = ?'
            return self.cursor.execute(query,[id])
            
        except:
            return("Error en la base")

    """

    ###########################################
    Manejo de la base de datos de los proveedores
    ###########################################

    """
    def MostarProveedores(self):
        query = 'SELECT * FROM proveedores'
        return self.cursor.execute(query)
        
    def MostrarProveedor(self,id):
        try:
            query = 'SELECT * FROM proveedores WHERE id_proveedor = ?'
            return self.cursor.execute(query,[id])
            
        except:
            return("Error en la base")
    
    """Usando datos de base para logear"""
    def ProveedorExiste(self,id_proveedor):
        #agarrando los datos usuario y contrasena de la base
        query = ('SELECT id_proveedor FROM proveedores')
        self.cursor.execute(query)
        #lista de elementos en el query
        cadena = [el for el in self.cursor]
        

        #buscando usuario y contrasena en base de datos y validando con elemntos en caja de texto usuario y password
        for elemento in range(len(cadena)):
            if cadena[elemento][0] == id_proveedor:
                return True

    
    def AgregandoProveedor(self,clave,empresa,nombreProveedor,telefono,correo):
        try:
            query = ('INSERT INTO proveedores(id_proveedor,empresa,nombreproveedor,telefono,correo)VALUES(?,?,?,?,?)')
            self.cursor.execute(query,[clave,empresa,nombreProveedor,telefono,correo])
            self.cursor.commit()
        except:
            return "FALLO EN LA BASE DE DATOS"

    def ActualizarProveedor(self,clave,empresa,nombreProveedor,telefono,corre):
        try:
            query = ('UPDATE proveedores SET id_proveedor=?,empresa=?,nombreproveedor=?,telefono=?,correo=? WHERE id_proveedor=?')
            self.cursor.execute(query,[clave,empresa,nombreProveedor,telefono,corre,clave])
            self.cursor.commit()
        except:
            return "FALLO EN LA BASE DE DATOS"

    def eliminandoProveedor(self,clave):
        try:
            query = ('DELETE FROM proveedores WHERE id_proveedor=?')
            self.cursor.execute(query,[clave])
            self.cursor.commit()
        except:
            return "fallo la consulta"

    """ 
    #############################
    Tabla para manejo de facturas
    #############################
    """

    def MostarFacturas(self):
        query = 'SELECT * FROM facturas'
        return self.cursor.execute(query)
    
    def AgregandoFactura(self,clave,empresa,cantidad,calle,colonia):
        try:
            query = ('INSERT INTO facturas(id_factura,empresa,cantidadproducto,calle,colonia)VALUES(?,?,?,?,?)')
            self.cursor.execute(query,[clave,empresa,cantidad,calle,colonia])
            self.cursor.commit()
        except:
            return "FALLO EN LA BASE DE DATOS"

    def EditarFactura(self,clave,empresa,cantidad,calle,colonia):
        try:
            query = ('UPDATE facturas SET id_factura=?,empresa=?,cantidadproducto=?,calle=?,colonia=? WHERE id_factura=?')
            self.cursor.execute(query,[clave,empresa,cantidad,calle,colonia,clave])
            self.cursor.commit()
        except:
            return "FALLO EN LA BASE DE DATOS"

    def eliminandoFactura(self,clave):
        try:
            query = ('DELETE FROM facturas WHERE id_factura=?')
            self.cursor.execute(query,[clave])
            self.cursor.commit()
        except:
            return "fallo la consulta"


    """
    ###############################################
    Manejo Tabla Ventas
    ###############################################
    """
    def insertarVenta(self,codigo,producto,precio,cantidad,total):
        query = ('INSERT INTO ventas(codigo,producto,precio,cantidad,total)VALUES(?,?,?,?,?)')
        self.cursor.execute(query,[codigo,producto,precio,cantidad,total])
        self.cursor.commit()

    def MostarVentas(self):
        query = 'SELECT * FROM ventas'
        return self.cursor.execute(query)

    def eliminandoVenta(self):
        try:
            query = ('DELETE FROM ventas')
            self.cursor.execute(query)
            self.cursor.commit()
        except:
            return "fallo la consulta"


    """
    ###############################################
    Manejo Tabla Ventas
    ###############################################
    """
    def insertarInvercion(self,codigo,fecha,cantidad,total):
        query = ('INSERT INTO invercion(codigo_barras,fecha,cantidad,total)VALUES(?,?,?,?)')
        self.cursor.execute(query,[codigo,fecha,cantidad,total])
        self.cursor.commit()

    def MostrarInvercion(self):
        query = 'SELECT * FROM invercion'
        return self.cursor.execute(query)

    def eliminandoInvercion(self):
        try:
            query = ('DELETE FROM invercion')
            self.cursor.execute(query)
            self.cursor.commit()
        except:
            return "fallo la consulta"

