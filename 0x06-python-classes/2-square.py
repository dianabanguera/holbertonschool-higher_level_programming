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
        if type(size) is not int:
            raise TypeError("size must be an integer")
        else:
            if size < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = size
