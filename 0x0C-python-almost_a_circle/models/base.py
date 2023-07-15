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
if __name__ == "__main__":

    b1 = Base()
    print(b1.id)

    b2 = Base()
    print(b2.id)

    b3 = Base()
    print(b3.id)

    b4 = Base(12)
    print(b4.id)

    b5 = Base()
    print(b5.id)
