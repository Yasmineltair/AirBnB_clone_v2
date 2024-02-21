#!/usr/bin/python3
"""User Class Definition"""
from models.base_model import BaseModel


class User(BaseModel):
    """ User class based on BaseModel """
    first_name = ""
    last_name = ""
    password = ""
    email = ""
