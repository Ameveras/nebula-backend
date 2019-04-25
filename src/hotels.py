
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Base, Hotel

engine = create_engine('sqlite:///nebula.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()


# Menu for UrbanBurger
newHotel = Hotel(idHotel = 1, hNombre = "NebulaBase", direccion = "Santo Domingo, Dominican Republic", pais = "Dominican Republic", telefono = "809-000-0001", email = "nebula@gmail.com")

session.add(newHotel)
session.commit()