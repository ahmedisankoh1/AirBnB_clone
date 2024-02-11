#!/usr/bin/python3
"""Defines the BaseModel class."""
import models
import uuid
from datetime import datetime


class BaseModel:
    """Represents the BaseModel of the HBnB project."""

    def __init__(self, *arg, **kwargs):
        """
        Initialises a new instance of the BaseModel.

        Args:
            *args: unused here.
            **kwargs: Dictionary representation of the instance
        If kwargs is not empty:
            Each key has an attribute name
            Each value is the value of the corresponding attr name
            Converts datetime to datetime objects
        Otherwise:
            Create id and created_at as done innitially
        """
        if kwargs:
            if '__class__' in kwargs:
                del kwargs['__class__']
            if 'created_at' in kwargs:
                kwargs['created_at'] = datetime.strptime(
                        kwargs['created_at'], '%Y-%m-%dT%H:%M:%S.%f')
            if 'updated_at' in kwargs:
                kwargs['updated_at'] = datetime.strptime(
                        kwargs['updated_at'], '%Y-%m-%dT%H:%M:%S.%f')
            for key, value in kwargs.items():
                setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.today()
            self.updated_at = datetime.today()

    def save(self):
        """Update updated_at with the current datetime."""
        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        """Return the dictionary of the BaseModel instance.

        Includes the key/value pair __class__ representing
        the class name of the object.
        """
        clsdict = self.__dict__.copy()
        clsdict["created_at"] = self.created_at.isoformat()
        clsdict["updated_at"] = self.updated_at.isoformat()
        clsdict["__class__"] = self.__class__.__name__
        return clsdict

    def __str__(self):
        """Return the print/str representation of the BaseModel instance."""
        clsname = self.__class__.__name__
        return "[{}] ({}) {}".format(clsname, self.id, self.__dict__)
