import json
from models.actividad import Actividad
from common.crud import Crud
class ActividadController:
    operacionCrud = None
    def __init__(self):
        self.operacionCrud = Crud()

    # Crear un nuevo registro de actividad
    def crear_actividad(self, nombre, descripcion):
    
        nueva_actividad = Actividad(
            nombre = nombre,
            descripcion = descripcion
        )
       # Convertir la actividad en un diccionario para que sea serializable
        actividad_dict = nueva_actividad.to_dict()
        # Convertir el diccionario a JSON
        actividad_json = json.dumps(actividad_dict)

        # Imprimir el objeto original y el JSON
        print(nueva_actividad)  # Imprime el objeto actividad
        print(actividad_json)   # Imprime el objeto convertido en JSON

        # Llamar al método para insertar en la base de datos
        self.operacionCrud.execInsert("actividad", actividad_json)
        print(f"actividad {nombre} creada con éxito.")  # Cambiar "Interno" por "actividad"
