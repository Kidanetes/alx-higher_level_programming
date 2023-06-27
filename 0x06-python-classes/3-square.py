#!/usr/bin/python3
""" a module with an empty class """


class Square:
    """class with private field
    Args:
    size(int): size of the square
    """
    def __init__(self, size=0):
        if type(size) is int:
            if size >= 0:
                self.__size = size
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")

    def area(self):
        """calculate the area of a square
        Returns: area of the square
        """
        return self.__size ** 2
