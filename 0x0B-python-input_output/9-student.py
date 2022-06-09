#!/usr/bin/python3
"""Student class"""


class Student:
    """Representation of the student class"""
    def __init__(self, first_name, last_name, age):
        """Initialize the class"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """returns a dictionary"""
        return self.__dict__