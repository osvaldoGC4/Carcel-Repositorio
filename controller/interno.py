
from models.interno import Interno


class InternoController():

    # Crear un nuevo registro de Interno
    def crear_interno(conexion, nombre, fecha_ingreso, estado, id_celda, fecha_liberacion=None):
        nuevo_interno = Interno(
            Nombre=nombre,
            Fecha_Ingreso=fecha_ingreso,
            Estado=estado,
            ID_Celda=id_celda,
            Fecha_Liberacion=fecha_liberacion
        )
        conexion.session.add(nuevo_interno)
        conexion.session.commit()
        print(f"Interno {nombre} creado con éxito.")

    # Leer todos los registros de Interno
    def leer_internos(conexion):
        internos = conexion.session.query(Interno).all()
        for interno in internos:
            print(interno.Nombre, interno.Estado, interno.Fecha_Ingreso)

    # Actualizar un registro de Interno
    def actualizar_interno(conexion, id_interno, nuevo_estado):
        interno = conexion.session.query(Interno).filter_by(ID_Interno=id_interno).first()
        if interno:
            interno.Estado = nuevo_estado
            conexion.session.commit()
            print(f"Interno {interno.Nombre} actualizado a {nuevo_estado}.")
        else:
            print("Interno no encontrado.")

    # Eliminar un registro de Interno
    def eliminar_interno(conexion, id_interno):
        interno = conexion.session.query(Interno).filter_by(ID_Interno=id_interno).first()
        if interno:
            conexion.session.delete(interno)
            conexion.session.commit()
            print(f"Interno {interno.Nombre} eliminado con éxito.")
        else:
            print("Interno no encontrado.")