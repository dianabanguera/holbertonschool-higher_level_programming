#!/usr/bin/python3
"""My list class"""


class MyList(list):
    """subclass of list"""
    def print_sorted(self):
        """prints the sorted list"""
        print(sorted(self))
