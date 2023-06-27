#!/usr/bin/python3
""" a module with an empty class """


class Square:
    """class with private field
    Args:
    size(int): size of the square
    """
    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        """size should be integer and positive or zero
        if it is not integer, it will raise TypeError
        if it is not zero or positive, it will raise ValueError
        """
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is int:
            if value >= 0:
                self.__size = value
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")

    def area(self):
        """calculate the area of a square
        Returns: area of the square
        """
        return self.__size ** 2
