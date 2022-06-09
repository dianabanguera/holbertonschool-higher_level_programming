#!/usr/bin/python3
"""Write file"""


def write_file(filename="", text=""):
    """function that writes a string to a text file"""
    with open(filename, mode="w", encoding="UTF-8") as f:
        """returns the number of characters written"""
        return f.write(text)
