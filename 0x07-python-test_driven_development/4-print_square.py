#!/usr/bin/python3
"""this module contains a function
which print a square when the function called
with a size"""


def print_square(size):
    """this function accepts an argument
    size, and print a square
    Args:
    size(int): size of the sqaure
    """
    if type(size) is not int:
        raise TypeError('size must be an integer')
    if size < 0:
        raise ValueError('size must be >= 0')
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()
