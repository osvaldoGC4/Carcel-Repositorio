class Personal:
    def __init__(self, ID_Personal=None, Nombre=None, Rol=None, Horario=None, Estado=None):
        self._ID_Personal = ID_Personal
        self._Nombre = Nombre
        self._Rol = Rol
        self._Horario = Horario
        self._Estado = Estado

    # Getters
    def get_ID_Personal(self):
        return self._ID_Personal

    def get_Nombre(self):
        return self._Nombre

    def get_Rol(self):
        return self._Rol

    def get_Horario(self):
        return self._Horario

    def get_Estado(self):
        return self._Estado

    # Setters con validación
    def set_ID_Personal(self, ID_Personal):
        self._ID_Personal = ID_Personal

    def set_Nombre(self, Nombre):
        self._Nombre = Nombre

    def set_Rol(self, Rol):
        self._Rol = Rol

    def set_Horario(self, Horario):
        self._Horario = Horario

    def set_Estado(self, Estado):
        self._Estado = Estado

    # Método para convertir a diccionario
    def to_dict(self):
        return {
            'ID_Personal': self._ID_Personal,
            'Nombre': self._Nombre,
            'Rol': self._Rol,
            'Horario': self._Horario,
            'Estado': self._Estado
        }
