# main.py
from common.conexion import Conexion
from controller.celda import CeldaController
from models.celda import Celda

if __name__ == '__main__':
    conexion = Conexion()
    celdaController = CeldaController()
    itemCelda = Celda(1, "Medellin",5,"Disponible")
    print("############# crear_celda ####################")
    celdaController.crear_celda(itemCelda)
    print("############# obtener_celdas ####################")
    celdaController.obtener_celdas()
    itemCelda.set_Capacidad(8)
    print("############# actualizar_celda ####################")
    celdaController.actualizar_celda(itemCelda)
    print("############# obtener_celda ####################")
    celdaController.obtener_celda(itemCelda.get_ID_Celda())
    print("############# eliminar_celda ####################")
    celdaController.eliminar_celda(itemCelda.get_ID_Celda())
    print("############# obtener_celdas ####################")
    celdaController.obtener_celdas()
    