from sqlalchemy import Column, Integer, String, Date, Text, ForeignKey, Time
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Visitante(Base):
    __tablename__ = 'visitante'
    
    ID_Visitante = Column(Integer, primary_key=True)
    Nombre = Column(String)
    Relacion = Column(String)  # 'Familiar, Abogado'
    Documento = Column(String)
    
    # Relaciones
    visitas = relationship("Visita", back_populates="visitante")