#!/usr/bin/python3
"""to_json_string"""
from json import dumps


def to_json_string(my_obj):
    """function that returns the JSON representation of an object"""
    return dumps(my_obj)
