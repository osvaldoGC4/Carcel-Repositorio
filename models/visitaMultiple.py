class VisitaMultiple:
    def __init__(self, ID=None, ID_Visita=None, ID_Visitante=None, Observacion=None):
        self._ID = ID
        self._ID_Visita = ID_Visita
        self._ID_Visitante = ID_Visitante
        self._Observacion = Observacion

    # Getters
    def get_ID(self):
        return self._ID

    def get_ID_Visita(self):
        return self._ID_Visita

    def get_ID_Visitante(self):
        return self._ID_Visitante

    def get_Observacion(self):
        return self._Observacion

    # Setters con validación
    def set_ID(self, ID):
        self._ID = ID

    def set_ID_Visita(self, ID_Visita):
        self._ID_Visita = ID_Visita

    def set_ID_Visitante(self, ID_Visitante):
        self._ID_Visitante = ID_Visitante

    def set_Observacion(self, Observacion):
        self._Observacion = Observacion

    # Método para convertir a diccionario
    def to_dict(self):
        return {
            'ID': self._ID,
            'ID_Visita': self._ID_Visita,
            'ID_Visitante': self._ID_Visitante,
            'Observacion': self._Observacion
        }
