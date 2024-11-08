import json
import pyodbc
from models.condena import Condena
from common.crud import Crud
from common.conexion import Conexion
from common.utiles import Utiles

class CondenaController:
    operacionCrud = None

    def __init__(self, app):
        self.operacionCrud = Crud()
        app.add_url_rule('/visitantes', view_func=self.getAll, methods=["GET"])
        app.add_url_rule('/visitante/<int:id>', view_func=self.getById, methods=["GET"])
        app.add_url_rule('/visitante', view_func=self.create, methods=["POST"])
        app.add_url_rule('/visitante', view_func=self.update, methods=["PATCH"])
        app.add_url_rule('/visitante/<int:id>', view_func=self.delete, methods=["DELETE"])

    def crear_condena(self, nueva_condena: Condena):
        condena_dict = nueva_condena.to_dict()
        condena_json = json.dumps(condena_dict)
        if self.operacionCrud.execInsert("condena", condena_json):
            print(f"Condena {nueva_condena.get_ID_Condena()} creada con éxito.")
        else:
            print(f"Problemas al insertar Condena para el Interno {nueva_condena.get_ID_Interno()}.")

    def obtener_condenas(self):
        conexion = Conexion()
        conexion.conectar()
        try:
            print("Ejecutando la consulta para obtener condenas...")
            respuesta = self.operacionCrud.execSelect('condena', '*', '')
            Utiles.mostrar_resultados_dinamico(respuesta)
        except pyodbc.Error as e:
            print(f"Error en la ejecución de la consulta: {e}")
        finally:
            conexion.cerrar()

    def obtener_condena(self, ID_Condena):
        conexion = Conexion()
        conexion.conectar()
        try:
            respuesta = self.operacionCrud.execSelect('condena', '*', '{"where": "ID_Condena = ' + str(ID_Condena) + '"}')
            Utiles.mostrar_resultados_dinamico(respuesta)
        except pyodbc.Error as e:
            print(f"Error en la ejecución de la consulta: {e}")
        finally:
            conexion.cerrar()

    def actualizar_condena(self, editar_condena: Condena):
        condena_dict = editar_condena.to_dict()
        condena_json = json.dumps(condena_dict)
        self.operacionCrud.execUpdate('condena', condena_json, '{"where": "ID_Condena = ' + str(editar_condena.get_ID_Condena()) + '"}')

    def eliminar_condena(self, ID_Condena):
        self.operacionCrud.execDelete('condena', f'ID_Condena = {ID_Condena}')
