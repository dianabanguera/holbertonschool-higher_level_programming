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

    def area(self):
        """returns the area of the rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """representation of the
        rectangle in string format"""
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)
