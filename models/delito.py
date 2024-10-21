class Delito:
    def __init__(self, ID_Delito=None, Tipo=None, Descripcion=None):
        self._ID_Delito = ID_Delito
        self._Tipo = Tipo
        self._Descripcion = Descripcion

    # Getters
    def get_ID_Delito(self):
        return self._ID_Delito

    def get_Tipo(self):
        return self._Tipo

    def get_Descripcion(self):
        return self._Descripcion

    # Setters con validación
    def set_ID_Delito(self, ID_Delito):
        self._ID_Delito = ID_Delito

    def set_Tipo(self, Tipo):
        self._Tipo = Tipo

    def set_Descripcion(self, Descripcion):
        self._Descripcion = Descripcion

    # Método para convertir a diccionario
    def to_dict(self):
        return {
            'ID_Delito': self._ID_Delito,
            'Tipo': self._Tipo,
            'Descripcion': self._Descripcion
        }
