#!/usr/bin/python3
"""
add_integer: it checks if the parameters
are integer an return the sum of both"""


def add_integer(a, b=98):
    if type(a) == float or type(b) == float:
            a = int(a)
            b = int(b)
    if type(a) != int:
        raise TypeError("a must be an integer")
    elif type(b) != int:
        raise TypeError("b must be an integer")
    else:
       return a + b
