import json
from models.informeDisciplina import InformeDisciplina
from common.crud import Crud

class informeDisciplinaController:
    operacionCrud = None
    def __init__(self):
        self.operacionCrud = Crud()

    # Crear un nuevo registro de informeDisciplina
    def crear_informeDisciplina(self, id_interno,fecha_informe,descripcion,accion):
    
        nueva_informeDisciplina = InformeDisciplina(
            id_interno = id_interno,
            fecha_informe = fecha_informe,
            descripcion = descripcion,
            accion = accion
        )
       # Convertir la informeDisciplina en un diccionario para que sea serializable
        informeDisciplina_dict = nueva_informeDisciplina.to_dict()
        # Convertir el diccionario a JSON
        informeDisciplina_json = json.dumps(informeDisciplina_dict)

        # Imprimir el objeto original y el JSON
        print(nueva_informeDisciplina)  # Imprime el objeto informeDisciplina
        print(informeDisciplina_json)   # Imprime el objeto convertido en JSON

        # Llamar al método para insertar en la base de datos
        self.operacionCrud.execInsert("informeDisciplina", informeDisciplina_json)
        print(f"informeDisciplina {descripcion} creada con éxito.")  # Cambiar "Interno" por "informeDisciplina"
