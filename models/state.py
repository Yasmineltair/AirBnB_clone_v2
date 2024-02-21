#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models import storage


class State(BaseModel, Base):
    """
    State class -> table `states`
    cols;   name: string(128), not nullable

    cascade relation to citites.
    """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", cascade="all, delete, delete-orphan",
                           backref="state")

    @property
    def cities(self):
        all_cities = storage.all()
        out_list = []
        for inp in all_cities:
            if inp.split('.')[0] == "City":
                if all_cities[inp].state_id == self.id:
                    out_list.append(all_cities[inp])
        return out_list
