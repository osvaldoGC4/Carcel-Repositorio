
# main.py

import datetime
from common.conexion import Conexion
from controller.interno import InternoController
from controller.celda import CeldaController

if __name__ == '__main__':
    conexion = Conexion()
    Interno = InternoController()
    Celda = CeldaController()
    Celda.crear_celda(1, "Medellin",5,"Disponible")
    #conexion.conectar()
    #conexion.cerrar()