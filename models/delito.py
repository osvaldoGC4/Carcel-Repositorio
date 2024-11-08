class Delito:
    def __init__(self, ID=None, Tipo=None, Descripcion=None):
        self._ID = ID
        self._Tipo = Tipo
        self._Descripcion = Descripcion

    # Getters
    def get_ID(self):
        return self._ID

    def get_Tipo(self):
        return self._Tipo

    def get_Descripcion(self):
        return self._Descripcion

    # Setters con validación
    def set_ID(self, ID):
        self._ID = ID

    def set_Tipo(self, Tipo):
        self._Tipo = Tipo

    def set_Descripcion(self, Descripcion):
        self._Descripcion = Descripcion

    # Método para convertir a diccionario
    def to_dict(self):
        return {
            'ID': self._ID,
            'Tipo': self._Tipo,
            'Descripcion': self._Descripcion
        }
