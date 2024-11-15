from models.actividad import Actividad
from repositorios.IRepositorio import IRepositorio  # Importamos la interfaz
from common.conexion import Conexion
from common.encriptador import EncriptadorAES
from common.utiles import Utiles
import json

class ActividadRepositorio(IRepositorio):
    
    def __init__(self):
        self.conexion = Conexion()
        clave="qwertyui12345678"
        self.encriptador = EncriptadorAES(clave)
        self.entidad_nombre = 'actividad'

    def getAll(self):
        data = []
        try:
            self.conexion.conectar()
            data = self.conexion.execSPResult(f"sp_Select{self.entidad_nombre}", [0])
        except Exception as e:
            data = []
        finally:
            self.conexion.cerrar()
        return data
    
    def getById(self, id: int):
        data = []
        try:
            self.conexion.conectar()
            data = self.conexion.execSPResult(f"sp_Select{self.entidad_nombre}", [id])
        except Exception as e:
            data = []
        finally:
            self.conexion.cerrar()
        return data

    def create(self, datos: dict):
        data = []
        try:
            # No encriptar los valores que son fechas
            datos = {
                k: self.encriptador.encriptar(v) if isinstance(v, str) and not Utiles.is_date_format(v) else v
                for k, v in datos.items()
            }
            entidad_json = json.dumps(datos)

            self.conexion.conectar()
            data = self.conexion.execSPResult(f"sp_Insert{self.entidad_nombre}", [entidad_json])
        except Exception as e:
            data = []
        finally:
            self.conexion.cerrar()
        return data

    def update(self, id: int, datos: dict):
        data = []
        try:
            # No encriptar los valores que son fechas
            datos = {
                k: self.encriptador.encriptar(v) if isinstance(v, str) and not Utiles.is_date_format(v) else v
                for k, v in datos.items()
            }
            entidad_json = json.dumps(datos)

            self.conexion.conectar()
            data = self.conexion.execSPResult(f"sp_Update{self.entidad_nombre}", [entidad_json, id])
        except Exception as e:
            data = []
        finally:
            self.conexion.cerrar()
        return data
    def delete(self, id: int):
        data = []
        try:
            # No encriptar los valores que son fechas
            where_clause = f'ID = {id}'
            self.conexion.conectar()
            data = self.conexion.execSP(f"sp_Delete{self.entidad_nombre}", [where_clause])
        except Exception as e:
            data = []
        finally:
            self.conexion.cerrar()
        return data