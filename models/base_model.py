#!/usr/bin/python3
"""Defination of the BaseModel class for the project."""
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """Represents the BaseModel of the AirBnB clone project."""
    id = str(uuid.uuid4())
    created_at = datetime.now()
    updated_at = datetime.now()

    def __str__(self):
        """Returns the printed representation of the BaseModel instance."""
        clsname = self.__class__.__name__
        return "[{}] ({}) {}".format(clsname, self.id, self.__dict__)

    def save(self):
        """Updates updated_at with the current datetime."""
        self.updated_at = datetime.today()

    def to_dict(self):
        """Returns the dictionary of the BaseModel instance in a neat way.

        Includes the key-value pair __class__ representing
        the class name of the object.
        """
        clsdict = self.__dict__.copy()
        clsdict["created_at"] = self.created_at.isoformat()
        clsdict["updated_at"] = self.updated_at.isoformat()
        clsdict["__class__"] = self.__class__.__name__
        return (clsdict)
