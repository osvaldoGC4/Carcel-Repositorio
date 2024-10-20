import json
from models.celda import Celda
from common.crud import Crud

class CeldaController:
    operacionCrud = None
    def __init__(self):
        self.operacionCrud = Crud()

    # Crear un nuevo registro de Celda
    def crear_celda(self, nueva_celda: Celda):
       # Convertir la celda en un diccionario para que sea serializable
        celda_dict = nueva_celda.to_dict()
        # Convertir el diccionario a JSON
        celda_json = json.dumps(celda_dict)
        # Llamar al método para insertar en la base de datos
        if self.operacionCrud.execInsert("celda", celda_json):
            print(f"Celda {nueva_celda.get_Capacidad()} creada con éxito.")  # Cambiar "Interno" por "Celda"
        else: 
            print(f"Problemas al insertar Celda {nueva_celda.get_Capacidad()}.")  # Cambiar "Interno" por "Celda"

    def obtener_celdas(self):
        self.operacionCrud.execSelect('celda', '*', '')
    
    def obtener_celda(self, ID_Celda):
        self.operacionCrud.execSelect('celda', '*', '{"where": "ID_Celda = '+ ID_Celda +'"}')
    
    def actualizar_celda(self, editar_celda: Celda):
        celda_dict = editar_celda.to_dict()
        celda_json = json.dumps(celda_dict)
        self.operacionCrud.execUpdate('celda', celda_json, '{"where": "ID_celda = ' + editar_celda.get_ID_Celda() + '"}')

    def eliminar_celda(self, ID_Celda):
        self.operacionCrud.execDelete('celda', f'ID_Celda = {ID_Celda}')

