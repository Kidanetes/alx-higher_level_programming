#!/usr/bin/python3
"""this module contains a function which
will append a text file
"""


def append_write(filename="", text=""):
    """append a file
    Args:
    filename(str): name of a file
    text(str): string to be written into a file
    Returns: number of characters written into a file
    """
    with open(filename, 'a', encoding="utf-8") as f:
        if text:
            return f.write(text)
