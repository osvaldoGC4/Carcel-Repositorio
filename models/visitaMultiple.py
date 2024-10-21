class VisitaMultiple:
    def __init__(self, ID_Visita=None, ID_Visitante=None):
        self._ID_Visita = ID_Visita
        self._ID_Visitante = ID_Visitante

    # Getters
    def get_ID_Visita(self):
        return self._ID_Visita

    def get_ID_Visitante(self):
        return self._ID_Visitante

    # Setters con validación
    def set_ID_Visita(self, ID_Visita):
        self._ID_Visita = ID_Visita

    def set_ID_Visitante(self, ID_Visitante):
        self._ID_Visitante = ID_Visitante

    # Método para convertir a diccionario
    def to_dict(self):
        return {
            'ID_Visita': self._ID_Visita,
            'ID_Visitante': self._ID_Visitante
        }
