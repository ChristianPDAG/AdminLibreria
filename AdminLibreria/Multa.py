import os
import pymysql
from datetime import datetime
from Prestamomodi import *

class Multa:
    def __init__(self,id_multa,dias_retraso):
        self.id_multa = id_multa
        self.dias_retraso = dias_retraso

    def calcular_retraso(idPrestamo):
        conn = pymysql.connect(host="localhost", user="root", passwd="", database="bdbiblioteca")
        cursor = conn.cursor()
        sql = """SELECT fecha_devolucion FROM prestamo WHERE id_prestamo = %s"""
        sql1 = """SELECT libro_devuelto FROM prestamo WHERE id_prestamo = %s"""
        cursor.execute(sql,(idPrestamo,))
        fechaP = cursor.fetchall()
        for fila in fechaP:
                fecha_devolucion = str(fila[0])
                cursor.execute(sql1,(idPrestamo,))
                fechaD = cursor.fetchall()
                for fila in fechaD:
                    fecha_devuelto = str(fila[0])
                    fecha1 = datetime.strptime(fecha_devolucion, '%Y-%m-%d')
                    fecha2 = datetime.strptime(fecha_devuelto, '%Y-%m-%d')
                    fecha1 = int(fecha1.strftime('%Y%m%d'))
                    fecha2 = int(fecha2.strftime('%Y%m%d'))
                    dias_retraso = (fecha2 - fecha1) 
                    return dias_retraso

    def calcular_multa(idPrestamo):
        conn = pymysql.connect(host="localhost", user="root", passwd="", database="bdbiblioteca")
        cursor = conn.cursor()
        deuda = Multa.calcular_retraso(idPrestamo) * 1000
        return deuda

    def listar_multa():
         pass
        


              
def __str__(self):
        return f"ID: {self.id_multa}\n Días de retraso: {self.dias_retraso}"

