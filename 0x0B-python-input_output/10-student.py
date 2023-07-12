#!/usr/bin/python3
"""this module contains a student classs"""


class Student:
    """class student
    Attributes:
    first_name(str): first name
    last_name(str): last name
    age(int): age
    """

    def __init__(self, first_name, last_name, age):
        """ intialize the object
        Args:
        first_name(str): first name
        last_name(str): last name
        age(int): age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """dictionary representation of an object"""
        if type(attrs) is list:
            for i in attrs:
                if type(i) is not str:
                    break
            else:
                x = self.__dict__.copy()
                y = {}
                for i, j in  x.items():
                    for k in attrs:
                        if i == k:
                            y[i] = j
                return y
        return self.__dict__
