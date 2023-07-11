#!/usr/bin/python3
"""this module contains a function which
will writes an Object to a text file, using
a JSON representation
"""


import json


def save_to_json_file(my_obj, filename):
	"""write json representation of an
	object to a file
	Args:
	my_obj(object): any object
	filename(str): name of a file
	"""
	with open(filename, 'w', encoding="utf-8") as f:
		json.dump(my_obj, f)