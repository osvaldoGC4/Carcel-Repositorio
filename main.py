# main.py
from common.conexion import Conexion
from controller.interno import InternoController
from controller.celda import CeldaController
from models.celda import Celda

if __name__ == '__main__':
    conexion = Conexion()
    Interno = InternoController()
    celdaController = CeldaController()
    itemCelda = Celda(4, "Aranjuez",100,"Disponible")
    print("############# crear_celda ####################")
    celdaController.crear_celda(itemCelda)
    print("############# obtener_celdas ####################")
    celdaController.obtener_celdas()
    itemCelda.set_Capacidad(10)
    print("############# actualizar_celda ####################")
    celdaController.actualizar_celda(itemCelda)
    print("############# obtener_celda ####################")
    celdaController.obtener_celda(itemCelda.get_ID_Celda())
    print("############# eliminar_celda ####################")
    celdaController.eliminar_celda(itemCelda.get_ID_Celda())
    print("############# obtener_celdas ####################")
    celdaController.obtener_celdas()
    
    #conexion.conectar()
    #conexion.cerrar()