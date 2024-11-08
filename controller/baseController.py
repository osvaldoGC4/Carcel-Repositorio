import json
from flask import jsonify, request
from common.crud import Crud
from common.utiles import Utiles
from common.conexion import Conexion

class BaseController:
    def __init__(self, entidad_nombre):
        self.conexion = Conexion()
        self.entidad_nombre = entidad_nombre

    def getAll(self):
        respuesta = {}
        try:
            self.conexion.conectar()
            # dataResponse = self.conexion.execSPResult(f"DynamicalSelect", [self.entidad_nombre, '*', ''])
            dataResponse = self.conexion.execSPResult(f"sp_Select{self.entidad_nombre}", [0])
            respuesta["data"] = Utiles.list_to_dict(dataResponse)
            respuesta["Response"] = "Ok"
        except Exception as e:
            respuesta["Error"] = str(e)
        finally:
            self.conexion.cerrar()  # Asegúrate de cerrar la conexión, que incluye el cursor
        return jsonify(respuesta)

    def getById(self, id):
        respuesta = {}
        try:
            self.conexion.conectar()
            # dataResponse = self.operacionCrud.execSelect(self.entidad_nombre, '*', f'{{"where": "ID = {id}"}}')
            dataResponse = self.conexion.execSPResult(f"sp_Select{self.entidad_nombre}", [id])
            respuesta["data"] = Utiles.list_to_dict(dataResponse)
            respuesta["Response"] = "Ok"
        except Exception as e:
            respuesta["Error"] = str(e)
        finally:
            self.conexion.cerrar()  # Asegúrate de cerrar la conexión, que incluye el cursor
        return jsonify(respuesta)


    def create(self):
        respuesta = {}
        try:
            # Intentar obtener y validar la data enviada
            entidad_data = request.json
            if not entidad_data:
                raise ValueError("Los datos de la entidad están vacíos.")

            # Convertir los datos del JSON a un formato que el SP puede manejar
            entidad_json = json.dumps(entidad_data)

            # Conectar antes de ejecutar el SP
            self.conexion.conectar()
            
            # Llamar al SP con el JSON de datos
            dataResponse = self.conexion.execSPResult(f"sp_Insert{self.entidad_nombre}", [entidad_json])

            # Manejar posibles errores devueltos por el SP
            if dataResponse and 'Status' in dataResponse[0] and dataResponse[0]['Status'] == 'Error':
                return jsonify({"Error": dataResponse[0]['Message']}), 400

            # Preparar la respuesta con los datos insertados
            respuesta["data"] = Utiles.list_to_dict(dataResponse)
            respuesta["Response"] = "Ok"

        except ValueError as ve:
            respuesta["Error"] = f"Entrada inválida: {str(ve)}"
        except Exception as e:
            respuesta["Error"] = f"Error interno: {str(e)}"
        finally:
            try:
                self.conexion.cerrar()  # Asegúrate de que se cierre la conexión
            except Exception as e:
                print(f"Error al cerrar la conexión: {str(e)}")

        return jsonify(respuesta)


    def update(self, id, extra_params=None):
        respuesta = {}
        try:
            self.conexion.conectar()
            # Obtener los datos enviados en la solicitud
            entidad_data = request.json
            entidad_json = json.dumps(entidad_data)

            # Llamar al SP con los parámetros
            dataResponse = self.conexion.execSPResult(f"sp_Update{self.entidad_nombre}", [entidad_json, id])

            # Manejar el posible mensaje de error devuelto por el SP
            if dataResponse and 'Status' in dataResponse[0] and dataResponse[0]['Status'] == 'Error':
                return jsonify({"Error": dataResponse[0]['Message']}), 400

            respuesta["data"] = Utiles.list_to_dict(dataResponse)
            respuesta["Response"] = f"{self.entidad_nombre} actualizado con éxito"
            return jsonify(respuesta), 200
        except Exception as e:
            return jsonify({"Error": str(e)}), 500
        finally:
            self.conexion.cerrar()  # Cerrar la conexión al final


    def delete(self, id, extra_params=None):
        respuesta = False
        try:
            self.conexion.conectar()
            # Configurar filtro
            where_clause = f'ID = {id}'
            # if extra_params:
            #     where_clause += ' AND ' + ' AND '.join([f"{key} = '{value}'" for key, value in extra_params.items()])
            respuesta = self.conexion.execSP(f"sp_Delete{self.entidad_nombre}", [where_clause])
        except Exception as e:
            return jsonify({"Error": str(e)}), 500
        finally:
            self.conexion.cerrar()  # Cerrar la conexión al final
            if respuesta:
                return jsonify({"Response": f"{self.entidad_nombre} eliminado con éxito"}), 200
            else:
                return jsonify({"Response": f"{self.entidad_nombre} error al eliminar"}), 500