import json
import pyodbc
from common.conexion import Conexion
from models.reglasN import ReglasN


class ReglasNController:

    def __init__(self) -> None:
        self.conexion = Conexion()
        
    
    def contar_reclusos_por_celda(self) -> None:
        # Crear una instancia de la clase Conexion
        self.conexion.conectar()  # Establecer la conexión
        
        try:
            print("Ejecutando el procedimiento almacenado para contar reclusos por celda...")
            respuesta = self.conexion.execSPResult('ContarReclusosPorCelda', [])
            self.mostrar_resultadosDinamico(respuesta)

        except pyodbc.Error as e:
            print(f"Error en la ejecución del SP: {e}")
            
        finally:
            self.conexion.cerrar()  # Asegurarse de cerrar la conexión


    def obtener_condena_por_interno_y_delito(self, id_interno, id_delito):
        try:
            
            params = (2, 2)
            resultado = self.conexion.execSPResult('ObtenerCondenaPorInternoYDelito', params)
            columnas = ['ID_Condena', 'Nombre_Interno', 'Tipo_Delito', 'Fecha_Inicio', 'Duracion', 'Tipo']  # Asegúrate de definir las columnas
            self.mostrar_resultadosDinamico(resultado, columnas)
        except pyodbc.Error as e:
            print(f"Error en la ejecución del SP: {e}")
        finally:
            self.conexion.cerrar()


    def mostrar_resultadosDinamico(self, respuesta, columnas):
        # Mostrar encabezados dinámicos
        print(" | ".join(columnas))
        print("-" * (len(columnas) * 10))  # Línea separadora

        # Procesar los resultados
        if respuesta:  # Verificar si 'respuesta' tiene datos
            for row in respuesta:
                # Crear una lista con los valores correspondientes a las columnas
                valores = [str(row[col]) for col in columnas]  # Convertir a string
                print(" | ".join(valores))
        else:
            print("No se encontraron resultados.")


