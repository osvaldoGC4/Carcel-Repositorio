class InternoActividad:
    def __init__(self, ID_Interno=None, ID_Actividad=None):
        self._ID_Interno = ID_Interno
        self._ID_Actividad = ID_Actividad

    # Getters
    def get_ID_Interno(self):
        return self._ID_Interno

    def get_ID_Actividad(self):
        return self._ID_Actividad

    # Setters con validación
    def set_ID_Interno(self, ID_Interno):
        self._ID_Interno = ID_Interno

    def set_ID_Actividad(self, ID_Actividad):
        self._ID_Actividad = ID_Actividad

    # Método para convertir a diccionario
    def to_dict(self):
        return {
            'ID_Interno': self._ID_Interno,
            'ID_Actividad': self._ID_Actividad
        }
