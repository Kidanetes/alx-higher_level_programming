#!/usr/bin/python3
class LockedClass:
    __slots__ = ['first_name']

    def __init__(self, name=""):
        self.name = name
