class InternoActividad:
    def __init__(self, ID=None, ID_Interno=None, ID_Actividad=None, FechaActividad= None):
        self._ID = ID
        self._ID_Interno = ID_Interno
        self._ID_Actividad = ID_Actividad
        self._FechaActividad = FechaActividad

    # Getters
    def get_ID(self):
        return self._ID

    def get_ID_Interno(self):
        return self._ID_Interno

    def get_ID_Actividad(self):
        return self._ID_Actividad

    def get_FechaActividad(self):
        return self._FechaActividad

    # Setters con validación
    def set_ID(self, ID):
        self._ID = ID

    def set_ID_Interno(self, ID_Interno):
        self._ID_Interno = ID_Interno

    def set_ID_Actividad(self, ID_Actividad):
        self._ID_Actividad = ID_Actividad

    def set_FechaActividad(self, FechaActividad):
        self._FechaActividad = FechaActividad

    # Método para convertir a diccionario
    def to_dict(self):
        return {
            'ID': self._ID,
            'ID_Interno': self._ID_Interno,
            'ID_Actividad': self._ID_Actividad,
            'FechaActividad': self._FechaActividad
        }
