#!/usr/bin/python3
"""this module contains a function called
is_kind_of_class
"""


def is_kind_of_class(obj, a_class):
    """check whether an object is
    instance of a class
    Args:
    obj(object): any object
    a_class(class): class
    returns:
    True: if it is the an instance of class or parent class
    False: otherwise
    """
    if isinstance(obj, a_class):
        return True
    return False
