"""
Deques based on Python collections.deque
"""
from collections import deque

class ArrayDeque:
    """
    supports insertion and deletion at both the front and the back of the queue
    """
    def __init__(self):
        """
        create an empty deque
        """
        self._data = deque()

    def __len__(self):
        """

        :return:
        """
        return len(self._data)

    def is_empty(self):
        """

        :return: True if empty
        """
        return len(self._data) == 0

    def add_first(self, element):
        """
        add to beginning
        :param element:
        :return:
        """
        self._data.appendleft(element)

    def add_last(self, element):
        """
        add to end
        :param element:
        :return:
        """
        self._data.append(element)

    def delete_first(self):
        """
        remove from beginning
        :return:
        """
        return self._data.popleft()

    def delete_last(self):
        """
        remove from end
        :return:
        """
        return self._data.pop()

    def first(self):
        """
        access first element
        :return:
        """
        return self._data[0]

    def last(self):
        """
        access last element
        :return:
        """
        return self._data[-1]

    def clear(self):
        """
        clear all contents
        :return:
        """
        self._data.clear()

    def rotate(self, k):
        """
        circularly shift rightward k steps
        :param k
        :return:
        """
        self._data.rotate(k)

    def remove(self, element):
        """
        remove first matching element
        :param element:
        :return:
        """
        self._data.remove(element)

    def count(self, element):
        """
        count number of matches for element
        :param element:
        :return:
        """
        self._data.count(element)