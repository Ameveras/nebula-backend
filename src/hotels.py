
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Base, Hotel

engine = create_engine('sqlite:///nebula.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


# Menu for UrbanBurger
newHotel = Hotel(idHotel=1, hNombre="NebulaBase", direccion="Santo Domingo, Dominican Republic",
                 pais="Dominican Republic", telefono="809-000-0001", email="nebula@gmail.com")

session.add(newHotel)
session.commit()
