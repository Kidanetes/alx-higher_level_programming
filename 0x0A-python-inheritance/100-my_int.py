#!/usr/bin/python3
"""a sub class of int"""


class MyInt(int):
    """a sub class of int"""

    def __eq__(self, x):
        """overide the int class equality method
        and change it to inequality
        """
        return super().__ne__(x)

    def __ne__(self, x):
        """overide the int class inequality method
        and change it to equality
        """
        return super().__eq__(x)
