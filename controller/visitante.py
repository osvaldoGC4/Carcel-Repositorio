import json
import pyodbc
from models.visitante import Visitante
from common.crud import Crud
from common.conexion import Conexion
from common.utiles import Utiles

class VisitanteController:
    operacionCrud = None

    def __init__(self):
        self.operacionCrud = Crud()
        self.show = Utiles()

    def crear_visitante(self, nuevo_visitante: Visitante):
        visitante_dict = nuevo_visitante.to_dict()
        visitante_json = json.dumps(visitante_dict)
        if self.operacionCrud.execInsert("visitante", visitante_json):
            print(f"Visitante {nuevo_visitante.get_ID_Visitante()} creado con éxito.")
        else:
            print(f"Problemas al insertar Visitante {nuevo_visitante.get_Nombre()}.")

    def obtener_visitantes(self):
        conexion = Conexion()
        conexion.conectar()
        try:
            print("Ejecutando la consulta para obtener visitantes...")
            respuesta = self.operacionCrud.execSelect('visitante', '*', '')
            self.show.mostrar_resultados_dinamico(respuesta)
        except pyodbc.Error as e:
            print(f"Error en la ejecución de la consulta: {e}")
        finally:
            conexion.cerrar()

    def obtener_visitante(self, ID_Visitante):
        conexion = Conexion()
        conexion.conectar()
        try:
            respuesta = self.operacionCrud.execSelect('visitante', '*', '{"where": "ID_Visitante = ' + str(ID_Visitante) + '"}')
            self.show.mostrar_resultados_dinamico(respuesta)
        except pyodbc.Error as e:
            print(f"Error en la ejecución de la consulta: {e}")
        finally:
            conexion.cerrar()

    def actualizar_visitante(self, editar_visitante: Visitante):
        visitante_dict = editar_visitante.to_dict()
        visitante_json = json.dumps(visitante_dict)
        self.operacionCrud.execUpdate('visitante', visitante_json, '{"where": "ID_Visitante = ' + str(editar_visitante.get_ID_Visitante()) + '"}')

    def eliminar_visitante(self, ID_Visitante):
        self.operacionCrud.execDelete('visitante', f'ID_Visitante = {ID_Visitante}')
