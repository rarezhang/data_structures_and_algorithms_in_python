"""
an implementation of an adaptable priority queue
"""

from HeapPriorityQueue import HeapPriorityQueue

class AdaptableHeapPriorityQueue(HeapPriorityQueue):
    """
    a locator-based priority queue implemented with a binary heap
    """

    # ------------- nested locator class ------------------------
    class Locator(HeapPriorityQueue._Item):
        """
        token for locating an entry of the priority queue
        """
        __slots__ = '_index'  # add index as additional field

        def __init__(self, k, v, j):
            super().__init__(k, v)
            self._index = j

    # ----------------- nonpublic methods --------------------------
    def _swap(self, i, j):
        """
        override swap to record new indices
        :param i:
        :param j:
        :return:
        """
        super()._swap(i, j)  # perform the swap
        self._data[i]._index = i  # reset locator index (post-swap)
        self._data[j]._index = j  # reset locator index (post-swap)

    def _bubble(self, j):
        """
        manages the reinstatement of the heap-order property when a key has changed at an arbitrary position within the heap,
        either due to a key update, or the blind replacement of a removed element with the item from the last position of the tree.
        :param j:
        :return:
        """
        if j > 0 and self._data[j] < self._data[self._parent(j)]:
            self._upheap(j)
        else:
            self._downheap(j)

    # ---------------- public method ---------------------------------
    def add(self, key, value):
        """
        add a key-value pair
        :param key:
        :param value:
        :return:
        """
        token = self.Locator(key, value, len(self._data))  # initialize locator index
        self._data.append(token)
        self._upheap(len(self._data) - 1)
        return token

    def update(self, loc, newkey, newval):
        """
        update the key and value for the entry identified by locator loc
        :param loc:
        :param newkey:
        :param newval:
        :return:
        """
        j = loc._index
        if not (0 <= j <= len(self) and self._data[j] is loc):
            raise ValueError('Invalid locator')
        loc._key = newkey
        loc._value = newval
        self._bubble(j)

    def remove(self, loc):
        """
        remove and return the (k,v) pair identified by locator loc
        :param loc:
        :return:
        """
        j = loc._index
        if not (0 <= j <= len(self) and self._data[j] is loc):
            raise ValueError('Invalid locator')
        if j == len(self) - 1:  # item at last position
            self._data.pop()  # just remove it
        else:
            self._swap(j, len(self)-1)  # swap item to the last position
            self._data.pop()  # remove it from the list
            self._bubble(j)  # fix item displaced by the swap
        return (loc._key, loc._value)
