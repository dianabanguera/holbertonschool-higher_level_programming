#!/usr/bin/python3
class LockedClass:
    """A lockedclass that only
    lets the user create the
    attribute 'first_name'"""
    ___slots__ = ['first_name']
