import os
import sys
import datetime
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()


class Hotel(Base):
    __tablename__ = 'Hotel'
    idHotel = Column(Integer, primary_key=True)
    hNombre = Column(String(250), nullable=False)
    direccion = Column(String(250), nullable=False)
    pais = Column(String(250), nullable=True)
    telefono = Column(String(25), nullable=True)
    email = Column(String(250), nullable=True)


class Usuario(Base):
    __tablename__ = 'Usuario'
    IdCliente = Column(Integer, primary_key=True, nullable=True)
    TipoDoc = Column(String(100), Nulable=True)
    Documento = Column(String(100), nullable=True)
    CNombre = Column(String(100), nullable=True)
    CApellido = Column(String(100), nullable=True)
    Sexo = Column(String(10), nullable=True)
    Pais = Column(String(100), nullable=True)
    FechaNacimiento = Column(datetime.date, nullable=True)
    Telefono = Column(String(15), nullable=True)
    Email = Column(String(15), nullable=True)
    Contraseña = Column(String(15), nullable=True)
    Foto = Column(String(15), nullable=True)
    FechaRegistro = Column(datetime.date, nullable=True)


engine = create_engine('sqlite:///nebula.db')


Base.metadata.create_all(engine)
