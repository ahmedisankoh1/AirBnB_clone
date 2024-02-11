#!/usr/bin/python3
"""Defines the BaseModel class."""
import models
import uuid
from datetime import datetime


class BaseModel:
    """Represents the BaseModel of the HBnB project."""

    id = str(uuid.uuid4())
    created_at = datetime.today()
    updated_at = datetime.today()

    def save(self):
        """Updates updated_at with the current datetime."""

        self.updated_at = datetime.today()

    def to_dict(self):
        """Returns the dictionary of the BaseModel instance.

        Includes the key-value pair __class__ representing
        the class name of the object.
        """
        clsdict = self.__dict__.copy()
        clsdict["created_at"] = self.created_at.isoformat()
        clsdict["updated_at"] = self.updated_at.isoformat()
        clsdict["__class__"] = self.__class__.__name__
        return clsdict

    def __str__(self):
        """Returns the printed representation of the BaseModel instance in a neat way."""

        clsname = self.__class__.__name__
        return "[{}] ({}) {}".format(clsname, self.id, self.__dict__)
