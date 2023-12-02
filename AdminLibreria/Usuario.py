import os
os.system("cls")
from Libro import *
import pymysql

# Definición de la clase Usuario
class Usuario:
    def __init__(self, rut, nombre, email, direccion, telefono, tipo):
        self.rut = rut
        self.nombre = nombre
        self.email = email
        self.direccion = direccion
        self.telefono = telefono
        self.tipo = tipo

    def guardar_en_bd(self):
        conn = pymysql.connect(host="localhost", user="root", passwd="", database="bdbiblioteca")
        cursor = conn.cursor()
        sql = "INSERT INTO usuario VALUES (%s, %s, %s, %s, %s, %s)"
        datos = [self.rut, self.nombre, self.email, self.direccion, self.telefono, self.tipo]
        cursor.execute(sql, datos)
        conn.commit()
        conn.close()

    def eliminarusu(self):
        rut = input("ingrese rut usuario a eliminar: ")
        conn = pymysql.connect(host="localhost", user="root", passwd="", database="bdbiblioteca")
        cursor = conn.cursor()
        sql = "DELETE FROM usuario WHERE rut = %s"
        cursor.execute(sql, (rut,))
        usuarios = cursor.fetchall()
        conn.close()
        print("eliminado correctamente:")

    def agregarUsuario():
        conn = pymysql.connect(host="localhost", user="root", passwd="", database="bdbiblioteca")
        cursor = conn.cursor()
        rut = input("Ingrese el rut: ")
        nombre = input("Ingrese el nombre: ").capitalize()
        email = input("Ingrese el mail: ")
        direccion = input("Ingrese la direccion: ").capitalize()
        telefono = input("Ingrese el telefono: ")
        tipo = input("¿Qué tipo de usuario es? (alumno/docente): ").capitalize()

        usuario = Usuario(rut, nombre, email, direccion, telefono, tipo)
        os.system("cls")
        confirmacion = input(f"\nHaz ingresado los siguientes datos:\n {usuario} \n \n¿Está seguro de agregar este usuario? (S/N)\n > ").upper()

        if confirmacion == "S":
            os.system("cls")
            sql_select = "SELECT * FROM usuario WHERE rut = %s"
            cursor.execute(sql_select, (rut,))
            resultado = cursor.fetchone()

            if resultado:
                print("El usuario ya está registrado.")
                return

           
            usuario.guardar_en_bd()
            print("\nUsuario creado exitosamente.")

        elif confirmacion == "N":
            os.system("cls")
            print("\nCreación de usuario cancelada.")

        else:
            os.system("cls")
            print("Debe ingresar una opción válida > 'S' para Sí o 'N' para No <")


    def listarUsuario():
        conn = pymysql.connect(host="localhost", user="root", passwd="", database="bdbiblioteca")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM usuario")
        usuarios = cursor.fetchall()
        conn.close()

        for usuario in usuarios:
            print(Usuario(usuario[0], usuario[1], usuario[2], usuario[3], usuario[4], usuario[5]))
        

    def __str__(self):
        return f"\nRut: {self.rut} \nNombre: {self.nombre}\nEmail: {self.email} \nDireccion: {self.direccion}\nTelefono: {self.telefono}\nTipo: {self.tipo}"
