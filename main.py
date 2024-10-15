
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

    # Crear una nueva celda primero
    Celda.crear_celda(conexion, "Medellin", 5, "Disponible")

    # Luego crear un nuevo interno, utilizando el ID de la celda creada (asumimos que es 1 por simplicidad)
    Interno.crear_interno(conexion, "Juan Perez", datetime.date(2023, 10, 1), "Activo", 1)


    # Leer internos
    #Interno.leer_internos(conexion)

    # Actualizar un interno
    #Interno.actualizar_interno(conexion, 1, "Liberado")

    # Eliminar un interno
    #Interno.eliminar_interno(conexion, 1)

    # Cerrar la conexión
    conexion.cerrar()