#!/usr/bin/python3
"""this module conatin a function
which will indent the text when it encounters
a certain characters
"""


def text_indentation(text):
    """this function will print an indented
    a text when it reaches ., ?, :
    Args
    text(string): string to be indented
    """
    if type(text) is not str:
        raise TypeError('text must be a string')
    text = text.strip()
    str1 = ""
    for i in range(len(text)):
        str1 = str1 + text[i]
        if text[i] in ".?:":
            str1 = str1.strip()
            print("{}\n".format(str1))
            str1 = ""
        elif i < len(text) - 1:
            pass
        else:
            print(str1.strip(), end="")
