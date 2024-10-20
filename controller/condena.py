import json
from models.condena import Condena
from common.crud import Crud

class CondenaController:
    operacionCrud = None
    def __init__(self):
        self.operacionCrud = Crud()

    # Crear un nuevo registro de condena
    def crear_condena(self, id_interno,id_delito,fecha_inicio,duracion,tipo,id_personal):    
        nueva_condena = Condena(
            id_interno = id_interno,
            id_delito = id_delito,
            fecha_inicio = fecha_inicio,
            duracion = duracion,
            tipo = tipo,
            id_personal = id_personal,
        )
       # Convertir la condena en un diccionario para que sea serializable
        condena_dict = nueva_condena.to_dict()
        # Convertir el diccionario a JSON
        condena_json = json.dumps(condena_dict)

        # Imprimir el objeto original y el JSON
        print(nueva_condena)  # Imprime el objeto condena
        print(condena_json)   # Imprime el objeto convertido en JSON

        # Llamar al método para insertar en la base de datos
        self.operacionCrud.execInsert("condena", condena_json)
        print(f"condena {tipo} creada con éxito.")  # Cambiar "Interno" por "condena"
