
class Transferencia:
    def __init__(self, id_transferencia=None, id_interno=None, fecha_transferencia=None, motivo=None, destino=None):
        self._id_transferencia = id_transferencia
        self._id_interno = id_interno
        self._fecha_transferencia = fecha_transferencia
        self._motivo = motivo
        self._destino = destino

    # Métodos Getters
    def get_id_transferencia(self):
        return self._id_transferencia

    def get_id_interno(self):
        return self._id_interno

    def get_fecha_transferencia(self):
        return self._fecha_transferencia

    def get_motivo(self):
        return self._motivo

    def get_destino(self):
        return self._destino

    # Métodos Setters
    def set_id_transferencia(self, id_transferencia):
        if isinstance(id_transferencia, int) and id_transferencia > 0:
            self._id_transferencia = id_transferencia
        else:
            raise ValueError("El ID de la transferencia debe ser un entero positivo.")

    def set_id_interno(self, id_interno):
        self._id_interno = id_interno

    def set_fecha_transferencia(self, fecha_transferencia):
        self._fecha_transferencia = fecha_transferencia

    def set_motivo(self, motivo):
        self._motivo = motivo

    def set_destino(self, destino):
        self._destino = destino

    # Método para representar el objeto
    def __str__(self):
        return f"Transferencia(id: {self._id_transferencia}, id_interno: {self._id_interno}, fecha_transferencia: {self._fecha_transferencia}, motivo: {self._motivo}, destino: {self._destino})"
