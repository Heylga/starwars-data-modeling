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
    id = Column(Integer, primary_key=True)
    username = Column(String(50), nullable=False)
    firstname = Column(String(50),nullable=False)
    lastname = Column(String(50),nullable=False)
    email = Column(String(50),nullable=False)
    password = Column(String(50), nullable=False)
    favorite = relationship('Favorites')


class Favorites(Base):
    __tablename__ = 'favorites'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship('User')
    character = relationship('Characters')
    planet = relationship('Planets')
    

class Characters(Base):
    __tablename__= 'characters'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    gender = Column(String(50))
    hair_color = Column(String(50))
    eye_color = Column(String(50))
    favorite_id = Column(Integer, ForeignKey('favorites.id'))


class Planets(Base):
    __tablename__= 'planets'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    population = Column(String(50))
    terrain = Column(String(50))
    favorite_id = Column(Integer, ForeignKey('favorites.id'))
    
    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram4.png')