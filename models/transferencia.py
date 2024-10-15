from sqlalchemy import Column, Integer, String, Date, Text, ForeignKey, Time
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Transferencia(Base):
    __tablename__ = 'transferencia'
    
    ID_Transferencia = Column(Integer, primary_key=True)
    ID_Interno = Column(Integer, ForeignKey('interno.ID_Interno'))
    ID_Celda_Origen = Column(Integer, ForeignKey('celda.ID_Celda'))
    ID_Celda_Destino = Column(Integer, ForeignKey('celda.ID_Celda'))
    Fecha = Column(Date)
    Motivo = Column(Text)
    
    # Relaciones
    interno = relationship("Interno", back_populates="transferencias")
    celda_origen = relationship("Celda", foreign_keys=[ID_Celda_Origen])
    celda_destino = relationship("Celda", foreign_keys=[ID_Celda_Destino])