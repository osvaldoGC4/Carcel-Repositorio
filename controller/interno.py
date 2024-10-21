import json
import pyodbc
from models.interno import Interno
from common.crud import Crud
from common.conexion import Conexion
from common.utiles import Utiles

class InternoController:
    operacionCrud = None

    def __init__(self):
        self.operacionCrud = Crud()
        self.show = Utiles()

    def crear_interno(self, nuevo_interno: Interno):
        interno_dict = nuevo_interno.to_dict()
        interno_json = json.dumps(interno_dict)
        if self.operacionCrud.execInsert("interno", interno_json):
            print(f"Interno {nuevo_interno.get_ID_Interno()} creado con éxito.")
        else:
            print(f"Problemas al insertar Interno {nuevo_interno.get_Nombre()}.")

    def obtener_internos(self):
        conexion = Conexion()
        conexion.conectar()
        try:
            print("Ejecutando la consulta para obtener internos...")
            respuesta = self.operacionCrud.execSelect('interno', '*', '')
            self.show.mostrar_resultados_dinamico(respuesta)
        except pyodbc.Error as e:
            print(f"Error en la ejecución de la consulta: {e}")
        finally:
            conexion.cerrar()

    def obtener_interno(self, ID_Interno):
        conexion = Conexion()
        conexion.conectar()
        try:
            respuesta = self.operacionCrud.execSelect('interno', '*', '{"where": "ID_Interno = ' + str(ID_Interno) + '"}')
            self.show.mostrar_resultados_dinamico(respuesta)
        except pyodbc.Error as e:
            print(f"Error en la ejecución de la consulta: {e}")
        finally:
            conexion.cerrar()

    def actualizar_interno(self, editar_interno: Interno):
        interno_dict = editar_interno.to_dict()
        interno_json = json.dumps(interno_dict)
        self.operacionCrud.execUpdate('interno', interno_json, '{"where": "ID_Interno = ' + str(editar_interno.get_ID_Interno()) + '"}')

    def eliminar_interno(self, ID_Interno):
        self.operacionCrud.execDelete('interno', f'ID_Interno = {ID_Interno}')

    
