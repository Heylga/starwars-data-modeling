
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
    name = Column(String(50), nullable=False)
    email = Column(String(50), nullable=False)
    password = Column(String(50), nullable=False)

class User_Favorites(Base):
    __tablename__ = 'user_favorites'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    character = Column(Integer, ForeignKey('character.id'))
    planet = Column(Integer, ForeignKey('planet.id'))
    starship = Column(Integer, ForeignKey('starship.id'))
    vehicles = Column(Integer, ForeignKey('vehicles.id'))


class Starship(Base):
    __tablename__ = 'starship'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    model = Column(String(50))
    manufacturer = Column(String(50))
    cost_in_credits = Column(Integer)
    length = Column(Integer)
    max_atmosphering_speed = Column(Integer)
    cargo_capacity = Column(Integer)

    user_favorites = relationship('user_favorites')

class Planet(Base):
    __tablename__ = 'planet'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    rotation_period = Column(Integer)
    orbital_period = Column(Integer)
    diameter = Column(Integer)
    climate = Column(String(50))
    gravity = Column(Integer)
    terrain = Column(String(50))
    population = Column(Integer)

    user_favorites = relationship('user_favorites')

class Character(Base):
    __tablename__ = 'character'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    height = Column(String(20))
    mass = Column(Integer)
    hair_color = Column(String(50))
    skin_color = Column(String(50))
    eye_color = Column(String(50))
    birth_year = Column(Date)
    gender = Column(String(25))
    species = Column(String(50), ForeignKey('species.name'))
    
    user_favorites = relationship('user_favorites')

class Vehicles(Base):
    __tablename__ = 'vehicles'
    id = Column(Integer, primary_key=True)
    name = Column(String(120), nullable=False)
    model = Column(String(120))
    cost_in_credits = Column(Integer)
    vehicle_class = Column(String(20))

    user_favorites = relationship('user_favorites')

class Species(Base):
    __tablename__ = 'species'
    id = Column(Integer, primary_key=True)
    name = Column(String(120), nullable=False)
    designation = Column(String(20))
    classification = Column(String(20))
    average_height = Column(Integer)
    average_lifespan = Column(Integer)
    homeworld = Column(String(20, ForeignKey('planet.name')))

    user_favorites = relationship('user_favorites')

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram3.png')