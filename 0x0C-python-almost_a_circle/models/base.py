#!/usr/bin/python3
"""Base class"""
from fileinput import filename
import json
from multiprocessing import dummy

from pyrsistent import l


class Base:
    """Base"""
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of list_dictionaries"""
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file"""
        if list_objs is None or list_objs == []:
            json_s = "[]"
        else:
            json_s = cls.to_json_string([element.to_dictionary() for element in list_objs])
        filename = f"{cls.__name__}.json"
        with open(filename, "w") as file:
            file.write(json_s)

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the JSON string representation json_string"""
        if json_string is None or json_string == []:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set"""
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        """update dummy with obj func update()"""
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""
        filename = f"{cls.__name__}.json"
        list = []
        try:
            with open(filename, "r") as file:
                list = cls.from_json_string(file.read())
            for i, element in enumerate(list):
                list[i] = cls.create(**list[i])
        except:
            pass
        return list
