from sqlalchemy import Column, Integer, String, Date, Text, ForeignKey, Time
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class VisitaMultiple(Base):
    __tablename__ = 'visita_multiple'
    
    ID_Visita = Column(Integer, ForeignKey('visita.ID_Visita'), primary_key=True)
    ID_Visitante = Column(Integer, ForeignKey('visitante.ID_Visitante'), primary_key=True)