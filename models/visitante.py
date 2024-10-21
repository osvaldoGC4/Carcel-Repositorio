class Visitante:
    def __init__(self, ID_Visitante=None, Nombre=None, Relacion=None, Documento=None):
        self._ID_Visitante = ID_Visitante
        self._Nombre = Nombre
        self._Relacion = Relacion
        self._Documento = Documento

    # Getters
    def get_ID_Visitante(self):
        return self._ID_Visitante

    def get_Nombre(self):
        return self._Nombre

    def get_Relacion(self):
        return self._Relacion

    def get_Documento(self):
        return self._Documento

    # Setters con validación
    def set_ID_Visitante(self, ID_Visitante):
        self._ID_Visitante = ID_Visitante

    def set_Nombre(self, Nombre):
        self._Nombre = Nombre

    def set_Relacion(self, Relacion):
        self._Relacion = Relacion

    def set_Documento(self, Documento):
        self._Documento = Documento

    # Método para convertir a diccionario
    def to_dict(self):
        return {
            'ID_Visitante': self._ID_Visitante,
            'Nombre': self._Nombre,
            'Relacion': self._Relacion,
            'Documento': self._Documento
        }
