class InformeDisciplina:
    def __init__(self, ID_Informe=None, ID_Interno=None, Fecha=None, Descripcion=None, Sancion=None):
        self._ID_Informe = ID_Informe
        self._ID_Interno = ID_Interno
        self._Fecha = Fecha
        self._Descripcion = Descripcion
        self._Sancion = Sancion

    # Getters
    def get_ID_Informe(self):
        return self._ID_Informe

    def get_ID_Interno(self):
        return self._ID_Interno

    def get_Fecha(self):
        return self._Fecha

    def get_Descripcion(self):
        return self._Descripcion

    def get_Sancion(self):
        return self._Sancion

    # Setters con validación
    def set_ID_Informe(self, ID_Informe):
        self._ID_Informe = ID_Informe

    def set_ID_Interno(self, ID_Interno):
        self._ID_Interno = ID_Interno

    def set_Fecha(self, Fecha):
        self._Fecha = Fecha

    def set_Descripcion(self, Descripcion):
        self._Descripcion = Descripcion

    def set_Sancion(self, Sancion):
        self._Sancion = Sancion

    # Método para convertir a diccionario
    def to_dict(self):
        return {
            'ID_Informe': self._ID_Informe,
            'ID_Interno': self._ID_Interno,
            'Fecha': self._Fecha,
            'Descripcion': self._Descripcion,
            'Sancion': self._Sancion
        }
