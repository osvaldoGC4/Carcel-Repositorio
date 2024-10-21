class Interno:
    def __init__(self, ID_Interno=None, Nombre=None, Fecha_Ingreso=None, Estado=None, ID_Celda=None, Fecha_Liberacion=None):
        self._ID_Interno = ID_Interno
        self._Nombre = Nombre
        self._Fecha_Ingreso = Fecha_Ingreso
        self._Estado = Estado
        self._ID_Celda = ID_Celda
        self._Fecha_Liberacion = Fecha_Liberacion

    # Getters
    def get_ID_Interno(self):
        return self._ID_Interno

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
    def set_ID_Interno(self, ID_Interno):
        if isinstance(ID_Interno, int) and ID_Interno > 0:
            self._ID_Interno = ID_Interno
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
            'ID_Interno': self._ID_Interno,
            'Nombre': self._Nombre,
            'Fecha_Ingreso': self._Fecha_Ingreso,
            'Estado': self._Estado,
            'ID_Celda': self._ID_Celda,
            'Fecha_Liberacion': self._Fecha_Liberacion
        }
