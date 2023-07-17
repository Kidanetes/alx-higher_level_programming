#!/usr/bin/python3
"""a module which contains a
base class
"""


import json


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
