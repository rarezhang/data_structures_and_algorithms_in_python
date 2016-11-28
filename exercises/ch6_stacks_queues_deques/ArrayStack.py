"""
Array Stack
Last in first out
"""

from Empty import *


class ArrayStack():
    """
    LIFO Stack implementation using a Python list as underlying storage
    """
    def __init__(self):
        """
        create an empty stack
        """

        # empty list and expands as needed
        self._data = []   # nonpublic list instance

        # it is more efficient in practice to construct a list with initial
        # length n than it is to start with an empty list and append n items


    def __len__(self):
        """

        :return: then number of elements in the stack
        """
        return len(self._data)

    def is_empty(self):
        """
        return true if the stack is empty
        :return: True | False
        """
        return len(self._data) == 0

    def push(self, element):
        """
        add element to the top of the stack
        :param element:
        :return:
        """
        self._data.append(element)  # new item stored at end of list

    def top(self):
        """
        return __but do not remove__ the element at the top of the stack
        Raise Empty exception if the stack is empty
        :return:
        """
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._data[-1]  # the last item in the list

    def pop(self):
        """
        remove and return the element from the top of the stack
        last in first out
        :return:
        """
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._data.pop()  # return and remove last item form list