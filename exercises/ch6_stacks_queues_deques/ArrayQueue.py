"""
Array Queue
First in first out
"""

from Empty import *

class ArrayQueue:
    """
    first in first out queue implementation
    using a python list as underlying storage
    """
    DEFAULT_CAPACITY = 10  # moderate capacity for all new queues

    def __init__(self):
        """
        create an empty queue
        """
        self._data = [None] * ArrayQueue.DEFAULT_CAPACITY
        self._size = 0
        self._front = 0

    def __len__(self):
        """
        return the number of elements in the queue
        :return:
        """
        return self._size

    def is_empty(self):
        """
        return true if the queue is empty
        :return:
        """
        return self._size == 0

    def first(self):
        """
        return __but do not remove__ the element at the front of the queue
        raise Empty exception if the queue is empty
        :return:
        """
        if self.is_empty():
            raise Empty('queue is empty')
        return self._data[self._front]

    def dequeue(self):
        """
        remove and return the first element of the queue
        first in first out
        raise Empty exception if the queue is empty
        :return:
        """
        if self.is_empty():
            raise Empty('queue is empty')
        first_element = self._data[self._front]
        self._data[self._front] = None  # help garbage collection
        self._front = (self._front + 1) % len(self._data)  # P264
        self._size -= 1
        return first_element

    def enqueue(self, element):
        """
        add an element to the back of queue
        :param element:
        :return:
        """
        if self._size == len(self._data):
            self._resize(2 * len(self._data))  # double the array size
        avail = (self._front + self._size) % len(self._data)  # next opening P266
        self._data[avail] = element
        self._size += 1

    def _resize(self, c):  # assume capacity >= len(self)
        """
        resize to a new list of capacity >= len(self)
        :param c:
        :return:
        """
        old = self._data  # keep track of existing list
        self._data = [None] * c  # allocate list with new capacity
        walk = self._front
        for k in range(self._size):  # only consider existing elements
            self._data[k] = old[walk]  # intentionally shift indices
            walk = (1 + walk) % len(old)  # use old size as modulus
        self._front = 0  # front has been realigned


