import json
import pyodbc
from models.celda import Celda
from common.crud import Crud
from common.conexion import Conexion
from common.utiles import Utiles
from common.encriptador import EncriptadorAES

class CeldaController:
    operacionCrud = None

    def __init__(self):
        self.operacionCrud = Crud()
        self.show = Utiles()
        self.encriptar = EncriptadorAES()
        

    # Crear un nuevo registro de Celda
    def crear_celda(self, nueva_celda: Celda):
        # Convertir la celda en un diccionario para que sea serializable
        celda_dict = nueva_celda.to_dict()
        # Encriptar la 'Ubicacion' antes de insertarla
        if 'Ubicacion' in celda_dict:
            celda_dict['Ubicacion'] = self.encriptar.encriptar(celda_dict['Ubicacion'])

        # Convertir el diccionario a JSON
        celda_json = json.dumps(celda_dict)
        
        try:
            # Llamar al método para insertar en la base de datos
            if self.operacionCrud.execInsert("sp_InsertCelda", celda_json):
                print(f"Celda {nueva_celda.get_ID_Celda()} creada con éxito.")  # Cambiar "Interno" por "Celda"
            else: 
                print(f"Problemas al insertar Celda {nueva_celda.get_Capacidad()}.")  # Cambiar "Interno" por "Celda"
        
        except Exception as e:
            # Mostrar un error bonito si el ID ya existe
            if str(e) == "El ID_Celda ya existe. No se puede insertar.":
                print(f"Error: El ID de la Celda {nueva_celda.get_ID_Celda()} ya está registrado. Por favor, use otro ID.")
            else:
                print(f"Error al crear la celda: {e}")


    def obtener_celdas(self) -> None:
        # Crear una instancia de la clase Conexion
        conexion = Conexion()
        conexion.conectar()  # Establecer la conexión
        
        try:
            print("Ejecutando la consulta para obtener celdas...")
            respuesta = self.operacionCrud.execSelect('sp_SelectCelda', '{}')  # JSON vacío

            # Desencriptar la Ubicacion en cada resultado
            for celda in respuesta:
                if 'Ubicacion' in celda:
                    celda['Ubicacion'] = self.encriptar.desencriptar(celda['Ubicacion'])

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
            # Crear el JSON que pasará como parámetro al SP
            json_param = '{"where": {"ID_Celda": ' + str(ID_Celda) + '}}'
        
            # Llamar al procedimiento almacenado pasando el JSON como parámetro
            respuesta = self.operacionCrud.execSelect('sp_SelectCelda', json_param)  # Pasar el JSON completo

            self.show.mostrar_resultados_dinamico(respuesta)

        except pyodbc.Error as e:
            print(f"Error en la ejecución de la consulta: {e}")
            
        finally:
            conexion.cerrar()  # Asegurarse de cerrar la conexión

    
    def actualizar_celda(self, editar_celda: Celda):
        celda_dict = editar_celda.to_dict()
        celda_json = json.dumps(celda_dict)
        self.operacionCrud.execUpdate('sp_UpdateCelda', celda_json, '{"where": "ID_celda = ' + str(editar_celda.get_ID_Celda()) + '"}')

    def eliminar_celda(self, ID_Celda):
        # Construir la condición como una cadena
        condition = f"ID_Celda = {ID_Celda}"
        # Llamar al procedimiento almacenado pasando la condición como parámetro
        self.operacionCrud.execDelete('sp_DeleteCelda', condition)
