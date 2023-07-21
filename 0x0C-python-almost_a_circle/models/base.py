#!/usr/bin/python3
"""a module which contains a
base class
"""


import json
import csv
import turtle


class Base:
    """Base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """intializer of a base class
        Attributes:
        id(int): id of the object
        Args:
        id(int): an id passed when an object is
        intialized
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects = Base.__nb_objects + 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """json representation of an objects dictionary"""
        if list_dictionaries == [] or list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """save json representation of an object to a file"""
        list_dictionaries = []
        if list_objs:
            for i in list_objs:
                list_dictionaries.append(i.to_dictionary())
        else:
            pass
        name = cls.__name__ + '.json'
        with open(name, 'w', encoding='utf-8') as f:
            f.write(cls.to_json_string(list_dictionaries))

    @staticmethod
    def from_json_string(json_string):
        """return a list of dictionary representation from Json string"""
        if json_string == "" or json_string is None:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """create an object using a dictionary representation"""
        if dictionary is not None and len(dictionary) > 0:
            if cls.__name__ == 'Rectangle':
                obj = cls(1, 1, 0, 0)
            else:
                obj = cls(1, 0, 0)
            obj.update(**dictionary)
            return obj

    @classmethod
    def load_from_file(cls):
        """return a list of instances from a json file"""
        name = cls.__name__ + '.json'
        try:
            list_obj = []
            with open(name, 'r', encoding='utf-8') as f:
                list_dict = cls.from_json_string(f.read())
                for i in list_dict:
                    list_obj.append(cls.create(**i))
            return list_obj
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Write the CSV representation of a rectangle/square object"""
        name = cls.__name__ + ".csv"
        with open(name, "w", newline="") as csvfile:
            if list_objs is None or list_objs == []:
                csvfile.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    x = ["id", "width", "height", "x", "y"]
                else:
                    x  = ["id", "size", "x", "y"]
                writer = csv.DictWriter(csvfile, fieldnames=x)
                for i in list_objs:
                    writer.writerow(i.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """Return a list of objects from CSV representation"""
        name = cls.__name__ + ".csv"
        try:
            with open(name, "r", newline="") as csvfile:
                if cls.__name__ == "Rectangle":
                    x = ["id", "width", "height", "x", "y"]
                else:
                    x = ["id", "size", "x", "y"]
                list_dicts = csv.DictReader(csvfile, fieldnames=x)
                list_dicts = [dict([k, int(v)] for k, v in d.items())
                              for d in list_dicts]
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Draw Rectangles and Squares using the turtle module.

        Args:
            list_rectangles (list): A list of Rectangle objects to draw.
            list_squares (list): A list of Square objects to draw.
        """
        turt = turtle.Turtle()
        turt.screen.bgcolor("#b7312c")
        turt.pensize(3)
        turt.shape("turtle")

        turt.color("#ffffff")
        for rect in list_rectangles:
            turt.showturtle()
            turt.up()
            turt.goto(rect.x, rect.y)
            turt.down()
            for i in range(2):
                turt.forward(rect.width)
                turt.left(90)
                turt.forward(rect.height)
                turt.left(90)
            turt.hideturtle()

        turt.color("#b5e3d8")
        for sq in list_squares:
            turt.showturtle()
            turt.up()
            turt.goto(sq.x, sq.y)
            turt.down()
            for i in range(2):
                turt.forward(sq.width)
                turt.left(90)
                turt.forward(sq.height)
                turt.left(90)
            turt.hideturtle()
        turtle.exitonclick()
