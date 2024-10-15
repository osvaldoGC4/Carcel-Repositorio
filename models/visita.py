from sqlalchemy import Column, Integer, String, Date, Text, ForeignKey, Time
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Visita(Base):
    __tablename__ = 'visita'
    
    ID_Visita = Column(Integer, primary_key=True)
    ID_Interno = Column(Integer, ForeignKey('interno.ID_Interno'))
    ID_Visitante = Column(Integer, ForeignKey('visitante.ID_Visitante'))
    Fecha = Column(Date)
    Hora_Inicio = Column(Time)
    Duracion = Column(Integer)  # 'En minutos'
    
    # Relaciones
    interno = relationship("Interno", back_populates="visitas")
    visitante = relationship("Visitante")