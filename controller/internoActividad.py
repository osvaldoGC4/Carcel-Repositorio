import json
from models.interno_actividad import InternoActividad
from common.crud import Crud
from common.conexion import Conexion

class InternoActividadController:
    operacionCrud = None

    def __init__(self):
        self.operacionCrud = Crud()

    def crear_interno_actividad(self, nuevo_interno_actividad: InternoActividad):
        interno_actividad_dict = nuevo_interno_actividad.to_dict()
        interno_actividad_json = json.dumps(interno_actividad_dict)
        if self.operacionCrud.execInsert("interno_actividad", interno_actividad_json):
            print(f"InternoActividad para Interno {nuevo_interno_actividad.get_ID_Interno()} y Actividad {nuevo_interno_actividad.get_ID_Actividad()} creada con éxito.")
        else:
            print(f"Problemas al insertar la relación Interno-Actividad.")

    def obtener_interno_actividades(self):
        conexion = Conexion()
        conexion.conectar()
        try:
            print("Ejecutando la consulta para obtener relaciones Interno-Actividad...")
            respuesta = self.operacionCrud.execSelect('interno_actividad', '*', '')
            self.mostrar_interno_actividades(respuesta)
        except pyodbc.Error as e:
            print(f"Error en la ejecución de la consulta: {e}")
        finally:
            conexion.cerrar()

    def obtener_interno_actividad(self, ID_Interno, ID_Actividad):
        conexion = Conexion()
        conexion.conectar()
        try:
            where_clause = f'ID_Interno = {ID_Interno} AND ID_Actividad = {ID_Actividad}'
            respuesta = self.operacionCrud.execSelect('interno_actividad', '*', f'{{"where": "{where_clause}"}}')
            self.mostrar_interno_actividades(respuesta)
        except pyodbc.Error as e:
            print(f"Error en la ejecución de la consulta: {e}")
        finally:
            conexion.cerrar()

    def actualizar_interno_actividad(self, editar_interno_actividad: InternoActividad):
        interno_actividad_dict = editar_interno_actividad.to_dict()
        interno_actividad_json = json.dumps(interno_actividad_dict)
        self.operacionCrud.execUpdate('interno_actividad', interno_actividad_json, f'{{"where": "ID_Interno = {editar_interno_actividad.get_ID_Interno()} AND ID_Actividad = {editar_interno_actividad.get_ID_Actividad()}"}}')

    def eliminar_interno_actividad(self, ID_Interno, ID_Actividad):
        where_clause = f'ID_Interno = {ID_Interno} AND ID_Actividad = {ID_Actividad}'
        self.operacionCrud.execDelete('interno_actividad', where_clause)

    def mostrar_interno_actividades(self, respuesta):
        relaciones = []
        if respuesta:
            for row in respuesta:
                interno_actividad = InternoActividad(
                    ID_Interno=row['ID_Interno'],
                    ID_Actividad=row['ID_Actividad']
                )
                relaciones.append(interno_actividad)