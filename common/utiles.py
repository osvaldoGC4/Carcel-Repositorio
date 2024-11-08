import sys;
import json;
from datetime import datetime, date, time
class Utiles:

    @staticmethod
    def ADict(data: str) -> dict:
        respuesta = {}
        try:
            data = data.replace("'", '"')
            respuesta = json.loads(data)
            return respuesta
        except:
            print(sys.exc_info())
            return None

    @staticmethod
    def to_dict(obj):
        """
        Convierte cualquier objeto a un diccionario de manera dinámica.
        Si el objeto tiene atributos que también son objetos, aplica la conversión recursiva.
        Convierte valores de tipo datetime, date y time a cadenas formateadas para que sean serializables.
        """
        if isinstance(obj, list):
            return [Utiles.to_dict(item) for item in obj]
        
        if isinstance(obj, dict):
            return {k: Utiles.to_dict(v) for k, v in obj.items()}
        
        if isinstance(obj, (date, datetime)):
            return obj.strftime('%Y-%m-%d')
        
        if isinstance(obj, time):
            return obj.strftime('%H:%M:%S')
        
        if hasattr(obj, "__dict__"):
            result = {}
            for key, value in obj.__dict__.items():
                result[key] = Utiles.to_dict(value)
            return result
        
        return obj

    @staticmethod
    def list_to_dict(objects):
        """
        Convierte una lista de objetos en una lista de diccionarios.
        :param objects: Lista de objetos.
        :return: Lista de diccionarios.
        """
        return [Utiles.to_dict(obj) for obj in objects]

    @staticmethod
    def mostrar_resultados_dinamico(respuesta):
        if respuesta:  # Verificar si 'respuesta' tiene datos
            # Obtener las columnas de la primera fila de la respuesta
            columnas = respuesta[0].keys()

            # Mostrar encabezados dinámicos
            encabezado = " | ".join([f"{col:<20}" for col in columnas])
            print(encabezado)
            print("-" * len(encabezado))  # Línea separadora con longitud dinámica

            # Mostrar los valores de cada fila
            for row in respuesta:
                valores = " | ".join([f"{str(row[col]):<20}" for col in columnas])
                print(valores)
        else:
            print("No se encontraron datos.")