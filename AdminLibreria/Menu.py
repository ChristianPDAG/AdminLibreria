import os
os.system("cls")
from Libro import *
from Usuario import *
from Prestamomodi import *

from datetime import datetime

import pymysql



def menu():
    continuar = True
    os.system("cls")
    print("---- [ MENÚ ADMINISTRADOR ] ------ \n")
    print("1. Usuarios registrados ")
    print("2. Libros registrados ")
    print("3. Registrar usuario")
    print("4. Registrar libro")
    print("5. Modificar o eliminar libros")
    print("6. Préstamos por usuario-RUT")
    print("7. Renovación de préstamo")
    print("8. Registrar préstamo")
    print("9. Historial de préstamos")
    print("10. Devolver libro")
    print("11. Salir \n ")
    op = int(input("Ingrese una opción entre 1 y 10 \n > "))

    if op == 1:
        while True:
            os.system("cls")
            print("--- [ USUARIOS REGISTRADOS ] --- \n  ")
            Usuario.listarUsuario()
            input("\nPresione Enter para volver al menú...")
            break

    elif op == 2:
        while True:
            os.system("cls")
            print("--- [ LIBROS REGISTRADOS ] --- \n  ")
            Libro.listarLibro()
            input("\nPresione Enter para volver al menú...")
            break
        
    elif op == 3:
        while True:
            os.system("cls")
            print("--- [ REGISTRAR NUEVO USUARIO ] ---\n")
            Usuario.agregarUsuario()
            input("\nPresione Enter para volver al menú...")
            break

    elif op ==4:
        while True:
            os.system("cls")
            print("--- [ REGISTRAR NUEVO LIBRO ] ---\n")
            Libro.agregarLibro()
            input("\nPresione Enter para volver al menú...")
            break

    elif op ==5:
        while True:
            os.system("cls")
            print("--- [ MODIFICAR / ELIMINAR LIBRO ] ---\n")
            Libro.updateLibro()
            input("\nPresione Enter para volver al menú...")
            break

    elif op ==6:
        while True:
            os.system("cls")
            print("--- [ BUSCAR PRÉSTAMOS POR RUT ] ---\n")
            Prestamo.buscar_prestamos()
            input("\nPresione Enter para volver al menú...")  
            break

    elif op ==7:
        while True:
            os.system("cls")  
            print("--- [ RENOVACIÓN DE PRÉSTAMO ] ---\n")
            Prestamo.renovacion()
            input("\nPresione Enter para volver al menú...")  
            break
    
    elif op ==8 :
        while True:
            os.system("cls")
            print("--- [ REGISTRAR PRÉSTAMO ] ---\n")
            Prestamo.registrar_prestamo()
            input("\nPresione Enter para volver al menú...")  
            break
    
    elif op ==9 :
        while True:
            os.system("cls")
            print("--- [ HISTORIAL DE PRÉSTAMOS ] ---\n")
            Prestamo.historial_prestamos()
            input("\nPresione Enter para volver al menú...")  
            break

    elif op==10:
        while True:
            os.system("cls")
            print("--- [ DEVOLUCIÓN DE LIBRO ] ---")
            Prestamo.devolver_libro()
            input("\nPresione Enter para volver al menú...")  
            break


    elif op == 11:
        continuar = False

    return continuar



def programa():
    os.system("cls")
    print("--- [ INGRESO ADMINISTRADOR ] ---\n")
    conn = pymysql.connect(host="localhost", user="root", passwd="", database="bdbiblioteca")
    cursor = conn.cursor()
    ingreso = input("Ingrese RUT:\n > ")
    sql_select = """SELECT * FROM usuario WHERE rut = %s AND tipo_usuario = 'Bibliotecario' """
    cursor.execute(sql_select, ingreso) 
    resultado = cursor.fetchone()
    if resultado:
        while menu():
            print()
    else:
        os.system("cls")
        input("USUARIO INGRESADO NO CUENTA CON PERMISOS SUFICIENTES PARA INGRESAR\n \n  Presione Enter para volver a intentar...")
        return programa()

# Ejecución del programa
programa()
