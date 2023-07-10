#!/usr/bin/python3
"""this module contains a function called
is_kind_of_class
"""


def inherits_from(obj, a_class):
    """check whether an object is
    a subclass of a class
    Args:
    obj(object): any object
    a_class(class): class
    returns:
    True: if it is the a subclass of a parent class
    False: otherwise
    """
    if isinstance(obj, a_class) and type(obj) is not a_class:
        return True
    return False
