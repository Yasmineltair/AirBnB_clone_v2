#!/usr/bin/python3
"""This module defines a class User"""
<<<<<<< HEAD
from models.base_model import BaseModel
from sqlalchemy import String, relationship


class User(BaseModel, Base):
    """This class defines a user by various attributes"""
    __tablename__ = 'users'
=======
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.place import Place

class User(BaseModel, Base):
    """
    User class -> table `users`
    cols;   email: string(128), not nullable
            password: string(128), not nullable
            first_name: string(128), not nullable
            last_name: string(128), not nullable
    """
    __tablename__ = "users"
>>>>>>> 54b12da (678)
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128))
    last_name = Column(String(128))
<<<<<<< HEAD
    places = relationsip("place", cascade="delete", backref="user")
=======
    places = relationship("Place", cascade="all", backref="user")
>>>>>>> 54b12da (678)
