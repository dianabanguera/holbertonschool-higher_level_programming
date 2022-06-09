#!/usr/bin/python3
"""Read file method"""


def read_file(filename=""):
    """read a text in utf-8"""
    with open(filename, mode="r", encoding="UTF-8") as f:
        """prints the file"""
        print(f.read(), end="")
