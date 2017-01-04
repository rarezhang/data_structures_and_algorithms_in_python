from PriorityQueueBase import PriorityQueueBase

import sys, os
sys.path.append(os.path.abspath("D:\\Projects\\data_structures_and_algorithms_in_python\\exercises\\ch7_linked_lists"))
from Excep import Empty
from PositionalList import PositionalList


class UnsortedPriorityQueue(PriorityQueueBase):
    """
    a min-oriented priority queue implemented with an unsorted list
    """

    # base class defines _Item

    def _find_min(self):  # nonpublic utility
        """
        return Position of item with minimum key
        :return:
        """
        if self.is_empty():
            raise Empty('priority queue is empty')
        small = self._data.first()
        walk = self._data.after(small)
        while walk is not None:
            if walk.element() < small.element():
                small = walk
            walk = self._data.after(walk)
        return small

    def __init__(self):
        """
        create a new empty Priority Queue
        """
        self._data = PositionalList()

    def __len__(self):
        """
        return the number of items in the priority queue
        :return:
        """
        return len(self._data)

    def add(self, key, value):
        """
        add a key-value pair
        :param key:
        :param value:
        :return:
        """
        self._data.add_last(self._Item(key, value))

    def min(self):
        """
        return but do not remove (k,v) pair with minimum key
        :return:
        """
        p = self._find_min()  # return the position
        item = p.element()
        return (item._key, item._value)

    def remove_min(self):
        """
        remove and return (k,v) pair with minimum key
        :return:
        """
        p = self._find_min()  # return the position
        item = self._data.delete(p)
        return (item._key, item._value)

