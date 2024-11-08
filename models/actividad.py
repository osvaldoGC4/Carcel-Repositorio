class Actividad:
    def __init__(self, ID=None, Nombre=None, Tipo=None, Horario=None):
        self._ID = ID
        self._Nombre = Nombre
        self._Tipo = Tipo
        self._Horario = Horario

    # Getters
    def get_ID(self):
        return self._ID

    def get_Nombre(self):
        return self._Nombre

    def get_Tipo(self):
        return self._Tipo

    def get_Horario(self):
        return self._Horario

    # Setters con validación
    def set_ID(self, ID):
        if isinstance(ID, int) and ID > 0:
            self._ID = ID
        else:
            raise ValueError("El ID de la actividad debe ser un entero positivo.")

    def set_Nombre(self, Nombre):
        self._Nombre = Nombre

    def set_Tipo(self, Tipo):
        self._Tipo = Tipo

    def set_Horario(self, Horario):
        self._Horario = Horario

    # Método para convertir a diccionario
    def to_dict(self):
        return {
            'ID': self._ID,
            'Nombre': self._Nombre,
            'Tipo': self._Tipo,
            'Horario': self._Horario
        }
