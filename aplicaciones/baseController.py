import traceback  # Importar módulo para manejar trazas detalladas de errores
from flask import jsonify, request
from common.utiles import Utiles
from common.encriptador import EncriptadorAES
from repositorios.IRepositorio import IRepositorio
class BaseController:
    def __init__(self, entidad_nombre, clave="qwertyui12345678"):
        self.entidad_nombre = entidad_nombre
        self.encriptador = EncriptadorAES(clave)

    def getAll(self, repositorio: IRepositorio):
        respuesta = {}
        try:
            dataResponse = repositorio.getAll()
            respuesta["data"] = Utiles.list_to_dict(dataResponse, self.encriptador.desencriptar)
            respuesta["Response"] = "Ok"
        except Exception as e:
            # Captura de la traza completa
            traza = traceback.format_exc()
            respuesta["Error"] = f"{str(e)} (Archivo: {traceback.extract_tb(e.__traceback__)[-1].filename}, Línea: {traceback.extract_tb(e.__traceback__)[-1].lineno})"
            print(traza)  # Mostrar la traza completa en la consola para depuración
        return jsonify(respuesta)

    def getById(self, id, repositorio: IRepositorio):
        respuesta = {}
        try:
            dataResponse = repositorio.getById(id)
            respuesta["data"] = Utiles.list_to_dict(dataResponse, self.encriptador.desencriptar)
            respuesta["Response"] = "Ok"
        except Exception as e:
            traza = traceback.format_exc()
            respuesta["Error"] = f"{str(e)} (Archivo: {traceback.extract_tb(e.__traceback__)[-1].filename}, Línea: {traceback.extract_tb(e.__traceback__)[-1].lineno})"
            print(traza)
        return jsonify(respuesta)

    def create(self, repositorio: IRepositorio):
        respuesta = {}
        try:
            entidad_data = request.json
            if not entidad_data:
                raise ValueError("Los datos de la entidad están vacíos.")
            
            dataResponse = repositorio.create(entidad_data)

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
        return jsonify(respuesta)


    def update(self, id, repositorio: IRepositorio, extra_params=None):
        respuesta = {}
        try:
            entidad_data = request.json
            dataResponse = repositorio.update(id, entidad_data)

            if dataResponse and 'Status' in dataResponse[0] and dataResponse[0]['Status'] == 'Error':
                return jsonify({"Error": dataResponse[0]['Message']}), 400

            respuesta["data"] = Utiles.list_to_dict(dataResponse)
            respuesta["Response"] = f"{self.entidad_nombre} actualizado con éxito"
            return jsonify(respuesta), 200
        except Exception as e:
            traza = traceback.format_exc()
            respuesta["Error"] = f"{str(e)} (Archivo: {traceback.extract_tb(e.__traceback__)[-1].filename}, Línea: {traceback.extract_tb(e.__traceback__)[-1].lineno})"
            print(traza)


    def delete(self, id, repositorio: IRepositorio, extra_params=None):
        respuesta = False
        try:
            respuesta = repositorio.delete(id)
        except Exception as e:
            traza = traceback.format_exc()
            return jsonify({"Error": f"{str(e)} (Archivo: {traceback.extract_tb(e.__traceback__)[-1].filename}, Línea: {traceback.extract_tb(e.__traceback__)[-1].lineno})"}), 500
        finally:
            if respuesta:
                return jsonify({"Response": f"{self.entidad_nombre} eliminado con éxito"}), 200
            else:
                return jsonify({"Response": f"{self.entidad_nombre} error al eliminar"}), 500
