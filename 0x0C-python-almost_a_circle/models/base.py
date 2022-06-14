#!/usr/bin/python3
"""
Base .__nb_objects
"""
from fileinput import filename
import json
import os


class Base:
    """
    Class base
    """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Return a json
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        writes the JSON string representation of list_objs to a file
        """
        if list_objs is None or len(list_objs) == 0:
            json_s = "[]"
        else:
            json_s = cls.to_json_string(
                [element.to_dictionary() for element in list_objs])
        filename = f"{cls.__name__}.json"
        with open(filename, "w") as file:
            file.write(json_s)

    @staticmethod
    def from_json_string(json_string):
        """
        Return json string
        """
        if type(json_string) is not str or len(json_string) == 0:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set"""
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """
        Return a list
        """
        filename = cls.__name__ + ".json"
        l1 = []
        try:
            with open(filename, 'r') as f:
                l1 = cls.from_json_string(f.read())
            for i, e in enumerate(l1):
                l1[i] = cls.create(**l1[i])
        except Exception:
            pass
        return l1
