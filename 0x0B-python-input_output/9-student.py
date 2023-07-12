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

    def to_json(self):
        """dictionary representation of an object"""
        return self.__dict__
