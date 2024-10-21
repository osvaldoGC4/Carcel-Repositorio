import json
import pyodbc
from models.transferencia import Transferencia
from common.crud import Crud
from common.conexion import Conexion
from common.utiles import Utiles

class TransferenciaController:
    operacionCrud = None

    def __init__(self):
        self.operacionCrud = Crud()
        self.show = Utiles()

    def crear_transferencia(self, nueva_transferencia: Transferencia):
        transferencia_dict = nueva_transferencia.to_dict()
        transferencia_json = json.dumps(transferencia_dict)
        if self.operacionCrud.execInsert("transferencia", transferencia_json):
            print(f"Transferencia {nueva_transferencia.get_ID_Transferencia()} creada con éxito.")
        else:
            print(f"Problemas al insertar Transferencia para el Interno {nueva_transferencia.get_ID_Interno()}.")

    def obtener_transferencias(self):
        conexion = Conexion()
        conexion.conectar()
        try:
            print("Ejecutando la consulta para obtener transferencias...")
            respuesta = self.operacionCrud.execSelect('transferencia', '*', '')
            self.show.mostrar_resultados_dinamico(respuesta)
        except pyodbc.Error as e:
            print(f"Error en la ejecución de la consulta: {e}")
        finally:
            conexion.cerrar()

    def obtener_transferencia(self, ID_Transferencia):
        conexion = Conexion()
        conexion.conectar()
        try:
            respuesta = self.operacionCrud.execSelect('transferencia', '*', '{"where": "ID_Transferencia = ' + str(ID_Transferencia) + '"}')
            self.show.mostrar_resultados_dinamico(respuesta)
        except pyodbc.Error as e:
            print(f"Error en la ejecución de la consulta: {e}")
        finally:
            conexion.cerrar()

    def actualizar_transferencia(self, editar_transferencia: Transferencia):
        transferencia_dict = editar_transferencia.to_dict()
        transferencia_json = json.dumps(transferencia_dict)
        self.operacionCrud.execUpdate('transferencia', transferencia_json, '{"where": "ID_Transferencia = ' + str(editar_transferencia.get_ID_Transferencia()) + '"}')

    def eliminar_transferencia(self, ID_Transferencia):
        self.operacionCrud.execDelete('transferencia', f'ID_Transferencia = {ID_Transferencia}')

