class Visita:
    def __init__(self, ID_Visita=None, ID_Interno=None, ID_Visitante=None, Fecha=None, Hora_Inicio=None, Duracion=None):
        self._ID_Visita = ID_Visita
        self._ID_Interno = ID_Interno
        self._ID_Visitante = ID_Visitante
        self._Fecha = Fecha
        self._Hora_Inicio = Hora_Inicio
        self._Duracion = Duracion

    # Getters
    def get_ID_Visita(self):
        return self._ID_Visita

    def get_ID_Interno(self):
        return self._ID_Interno

    def get_ID_Visitante(self):
        return self._ID_Visitante

    def get_Fecha(self):
        return self._Fecha

    def get_Hora_Inicio(self):
        return self._Hora_Inicio

    def get_Duracion(self):
        return self._Duracion

    # Setters con validación
    def set_ID_Visita(self, ID_Visita):
        self._ID_Visita = ID_Visita

    def set_ID_Interno(self, ID_Interno):
        self._ID_Interno = ID_Interno

    def set_ID_Visitante(self, ID_Visitante):
        self._ID_Visitante = ID_Visitante

    def set_Fecha(self, Fecha):
        self._Fecha = Fecha

    def set_Hora_Inicio(self, Hora_Inicio):
        self._Hora_Inicio = Hora_Inicio

    def set_Duracion(self, Duracion):
        self._Duracion = Duracion

    # Método para convertir a diccionario
    def to_dict(self):
        return {
            'ID_Visita': self._ID_Visita,
            'ID_Interno': self._ID_Interno,
            'ID_Visitante': self._ID_Visitante,
            'Fecha': self._Fecha,
            'Hora_Inicio': self._Hora_Inicio,
            'Duracion': self._Duracion
        }
