#!/usr/bin/python3
"""this module contains a function which
will creates an Object from a JSON representation
"""


import json


def load_from_json_file(filename):
    """write json representation of an
    object to a file
    Args:
    filename(str): name of a JSON file
    """
    with open(filename, 'r', encoding="utf-8") as f:
        return json.load(f)
