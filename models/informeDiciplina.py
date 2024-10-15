from sqlalchemy import Column, Integer, String, Date, Text, ForeignKey, Time
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class InformeDisciplina(Base):
    __tablename__ = 'informe_disciplina'
    
    ID_Informe = Column(Integer, primary_key=True)
    ID_Interno = Column(Integer, ForeignKey('interno.ID_Interno'))
    Fecha = Column(Date)
    Descripcion = Column(Text)
    Sancion = Column(String)
    
    # Relaciones
    interno = relationship("Interno", back_populates="informes")