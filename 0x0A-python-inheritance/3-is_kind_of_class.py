#!/usr/bin/python3
"""
is_kind_of_class
"""


def is_kind_of_class(obj, a_class):
    """True or false if obj is an instance or inherited from a_class"""
    return (isinstance(obj, a_class))
