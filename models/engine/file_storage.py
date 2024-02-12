#!/usr/bin/python3
"""Module for the storage of files"""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """ Responsible for Serializing objects to JSON
        Also Deserializing JSON to objects.
    """
    __file_path = "file.json"
    __object = {}

    def all(self):
        """REturns a dictionary of the objects"""
        return self.__object

    def new(self, obj):
        """Sets in the __objects the obj with key <classname>.id"""
        obj_name = obj.__class__.__name__
        obj_key = "{}.{}".format(obj.name, obj.id)
        self.__objcts[obj_key] = obj

    def save(self):
        """Serializes __object into JSON file"""
        obj_dict = {}
        for key, obj in self.all().items():
            obj_dict[key] = obj.to_dict()
        with open(self.__file_path, "w") as text_file:
            json.dump(obj_dict, text_file)

    def reload(self):
        """Deserializes a JSON file to an objects
           If file dosen't exist does nothing
        """
        class_map = {
            'BaseModel': BaseModel
        }
        try:
            with open(self.__file_path, "r") as text_file:
                obj_dict = json.load(text_file)
                for key, val in obj_dict.items():
                    class_name = val['__class__']
                    class_instance = class_map[class_name]
                    instance = class_instance(**val)
                    all_objects = self.all()
                    all_objects[key] = instance
        except FileNotFoundError:
            pass
