import json
import pyodbc
from models.informeDisciplina import InformeDisciplina
from common.crud import Crud
from common.conexion import Conexion
from common.utiles import Utiles

class InformeDisciplinaController:
    operacionCrud = None

    def __init__(self):
        self.operacionCrud = Crud()
        self.show = Utiles()

    def crear_informe(self, nuevo_informe: InformeDisciplina):
        informe_dict = nuevo_informe.to_dict()
        informe_json = json.dumps(informe_dict)
        if self.operacionCrud.execInsert("informe_disciplina", informe_json):
            print(f"Informe {nuevo_informe.get_ID_Informe()} creado con éxito.")
        else:
            print(f"Problemas al insertar Informe para el Interno {nuevo_informe.get_ID_Interno()}.")

    def obtener_informes(self):
        conexion = Conexion()
        conexion.conectar()
        try:
            print("Ejecutando la consulta para obtener informes disciplinarios...")
            respuesta = self.operacionCrud.execSelect('informe_disciplina', '*', '')
            self.show.mostrar_resultados_dinamico(respuesta)
        except pyodbc.Error as e:
            print(f"Error en la ejecución de la consulta: {e}")
        finally:
            conexion.cerrar()

    def obtener_informe(self, ID_Informe):
        conexion = Conexion()
        conexion.conectar()
        try:
            respuesta = self.operacionCrud.execSelect('informe_disciplina', '*', '{"where": "ID_Informe = ' + str(ID_Informe) + '"}')
            self.show.mostrar_resultados_dinamico(respuesta)
        except pyodbc.Error as e:
            print(f"Error en la ejecución de la consulta: {e}")
        finally:
            conexion.cerrar()

    def actualizar_informe(self, editar_informe: InformeDisciplina):
        informe_dict = editar_informe.to_dict()
        informe_json = json.dumps(informe_dict)
        self.operacionCrud.execUpdate('informe_disciplina', informe_json, '{"where": "ID_Informe = ' + str(editar_informe.get_ID_Informe()) + '"}')

    def eliminar_informe(self, ID_Informe):
        self.operacionCrud.execDelete('informe_disciplina', f'ID_Informe = {ID_Informe}')


