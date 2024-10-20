
class Visitante:
    def __init__(self, id_visitante=None, nombre=None, documento_identidad=None, telefono=None):
        self._id_visitante = id_visitante
        self._nombre = nombre
        self._documento_identidad = documento_identidad
        self._telefono = telefono

    # Métodos Getters
    def get_id_visitante(self):
        return self._id_visitante

    def get_nombre(self):
        return self._nombre

    def get_documento_identidad(self):
        return self._documento_identidad

    def get_telefono(self):
        return self._telefono

    # Métodos Setters
    def set_id_visitante(self, id_visitante):
        if isinstance(id_visitante, int) and id_visitante > 0:
            self._id_visitante = id_visitante
        else:
            raise ValueError("El ID del visitante debe ser un entero positivo.")

    def set_nombre(self, nombre):
        self._nombre = nombre

    def set_documento_identidad(self, documento_identidad):
        self._documento_identidad = documento_identidad

    def set_telefono(self, telefono):
        self._telefono = telefono

    # Método para representar el objeto
    def __str__(self):
        return f"Visitante(id: {self._id_visitante}, nombre: {self._nombre}, documento_identidad: {self._documento_identidad}, telefono: {self._telefono})"
