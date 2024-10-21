import json
from models.personal import Personal
from common.crud import Crud
from common.conexion import Conexion
import pyodbc
from common.utiles import Utiles

class PersonalController:
    operacionCrud = None

    def __init__(self):
        self.operacionCrud = Crud()
        self.show = Utiles()

    def crear_personal(self, nuevo_personal: Personal):
        personal_dict = nuevo_personal.to_dict()
        personal_json = json.dumps(personal_dict)
        if self.operacionCrud.execInsert("personal", personal_json):
            print(f"Personal {nuevo_personal.get_ID_Personal()} creado con éxito.")
        else:
            print(f"Problemas al insertar Personal {nuevo_personal.get_Nombre()}.")

    def obtener_personal(self):
        conexion = Conexion()
        conexion.conectar()
        try:
            print("Ejecutando la consulta para obtener personal...")
            respuesta = self.operacionCrud.execSelect('personal', '*', '')
            self.show.mostrar_resultados_dinamico(respuesta)
        except pyodbc.Error as e:
            print(f"Error en la ejecución de la consulta: {e}")
        finally:
            conexion.cerrar()

    def obtener_personal_por_id(self, ID_Personal):
        conexion = Conexion()
        conexion.conectar()
        try:
            respuesta = self.operacionCrud.execSelect('personal', '*', '{"where": "ID_Personal = ' + str(ID_Personal) + '"}')
            self.show.mostrar_resultados_dinamico(respuesta)
        except pyodbc.Error as e:
            print(f"Error en la ejecución de la consulta: {e}")
        finally:
            conexion.cerrar()

    def actualizar_personal(self, editar_personal: Personal):
        personal_dict = editar_personal.to_dict()
        personal_json = json.dumps(personal_dict)
        self.operacionCrud.execUpdate('personal', personal_json, '{"where": "ID_Personal = ' + str(editar_personal.get_ID_Personal()) + '"}')

    def eliminar_personal(self, ID_Personal):
        self.operacionCrud.execDelete('personal', f'ID_Personal = {ID_Personal}')

