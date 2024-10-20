
class Celda:
    def __init__(self, ID_Celda=None, Ubicacion=None, Capacidad=None, Estado=None):
        self._ID_Celda = ID_Celda
        self._Ubicacion = Ubicacion
        self._Capacidad = Capacidad
        self._Estado = Estado

    # Métodos Getters
    def get_ID_Celda(self):
        return self._ID_Celda

    def get_Ubicacion(self):
        return self._Ubicacion

    def get_Capacidad(self):
        return self._Capacidad

    def get_Estado(self):
        return self._Estado

    # Métodos Setters con validación
    def set_ID_Celda(self, ID_Celda):
        if isinstance(ID_Celda, int) and ID_Celda > 0:
            self._ID_Celda = ID_Celda
        else:
            raise ValueError("El ID de la celda debe ser un entero positivo.")

    def set_Ubicacion(self, Ubicacion):
        self._Ubicacion = Ubicacion

    def set_Capacidad(self, Capacidad):
        if isinstance(Capacidad, int) and Capacidad > 0:
            self._Capacidad = Capacidad
        else:
            raise ValueError("La Capacidad debe ser un entero positivo.")

    def set_Estado(self, Estado):
        if Estado in ['Ocupada', 'Disponible']:
            self._Estado = Estado
        else:
            raise ValueError("Estado inválido. Debe ser 'Ocupada' o 'Disponible'.")

    # Método para representar el objeto
    def __str__(self):
        return f"Celda(id: {self._ID_Celda}, Ubicacion: {self._Ubicacion}, Capacidad: {self._Capacidad}, Estado: {self._Estado})"


      # Método para convertir el objeto en un diccionario
    def to_dict(self):
        return {
            'ID_Celda': self._ID_Celda,
            'Ubicacion': self._Ubicacion,
            'Capacidad': self._Capacidad,
            'Estado': self._Estado
        }
