from sqlalchemy import Column, Integer, String, Date, Text, ForeignKey, Time
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Delito(Base):
    __tablename__ = 'delito'
    
    ID_Delito = Column(Integer, primary_key=True)
    Tipo = Column(String)
    Descripcion = Column(Text)