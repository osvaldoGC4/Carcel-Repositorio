from sqlalchemy import Column, Integer, String, Date, Text, ForeignKey, Time
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Condena(Base):
    __tablename__ = 'condena'
    
    ID_Condena = Column(Integer, primary_key=True)
    ID_Interno = Column(Integer, ForeignKey('interno.ID_Interno'))
    ID_Delito = Column(Integer, ForeignKey('delito.ID_Delito'))
    Fecha_Inicio = Column(Date)
    Duracion = Column(Integer)  # 'En meses'
    Tipo = Column(String)  # 'Permanente, Temporal'
    ID_Personal = Column(Integer, ForeignKey('personal.ID_Personal'))
    
    # Relaciones
    interno = relationship("Interno", back_populates="condenas")
    delito = relationship("Delito")
    personal = relationship("Personal")