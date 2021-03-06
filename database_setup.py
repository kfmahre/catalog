import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'

    name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    picture = Column(String(250))
    id = Column(Integer, primary_key=True)

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
        'name': self.name,
        'email': self.email,
        'id': self.id,
        }

class Location(Base):
    __tablename__ = 'location'

    id = Column(Integer, primary_key=True)
    name = Column(String(80), nullable=False)
    user_id = Column(Integer,ForeignKey('user.id'))
    user = relationship(User)

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
        'name': self.name,
        'id': self.id,
        }

class MenuItem(Base):
    __tablename__ = 'menu_item'

    name =Column(String(80), nullable = False)
    id = Column(Integer, primary_key = True)
    description = Column(String(250))
    price = Column(String(8))
    shoe_class = Column(String(250))
    location_id = Column(Integer,ForeignKey('location.id'))
    location = relationship(Location)
    user_id = Column(Integer,ForeignKey('user.id'))
    user = relationship(User)

    @property
    def serialize(self):
        return {
        'name': self.name,
        'description' : self.description,
        'id' : self.id,
        'price' : self.price,
        'class' : self.shoe_class,
        }


engine = create_engine('sqlite:///runningstoreapp.db')
Base.metadata.create_all(engine)