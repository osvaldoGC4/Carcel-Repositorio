from sqlalchemy import Column, Integer, String, Date, Text, ForeignKey, Time
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Personal(Base):
    __tablename__ = 'personal'
    
    ID_Personal = Column(Integer, primary_key=True)
    Nombre = Column(String)
    Rol = Column(String)  # 'Guardia, Administrador'
    Horario = Column(String)
    Estado = Column(String)  # 'Activo, Inactivo'