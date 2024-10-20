import json
from models.celda import Celda
from common.crud import Crud

class CeldaController:
    operacionCrud = None
    def __init__(self):
        self.operacionCrud = Crud()

    # Crear un nuevo registro de Celda
    def crear_celda(self, id_celda, ubicacion, capacidad, estado):
    
        nueva_celda = Celda(
            id_celda = id_celda,
            ubicacion = ubicacion,
            capacidad = capacidad,
            estado = estado
        )
       # Convertir la celda en un diccionario para que sea serializable
        celda_dict = nueva_celda.to_dict()
        # Convertir el diccionario a JSON
        celda_json = json.dumps(celda_dict)

        # Imprimir el objeto original y el JSON
        print(nueva_celda)  # Imprime el objeto Celda
        print(celda_json)   # Imprime el objeto convertido en JSON

        # Llamar al método para insertar en la base de datos
        self.operacionCrud.execInsert("celda", celda_json)
        print(f"Celda {ubicacion} creada con éxito.")  # Cambiar "Interno" por "Celda"
