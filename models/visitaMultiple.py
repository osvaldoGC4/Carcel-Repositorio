
class VisitaMultiple:
    def __init__(self, id_visita_multiple=None, id_visita=None, id_actividad=None, id_visitante=None, fecha_visita_multiple=None):
        self._id_visita_multiple = id_visita_multiple
        self._id_visita = id_visita
        self._id_actividad = id_actividad
        self._id_visitante = id_visitante
        self._fecha_visita_multiple = fecha_visita_multiple

    # Métodos Getters
    def get_id_visita_multiple(self):
        return self._id_visita_multiple

    def get_id_visita(self):
        return self._id_visita

    def get_id_actividad(self):
        return self._id_actividad

    def get_id_visitante(self):
        return self._id_visitante

    def get_fecha_visita_multiple(self):
        return self._fecha_visita_multiple

    # Métodos Setters
    def set_id_visita_multiple(self, id_visita_multiple):
        if isinstance(id_visita_multiple, int) and id_visita_multiple > 0:
            self._id_visita_multiple = id_visita_multiple
        else:
            raise ValueError("El ID de la visita múltiple debe ser un entero positivo.")

    def set_id_visita(self, id_visita):
        self._id_visita = id_visita

    def set_id_actividad(self, id_actividad):
        self._id_actividad = id_actividad

    def set_id_visitante(self, id_visitante):
        self._id_visitante = id_visitante

    def set_fecha_visita_multiple(self, fecha_visita_multiple):
        self._fecha_visita_multiple = fecha_visita_multiple

    # Método para representar el objeto
    def __str__(self):
        return f"VisitaMultiple(id: {self._id_visita_multiple}, id_visita: {self._id_visita}, id_actividad: {self._id_actividad}, id_visitante: {self._id_visitante}, fecha_visita_multiple: {self._fecha_visita_multiple})"
