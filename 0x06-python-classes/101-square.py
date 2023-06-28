#!/usr/bin/python3
""" a module with an empty class """


class Square:
    """class with private field
    Args:
    size(int): size of the square
    position(tuple): postion of the square
    """
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """postion should be a tuple of integers
        and both elements should be greater than zero
        """
        return self.__position

    @position.setter
    def position(self, value):
        if (type(value) is not tuple or type(value[0]) is not int
                or len(value) != 2 or type(value[1]) is not int
                or value[0] < 0 or value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """calculate the area of a square
        Returns: area of the square
        """
        return self.__size ** 2

    def my_print(self):
        """print a square using #"""
        if (self.__size != 0):
            for i in range(self.__position[1]):
                print()
        for i in range(self.__size):
            for k in range(self.__position[0]):
                print(" ", end="")
            for j in range(self.__size):
                print("#", end="")
            if i < self.__size - 1:
                print()
        print()
    def __str__(self):
        """representation of square class"""
        str1 = ""
        if (self.__size != 0):
            for i in range(self.__position[1]):
                str1 = str1 + "\n"
        for i in range(self.__size):
            for k in range(self.__position[0]):
                str1 = str1 + " "
            for j in range(self.__size):
                str1 = str1 + "#"
            if i < self.__size - 1:
                str1 = str1 + "\n"
        str1 = str1 + "\n"
        return str1
