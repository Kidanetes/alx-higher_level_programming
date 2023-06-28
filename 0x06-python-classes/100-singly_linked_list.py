#!/usr/bin/python3
"""single linked list module"""


class Node:
    """Node of a linekde list
    Args:
    data(int): data of the node
    next_node(Node): next node
    """

    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """to set and retrive data
        to set data, data has to be an integer
        """
        return self.__data

    @data.setter
    def data(self, data):
        if isinstance(data, int):
            self.__data = data
        else:
            raise TypeError("data must be an integer")

    @property
    def next_node(self):
        """to set or retrive next node
        to set next node, next node has to be None or Node
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, next_node):
        if next_node is None or isinstance(next_node, Node):
            self.__next_node = next_node
        else:
            raise TypeError("next_node must be a Node object")


class SinglyLinkedList:
    """singl linked list class"""

    def __init__(self):
        self.__head = None

    def sorted_insert(self, value):
        """insert value into sorted list"""
        obj = Node(value)
        if self.__head is None:
            obj.next_node = None
            self.__head = obj
        else:
            if value < self.__head.data:
                obj.next_node = self.__head
                self.__head = obj
            else:
                tmp = self.__head
                while tmp.next_node is not None:
                    if value < tmp.next_node.data:
                        break
                    tmp = tmp.next_node
                obj.next_node = tmp.next_node
                tmp.next_node = obj

    def __str__(self):
        """representation of single linked list"""
        str1 = ''
        tmp = self.__head
        while tmp.next_node is not None:
            str1 = str1 + str(tmp.data)
            str1 = str1 + '\n'
            tmp = tmp.next_node
        if tmp is not None:
            str1 = str1 + str(tmp.data)
            return str1
