#!/usr/bin/python3
"""add atttribute to an object"""


def add_attribute(obj, name, val):
    """add new attribute to an object
    Args:
    obj(any): the object to be added
    name(str): the name of the attribute
    value(any): value to be added
    """
    if hasattr(obj, "__dict__") is False:
        raise TypeError("can't add new attribute")
    setattr(obj, name, val)
