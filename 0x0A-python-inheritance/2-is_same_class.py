#!/usr/bin/python3
"""this module contains a function called
is_same_class
"""


def is_same_class(obj, a_class):
    """check whether an object is
    instance of a class
    Args:
    obj(object): any object
    a_class(class): class
    returns:
    True: if it is the same class
    False: otherwise
    """
    if type(obj) is a_class:
        return True
    return False
