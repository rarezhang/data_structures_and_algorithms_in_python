from PriorityQueueBase import PriorityQueueBase
import sys, os
sys.path.append(os.path.abspath("D:\\Projects\\data_structures_and_algorithms_in_python\\exercises\\ch7_linked_lists"))
from Excep import Empty
from PositionalList import PositionalList

class SortedPriorityQueue(PriorityQueueBase):
    """
    a min-oriented priority queue implemented with a sorted list
    """

    # base class defines _Item

    def __init__(self):
        """
        create a new empty Priority queue
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
        newest = self._Item(key, value)  # make new item instance
        walk = self._data.last()  # walk backward looking for smaller key, [last() return a position]
        while walk is not None and newest < walk.element():
            walk = self._data.before(walk)
        if walk is None:
            self._data.add_first(newest)   # new key is smallest
        else:
            self._data.add_after(walk, newest)  # newest goes after walk

    def min(self):
        """
        return but do not remove (k,v) tuple with minimum key
        :return:
        """
        if self.is_empty():
            raise Empty('priority queue is empty')
        p = self._data.first()  # return a position
        item = p.element()
        return (item._key, item._value)

    def remove_min(self):
        """
        remove and return (k,v) tuple with minimum key
        :return:
        """
        if self.is_empty():
            raise Empty('priority queue is empty')
        item = self._data.delete(self._data.first())  # delete() return the element
        return (item._key, item._value)