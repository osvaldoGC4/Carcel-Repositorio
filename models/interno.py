
class Interno:
    def __init__(self, id_interno=None, nombre=None, fecha_ingreso=None, estado=None, id_celda=None, fecha_liberacion=None):
        self._id_interno = id_interno
        self._nombre = nombre
        self._fecha_ingreso = fecha_ingreso
        self._estado = estado
        self._id_celda = id_celda
        self._fecha_liberacion = fecha_liberacion

    # Métodos Getters
    def get_id_interno(self):
        return self._id_interno

    def get_nombre(self):
        return self._nombre

    def get_fecha_ingreso(self):
        return self._fecha_ingreso

    def get_estado(self):
        return self._estado

    def get_id_celda(self):
        return self._id_celda

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

    def set_estado(self, estado):
        if estado in ['Activo', 'Liberado', 'Transferido']:
            self._estado = estado
        else:
            raise ValueError("Estado inválido. Debe ser 'Activo', 'Liberado' o 'Transferido'.")

    def set_id_celda(self, id_celda):
        self._id_celda = id_celda

    def set_fecha_liberacion(self, fecha_liberacion):
        self._fecha_liberacion = fecha_liberacion

    # Método para representar el objeto
    def __str__(self):
        return f"Interno(id: {self._id_interno}, nombre: {self._nombre}, fecha_ingreso: {self._fecha_ingreso}, estado: {self._estado}, id_celda: {self._id_celda}, fecha_liberacion: {self._fecha_liberacion})"
