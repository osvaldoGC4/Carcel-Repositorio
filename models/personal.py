
class Personal:
    def __init__(self, id_personal=None, nombre=None, rol=None, horario=None, estado=None):
        self._id_personal = id_personal
        self._nombre = nombre
        self._rol = rol
        self._horario = horario
        self._estado = estado

    # Métodos Getters
    def get_id_personal(self):
        return self._id_personal

    def get_nombre(self):
        return self._nombre

    def get_rol(self):
        return self._rol

    def get_horario(self):
        return self._horario

    def get_estado(self):
        return self._estado

    # Métodos Setters con validación
    def set_id_personal(self, id_personal):
        if isinstance(id_personal, int) and id_personal > 0:
            self._id_personal = id_personal
        else:
            raise ValueError("El ID del personal debe ser un entero positivo.")

    def set_nombre(self, nombre):
        self._nombre = nombre

    def set_rol(self, rol):
        self._rol = rol

    def set_horario(self, horario):
        self._horario = horario

    def set_estado(self, estado):
        if estado in ['Activo', 'Inactivo']:
            self._estado = estado
        else:
            raise ValueError("Estado inválido. Debe ser 'Activo' o 'Inactivo'.")

    # Método para representar el objeto
    def __str__(self):
        return f"Personal(id: {self._id_personal}, nombre: {self._nombre}, rol: {self._rol}, horario: {self._horario}, estado: {self._estado})"
