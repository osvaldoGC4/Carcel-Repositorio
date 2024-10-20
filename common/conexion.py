from sqlite3 import Row
import pyodbc

class Conexion:
    string_conexion: str = """
        Driver={MySQL ODBC 9.0 Unicode Driver};
        Server=localhost;
        Database=carcel;
        PORT=3306;
        user=user_carcel;
        password=carcel1234""";
    
    parametros_salidas: str = ''
    
    def __init__(self):
        self.conexion = None
        self.cursor = None

    def conectar(self):
        try:
            self.conexion = pyodbc.connect(self.string_conexion)
            self.cursor = self.conexion.cursor()
            print("Conexión exitosa a la base de datos.")
        except pyodbc.Error as e:
            print(f"Error al conectar a la base de datos: {e}")

    def cerrar(self):
        if self.cursor:
            self.cursor.close()
        if self.conexion:
            self.conexion.close()
            print("Conexión cerrada.")

    def execSP(self, spName, params):
        try:
            # Convertir cada parámetro en string y rodear los strings con comillas simples
            params_str = ', '.join([f"'{param}'" if isinstance(param, str) else str(param) for param in params])

            # Ejecutar la llamada al procedimiento almacenado con los parámetros formateados
            query = f"CALL {spName} ({params_str})"
            print("####################################################")
            print(query)
            self.cursor.execute(query)
            self.conexion.commit()
            return True
        except pyodbc.Error as e:
            print(f"Error al ejecutar el SP: {e}")
            return False
        
    def execSPResult(self, spName, params):
        try:
            # Convertir cada parámetro en string y rodear los strings con comillas simples
            params_str = ', '.join([f"'{param}'" if isinstance(param, str) else str(param) for param in params])

            # Ejecutar la llamada al procedimiento almacenado con los parámetros formateados
            query = f"CALL {spName} ({params_str})"
            print("####################################################")
            print(query)
            self.cursor.execute(query)
            # Obtener los nombres de las columnas
            columns = [column[0] for column in self.cursor.description]  # Obtener los nombres de las columnas
        
            resultado = self.cursor.fetchall()
            return [dict(zip(columns, row)) for row in resultado]
        except pyodbc.Error as e:
            print(f"Error al ejecutar el SP: {e}")
            return []
