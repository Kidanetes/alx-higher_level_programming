#!/usr/bin/python3
"""square class inherited from Rectangle"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """square class inherited from Rectangle"""

    def __init__(self, size):
        """intialize a square object
        Args:
        size(int): size of a square
        """
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """return area of Square"""
        return self.__size * self.__size

    def __str__(self):
        """represent square object"""
        return "[Square] {}/{}".format(self.__size, self.__size)
