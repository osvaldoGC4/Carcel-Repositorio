import json
from datetime import datetime, date, time

class Utiles:
    @staticmethod
    def list_to_dict(objects, decrypt_fn=None):
        """
        Convierte una lista de objetos en una lista de diccionarios y desencripta si se proporciona una función de desencriptación.
        :param objects: Lista de objetos.
        :param decrypt_fn: Función de desencriptado a aplicar en los valores de tipo string.
        :return: Lista de diccionarios.
        """
        resultado = []
        for obj in objects:
            item_dict = Utiles.to_dict(obj)
            if decrypt_fn:
                item_dict = {k: decrypt_fn(v) if isinstance(v, str) else v for k, v in item_dict.items()}
            resultado.append(item_dict)
        return resultado

    @staticmethod
    def to_dict(obj):
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
