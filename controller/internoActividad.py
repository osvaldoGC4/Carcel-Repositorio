
class InternoActividad:
    def __init__(self, id_interno_actividad=None, id_interno=None, id_actividad=None, fecha_participacion=None):
        self._id_interno_actividad = id_interno_actividad
        self._id_interno = id_interno
        self._id_actividad = id_actividad
        self._fecha_participacion = fecha_participacion

    # Métodos Getters
    def get_id_interno_actividad(self):
        return self._id_interno_actividad

    def get_id_interno(self):
        return self._id_interno

    def get_id_actividad(self):
        return self._id_actividad

    def get_fecha_participacion(self):
        return self._fecha_participacion

    # Métodos Setters
    def set_id_interno_actividad(self, id_interno_actividad):
        if isinstance(id_interno_actividad, int) and id_interno_actividad > 0:
            self._id_interno_actividad = id_interno_actividad
        else:
            raise ValueError("El ID de la actividad del interno debe ser un entero positivo.")

    def set_id_interno(self, id_interno):
        self._id_interno = id_interno

    def set_id_actividad(self, id_actividad):
        self._id_actividad = id_actividad

    def set_fecha_participacion(self, fecha_participacion):
        self._fecha_participacion = fecha_participacion

    # Método para representar el objeto
    def __str__(self):
        return f"InternoActividad(id: {self._id_interno_actividad}, id_interno: {self._id_interno}, id_actividad: {self._id_actividad}, fecha_participacion: {self._fecha_participacion})"
