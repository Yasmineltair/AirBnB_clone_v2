#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import String, Column


class User(BaseModel, Base):
    """This class defines a user by various attributes"""
    __tablename__ = 'users'
    reviews = relationship('Review', cascade='delete', backref='user')
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=False)
    last_name = Column(String(128), nullable=False)
