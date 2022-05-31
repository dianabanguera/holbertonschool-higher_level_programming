#!/usr/bin/python3
""" print_square prints a square depending on the "size" parameter
"""


def print_square(size):
    """ Prints a square with a size
    check that the "size" is an int
    check that the "size" is less than 0 and is a float
    check that the "size" is less than 0
    check that the "size" isn't equal to 0
    """
    if type(size) != int:
        raise TypeError("size must be an integer")
    if type(size) == float and size < 0:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if size == 0:
        return None

    for row in range(size):
        print('#' * size)
