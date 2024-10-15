from sqlalchemy import Column, Integer, String, Date, Text, ForeignKey, Time
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from models.interno import Interno  # Asegúrate de importar Interno aquí

Base = declarative_base()

# models/celda.py

class Celda(Base):
    __tablename__ = 'celda'
    
    ID_Celda = Column(Integer, primary_key=True)
    Ubicacion = Column(String)
    Capacidad = Column(Integer)
    Estado = Column(String)  # 'Ocupada, Disponible'
    
   # Relaciones
    internos = relationship("Interno", back_populates="celda")  # Relación con la clase Interno



