#!/usr/bin/python3
"""This Module contains the Rectangle Class"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """class rectangle, a sub class of Base Geometry"""

    def __init__(self, width, height):
        """intiaization a Rectangle object
        Args:
        width(int): width
        height(int): height
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """returns the area of rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """represent the object"""
        return f"[Rectangle] {self.__width}/{self.__height}"
