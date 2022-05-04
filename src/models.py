import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(200), nullable=False)

class LogIn(Base):
    __tablename__ = 'Login'

    email = Column(String, ForeignKey('user.email'), primary_key=True)
    password = Column(String(250))
    LogIn = relationship(User)


class Favorites(Base):
    __tablename__ = 'favorites'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    characters_id = Column(Integer, ForeignKey('characters.id'))
    planets_id = Column(Integer, ForeignKey('planets.id'))
    starships = Column(Integer, ForeignKey('starships.id'))
    favorites = relationship(User)
    

class Characters(Base):
    __tablename__= 'characters'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    gender = Column(String(50))
    hair_color = Column(String(50))
    eye_color = Column(String(50))
    characters = relationship(Favorites)

class Planets(Base):
    __tablename__= 'planets'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    population = Column(String(50))
    terrain = Column(String(50))
    planets = relationship(Favorites)

class Starships(Base):
    __tablename__= 'starships'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    model = Column(String(50))
    manufacturer = Column(String(50))
    starships = relationship(Favorites)


    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')