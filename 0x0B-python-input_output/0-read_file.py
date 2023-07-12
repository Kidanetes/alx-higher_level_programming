#!/usr/bin/python3
"""this module contains a function which
will read from a text file
"""


def read_file(filename=""):
    """reads from a file
    Args:
    filename(str): name of a file
    """
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
