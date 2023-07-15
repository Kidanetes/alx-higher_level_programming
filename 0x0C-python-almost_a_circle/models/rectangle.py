#!/usr/bin/python3
"""this module define a class
Rectangle which is a sub class
of Base class"""


from models.base import Base


class Rectangle(Base):
    """Rectangle class which is
    a sub class of Base class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """intialization of a Rectangle object
        Args:
        width(int): width of a rectangle
        height(int): height of a rectangle
        x(int): x-coordinate
        y(int): y-cordinate
        id(int): id of rectangle object
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """return width of a rectangle object
        the setter will check if width is integer
        and above 0
        """
        return self.__width

    @width.setter
    def width(self, width):
        self.__num_validate('width', width)
        self.__width = width

    @property
    def height(self):
        """return height of a rectangle object
        the setter will check if height is integer
        and above 0
        """
        return self.__height

    @height.setter
    def height(self, height):
        self.__num_validate('height', height)
        self.__height = height

    @property
    def x(self):
        """return x-coordinate of a rectangle object
        the setter will check if x is integer
        and not negative
        """
        return self.__x

    @x.setter
    def x(self, x):
        self.__num_validate('x', x)
        self.__x = x

    @property
    def y(self):
        """return y-coordinate of a rectangle object
        the setter will check if y is integer
        and not negative
        """
        return self.__y

    @x.setter
    def y(self, y):
        self.__num_validate('y', y)
        self.__y = y

    @staticmethod
    def __num_validate(name, value):
        """checks the validity of a rectangle object
        field
        Args
        name(str): name of the field
        value(int): value of the string
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if name == 'x' or name == 'y':
            if value < 0:
                raise ValueError(f"{name} must be >= 0")
        if name == 'width' or name == 'height':
            if value <= 0:
                raise ValueError(f"{name} must be > 0")

    def area(self):
        """return the area of the rectangle object"""
        area = self.__width * self.__height
        return area

    def display(self):
        """display a rectangle object using # character"""
        for i in range(self.__height):
            for j in range(self.__width):
                print("#", end="")
            print()
