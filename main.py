
# main.py

import datetime
from common.conexion import Conexion
from controller.interno import InternoController
from controller.celda import CeldaController

if __name__ == '__main__':
    conexion = Conexion()
    Interno = InternoController()
    Celda = CeldaController()
    conexion.conectar()
    conexion.cerrar()