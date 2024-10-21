class Transferencia:
    def __init__(self, ID_Transferencia=None, ID_Interno=None, ID_Celda_Origen=None, ID_Celda_Destino=None, Fecha=None, Motivo=None):
        self._ID_Transferencia = ID_Transferencia
        self._ID_Interno = ID_Interno
        self._ID_Celda_Origen = ID_Celda_Origen
        self._ID_Celda_Destino = ID_Celda_Destino
        self._Fecha = Fecha
        self._Motivo = Motivo

    # Getters
    def get_ID_Transferencia(self):
        return self._ID_Transferencia

    def get_ID_Interno(self):
        return self._ID_Interno

    def get_ID_Celda_Origen(self):
        return self._ID_Celda_Origen

    def get_ID_Celda_Destino(self):
        return self._ID_Celda_Destino

    def get_Fecha(self):
        return self._Fecha

    def get_Motivo(self):
        return self._Motivo

    # Setters con validación
    def set_ID_Transferencia(self, ID_Transferencia):
        self._ID_Transferencia = ID_Transferencia

    def set_ID_Interno(self, ID_Interno):
        self._ID_Interno = ID_Interno

    def set_ID_Celda_Origen(self, ID_Celda_Origen):
        self._ID_Celda_Origen = ID_Celda_Origen

    def set_ID_Celda_Destino(self, ID_Celda_Destino):
        self._ID_Celda_Destino = ID_Celda_Destino

    def set_Fecha(self, Fecha):
        self._Fecha = Fecha

    def set_Motivo(self, Motivo):
        self._Motivo = Motivo

    # Método para convertir a diccionario
    def to_dict(self):
        return {
            'ID_Transferencia': self._ID_Transferencia,
            'ID_Interno': self._ID_Interno,
            'ID_Celda_Origen': self._ID_Celda_Origen,
            'ID_Celda_Destino': self._ID_Celda_Destino,
            'Fecha': self._Fecha,
            'Motivo': self._Motivo
        }
