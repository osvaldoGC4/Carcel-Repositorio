import json
import pyodbc
from models.celda import Celda
from common.crud import Crud
from common.conexion import Conexion
from common.utiles import Utiles

class CeldaController:
    operacionCrud = None

    def __init__(self):
        self.operacionCrud = Crud()
        self.show = Utiles()

    # Crear un nuevo registro de Celda
    def crear_celda(self, nueva_celda: Celda):
       # Convertir la celda en un diccionario para que sea serializable
        celda_dict = nueva_celda.to_dict()
        # Convertir el diccionario a JSON
        celda_json = json.dumps(celda_dict)
        # Llamar al método para insertar en la base de datos
        if self.operacionCrud.execInsert("celda", celda_json):
            print(f"Celda {nueva_celda.get_ID_Celda()} creada con éxito.")  # Cambiar "Interno" por "Celda"
        else: 
            print(f"Problemas al insertar Celda {nueva_celda.get_Capacidad()}.")  # Cambiar "Interno" por "Celda"

    def obtener_celdas(self) -> None:
        # Crear una instancia de la clase Conexion
        conexion = Conexion()
        conexion.conectar()  # Establecer la conexión
        
        try:
            print("Ejecutando la consulta para obtener celdas...")
            respuesta = self.operacionCrud.execSelect('celda', '*', '')

            self.show.mostrar_resultados_dinamico(respuesta)

        except pyodbc.Error as e:
            print(f"Error en la ejecución de la consulta: {e}")
            
        finally:
            conexion.cerrar()  # Asegurarse de cerrar la conexión

    
    def obtener_celda(self, ID_Celda):
        # Crear una instancia de la clase Conexion
        conexion = Conexion()
        conexion.conectar()  # Establecer la conexión
        
        try:
            print("Ejecutando la consulta para obtener celdas...")
            respuesta = self.operacionCrud.execSelect('celda', '*', '{"where": "ID_Celda = '+ str(ID_Celda) +'"}')

            self.show.mostrar_resultados_dinamico(respuesta)

        except pyodbc.Error as e:
            print(f"Error en la ejecución de la consulta: {e}")
            
        finally:
            conexion.cerrar()  # Asegurarse de cerrar la conexión

    
    def actualizar_celda(self, editar_celda: Celda):
        celda_dict = editar_celda.to_dict()
        celda_json = json.dumps(celda_dict)
        self.operacionCrud.execUpdate('celda', celda_json, '{"where": "ID_celda = ' + str(editar_celda.get_ID_Celda()) + '"}')

    def eliminar_celda(self, ID_Celda):
        self.operacionCrud.execDelete('celda', f'ID_Celda = {ID_Celda}')
