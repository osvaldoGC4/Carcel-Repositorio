import json
from models.delito import Delito
from common.crud import Crud

class DelitoController:
    operacionCrud = None
    def __init__(self):
        self.operacionCrud = Crud()

    # Crear un nuevo registro de delito
    def crear_delito(self, tipo, descripcion):
    
        nueva_delito = Delito(
            tipo=tipo, 
            descripcion=descripcion, 
        )
       # Convertir la delito en un diccionario para que sea serializable
        delito_dict = nueva_delito.to_dict()
        # Convertir el diccionario a JSON
        delito_json = json.dumps(delito_dict)

        # Imprimir el objeto original y el JSON
        print(nueva_delito)  # Imprime el objeto delito
        print(delito_json)   # Imprime el objeto convertido en JSON

        # Llamar al método para insertar en la base de datos
        self.operacionCrud.execInsert("delito", delito_json)
        print(f"delito {tipo} {descripcion} creada con éxito.")  # Cambiar "Interno" por "delito"
