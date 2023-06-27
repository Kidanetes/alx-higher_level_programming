#!/usr/bin/python3
""" a module with an empty class """


class Square:
    """class with private field
    Args:
    size(int): size of the square
    """
    def __init__(self, size=0):
        if (size is not int):
            if size >= 0:
                self.__size = int(size)
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")
