#!/usr/bin/python3
"""
class BaseGeometry and subclass Rectangle
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """A rectangle representation"""
    def __init__(self, width, height):
        """initialize rectangle"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
