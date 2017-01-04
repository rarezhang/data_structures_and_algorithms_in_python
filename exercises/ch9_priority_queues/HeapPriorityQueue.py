"""
an implementation of a priority queue
using an array-based heap
"""

from PriorityQueueBase import PriorityQueueBase

import sys, os
sys.path.append(os.path.abspath("D:\\Projects\\data_structures_and_algorithms_in_python\\exercises\\ch7_linked_lists"))
from Excep import Empty


class HeapPriorityQueue(PriorityQueueBase):
    """
    a min-oriented priority queue implemented with a binary heap
    """

    # base class defines _Item

    # --------------------------nonpublic method---------------------------

    # If p is the root of T, then f ( p ) = 0.
    # If p is the left child of position q, then f ( p ) = 2 f ( q )+ 1.
    # If p is the right child of position q, then f ( p ) = 2 f ( q )+ 2.

    def _parent(self, j):
        """

        :param j: index
        :return:
        """
        return (j - 1) // 2

    def _left(self, j):
        """

        :param j: index
        :return:
        """
        return 2 * j + 1

    def _right(self, j):
        """

        :param j: index
        :return:
        """
        return 2 * j + 2

    def _has_left(self, j):
        """
        index beyond end of list?
        :param j:
        :return: if there is left child
        """
        return self._left(j) < len(self._data)

    def _has_right(self, j):
        """
        index beyond end of list?
        :param j:
        :return: if there is right child
        """
        return self._right(j) < len(self._data)

    def _swap(self, i, j):
        """
        swap the elements at indices i and j of array
        :param i:
        :param j:
        :return:
        """
        self._data[i], self._data[j] = self._data[j], self._data[i]

    def _upheap(self, j):
        """
        up-ward swapping process; up-heap bubbling
        use recursion to implement the repetition
        :param j:
        :return:
        """
        parent = self._parent(j)  # the index of parent
        if j > 0 and self._data[j] < self._data[parent]:
            self._swap(j, parent)
            self._upheap(parent)  # recursion at position of parent

    def _downheap(self, j):
        """
        down-ward swapping process; down-heap bubbling
        use recursion to implement the repetition
        :param j:
        :return:
        """
        if self._has_left(j):
            left = self._left(j)  # index of left child
            small_child = left  # although right may be smaller
            if self._has_right(j):
                right = self._right(j)  # index of right child
                if self._data[right] < self._data[left]:
                    small_child = right
            # swap
            if self._data[small_child] < self._data[j]:
                self._swap(j, small_child)
                self._downheap(small_child)  # recursion at position of small child

    # -------------------- public methods ------------------------------------
    def __init__(self):
        """
        create a new empty Priority Queue
        """
        self._data = []

    def __len__(self):
        """
        return the number of items in the priority queue
        :return:
        """
        return len(self._data)

    def add(self, key, value):
        """
        add a key-value pair to the priority queue
        :param key:
        :param value:
        :return:
        """
        self._data.append(self._Item(key, value))
        self._upheap(len(self._data)-1)  # upheap newly added position: j = len(_data)-1

    def min(self):
        """
        return but do not remove (k,v) pair with minimum key
        raise empty exception if empty
        :return:
        """
        if self.is_empty():
            raise Empty('priority queue is empty')
        item = self._data[0]
        return (item._key, item._value)

    def remove_min(self):
        """
        remove and return (k,v) pair with minimum key
        :return:
        """
        if self.is_empty():
            raise Empty('priority queue is empty')
        self._swap(0, len(self._data)-1)  # put minimum item at the end
        item = self._data.pop()  # remove the minimum item from the queue
        self._downheap(0)  # fix new root
        return (item._key, item._value)