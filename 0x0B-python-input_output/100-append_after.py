#!/usr/bin/python3
"""100-append_after.py"""


def append_after(filename="", search_string="", new_string=""):
    """append a file if a certain string is found init
    Args:
    filename(str): name of the file
    search_string(str): a string to be searhed
    new_string(str): a string to be be added
    """
    with open(filename, 'r', encoding="utf-8") as f:
        l1 = f.readlines()
    l2 = []
    for i in l1:
        l2.append(i)
        if search_string in i:
            l2.append(new_string)
    str1 = "".join(l2)
    with open(filename, 'w', encoding="utf-8") as f:
        f.write(str1)
