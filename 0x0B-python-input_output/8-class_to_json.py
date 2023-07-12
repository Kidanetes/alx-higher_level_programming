#!/usr/bin/python3
"""this module s function which return the
a dictionary of attributes of an object
"""


def class_to_json(obj):
    """Return the dictionary represntation of an object.
    Args:
    obj(object):  any object
    returns: dictionay of attributes
    """
    return obj.__dict__
