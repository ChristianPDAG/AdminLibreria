import pymysql
import os

class Libro:
    def __init__(self,id_libro,nombre_libro,editorial,estado):
        self.id_libro = id_libro
        self.nombre_libro = nombre_libro
        self.editorial = editorial
        self.estado = estado

    def agregarLibro():
        id_libro = 0
        nombre_libro = input("Ingrese el Nombre del Libro: ").capitalize()
        editorial = input("Ingrese la Editorial del Libro: ").capitalize()
        estado = "Disponible"
        libro = Libro(id_libro,editorial,nombre_libro,estado)
        os.system("cls")
        confirmacion = input(f"\nHaz ingresado los siguientes datos :\n {libro} \n \n¿Está seguro de agregar este libro? ( S/N )\n > ").upper()
        if confirmacion == "S":
            os.system("cls")
            conn = pymysql.connect(host="localhost", user="root", passwd="", database="bdbiblioteca")
            cursor = conn.cursor()
            sql = """INSERT INTO libro VALUES ( %s, %s, %s, %s)"""
            datos = [id_libro,editorial, nombre_libro,estado ]
            cursor.execute(sql, datos)
            conn.commit()
            conn.close()

            print("\nLibro creado exitosamente.")
        elif confirmacion == "N":
            os.system("cls")
            print ("\nCreación de libro cancelada. ")

        else:
            os.system("cls")
            print("Debe ingresar una opción válida > 'S' para Sí o 'N' para No <")
             

    def listarLibro():
            conn = pymysql.connect(host="localhost", user="root", passwd="", database="bdbiblioteca")
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM libro")
            libros = cursor.fetchall()
            conn.close()

            for libro in libros:
                print(Libro(libro[0], libro[1], libro[2],libro[3]))

    def updateLibro():
            
            nomEdit = input("¿Que desea modificar? (Nombre/Editorial/Eliminar/Estado): ").capitalize()

            if nomEdit == 'Nombre':
                idL = int(input("Ingrese ID de libro a modificar: "))
                nuevo = input("Ingrese el nuevo Nombre : ").capitalize()
                os.system("cls")
                confirmacion = input(f"\nHaz ingresado los siguientes datos :\nID: {idL} \nNombre/Editorial: {nomEdit} \nNuevo nombre: {nuevo} \n \n¿Está seguro de modificar este libro? ( S/N )\n > ").upper()
                if confirmacion == "S":

                    conn = pymysql.connect(host="localhost", user="root", passwd="", database="bdbiblioteca")
                    cursor = conn.cursor()
                    sql = """UPDATE libro SET nombre_libro = %s WHERE ID_LIBRO = %s"""
                    datos = (nuevo,idL)
                    cursor.execute(sql, datos)
                    conn.commit()
                    conn.close()
                    print("\nLibro modificado exitosamente.")

                elif confirmacion == "N":
                    os.system("cls")
                    print ("\nModificación de libro cancelada. ")

                else:
                    os.system("cls")
                    print("Debe ingresar una opción válida > 'S' para Sí o 'N' para No <")
                    

            elif nomEdit == 'Editorial':
                idL = int(input("Ingrese ID de libro a modificar: "))
                nuevo = input("Ingrese la nueva Editorial: ").capitalize()
                os.system("cls")
                confirmacion = input(f"\nHaz ingresado los siguientes datos :\n \nID: {idL} \nNombre/Editorial: {nomEdit} \nNuevo nombre: {nuevo} \n \n¿Está seguro de modificar este libro? ( S/N )\n > ").upper()
                if confirmacion == "S":

                    conn = pymysql.connect(host="localhost", user="root", passwd="", database="bdbiblioteca")
                    cursor = conn.cursor()
                    sql = """UPDATE libro SET editorial = %s WHERE ID_LIBRO = %s"""
                    datos = (nuevo,idL)
                    cursor.execute(sql, datos)
                    conn.commit()
                    conn.close()
                    print("\nLibro modificado exitosamente.")

                elif confirmacion == "N":
                    os.system("cls")
                    print ("\nModificación de libro cancelada. ")

                else:
                    os.system("cls")
                    print("Debe ingresar una opción válida > 'S' para Sí o 'N' para No <")

            elif nomEdit == "Eliminar":
                idL = int(input("Ingrese ID de libro a eliminar: "))
                conn = pymysql.connect(host="localhost", user="root", passwd="", database="bdbiblioteca")
                cursor = conn.cursor()
                sql =("""SELECT * FROM libro WHERE ID_LIBRO = %s""")
                datos =(idL)
                cursor.execute(sql,datos)
                libros = cursor.fetchall()
                print("\nEl siguiente libro será eliminado: ")
                for libro in libros:
                    print(Libro(libro[0], libro[1], libro[2]))

                    confirmacion = input("\n ¿Está seguro que desea eliminarlo? (S/N) \n > ").upper()
                    if confirmacion == 'S':
                        sql = """DELETE FROM libro WHERE ID_LIBRO = %s"""
                        datos = (idL)
                        cursor.execute(sql, datos)
                        conn.commit()
                        conn.close()
                        print("\nLibro eliminado exitosamente.")
                    
                    elif confirmacion == 'N':
                        os.system("cls")
                        print ("\nEliminación de libro cancelada. ")

                    else:
                        os.system("cls")
                        print("Debe ingresar una opción válida > 'S' para Sí o 'N' para No <")

            elif nomEdit == "Estado":
                idL = int(input("Ingrese ID de libro a modificar 'Estado': "))
                nuevoEstado = input("Ingrese nuevo 'Estado': ").capitalize()
                conn = pymysql.connect(host="localhost", user="root", passwd="", database="bdbiblioteca")
                cursor = conn.cursor()
                sql =("""SELECT * FROM libro WHERE ID_LIBRO = %s""")
                datos =(idL)
                cursor.execute(sql,datos)
                libros = cursor.fetchall()
                print("\nEl siguiente libro será modificado: ")
                for libro in libros:
                    print(Libro(libro[0], libro[1], libro[2],libro[3]))

                    confirmacion = input("\n ¿Está seguro que desea modificarlo? (S/N) \n > ").upper()
                    if confirmacion == 'S':
                        sql = """UPDATE libro SET estado_libro = %s WHERE id_libro = %s """
                        datos = (nuevoEstado,idL)
                        cursor.execute(sql, datos)
                        conn.commit()
                        conn.close()
                        print("\nLibro modificado exitosamente.")
                    
                    elif confirmacion == 'N':
                        os.system("cls")
                        print ("\nEliminación de libro cancelada. ")

                    else:
                        os.system("cls")
                        print("Debe ingresar una opción válida > 'S' para Sí o 'N' para No <")


            else:
                os.system("cls")
                print("Debe ingresar una opción válida...")

    def __str__(self):
        return f"\nID: {self.id_libro} \nTitulo: {self.editorial} \nEditorial: {self.nombre_libro} \nEstado: {self.estado}"

    