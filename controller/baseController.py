import json
from flask import jsonify, request
from common.crud import Crud
from common.utiles import Utiles

class BaseController:
    def __init__(self, entidad_nombre):
        self.operacionCrud = Crud()
        self.entidad_nombre = entidad_nombre

    def getAll(self):
        respuesta = {}
        try:
            dataResponse = self.operacionCrud.execSelect(self.entidad_nombre, '*', '')
            respuesta["data"] = Utiles.list_to_dict(dataResponse)
            respuesta["Response"] = "Ok"
            return jsonify(respuesta)
        except Exception as e:
            respuesta["Error"] = str(e)
            return jsonify(respuesta), 500

    def getById(self, id):
        respuesta = {}
        try:
            dataResponse = self.operacionCrud.execSelect(self.entidad_nombre, '*', f'{{"where": "ID = {id}"}}')
            respuesta["data"] = Utiles.list_to_dict(dataResponse)
            respuesta["Response"] = "Ok"
            return jsonify(respuesta)
        except Exception as e:
            respuesta["Error"] = str(e)
            return jsonify(respuesta), 500

    def create(self):
        try:
            entidad_data = request.json
            entidad_json = json.dumps(entidad_data)
            if self.operacionCrud.execInsert(self.entidad_nombre, entidad_json):
                return jsonify({"Response": f"{self.entidad_nombre} creado con éxito"}), 201
        except Exception as e:
            return jsonify({"Error": str(e)}), 500

    def update(self, id, extra_params=None):
        try:
            entidad_data = request.json
            entidad_json = json.dumps(entidad_data)
            # Configurar filtro
            where_clause = f'ID = {id}'
            if extra_params:
                where_clause += ' AND ' + ' AND '.join([f"{key} = '{value}'" for key, value in extra_params.items()])
            self.operacionCrud.execUpdate(self.entidad_nombre, entidad_json, f'{{"where": "{where_clause}"}}')
            return jsonify({"Response": f"{self.entidad_nombre} actualizado con éxito"}), 200
        except Exception as e:
            return jsonify({"Error": str(e)}), 500

    def delete(self, id, extra_params=None):
        try:
            # Configurar filtro
            where_clause = f'ID = {id}'
            if extra_params:
                where_clause += ' AND ' + ' AND '.join([f"{key} = '{value}'" for key, value in extra_params.items()])
            self.operacionCrud.execDelete(self.entidad_nombre, where_clause)
            return jsonify({"Response": f"{self.entidad_nombre} eliminado con éxito"}), 200
        except Exception as e:
            return jsonify({"Error": str(e)}), 500
