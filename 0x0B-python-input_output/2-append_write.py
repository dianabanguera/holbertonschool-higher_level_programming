#!/usr/bin/python3
"""append_write"""


def append_write(filename="", text=""):
    """function that appends a string at the end of a text file"""
    with open(filename, mode="a", encoding="utf-8") as f:
        """returns the number of characters added"""
        return f.write(text)
