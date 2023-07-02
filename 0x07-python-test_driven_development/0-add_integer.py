#!/usr/bin/python3
"""
This module contains a funtion
which adds two float or integers
"""


def add_integer(a, b=98):
    """ a function which adds two numbers
    Args:
    a(int or float): number
    b(int or float): number
    returns: sum of a and b
    """
    if not(type(a) is int or type(a) is float):
        raise TypeError('a must be an integer')
    if not(type(b) is int or type(b) is float):
        raise TypeError('b must be an integer')
    a = int(a)
    b = int(b)
    return a + b
