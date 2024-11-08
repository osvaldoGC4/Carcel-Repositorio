class Personal:
    def __init__(self, ID=None, Nombre=None, Rol=None, Horario=None, Estado=None):
        self._ID = ID
        self._Nombre = Nombre
        self._Rol = Rol
        self._Horario = Horario
        self._Estado = Estado

    # Getters
    def get_ID(self):
        return self._ID

    def get_Nombre(self):
        return self._Nombre

    def get_Rol(self):
        return self._Rol

    def get_Horario(self):
        return self._Horario

    def get_Estado(self):
        return self._Estado

    # Setters con validación
    def set_ID(self, ID):
        self._ID = ID

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
            'ID': self._ID,
            'Nombre': self._Nombre,
            'Rol': self._Rol,
            'Horario': self._Horario,
            'Estado': self._Estado
        }
