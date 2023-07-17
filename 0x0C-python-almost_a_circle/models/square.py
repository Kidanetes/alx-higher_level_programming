#!/usr/bin/python3
"""this module defines square class"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """class Square which is a sub class
    of Rectangle
    """

    def __init__(self, size, x=0, y=0, id=None):
        """intialize a square object"""
        self.size = size
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """return the size of the square object
        set the size to both width and height"""
        return self.width

    @size.setter
    def size(self, size):
        self.width = size
        self.height = size

    def __str__(self):
        """simple representation of square object"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    def update(self, *args, **kwargs):
        """update the rectangle object"""
        if len(args) > 0:
            attr = ['id', 'size', 'x', 'y']
            for i in range(len(args)):
                if i < 4:
                    setattr(self, attr[i], args[i])
        else:
            for i, k in kwargs.items():
                setattr(self, str(i), k)

    def to_dictionary(self):
        """dictionary represenation of a Rectangle object"""
        return {'id': self.id, 'size': self.width, 'x': self.x, 'y': self.y}
