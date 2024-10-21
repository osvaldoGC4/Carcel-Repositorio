class Actividad:
    def __init__(self, ID_Actividad=None, Nombre=None, Tipo=None, Horario=None):
        self._ID_Actividad = ID_Actividad
        self._Nombre = Nombre
        self._Tipo = Tipo
        self._Horario = Horario

    # Getters
    def get_ID_Actividad(self):
        return self._ID_Actividad

    def get_Nombre(self):
        return self._Nombre

    def get_Tipo(self):
        return self._Tipo

    def get_Horario(self):
        return self._Horario

    # Setters con validación
    def set_ID_Actividad(self, ID_Actividad):
        if isinstance(ID_Actividad, int) and ID_Actividad > 0:
            self._ID_Actividad = ID_Actividad
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
            'ID_Actividad': self._ID_Actividad,
            'Nombre': self._Nombre,
            'Tipo': self._Tipo,
            'Horario': self._Horario
        }
