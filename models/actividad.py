from sqlalchemy import Column, Integer, String, Date, Text, ForeignKey, Time
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Actividad(Base):
    __tablename__ = 'actividad'
    
    ID_Actividad = Column(Integer, primary_key=True)
    Nombre = Column(String)
    Tipo = Column(String)  # 'Educativa, Recreativa, Laboral'
    Horario = Column(String)
    
    # Relaciones
    internos = relationship("InternoActividad", back_populates="actividad")

 