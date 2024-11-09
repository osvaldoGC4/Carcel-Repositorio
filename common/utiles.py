import re
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
                item_dict = {
                    k: decrypt_fn(v) if isinstance(v, str) and not Utiles.is_date_format(v) else v 
                    for k, v in item_dict.items()
                }
            resultado.append(item_dict)
        return resultado

    @staticmethod
    def to_dict(obj):
        if isinstance(obj, list):
            return [Utiles.to_dict(item) for item in obj]
        if isinstance(obj, dict):
            return {k: Utiles.to_dict(v) for k, v in obj.items()}
        if isinstance(obj, (datetime, date)):
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
    def is_date_format(value):
        """
        Verifica si una cadena está en un formato válido de fecha o de tiempo.
        """
        # Patrones para formatos comunes de fecha y hora
        date_patterns = [
            '%Y-%m-%d',           # Formato de fecha (AAAA-MM-DD)
            '%Y-%m-%d %H:%M:%S',  # Fecha y hora (AAAA-MM-DD HH:MM:SS)
            '%d/%m/%Y',           # Formato alternativo de fecha (DD/MM/AAAA)
            '%Y/%m/%d',           # Otra variación (AAAA/MM/DD)
        ]
        
        time_patterns = [
            r'^\d{2}:\d{2}:\d{2}$',              # HH:MM:SS
            r'^\d{2}:\d{2}$',                    # HH:MM
            r'^\d{2}:\d{2} (AM|PM)$',            # HH:MM AM/PM
            r'^\d{2}:\d{2}:\d{2} (AM|PM)$'       # HH:MM:SS AM/PM
        ]

        # Verificar cada patrón de fecha usando datetime.strptime
        for pattern in date_patterns:
            try:
                datetime.strptime(value, pattern)
                return True
            except ValueError:
                continue

        # Verificar patrones de hora usando expresiones regulares
        for pattern in time_patterns:
            if re.match(pattern, value):
                return True

        return False
