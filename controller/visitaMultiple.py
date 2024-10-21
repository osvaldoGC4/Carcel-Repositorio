import json
from models.visita_multiple import VisitaMultiple
from common.crud import Crud
from common.conexion import Conexion

class VisitaMultipleController:
    operacionCrud = None

    def __init__(self):
        self.operacionCrud = Crud()

    def crear_visita_multiple(self, nueva_visita_multiple: VisitaMultiple):
        visita_multiple_dict = nueva_visita_multiple.to_dict()
        visita_multiple_json = json.dumps(visita_multiple_dict)
        if self.operacionCrud.execInsert("visita_multiple", visita_multiple_json):
            print(f"VisitaMultiple para Visita {nueva_visita_multiple.get_ID_Visita()} y Visitante {nueva_visita_multiple.get_ID_Visitante()} creada con éxito.")
        else:
            print(f"Problemas al insertar la Visita Múltiple.")

    def obtener_visitas_multiples(self):
        conexion = Conexion()
        conexion.conectar()
        try:
            print("Ejecutando la consulta para obtener visitas múltiples...")
            respuesta = self.operacionCrud.execSelect('visita_multiple', '*', '')
            self.mostrar_visitas_multiples(respuesta)
        except pyodbc.Error as e:
            print(f"Error en la ejecución de la consulta: {e}")
        finally:
            conexion.cerrar()

    def obtener_visita_multiple(self, ID_Visita, ID_Visitante):
        conexion = Conexion()
        conexion.conectar()
        try:
            where_clause = f'ID_Visita = {ID_Visita} AND ID_Visitante = {ID_Visitante}'
            respuesta = self.operacionCrud.execSelect('visita_multiple', '*', f'{{"where": "{where_clause}"}}')
            self.mostrar_visitas_multiples(respuesta)
        except pyodbc.Error as e:
            print(f"Error en la ejecución de la consulta: {e}")
        finally:
            conexion.cerrar()

    def actualizar_visita_multiple(self, editar_visita_multiple: VisitaMultiple):
        visita_multiple_dict = editar_visita_multiple.to_dict()
        visita_multiple_json = json.dumps(visita_multiple_dict)
        self.operacionCrud.execUpdate('visita_multiple', visita_multiple_json, f'{{"where": "ID_Visita = {editar_visita_multiple.get_ID_Visita()} AND ID_Visitante = {editar_visita_multiple.get_ID_Visitante()}"}}')

    def eliminar_visita_multiple(self, ID_Visita, ID_Visitante):
        where_clause = f'ID_Visita = {ID_Visita} AND ID_Visitante = {ID_Visitante}'
        self.operacionCrud.execDelete('visita_multiple', where_clause)

    def mostrar_visitas_multiples(self, respuesta):
        relaciones = []
        if respuesta:
            for row in respuesta:
                visita_multiple = VisitaMultiple(
                    ID_Visita=row['ID_Visita'],
                    ID_Visitante=row['ID_Visitante']
                )
                relaciones.append(visita_multiple)
