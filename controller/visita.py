import json
from models.visita import Visita
from common.crud import Crud
from common.conexion import Conexion

class VisitaController:
    operacionCrud = None

    def __init__(self):
        self.operacionCrud = Crud()

    def crear_visita(self, nueva_visita: Visita):
        visita_dict = nueva_visita.to_dict()
        visita_json = json.dumps(visita_dict)
        if self.operacionCrud.execInsert("visita", visita_json):
            print(f"Visita {nueva_visita.get_ID_Visita()} creada con éxito.")
        else:
            print(f"Problemas al insertar Visita para el Interno {nueva_visita.get_ID_Interno()}.")

    def obtener_visitas(self):
        conexion = Conexion()
        conexion.conectar()
        try:
            print("Ejecutando la consulta para obtener visitas...")
            respuesta = self.operacionCrud.execSelect('visita', '*', '')
            self.mostrar_visitas(respuesta)
        except pyodbc.Error as e:
            print(f"Error en la ejecución de la consulta: {e}")
        finally:
            conexion.cerrar()

    def obtener_visita(self, ID_Visita):
        conexion = Conexion()
        conexion.conectar()
        try:
            respuesta = self.operacionCrud.execSelect('visita', '*', '{"where": "ID_Visita = ' + str(ID_Visita) + '"}')
            self.mostrar_visitas(respuesta)
        except pyodbc.Error as e:
            print(f"Error en la ejecución de la consulta: {e}")
        finally:
            conexion.cerrar()

    def actualizar_visita(self, editar_visita: Visita):
        visita_dict = editar_visita.to_dict()
        visita_json = json.dumps(visita_dict)
        self.operacionCrud.execUpdate('visita', visita_json, '{"where": "ID_Visita = ' + str(editar_visita.get_ID_Visita()) + '"}')

    def eliminar_visita(self, ID_Visita):
        self.operacionCrud.execDelete('visita', f'ID_Visita = {ID_Visita}')

    def mostrar_visitas(self, respuesta):
        visitas = []
        if respuesta:
            for row in respuesta:
                visita = Visita(
                    ID_Visita=row['ID_Visita'],
                    ID_Interno=row['ID_Interno'],
                    ID_Visitante=row['ID_Visitante'],
                    Fecha=row['Fecha'],
                    Hora_Inicio=row['Hora_Inicio'],
                    Duracion=row['Duracion']
                )
                visitas.append(visita)
