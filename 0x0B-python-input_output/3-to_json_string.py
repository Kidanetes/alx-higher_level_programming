#!/usr/bin/python3
"""this module contains a function which
returns the JSON representation of an object (string)
"""


import json


def to_json_string(my_obj):
    """represent an oject with JSON
    Args:
    my_obj(object): any object
    returns: Json representation(string)
    """
    return json.dumps(my_obj)
