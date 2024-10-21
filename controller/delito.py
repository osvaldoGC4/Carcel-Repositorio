import json
import pyodbc
from models.delito import Delito
from common.crud import Crud
from common.conexion import Conexion

class DelitoController:
    operacionCrud = None

    def __init__(self):
        self.operacionCrud = Crud()

    def crear_delito(self, nuevo_delito: Delito):
        delito_dict = nuevo_delito.to_dict()
        delito_json = json.dumps(delito_dict)
        if self.operacionCrud.execInsert("delito", delito_json):
            print(f"Delito {nuevo_delito.get_ID_Delito()} creado con éxito.")
        else:
            print(f"Problemas al insertar Delito {nuevo_delito.get_Tipo()}.")

    def obtener_delitos(self):
        conexion = Conexion()
        conexion.conectar()
        try:
            print("Ejecutando la consulta para obtener delitos...")
            respuesta = self.operacionCrud.execSelect('delito', '*', '')
            self.mostrar_delitos(respuesta)
        except pyodbc.Error as e:
            print(f"Error en la ejecución de la consulta: {e}")
        finally:
            conexion.cerrar()

    def obtener_delito(self, ID_Delito):
        conexion = Conexion()
        conexion.conectar()
        try:
            respuesta = self.operacionCrud.execSelect('delito', '*', '{"where": "ID_Delito = ' + str(ID_Delito) + '"}')
            self.mostrar_delitos(respuesta)
        except pyodbc.Error as e:
            print(f"Error en la ejecución de la consulta: {e}")
        finally:
            conexion.cerrar()

    def actualizar_delito(self, editar_delito: Delito):
        delito_dict = editar_delito.to_dict()
        delito_json = json.dumps(delito_dict)
        self.operacionCrud.execUpdate('delito', delito_json, '{"where": "ID_Delito = ' + str(editar_delito.get_ID_Delito()) + '"}')

    def eliminar_delito(self, ID_Delito):
        self.operacionCrud.execDelete('delito', f'ID_Delito = {ID_Delito}')

    def mostrar_delitos(self, respuesta):
        delitos = []
        if respuesta:
            for row in respuesta:
                delito = Delito(
                    ID_Delito=row['ID_Delito'],
                    Tipo=row['Tipo'],
                    Descripcion=row['Descripcion']
                )
                delitos.append(delito)
