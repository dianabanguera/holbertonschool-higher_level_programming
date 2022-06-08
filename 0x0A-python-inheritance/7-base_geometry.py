#!/usr/bin/python3
"""BaseGeometry class"""


class BaseGeometry:
    """The area method"""
    def area(self):
        """raises a exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates that the value to
        evaluate is an integer and
        greater than 0"""
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
