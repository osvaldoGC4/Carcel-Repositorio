
class Delito:
    def __init__(self, id_delito=None, tipo=None, descripcion=None):
        self._id_delito = id_delito
        self._tipo = tipo
        self._descripcion = descripcion

    # Métodos Getters
    def get_id_delito(self):
        return self._id_delito

    def get_tipo(self):
        return self._tipo

    def get_descripcion(self):
        return self._descripcion

    # Métodos Setters
    def set_id_delito(self, id_delito):
        if isinstance(id_delito, int) and id_delito > 0:
            self._id_delito = id_delito
        else:
            raise ValueError("El ID del delito debe ser un entero positivo.")

    def set_tipo(self, tipo):
        self._tipo = tipo

    def set_descripcion(self, descripcion):
        self._descripcion = descripcion

    # Método para representar el objeto
    def __str__(self):
        return f"Delito(id: {self._id_delito}, tipo: {self._tipo}, descripcion: {self._descripcion})"
