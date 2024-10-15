from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class Conexion:
    def __init__(self):
        self.engine = None
        self.Session = None
        self.session = None

    def conectar(self):
        try:
            # Define la cadena de conexión
            string_conexion = "mysql+mysqldb://user_carcel:carcel1234@localhost:3306/carcel"
            
            # Crear el motor de SQLAlchemy
            self.engine = create_engine(string_conexion, echo=True)
            
            # Crear una sesión
            self.Session = sessionmaker(bind=self.engine)
            self.session = self.Session()
            
            print("Conexión exitosa a la base de datos.")
        except Exception as e:
            print(f"Error al conectar a la base de datos: {e}")

    def cerrar(self):
        if self.session:
            self.session.close()
            print("Conexión cerrada.")