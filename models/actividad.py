
class Actividad:
    def __init__(self, id_actividad=None, nombre=None, descripcion=None):
        self._id_actividad = id_actividad
        self._nombre = nombre
        self._descripcion = descripcion

    # Métodos Getters
    def get_id_actividad(self):
        return self._id_actividad

    def get_nombre(self):
        return self._nombre

    def get_descripcion(self):
        return self._descripcion

    # Métodos Setters
    def set_id_actividad(self, id_actividad):
        if isinstance(id_actividad, int) and id_actividad > 0:
            self._id_actividad = id_actividad
        else:
            raise ValueError("El ID de la actividad debe ser un entero positivo.")

    def set_nombre(self, nombre):
        self._nombre = nombre

    def set_descripcion(self, descripcion):
        self._descripcion = descripcion

    # Método para representar el objeto
    def __str__(self):
        return f"Actividad(id: {self._id_actividad}, nombre: {self._nombre}, descripcion: {self._descripcion})"


 