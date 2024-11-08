class Interno:
    def __init__(self, ID=None, Nombre=None, Fecha_Ingreso=None, Estado=None, ID_Celda=None, Fecha_Liberacion=None):
        self._ID = ID
        self._Nombre = Nombre
        self._Fecha_Ingreso = Fecha_Ingreso
        self._Estado = Estado
        self._ID_Celda = ID_Celda
        self._Fecha_Liberacion = Fecha_Liberacion

    # Getters
    def get_ID(self):
        return self._ID

    def get_Nombre(self):
        return self._Nombre

    def get_Fecha_Ingreso(self):
        return self._Fecha_Ingreso

    def get_Estado(self):
        return self._Estado

    def get_ID_Celda(self):
        return self._ID_Celda

    def get_Fecha_Liberacion(self):
        return self._Fecha_Liberacion

    # Setters con validación
    def set_ID(self, ID):
        if isinstance(ID, int) and ID > 0:
            self._ID = ID
        else:
            raise ValueError("El ID del interno debe ser un entero positivo.")

    def set_Nombre(self, Nombre):
        self._Nombre = Nombre

    def set_Fecha_Ingreso(self, Fecha_Ingreso):
        self._Fecha_Ingreso = Fecha_Ingreso

    def set_Estado(self, Estado):
        self._Estado = Estado

    def set_ID_Celda(self, ID_Celda):
        self._ID_Celda = ID_Celda

    def set_Fecha_Liberacion(self, Fecha_Liberacion):
        self._Fecha_Liberacion = Fecha_Liberacion

    # Método para convertir a diccionario
    def to_dict(self):
        return {
            'ID': self._ID,
            'Nombre': self._Nombre,
            'Fecha_Ingreso': self._Fecha_Ingreso,
            'Estado': self._Estado,
            'ID_Celda': self._ID_Celda,
            'Fecha_Liberacion': self._Fecha_Liberacion
        }
