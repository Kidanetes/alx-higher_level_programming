#!/usr/bin/python3
"""this module contains a function which
will write into a text file
"""


def write_file(filename="", text=""):
    """write into a file
    Args:
    filename(str): name of a file
    text(str): string to be written into a file
    Returns: number of characters written into a file
    """
    with open(filename, 'w', encoding="utf-8") as f:
        if text:
            return f.write(text)
