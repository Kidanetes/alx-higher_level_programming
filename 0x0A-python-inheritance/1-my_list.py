#!/usr/bin/python3
"""this module contains a mylist class which is
a subclass of List class"""


class MyList(list):
    """Mylist is a subclass of List"""
    def print_sorted(self):
        """this method will sort a list"""
        #/*l1 = self[:]*/
        #/*l1.sort()*/
        print(sorted(self))
