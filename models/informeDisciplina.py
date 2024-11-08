class InformeDisciplina:
    def __init__(self, ID=None, ID_Interno=None, Fecha=None, Descripcion=None, Sancion=None):
        self._ID = ID
        self._ID_Interno = ID_Interno
        self._Fecha = Fecha
        self._Descripcion = Descripcion
        self._Sancion = Sancion

    # Getters
    def get_ID(self):
        return self._ID

    def get_ID_Interno(self):
        return self._ID_Interno

    def get_Fecha(self):
        return self._Fecha

    def get_Descripcion(self):
        return self._Descripcion

    def get_Sancion(self):
        return self._Sancion

    # Setters con validación
    def set_ID(self, ID):
        self._ID = ID

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
            'ID': self._ID,
            'ID_Interno': self._ID_Interno,
            'Fecha': self._Fecha,
            'Descripcion': self._Descripcion,
            'Sancion': self._Sancion
        }
