#!/usr/bin/python3
"""Define a square class"""


class Square:
    """Represents the atributtes
    of the square
    __size (int): size
    """
    def __init__(self, size=0):
        """Initialize the square

        Args:
            size (int): size of the square
        """
        self.__size = size

    @property
    def size(self):
        """int: Return the size of the square"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """Sets the attribute size"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        else:
            if value < 0:
                raise ValueError("value must be >= 0")
            else:
                self.__size = value

    def area(self):
        """int: Return the area of the square"""
        return (self.__size ** 2)
