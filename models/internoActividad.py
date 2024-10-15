from sqlalchemy import Column, Integer, String, Date, Text, ForeignKey, Time
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class InternoActividad(Base):
    __tablename__ = 'interno_actividad'
    
    ID_Interno = Column(Integer, ForeignKey('interno.ID_Interno'), primary_key=True)
    ID_Actividad = Column(Integer, ForeignKey('actividad.ID_Actividad'), primary_key=True)
    
    # Relaciones
    interno = relationship("Interno", back_populates="actividades")
    actividad = relationship("Actividad", back_populates="internos")