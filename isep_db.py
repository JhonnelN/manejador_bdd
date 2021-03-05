import mysql.connector
import os
import json

from dotenv import load_dotenv
from pathlib import Path  # Python 3.6+ only

env_path = Path(".") / ".env"
load_dotenv(dotenv_path=env_path)

# Datos de conexion
host = os.getenv("DB_HOST")
user = os.getenv("DB_USER")
password = os.getenv("DB_PASS")
db = os.getenv("DB_NAME")


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
    mycursor.execute(
        "alter table leads add foreign key (id_usuario) references usuarios(id)"
    )
    mycursor.execute(
        "alter table leads add foreign key (id_ventas) references equipos_ventas(id)"
    )


# usuario:
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
    mycursor.execute(
        "DELETE FROM usuarios WHERE id =" + repr(id)
    )  # la funcion repr() permite concadenar int con str
    mydb.commit()


def mod_usuario(id, nombre, telefono, correo, direccion):
    mydb = conectar_db()
    mycursor = mydb.cursor()
    sql = "UPDATE usuarios SET nombre = %s, telefono = %s, correo = %s, address = %s WHERE id= %s"
    mycursor.execute(sql, (nombre, telefono, correo, direccion, id))
    mydb.commit()


# Ventas:
def crear_gventas(nombre):
    mydb = conectar_db()
    mycursor = mydb.cursor()
    mycursor.execute(
        "INSERT INTO equipos_ventas (id, nombre) VALUES (NULL, '" + nombre + "')"
    )
    mydb.commit()


def eliminar_gventas(id):
    mydb = conectar_db()
    mycursor = mydb.cursor()
    mycursor.execute(
        "DELETE FROM equipos_ventas WHERE id =" + repr(id)
    )  # la funcion repr() permite concadenar int con str
    mydb.commit()


def mod_gventas(id, nombre):
    mydb = conectar_db()
    mycursor = mydb.cursor()
    sql = "UPDATE equipos_ventas SET nombre = %s WHERE id= %s"
    mycursor.execute(sql, (nombre, id))
    mydb.commit()


# Leads:
# usuario:
def crear_lead(
    nombre, telefono, correo, direccion, id_usuario, id_ventas, notas, producto
):
    mydb = conectar_db()
    mycursor = mydb.cursor()
    sql = "INSERT INTO leads (nombre, telefono, correo, address, id_usuario, id_ventas, notas, producto) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
    val = (nombre, telefono, correo, direccion, id_usuario, id_ventas, notas, producto)
    mycursor.execute(sql, val)
    mydb.commit()


def eliminar_lead(id):
    mydb = conectar_db()
    mycursor = mydb.cursor()
    mycursor.execute(
        "DELETE FROM leads WHERE id =" + repr(id)
    )  # la funcion repr() permite concadenar int con str
    mydb.commit()


def mod_lead(
    id, nombre, telefono, correo, direccion, id_usuario, id_ventas, notas, producto
):
    mydb = conectar_db()
    mycursor = mydb.cursor()
    sql = "UPDATE leads SET nombre = %s, telefono = %s, correo = %s, address = %s WHERE id= %s"
    mycursor.execute(sql, (nombre, telefono, correo, direccion, id))
    mydb.commit()


# consultar
def consultar(campo, tabla):
    mydb = conectar_db()
    mycursor = mydb.cursor()
    mycursor.execute("SELECT " + campo + " FROM " + tabla)
    consulta = mycursor.fetchall()
    json_output = json.dumps(consulta)
    return json_output


print(consultar("nombre", "leads"))
