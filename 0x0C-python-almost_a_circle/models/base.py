#!/usr/bin/python3
"""a module which contains a
base class
"""


class Base:
    """Base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """intializer of a base class
        Attributes:
        id(int): id of the object
        Args:
        id(int): an id passed when an object is
        intialized
        """
        if id:
            self.id = id
        else:
            Base.__nb_objects = Base.__nb_objects + 1
            self.id = Base.__nb_objects
