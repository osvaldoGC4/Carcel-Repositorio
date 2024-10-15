from models.celda import Celda

# controller/celda.py

class CeldaController():
    def __init__(self):
        print("Controlador celda")

    # Crear un nuevo registro de Celda
    def crear_celda(self, conexion, ubicacion, capacidad, estado):
        nueva_celda = Celda(
            Ubicacion=ubicacion,
            Capacidad=capacidad,
            Estado=estado
        )
        conexion.session.add(nueva_celda)
        conexion.session.commit()
        print(f"Celda {ubicacion} creada con éxito.")  # Cambiar "Interno" por "Celda"
