import os
import sys
from sqlalchemy import  Table, Column, ForeignKey, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)

class User_Favorites(Base):
    __tablename__ = 'user_favorites'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    character = Column(Integer, ForeignKey('character.id'))
    planet = Column(Integer, ForeignKey('planet.id'))
    starship = Column(Integer, ForeignKey('starship.id'))


class Starship(Base):
    __tablename__ = 'starship'
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    model = Column(String(250))
    manufacturer = Column(String(250))
    cost_in_credits = Column(Integer)
    length = Column(Integer)
    max_atmosphering_speed = Column(Integer)
    cargo_capacity = Column(Integer)

    user_favorites_id = Column(Integer, ForeignKey('user_favorites.id'))
    user_favorites = relationship('user_favorites')

class Planet(Base):
    __tablename__ = 'planet'
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    rotation_period = Column(Integer)
    orbital_period = Column(Integer)
    diameter = Column(Integer)
    climate = Column(String(250))
    gravity = Column(Integer)
    terrain = Column(String(250))
    population = Column(Integer)

    user_favorites_id = Column(Integer, ForeignKey('user_favorites.id'))
    user_favorites = relationship('user_favorites')

class Character(Base):
    __tablename__ = 'character'
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    height = Column(String(20))
    mass = Column(Integer)
    hair_color = Column(String(250))
    skin_color = Column(String(250))
    eye_color = Column(String(250))
    birth_year = Column(Date)
    gender = Column(String(25))
    species = Column(String(250))
    
    user_favorites_id = Column(Integer, ForeignKey('user_favorites.id'))
    user_favorites = relationship('user_favorites')

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram2.png')