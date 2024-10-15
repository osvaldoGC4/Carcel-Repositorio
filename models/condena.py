
class Condena:
    def __init__(self, id_condena=None, id_interno=None, id_delito=None, fecha_inicio=None, duracion=None, tipo=None, id_personal=None):
        self._id_condena = id_condena
        self._id_interno = id_interno
        self._id_delito = id_delito
        self._fecha_inicio = fecha_inicio
        self._duracion = duracion
        self._tipo = tipo
        self._id_personal = id_personal

    # Métodos Getters
    def get_id_condena(self):
        return self._id_condena

    def get_id_interno(self):
        return self._id_interno

    def get_id_delito(self):
        return self._id_delito

    def get_fecha_inicio(self):
        return self._fecha_inicio

    def get_duracion(self):
        return self._duracion

    def get_tipo(self):
        return self._tipo

    def get_id_personal(self):
        return self._id_personal

    # Métodos Setters con validación
    def set_id_condena(self, id_condena):
        if isinstance(id_condena, int) and id_condena > 0:
            self._id_condena = id_condena
        else:
            raise ValueError("El ID de la condena debe ser un entero positivo.")

    def set_id_interno(self, id_interno):
        self._id_interno = id_interno

    def set_id_delito(self, id_delito):
        self._id_delito = id_delito

    def set_fecha_inicio(self, fecha_inicio):
        self._fecha_inicio = fecha_inicio

    def set_duracion(self, duracion):
        if isinstance(duracion, int) and duracion > 0:
            self._duracion = duracion
        else:
            raise ValueError("La duración debe ser un entero positivo.")

    def set_tipo(self, tipo):
        self._tipo = tipo

    def set_id_personal(self, id_personal):
        self._id_personal = id_personal

    # Método para representar el objeto
    def __str__(self):
        return f"Condena(id: {self._id_condena}, id_interno: {self._id_interno}, id_delito: {self._id_delito}, fecha_inicio: {self._fecha_inicio}, duracion: {self._duracion}, tipo: {self._tipo}, id_personal: {self._id_personal})"
