#!/usr/bin/python3
"""this module contains a function which
returns the an object (Python data structure)
represented by a JSON string
"""


import json


def from_json_string(my_str):
    """return an oject with JSON
    Args:
    my_str(str): json representation of an object
    returns: the object represented by JSON
    """
    if my_str:
        return json.loads(my_str)
