#!/usr/bin/python3
"""this module will create a locked class"""


class LockedClass:
    "this is alocked class"""
    __slots__ = ['first_name']

    def __init__(self, name=""):
        self.first_name = name
