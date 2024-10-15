from sqlalchemy import Column, Integer, String, Date, Text, ForeignKey, Time
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from models.celda import Celda  # Asegúrate de importar Celda aquí

Base = declarative_base()

# models/interno.py

class Interno(Base):
    __tablename__ = 'interno'
    
    ID_Interno = Column(Integer, primary_key=True)
    Nombre = Column(String)
    Fecha_Ingreso = Column(Date)
    Estado = Column(String)  # 'Activo, Liberado, Transferido'
    ID_Celda = Column(Integer, ForeignKey('celda.ID_Celda'))
    Fecha_Liberacion = Column(Date)
    
    # Relaciones
    celda = relationship("Celda", back_populates="internos")  # Añadir back_populates aquí
    condenas = relationship("Condena", back_populates="interno")
    visitas = relationship("Visita", back_populates="interno")
    actividades = relationship("InternoActividad", back_populates="interno")
    transferencias = relationship("Transferencia", back_populates="interno")
    informes = relationship("InformeDisciplina", back_populates="interno")
