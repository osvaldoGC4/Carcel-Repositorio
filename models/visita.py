
class Visita:
    def __init__(self, id_visita=None, id_interno=None, id_visitante=None, fecha_visita=None, hora_visita=None):
        self._id_visita = id_visita
        self._id_interno = id_interno
        self._id_visitante = id_visitante
        self._fecha_visita = fecha_visita
        self._hora_visita = hora_visita

    # Métodos Getters
    def get_id_visita(self):
        return self._id_visita

    def get_id_interno(self):
        return self._id_interno

    def get_id_visitante(self):
        return self._id_visitante

    def get_fecha_visita(self):
        return self._fecha_visita

    def get_hora_visita(self):
        return self._hora_visita

    # Métodos Setters
    def set_id_visita(self, id_visita):
        if isinstance(id_visita, int) and id_visita > 0:
            self._id_visita = id_visita
        else:
            raise ValueError("El ID de la visita debe ser un entero positivo.")

    def set_id_interno(self, id_interno):
        self._id_interno = id_interno

    def set_id_visitante(self, id_visitante):
        self._id_visitante = id_visitante

    def set_fecha_visita(self, fecha_visita):
        self._fecha_visita = fecha_visita

    def set_hora_visita(self, hora_visita):
        self._hora_visita = hora_visita

    # Método para representar el objeto
    def __str__(self):
        return f"Visita(id: {self._id_visita}, id_interno: {self._id_interno}, id_visitante: {self._id_visitante}, fecha_visita: {self._fecha_visita}, hora_visita: {self._hora_visita})"
