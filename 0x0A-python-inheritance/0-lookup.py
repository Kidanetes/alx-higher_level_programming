#!/usr/bin/python3
"""this module contains a function which
is called lookup"""


def lookup(obj):
    """
    this functions returns list of attributes
    of an object
    Args:
    obj(object): any object
    returns: list of attributes
    """
    return dir(obj)
