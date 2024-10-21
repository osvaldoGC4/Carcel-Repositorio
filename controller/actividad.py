import json
import pyodbc
from models.actividad import Actividad
from common.crud import Crud
from common.conexion import Conexion
from common.utiles import Utiles

class ActividadController:
    operacionCrud = None

    def __init__(self):
        self.operacionCrud = Crud()
        self.show = Utiles()

    def crear_actividad(self, nueva_actividad: Actividad):
        actividad_dict = nueva_actividad.to_dict()
        actividad_json = json.dumps(actividad_dict)
        if self.operacionCrud.execInsert("actividad", actividad_json):
            print(f"Actividad {nueva_actividad.get_ID_Actividad()} creada con éxito.")
        else:
            print(f"Problemas al insertar Actividad {nueva_actividad.get_Nombre()}.")

    def obtener_actividades(self):
        conexion = Conexion()
        conexion.conectar()
        try:
            print("Ejecutando la consulta para obtener actividades...")
            respuesta = self.operacionCrud.execSelect('actividad', '*', '')
            self.show.mostrar_resultados_dinamico(respuesta)
        except pyodbc.Error as e:
            print(f"Error en la ejecución de la consulta: {e}")
        finally:
            conexion.cerrar()

    def obtener_actividad(self, ID_Actividad):
        conexion = Conexion()
        conexion.conectar()
        try:
            respuesta = self.operacionCrud.execSelect('actividad', '*', '{"where": "ID_Actividad = ' + str(ID_Actividad) + '"}')
            self.show.mostrar_resultados_dinamico(respuesta)
        except pyodbc.Error as e:
            print(f"Error en la ejecución de la consulta: {e}")
        finally:
            conexion.cerrar()

    def actualizar_actividad(self, editar_actividad: Actividad):
        actividad_dict = editar_actividad.to_dict()
        actividad_json = json.dumps(actividad_dict)
        self.operacionCrud.execUpdate('actividad', actividad_json, '{"where": "ID_Actividad = ' + str(editar_actividad.get_ID_Actividad()) + '"}')

    def eliminar_actividad(self, ID_Actividad):
        self.operacionCrud.execDelete('actividad', f'ID_Actividad = {ID_Actividad}')

   
