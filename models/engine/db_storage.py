#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.ext.declarative import declarative_base
from models.base_model import BaseModel, Base
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class DBStorage:
    """This class manages storage of hbnb models in db storage format"""
    __engine = None
    __session = None

    def __init__(self):
        user = os.getenv('HBNB_MYSQL_USER')
        pswd = os.getenv('HBNB_MYSQL_PWD')
        host = os.getenv('HBNB_MYSQL_HOST')
        db = os.getenv('HBNB_MYSQL_DB')
        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}/{}".
                                      format(user, pswd, host, db),
                                      pool_pre_ping=True)
        if os.getenv('HBNB_ENV') == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        out_dict = {}
        list_of_classes = [cls] if cls else \
            ["State", "City", "Amenity", "Place", "User", "Review"]
        for class_name in list_of_classes:
            class_instances = self.__session.query(class_name)
            for ins in class_instances:
                out_dict["{}.{}".format(type(ins).__name__, ins.id)] = ins
        return out_dict

    def new(self, obj):
        self.__session.add(obj)

    def save(self):
        self.__session.commit()

    def delete(self, obj=None):
        if obj:
            self.__session.delete(obj)

    def reload(self):
        Base.metadata.create_all(self.__engine)
        mainSession = sessionmaker(bind=self.__engine, expire_on_commit=False)
        session = scoped_session(mainSession)
        self.__session = session()
