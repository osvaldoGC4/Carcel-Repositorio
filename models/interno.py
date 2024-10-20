
class Interno:
    def __init__(self, id_interno=None, nombre=None, fecha_ingreso=None, Estado=None, ID_Celda=None, fecha_liberacion=None):
        self._id_interno = id_interno
        self._nombre = nombre
        self._fecha_ingreso = fecha_ingreso
        self._Estado = Estado
        self._ID_Celda = ID_Celda
        self._fecha_liberacion = fecha_liberacion

    # Métodos Getters
    def get_id_interno(self):
        return self._id_interno

    def get_nombre(self):
        return self._nombre

    def get_fecha_ingreso(self):
        return self._fecha_ingreso

    def get_Estado(self):
        return self._Estado

    def get_ID_Celda(self):
        return self._ID_Celda

    def get_fecha_liberacion(self):
        return self._fecha_liberacion

    # Métodos Setters con validación
    def set_id_interno(self, id_interno):
        if isinstance(id_interno, int) and id_interno > 0:
            self._id_interno = id_interno
        else:
            raise ValueError("El ID del interno debe ser un entero positivo.")

    def set_nombre(self, nombre):
        self._nombre = nombre

    def set_fecha_ingreso(self, fecha_ingreso):
        self._fecha_ingreso = fecha_ingreso

    def set_Estado(self, Estado):
        if Estado in ['Activo', 'Liberado', 'Transferido']:
            self._Estado = Estado
        else:
            raise ValueError("Estado inválido. Debe ser 'Activo', 'Liberado' o 'Transferido'.")

    def set_ID_Celda(self, ID_Celda):
        self._ID_Celda = ID_Celda

    def set_fecha_liberacion(self, fecha_liberacion):
        self._fecha_liberacion = fecha_liberacion

    # Método para representar el objeto
    def __str__(self):
        return f"Interno(id: {self._id_interno}, nombre: {self._nombre}, fecha_ingreso: {self._fecha_ingreso}, Estado: {self._Estado}, ID_Celda: {self._ID_Celda}, fecha_liberacion: {self._fecha_liberacion})"
