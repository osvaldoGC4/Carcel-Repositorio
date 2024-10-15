
class Celda:
    def __init__(self, id_celda=None, ubicacion=None, capacidad=None, estado=None):
        self._id_celda = id_celda
        self._ubicacion = ubicacion
        self._capacidad = capacidad
        self._estado = estado

    # Métodos Getters
    def get_id_celda(self):
        return self._id_celda

    def get_ubicacion(self):
        return self._ubicacion

    def get_capacidad(self):
        return self._capacidad

    def get_estado(self):
        return self._estado

    # Métodos Setters con validación
    def set_id_celda(self, id_celda):
        if isinstance(id_celda, int) and id_celda > 0:
            self._id_celda = id_celda
        else:
            raise ValueError("El ID de la celda debe ser un entero positivo.")

    def set_ubicacion(self, ubicacion):
        self._ubicacion = ubicacion

    def set_capacidad(self, capacidad):
        if isinstance(capacidad, int) and capacidad > 0:
            self._capacidad = capacidad
        else:
            raise ValueError("La capacidad debe ser un entero positivo.")

    def set_estado(self, estado):
        if estado in ['Ocupada', 'Disponible']:
            self._estado = estado
        else:
            raise ValueError("Estado inválido. Debe ser 'Ocupada' o 'Disponible'.")

    # Método para representar el objeto
    def __str__(self):
        return f"Celda(id: {self._id_celda}, ubicacion: {self._ubicacion}, capacidad: {self._capacidad}, estado: {self._estado})"



