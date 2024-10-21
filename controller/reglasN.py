import json
import pyodbc
from common.conexion import Conexion
from common.utiles import Utiles


class ReglasNController:

    def __init__(self) -> None:
        self.conexion = Conexion()
        self.show = Utiles()
        
    
    def contar_reclusos_por_celda(self) -> None:
       
        try:
            # Crear una instancia de la clase Conexion
            self.conexion.conectar()  # Establecer la conexión

            print("Ejecutando el procedimiento almacenado para contar reclusos por celda...")
            respuesta = self.conexion.execSPResult('ContarReclusosPorCelda', [])
            self.show.mostrar_resultados_dinamico(respuesta)

        except pyodbc.Error as e:
            print(f"Error en la ejecución del SP: {e}")
            
        finally:
            self.conexion.cerrar()  # Asegurarse de cerrar la conexión


    def obtener_condena_por_interno_y_delito(self, id_interno, id_delito):
      
        try:
            # Crear una instancia de la clase Conexion
            self.conexion.conectar()  # Establecer la conexión

            params = (id_interno, id_delito)
            respuesta = self.conexion.execSPResult('ObtenerCondenaPorInternoYDelito', params)
    
            self.show.mostrar_resultados_dinamico(respuesta)
        except pyodbc.Error as e:
            print(f"Error en la ejecución del SP: {e}")
        finally:
            self.conexion.cerrar()



