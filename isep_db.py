import mysql.connector

host = "localhost"
user = "isep"
password = "isep"
db = "isep5"


# crea bd
def crear_db(nombre):
    # conecta al gestor de db
    mydb = mysql.connector.connect(host=host, user=user, password=password)
    mycursor = mydb.cursor()
    mycursor.execute("CREATE DATABASE " + nombre)
    
# conectar a bd
def conectar_db():
    mydb = mysql.connector.connect(host=host, user=user, password=password, database=db)
    mycursor = mydb.cursor()
    return mydb

# scrip crear tablas
def crear_tablas():
    # Tabla1 usuarios
    mycursor.execute(
        "CREATE TABLE usuarios (id INT AUTO_INCREMENT PRIMARY KEY, nombre VARCHAR(120),  telefono VARCHAR(255),  correo VARCHAR(100), address VARCHAR(255)) ENGINE=INNODB"
    )
    # Tabla2 equipo de ventas
    mycursor.execute(
        "CREATE TABLE equipos_ventas (id INT AUTO_INCREMENT PRIMARY KEY, nombre VARCHAR(120)) ENGINE=INNODB"
    )
    # Tabla 3 leads
    mycursor.execute(
        "CREATE TABLE leads (id INT AUTO_INCREMENT PRIMARY KEY, nombre VARCHAR(120),  telefono VARCHAR(255),  correo VARCHAR(100), address VARCHAR(255), id_usuario INT(11), id_ventas INT(11), notas VARCHAR(255), producto VARCHAR(255)) ENGINE=INNODB"
    )
    mycursor.execute( "alter table leads add foreign key (id_usuario) references usuarios(id)")
    mycursor.execute( "alter table leads add foreign key (id_ventas) references equipos_ventas(id)")

#usuario:
def crear_usuario(nombre, telefono, correo, direccion):
    mydb = conectar_db()
    mycursor = mydb.cursor()
    sql = "INSERT INTO usuarios (nombre, telefono, correo, address) VALUES (%s, %s,%s, %s)"
    val = (nombre, telefono, correo, direccion)
    mycursor.execute(sql, val)
    mydb.commit()

def eliminar_usuario(id):
    mydb = conectar_db()
    mycursor = mydb.cursor()
    mycursor.execute("DELETE FROM usuarios WHERE id ="+repr(id)) # la funcion repr() permite concadenar int con str
    mydb.commit()

def mod_usuario(id, nombre, telefono, correo, direccion):
    mydb = conectar_db()
    mycursor = mydb.cursor()
    #val = ("nombre=" + nombre + ", telefono=" + telefono + ", correo=" + correo + ", address= " + direccion)
    sql = ("UPDATE usuarios SET nombre = %s, telefono = %s, correo = %s, address = %s WHERE id= %s")
    mycursor.execute(sql, (nombre, telefono, correo, direccion, id))
    mydb.commit()

#mod_usuario(3, "Jhonnel", "0424", "mail@mail.com", "direccion")
#crear_usuario("Jhon2", "0424", "mail@mail.com", "direccion")
#eliminar_usuario(2)
#class Leads:
#    def cargar(nombre, telefono, correo, direccion, id_user, id_ventas)