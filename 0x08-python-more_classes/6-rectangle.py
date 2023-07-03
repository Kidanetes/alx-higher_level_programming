#!/usr/bin/python3
"""this module contains
the defintion of Rectangle Class
"""


class Rectangle:
    """class rectangle
    Attributes:
    number_of_instances(int): number of
    Rectangle object

    Args:
    width(int): Rectangl's width
    height(int): Rectangl's height
    """

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

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

    def __str__(self):
        """the informal representation of an object"""
        str1 = ""
        for i in range(self.__height):
            for j in range(self.__width):
                str1 = str1 + "#"
            if self.__width != 0 and i != self.__height - 1:
                str1 = str1 + "\n"
        return str1

    def __repr__(self):
        """official string representation of  an object"""
        return 'Rectangle({:d}, {:d})'.format(self.__width, self.__height)

    def __del__(self):
        """removes a rectangle object"""
        if Rectangle.number_of_instances > 0:
            Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
