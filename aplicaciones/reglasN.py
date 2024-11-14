import json
import pyodbc
from common.conexion import Conexion
from common.utiles import Utiles
from flask import Blueprint, request, jsonify
from common.encriptador import EncriptadorAES


class ReglasNController:

    def __init__(self, app, clave="qwertyui12345678") -> None:
        self.conexion = Conexion()
        self.show = Utiles()
        self.encriptador = EncriptadorAES(clave)
        regla_blueprint = Blueprint('reglas', __name__)
        regla_blueprint.add_url_rule('/reclusoxcelda', view_func=self.contar_reclusos_por_celda, methods=["GET"])
        regla_blueprint.add_url_rule('/condenaxinterno/<int:idInterno>/<int:idDelito>', view_func=self.obtener_condena_por_interno_y_delito, methods=["GET"])
        app.register_blueprint(regla_blueprint, url_prefix='/reglas')
    
    def contar_reclusos_por_celda(self) :
        respuesta = {}
        try:
            # Crear una instancia de la clase Conexion
            self.conexion.conectar()  # Establecer la conexión

            print("Ejecutando el procedimiento almacenado para contar reclusos por celda...")
            dataResponse = self.conexion.execSPResult('ContarReclusosPorCelda', [])
            respuesta["data"] = Utiles.list_to_dict(dataResponse, self.encriptador.desencriptar)
            respuesta["Response"] = "Ok"
        except pyodbc.Error as e:
            respuesta["Error"] = f"{str(e)}"
        finally:
            self.conexion.cerrar()  # Asegurarse de cerrar la conexión
        return jsonify(respuesta)

    def obtener_condena_por_interno_y_delito(self, idInterno, idDelito):
        respuesta = {}
        try:
            # Crear una instancia de la clase Conexion
            self.conexion.conectar()  # Establecer la conexión

            params = (idInterno, idDelito)
            dataResponse = self.conexion.execSPResult('ObtenerCondenaPorInternoYDelito', params)
    
            respuesta["data"] = Utiles.list_to_dict(dataResponse, self.encriptador.desencriptar)
            respuesta["Response"] = "Ok"
        except pyodbc.Error as e:
            respuesta["Error"] = f"{str(e)}"
        finally:
            self.conexion.cerrar()
        return jsonify(respuesta)



