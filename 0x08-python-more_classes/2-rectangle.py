#!/usr/bin/python3
"""this module contains
the defintion of Rectangle Class
"""


class Rectangle:
    """class rectangle
    Args:
    width(int): Rectangl's width
    height(int): Rectangl's height
    """

    def __init__(self, width=0, height=0):
        self.height = height
        self.width = width

    @property
    def width(self):
        """to retrive width
        setter method if value passed when the object is created
        is not int it raises TypeError or it is less than
        zero it it raises valu error
        """
        return self.__width

    @width.setter
    def width(self, x):
        if type(x) is not int:
            raise TypeError('width must be an integer')
        if x < 0:
            raise ValueError('width must be >= 0')
        self.__width = x

    @property
    def height(self):
        """to retrive height
        setter method if value passed when the object is created
        is not int it raises TypeError or it is less than
        zero it it raises valu error
        """
        return self.__height

    @height.setter
    def height(self, y):
        if type(y) is not int:
            raise TypeError('height must be an integer')
        if y < 0:
            raise ValueError('height must be >= 0')
        self.__height = y

    def area(self):
        """calculates area of the rectangle object
        Returns: area of the rectangle
        """
        return self.__width * self.__height

    def perimeter(self):
        """calculates the perimeter of the rectangle object
        Returns: perimeter of the rectangle
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)
