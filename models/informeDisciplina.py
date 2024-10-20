
class InformeDisciplina:
    def __init__(self, id_informe=None, id_interno=None, fecha_informe=None, descripcion=None, accion=None):
        self._id_informe = id_informe
        self._id_interno = id_interno
        self._fecha_informe = fecha_informe
        self._descripcion = descripcion
        self._accion = accion

    # Métodos Getters
    def get_id_informe(self):
        return self._id_informe

    def get_id_interno(self):
        return self._id_interno

    def get_fecha_informe(self):
        return self._fecha_informe

    def get_descripcion(self):
        return self._descripcion

    def get_accion(self):
        return self._accion

    # Métodos Setters
    def set_id_informe(self, id_informe):
        if isinstance(id_informe, int) and id_informe > 0:
            self._id_informe = id_informe
        else:
            raise ValueError("El ID del informe debe ser un entero positivo.")

    def set_id_interno(self, id_interno):
        self._id_interno = id_interno

    def set_fecha_informe(self, fecha_informe):
        self._fecha_informe = fecha_informe

    def set_descripcion(self, descripcion):
        self._descripcion = descripcion

    def set_accion(self, accion):
        self._accion = accion

    # Método para representar el objeto
    def __str__(self):
        return f"InformeDisciplina(id: {self._id_informe}, id_interno: {self._id_interno}, fecha_informe: {self._fecha_informe}, descripcion: {self._descripcion}, accion: {self._accion})"
