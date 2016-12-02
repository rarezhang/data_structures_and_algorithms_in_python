"""
Array Stack
Last in first out
"""

from Excep import *



class ArrayStack():
    """
    LIFO Stack implementation using a Python list as underlying storage
    """
    def __init__(self, maxlen=None):
        """
        create an empty stack
        :param maxlen: stack’s capacity is limited to maxlen elements (defaults to None)
        """
        self.maxlen = maxlen
        if maxlen == None:
            # empty list and expands as needed
            self._data = []   # nonpublic list instance
        else:
            self._data = [None] * self.maxlen

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
        if len(self._data) == self.maxlen:
            raise Full('Stack is full')
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