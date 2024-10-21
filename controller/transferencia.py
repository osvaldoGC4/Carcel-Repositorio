import json
import pyodbc
from models.transferencia import Transferencia
from common.crud import Crud
from common.conexion import Conexion

class TransferenciaController:
    operacionCrud = None

    def __init__(self):
        self.operacionCrud = Crud()

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
            self.mostrar_transferencias(respuesta)
        except pyodbc.Error as e:
            print(f"Error en la ejecución de la consulta: {e}")
        finally:
            conexion.cerrar()

    def obtener_transferencia(self, ID_Transferencia):
        conexion = Conexion()
        conexion.conectar()
        try:
            respuesta = self.operacionCrud.execSelect('transferencia', '*', '{"where": "ID_Transferencia = ' + str(ID_Transferencia) + '"}')
            self.mostrar_transferencias(respuesta)
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

    def mostrar_transferencias(self, respuesta):
        transferencias = []
        if respuesta:
            for row in respuesta:
                transferencia = Transferencia(
                    ID_Transferencia=row['ID_Transferencia'],
                    ID_Interno=row['ID_Interno'],
                    ID_Celda_Origen=row['ID_Celda_Origen'],
                    ID_Celda_Destino=row['ID_Celda_Destino'],
                    Fecha=row['Fecha'],
                    Motivo=row['Motivo']
                )
                print(row)
                transferencias.append(transferencia)
