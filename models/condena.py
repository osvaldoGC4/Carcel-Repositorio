class Condena:
    def __init__(self, ID_Condena=None, ID_Interno=None, ID_Delito=None, Fecha_Inicio=None, Duracion=None, Tipo=None, ID_Personal=None):
        self._ID_Condena = ID_Condena
        self._ID_Interno = ID_Interno
        self._ID_Delito = ID_Delito
        self._Fecha_Inicio = Fecha_Inicio
        self._Duracion = Duracion
        self._Tipo = Tipo
        self._ID_Personal = ID_Personal

    # Getters
    def get_ID_Condena(self):
        return self._ID_Condena

    def get_ID_Interno(self):
        return self._ID_Interno

    def get_ID_Delito(self):
        return self._ID_Delito

    def get_Fecha_Inicio(self):
        return self._Fecha_Inicio

    def get_Duracion(self):
        return self._Duracion

    def get_Tipo(self):
        return self._Tipo

    def get_ID_Personal(self):
        return self._ID_Personal

    # Setters con validación
    def set_ID_Condena(self, ID_Condena):
        self._ID_Condena = ID_Condena

    def set_ID_Interno(self, ID_Interno):
        self._ID_Interno = ID_Interno

    def set_ID_Delito(self, ID_Delito):
        self._ID_Delito = ID_Delito

    def set_Fecha_Inicio(self, Fecha_Inicio):
        self._Fecha_Inicio = Fecha_Inicio

    def set_Duracion(self, Duracion):
        self._Duracion = Duracion

    def set_Tipo(self, Tipo):
        self._Tipo = Tipo

    def set_ID_Personal(self, ID_Personal):
        self._ID_Personal = ID_Personal

    # Método para convertir a diccionario
    def to_dict(self):
        return {
            'ID_Condena': self._ID_Condena,
            'ID_Interno': self._ID_Interno,
            'ID_Delito': self._ID_Delito,
            'Fecha_Inicio': self._Fecha_Inicio,
            'Duracion': self._Duracion,
            'Tipo': self._Tipo,
            'ID_Personal': self._ID_Personal
        }
