import pymysql
from datetime import datetime
import os
from Multa import *

class Prestamo:
    def __init__(self, id_prestamo, fecha_prestamo, fecha_devolucion, renovacion, rut, id_libro):
        self.id_prestamo = id_prestamo
        self.fecha_prestamo = fecha_prestamo
        self.fecha_devolucion = fecha_devolucion
        self.renovacion = renovacion
        self.rut = rut
        self.id_libro = id_libro

    def guardar_prestamo(self):
        conn = pymysql.connect(host="localhost", user="root", passwd="", database="bdbiblioteca")
        cursor = conn.cursor()

        query_prestamo = "INSERT INTO prestamo (id_prestamo, fecha_prestamo, fecha_devolucion, renovacion, rut, libro_devuelto) VALUES (%s, %s, %s, NULL, %s, '0000-00-00')"
        valores_prestamo = (self.id_prestamo, self.fecha_prestamo, self.fecha_devolucion, self.rut)
        cursor.execute(query_prestamo, valores_prestamo)

        id_prestamo = cursor.lastrowid

        id_detalle= cursor.lastrowid
        query_detalle = "INSERT INTO detalle_prestamo (id_detalle,id_prestamo, id_libro) VALUES (%s,%s, %s)"
        valores_detalle = (id_detalle,id_prestamo, self.id_libro)
        cursor.execute(query_detalle, valores_detalle)

        conn.commit()
        cursor.close()
        conn.close()


    def registrar_prestamo():
        conn = pymysql.connect(host="localhost", user="root", passwd="", database="bdbiblioteca")
        cursor = conn.cursor()
        id_prestamo = 0
        tiempo_prestamo = 0
        rut = input("Ingrese el rut del usuario: ")
        sql = """SELECT * FROM usuario WHERE rut = %s"""
        rutExiste = cursor.execute(sql,rut)
        if rutExiste == True:
            while True:
                id_libro = int(input("Ingrese el ID del libro: "))
                sql5 = """SELECT * FROM libro WHERE id_libro = %s AND estado_libro = 'En prestamo'"""
                datos = [id_libro]
                cursor.execute(sql5,datos)
                enPrestamo = cursor.fetchone()
                if enPrestamo:
                    print("\n--- [ ERROR: LIBRO EN PRESTAMO ] ---\n \nIngrese un libro disponible \n")
                    input("\n  Presione Enter para volver a ingresar los datos...")
                    os.system("cls")
                else:
                    sql2 = """SELECT * FROM libro WHERE id_libro = %s"""
                    libroExiste = cursor.execute(sql2,id_libro)
                    if libroExiste == True:
                        sql_select = """SELECT * FROM usuario WHERE rut = %s AND tipo_usuario = 'Alumno' """
                        sql_select2 = """SELECT * FROM usuario WHERE rut = %s AND tipo_usuario = 'Docente' """
                        alumno = cursor.execute(sql_select, rut) 
                        docente = cursor.execute(sql_select2, rut) 
                        if alumno == True:
                            fecha_prestamo = input("Ingrese la fecha de préstamo: (AAAA-MM-DD) ")
                            fecha_devolucion = input("Ingrese la fecha de devolución: (AAAA-MM-DD) ")
                            sql3 = """SELECT * FROM prestamo p INNER JOIN detalle_prestamo dp on p.id_prestamo=dp.id_prestamo WHERE rut = %s AND id_libro = %s AND fecha_prestamo = %s"""
                            datos = [rut,id_libro,fecha_prestamo]
                            cursor.execute(sql3,datos)
                            prestamoExiste = cursor.fetchone()
                            if prestamoExiste: #Validación para que no se pueda prestar más de un ejemplar del mismo libro
                                input("\nERROR: Prestamo de libro EXISTE, [ No se puede pedir más un ejemplar del mismo libro ]\n OPERACIÓN CANCELADA")
                                os.system("cls")
                                break
                            else: #FORMULA: tiempo_prestamo = días solicitados
                                fecha1 = datetime.strptime(fecha_prestamo, '%Y-%m-%d')
                                fecha2 = datetime.strptime(fecha_devolucion, '%Y-%m-%d')
                                fecha1 = int(fecha1.strftime('%Y%m%d'))
                                fecha2 = int(fecha2.strftime('%Y%m%d'))
                                tiempo_prestamo = fecha2 - fecha1
                                if tiempo_prestamo <= 7:#Validación para no permitir prestar por más de 7 días
                                    renovacion = None
                                    prestamo = Prestamo(id_prestamo, fecha_prestamo, fecha_devolucion, renovacion, rut, id_libro)
                                    prestamo.guardar_prestamo()
                                    sql4 = """UPDATE libro SET estado_libro = 'En prestamo' WHERE id_libro = %s """
                                    datoss = [ id_libro]
                                    cursor.execute(sql4,datoss)
                                    conn.commit()
                                    print("\nEl prestamo ha sido registrado exitosamente.\n")
                                    print(f'Fecha prestamo: {fecha_prestamo}\nFecha devolución: {fecha_devolucion}')
                                    otroPrestamo = input("\n¿Desea pedir otro libro? (S/N) \n > ").upper()
                                    if otroPrestamo =='S':
                                        input(f"Enter para registrar otro prestamo para el usuario RUT: {rut}")
                                        os.system("cls")
                                    elif otroPrestamo == 'N':
                                        break
                                else:
                                    print("-- [ ERROR: CANTIDAD DE DÍAS INVALIDO ] ---")
                                    print("\nEl límite para el tipo de usuario 'Alumno' es 7 días, por favor ingrese una fecha de devolución válida\n" )
                                    input("\n  Presione Enter para volver a ingresar los datos...")
                                    os.system("cls")
                                
                                
                        
                        if docente == True:
                            fecha_prestamo = input("Ingrese la fecha de préstamo: (AAAA-MM-DD) ")
                            fecha_devolucion = input("Ingrese la fecha de devolución: (AAAA-MM-DD) ")
                            sql3 = """SELECT * FROM prestamo p INNER JOIN detalle_prestamo dp on p.id_prestamo=dp.id_prestamo WHERE rut = %s AND id_libro = %s AND fecha_prestamo = %s"""
                            datos = [rut,id_libro,fecha_prestamo]
                            cursor.execute(sql3,datos)
                            prestamoExiste = cursor.fetchone()
                            if prestamoExiste:
                                input("\nERROR: Prestamo de libro EXISTE, [ No se puede pedir más un ejemplar del mismo libro ]\n OPERACIÓN CANCELADA")
                                os.system("cls")
                                break
                            else:
                                fecha1 = datetime.strptime(fecha_prestamo, '%Y-%m-%d')
                                fecha2 = datetime.strptime(fecha_devolucion, '%Y-%m-%d')

                                fecha1 = int(fecha1.strftime('%Y%m%d'))
                                fecha2 = int(fecha2.strftime('%Y%m%d'))
                                tiempo_prestamo = fecha2 - fecha1
                                if tiempo_prestamo >= 7 and tiempo_prestamo <= 20 :
                                    renovacion = None
                                    prestamo = Prestamo(id_prestamo, fecha_prestamo, fecha_devolucion, renovacion, rut, id_libro)
                                    prestamo.guardar_prestamo()
                                    sql4 = """UPDATE libro SET estado_libro = 'En prestamo' WHERE id_libro = %s """
                                    datos = [ id_libro]
                                    cursor.execute(sql4,datos)
                                    conn.commit()
                                    print("\nEl prestamo ha sido registrado exitosamente.\n")
                                    print(f'Fecha prestamo: {fecha_prestamo}\nFecha devolución: {fecha_devolucion}')
                                    otroPrestamo = input("\n¿Desea pedir otro libro? (S/N) \n > ").upper()
                                    if otroPrestamo =='S':
                                        input(f"Enter para registrar otro prestamo para el usuario RUT: {rut}...")
                                        os.system("cls")
                                    elif otroPrestamo == 'N':
                                        break
                                else:
                                    print("-- [ ERROR: CANTIDAD DE DÍAS INVALIDO ] ---")
                                    print("\nEl mínimo para el tipo de usuario 'Docente' es 7 días y máximo 20 días, por favor ingrese una fecha de devolución válida\n" )
                                    input("\n  Presione Enter para volver a ingresar los datos...")
                                    os.system("cls")
                    else:
                        print("\n--- [ ERROR: LIBRO NO REGISTRADO] ---\n \nIngrese un libro registrado \n")
                        input("\n  Presione Enter para volver a ingresar los datos...")
                        os.system("cls")

        else:
            print("\n--- [ ERROR: RUT DE USUARIO NO REGISTRADO ] ---\n \nIngrese un RUT de usuario registrado \n")
            input("\n  Presione Enter para volver a ingresar los datos...")
            os.system("cls")
            return Prestamo.registrar_prestamo()
            
    def buscar_prestamos():
        conn = pymysql.connect(host="localhost", user="root", passwd="", database="bdbiblioteca")
        cursor = conn.cursor()
        rut = input("Ingrese RUT de usuario: ")
        sql = """SELECT DISTINCT u.rut,  u.nombre, u.email, u.telefono  FROM prestamo p INNER JOIN usuario u on u.rut=p.rut  INNER JOIN detalle_prestamo dp on dp.id_prestamo = p.id_prestamo INNER JOIN libro l on l.id_libro=dp.id_libro WHERE u.rut = %s"""
        cursor.execute(sql,rut)
        usuarios = cursor.fetchall()
        
        sql2 = """SELECT  l.NOMBRE_LIBRO, p.fecha_prestamo, p.fecha_devolucion FROM prestamo p INNER JOIN usuario u ON u.rut = p.rut INNER JOIN detalle_prestamo dp ON dp.id_prestamo = p.id_prestamo INNER JOIN libro l ON l.id_libro = dp.id_libro WHERE u.rut = %s"""
        cursor.execute (sql2,rut)
        libros = cursor.fetchall()

        sql3 = """SELECT * FROM prestamo p INNER JOIN usuario u ON u.rut = p.rut INNER JOIN detalle_prestamo dp ON dp.id_prestamo = p.id_prestamo INNER JOIN libro l ON l.id_libro = dp.id_libro WHERE u.rut = %s """
        cursor.execute(sql3,rut)
        prestamos = cursor.fetchall()
        for usuario in usuarios:
            rut, nombre, email, telefono = usuario
            print("\n--- [ DATOS USUARIO ] ---")
            print(f"\nRUT: {rut}\nNombre: {nombre}\nEmail: {email}\nTeléfono: {telefono}")

        print("\n--- [ PRESTAMOS ] ---")
        for libro in libros:
            nombre_libro, fecha_prestamo, fecha_devolucion = libro    
            print(f"\n Libro: {nombre_libro}\nFecha de préstamo: {fecha_prestamo}\nFecha de devolución: {fecha_devolucion}")

        for prestamo in prestamos:
            titulo_libro = prestamo[17]
            id_prestamo = prestamo [0]
            id_devuelto = prestamo[5]
            if  id_devuelto == '0000-00-00':
                print("\n--- [ NO POSEE DEUDAS ] ---")
            else:
                if Multa.calcular_retraso(id_prestamo) > 0:
                        print("\n--- [ DEUDAS ] ---")
                        print(f"Título: {titulo_libro}, Días de retraso: {Multa.calcular_retraso(id_prestamo)}, Monto: {Multa.calcular_multa(id_prestamo)}")
                else:
                        print("--- [ NO POSEE DEUDAS ] ---")
        cursor.close()
        conn.close()

    def renovacion():
        conn = pymysql.connect(host="localhost", user="root", passwd="", database="bdbiblioteca")
        cursor = conn.cursor()
        idPrestamo = int(input("Ingrese ID de prestamo a renovar: "))
        nuevaFecha = input("Ingrese nueva fecha de devolución: ")
        
        sql2 = """SELECT rut FROM prestamo WHERE id_prestamo = %s """
        cursor.execute(sql2,(idPrestamo,))
        ruts = cursor.fetchall()
        for rut in ruts:
            rut = str(rut[0])

            sql_select = """SELECT * FROM usuario WHERE rut = %s AND tipo_usuario = 'Alumno' """
            sql_select2 = """SELECT * FROM usuario WHERE rut = %s AND tipo_usuario = 'Docente' """
            cursor.execute(sql_select, (rut,) )
            alumno = cursor.fetchone()

            cursor.execute(sql_select2, (rut,)  )
            docente = cursor.fetchone()
        if alumno:
                sql = """SELECT fecha_devolucion FROM prestamo WHERE id_prestamo = %s"""
                cursor.execute(sql,(idPrestamo,))
                resultados = cursor.fetchall()
                for fila in resultados:
                        fecha_devolucion = str(fila[0])

                        fecha1 = datetime.strptime(fecha_devolucion, '%Y-%m-%d')
                        fecha2 = datetime.strptime(nuevaFecha, '%Y-%m-%d')
                        fecha1 = int(fecha1.strftime('%Y%m%d'))
                        fecha2 = int(fecha2.strftime('%Y%m%d'))
                        tiempo_renovacion = fecha2 - fecha1
                
                if tiempo_renovacion > 3 or tiempo_renovacion <= 0:
                    print("\n--- [ ERROR: EXCEDE TIEMPO DE RENOVACION ] ---")
                    input("\n  Presione Enter para volver al inicio...")
                    os.system("cls")
                
                else:
                    sql = """UPDATE prestamo SET renovacion = %s WHERE id_prestamo = %s """
                    datos = [nuevaFecha,idPrestamo]
                    cursor.execute(sql,datos)
                    conn.commit()    
                    print("\nLa renovación ha sido registrado exitosamente.\n")

        if docente:
            sql = """UPDATE prestamo SET renovacion = '%s' WHERE id_prestamo = %s """
            datos = [nuevaFecha,idPrestamo]
            cursor.execute(sql,datos)
            conn.commit()    
            print("\nLa renovación ha sido registrado exitosamente.\n")

      

    def historial_prestamos():
        conn = pymysql.connect(host="localhost", user="root", passwd="", database="bdbiblioteca")
        cursor = conn.cursor()
        diaEspecifico = input("Ingrese fecha de préstamo del libro: (YYYY/MM/DD) ")
        tipoUsuario = input("Ingrese tipo de usuario: (Alumno/Docente) ").capitalize()

        sql = """SELECT * FROM prestamo p INNER JOIN usuario u on p.rut=u.rut INNER JOIN detalle_prestamo dp on dp.id_prestamo=p.id_prestamo INNER JOIN libro l on l.id_libro=dp.id_libro WHERE tipo_usuario = %s AND fecha_prestamo = %s"""
        datos = [tipoUsuario,diaEspecifico]
        cursor.execute(sql,datos)
        prestamos = cursor.fetchall()
        for prestamo in prestamos:        
            id_prestamo = prestamo[0]
            fecha_prestamo = prestamo[1]
            fecha_devolucion = prestamo[2]
            renovacion = prestamo[3]
            rut = prestamo[4]
            devuelto = prestamo[5]
            nombre = prestamo[7]
            email = prestamo[8]
            direccion = prestamo[9]
            telefono = prestamo[10]
            tipo_usuario = prestamo[11]
            editorial_libro = prestamo[16]
            nombre_libro = prestamo[17]
            estado_libro = prestamo[18]

            print()
            print("ID de préstamo:", id_prestamo)
            print("Título del libro:", nombre_libro)
            print("Editorial:", editorial_libro)
            print("Estado libro:", estado_libro)
            print("Fecha de préstamo:", fecha_prestamo)
            print("Fecha de devolución:", fecha_devolucion)
            print("Renovación:", renovacion)
            print("RUT:", rut)
            print("Nombre:", nombre)
            print("Email:", email)
            print("Dirección:", direccion)
            print("Teléfono:", telefono)
            print("Tipo de usuario:", tipo_usuario)
            

    def devolver_libro():
        conn = pymysql.connect(host="localhost", user="root", passwd="", database="bdbiblioteca")
        cursor = conn.cursor()
        idPrestamo = int(input("Ingrese ID del préstamo: "))
        diaDevuelto = input("Ingrese fecha de día que devuelve el libro: (YYYY/MM/DD) ")
        9,10,11
        sqlLibro = """SELECT * FROM prestamo p INNER JOIN detalle_prestamo dp ON dp.id_prestamo=p.id_prestamo INNER JOIN libro l ON l.id_libro=dp.id_libro WHERE p.id_prestamo = %s"""
        cursor.execute(sqlLibro,idPrestamo)
        libros = cursor.fetchall()
        
        for libro in libros:
            id_libro = libro[9]
            nombre_libro = libro[11]
            editorial_libro = libro[10]
            print("\nVerifique que los datos del libro sean correctos:")
            print(f"\nID: {id_libro}\nTítulo: {nombre_libro}\nEditorial: {editorial_libro}")
            confirmacion = input(f"\n¿Desea confirmar la devolución del libro? ( S/N )\n > ").upper()
            if confirmacion == 'S':
                sql = """UPDATE prestamo SET libro_devuelto = %s WHERE id_prestamo = %s"""
                datos = [ diaDevuelto, idPrestamo]
                cursor.execute(sql,datos)                
                cursor.execute(f"""UPDATE libro SET estado_libro = 'Disponible' WHERE id_libro = {id_libro} """)
                conn.commit()
                print("\nEl libro ha sido devuelto exitosamente.\n")
            else:
                print("--- [ DEVOLUCIÓN CANCELADA ] ---")
                input("\n  Presione Enter para volver al inicio...")
                os.system("cls")

    def __str__(self):
        return f"ID Prestamo: {self.id_prestamo}\nFecha préstamo: {self.fecha_prestamo}\nFecha devolución: {self.fecha_devolucion}\nRenovación: {self.renovacion}\nRUT: {self.rut}\nID Libro: {self.id_libro}"
    
    