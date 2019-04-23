import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()


class Hotel(Base):
    __tablename__ = 'restaurant'
    idHotel = Column(Integer, primary_key=True)
    hNombre = Column(String(250), nullable=False)
    direccion = Column(String(250), nullable=False)
    pais = Column(String(250), nullable=False)
    telefono = Column(String(25), nullable=False)
    email = Column(String(250), nullable=False)


engine = create_engine('sqlite:///nebula.db')


Base.metadata.create_all(engine)
