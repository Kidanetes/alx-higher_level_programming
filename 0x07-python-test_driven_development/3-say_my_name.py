#!/usr/bin/python3
"""this module contains a function
which prints the arguments which are
passed when a function is called
"""


def say_my_name(first_name, last_name=""):
    """this function prints first name
    followed by an optional last name
    Args:
    first_name(str): first name
    last_name(str): last name
    """
    if type(first_name) is not str:
        raise TypeError('first_name must be a string')
    if type(last_name) is not str:
        raise TypeError('last_name must be a string')
    print('My name is {} {}'.format(first_name, last_name))
