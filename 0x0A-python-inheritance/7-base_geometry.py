#!/usr/bin/python3
"""this module contains a class
BaseGeometry
"""


class BaseGeometry:
    """Base Geometry class"""
    def area(self):
        """method area"""
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """validates an integer
    Args:
    name(str): name of the variable
    value(int): value of the variable
    """
    if type(value) is not int:
        raise TypeError("{} must be an integer".format(name))
    if value <= 0:
        raise ValueError("{} must be greater than 0".format(name))
