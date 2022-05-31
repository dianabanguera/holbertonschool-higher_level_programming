#!/usr/bin/python3
""" matrix_divided:
divides two matrix using "div",
and returns the result of the division
"""


def matrix_divided(matrix, div):
    """ Divides all elements of a matrix
    checks the list and verify if is int
    checks the size
    verify is an int/float or is 0 in de div position
    """
    mx1 = "matrix must be a matrix (list of lists) of integers/floats"
    mx2 = "Each row of the matrix must have the same size"
    matrix3 = []

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    for lists in matrix:
        if len(lists) != len(matrix[0]):
            raise TypeError(mx1)
        inner_list = []
        for items in lists:
            if not isinstance(items, (int, float)):
                raise TypeError(mx2)
            else:
                inner_list.append(round(items / div, 2))
        matrix3.append(inner_list)

    return matrix3