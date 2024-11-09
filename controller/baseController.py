import json
import traceback  # Importar módulo para manejar trazas detalladas de errores
from flask import jsonify, request
from common.crud import Crud
from common.utiles import Utiles
from common.conexion import Conexion
from common.encriptador import EncriptadorAES

class BaseController:
    def __init__(self, entidad_nombre, clave="qwertyui12345678"):
        self.conexion = Conexion()
        self.entidad_nombre = entidad_nombre
        self.encriptador = EncriptadorAES(clave)

    def getAll(self):
        respuesta = {}
        try:
            self.conexion.conectar()
            dataResponse = self.conexion.execSPResult(f"sp_Select{self.entidad_nombre}", [0])
            respuesta["data"] = Utiles.list_to_dict(dataResponse, self.encriptador.desencriptar)
            respuesta["Response"] = "Ok"
        except Exception as e:
            # Captura de la traza completa
            traza = traceback.format_exc()
            respuesta["Error"] = f"{str(e)} (Archivo: {traceback.extract_tb(e.__traceback__)[-1].filename}, Línea: {traceback.extract_tb(e.__traceback__)[-1].lineno})"
            print(traza)  # Mostrar la traza completa en la consola para depuración
        finally:
            self.conexion.cerrar()
        return jsonify(respuesta)

    def getById(self, id):
        respuesta = {}
        try:
            self.conexion.conectar()
            dataResponse = self.conexion.execSPResult(f"sp_Select{self.entidad_nombre}", [id])
            respuesta["data"] = Utiles.list_to_dict(dataResponse, self.encriptador.desencriptar)
            respuesta["Response"] = "Ok"
        except Exception as e:
            traza = traceback.format_exc()
            respuesta["Error"] = f"{str(e)} (Archivo: {traceback.extract_tb(e.__traceback__)[-1].filename}, Línea: {traceback.extract_tb(e.__traceback__)[-1].lineno})"
            print(traza)
        finally:
            self.conexion.cerrar()
        return jsonify(respuesta)

    def create(self):
        respuesta = {}
        try:
            entidad_data = request.json
            if not entidad_data:
                raise ValueError("Los datos de la entidad están vacíos.")

            entidad_data = {k: self.encriptador.encriptar(v) if isinstance(v, str) else v for k, v in entidad_data.items()}
            entidad_json = json.dumps(entidad_data)

            self.conexion.conectar()
            dataResponse = self.conexion.execSPResult(f"sp_Insert{self.entidad_nombre}", [entidad_json])

            if dataResponse and 'Status' in dataResponse[0] and dataResponse[0]['Status'] == 'Error':
                return jsonify({"Error": dataResponse[0]['Message']}), 400

            respuesta["data"] = Utiles.list_to_dict(dataResponse)
            respuesta["Response"] = "Ok"
        except ValueError as ve:
            respuesta["Error"] = f"Entrada inválida: {str(ve)}"
        except Exception as e:
            traza = traceback.format_exc()
            respuesta["Error"] = f"{str(e)} (Archivo: {traceback.extract_tb(e.__traceback__)[-1].filename}, Línea: {traceback.extract_tb(e.__traceback__)[-1].lineno})"
            print(traza)
        finally:
            self.conexion.cerrar()
        return jsonify(respuesta)

    def update(self, id, extra_params=None):
        respuesta = {}
        try:
            self.conexion.conectar()
            entidad_data = request.json
            entidad_data = {k: self.encriptador.encriptar(v) if isinstance(v, str) else v for k, v in entidad_data.items()}
            entidad_json = json.dumps(entidad_data)

            dataResponse = self.conexion.execSPResult(f"sp_Update{self.entidad_nombre}", [entidad_json, id])

            if dataResponse and 'Status' in dataResponse[0] and dataResponse[0]['Status'] == 'Error':
                return jsonify({"Error": dataResponse[0]['Message']}), 400

            respuesta["data"] = Utiles.list_to_dict(dataResponse)
            respuesta["Response"] = f"{self.entidad_nombre} actualizado con éxito"
            return jsonify(respuesta), 200
        except Exception as e:
            traza = traceback.format_exc()
            respuesta["Error"] = f"{str(e)} (Archivo: {traceback.extract_tb(e.__traceback__)[-1].filename}, Línea: {traceback.extract_tb(e.__traceback__)[-1].lineno})"
            print(traza)
        finally:
            self.conexion.cerrar()

    def delete(self, id, extra_params=None):
        respuesta = False
        try:
            self.conexion.conectar()
            where_clause = f'ID = {id}'
            respuesta = self.conexion.execSP(f"sp_Delete{self.entidad_nombre}", [where_clause])
        except Exception as e:
            traza = traceback.format_exc()
            return jsonify({"Error": f"{str(e)} (Archivo: {traceback.extract_tb(e.__traceback__)[-1].filename}, Línea: {traceback.extract_tb(e.__traceback__)[-1].lineno})"}), 500
        finally:
            self.conexion.cerrar()
            if respuesta:
                return jsonify({"Response": f"{self.entidad_nombre} eliminado con éxito"}), 200
            else:
                return jsonify({"Response": f"{self.entidad_nombre} error al eliminar"}), 500
