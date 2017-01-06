"""
an implementation of a map using a Python list as an unsorted table

simple but not efficient
getitem, setitem and delitem relies on for loop to scan
"""

from MapBase import MapBase


class UnsortedTableMap(MapBase):
    """
    Map implementation using an unordered list
    """

    def __init__(self):
        """
        create an empty map
        """
        self._table = []  # list of _Item

    def __getitem__(self, k):
        """
        return value associated with key k
        raise KeyError if not found
        :param k:
        :return:
        """
        for item in self._table:
            if k == item._key:
                return item._value
        raise KeyError('Key Error: ' + repr(k))

    def __setitem__(self, k, v):
        """
        assign value to key, overwriting existing value if present
        :param k: key
        :param v: value
        :return:
        """
        for item in self._table:
            if k == item._key:  # found a match
                item._value = v  # reassign value
                return  # quit
        self._table.append(self._Item(k, v))  # did not find match for key

    def __delitem__(self, k):
        """
        remove item associated with key
        raise KeyError if not found
        :param k: key
        :return:
        """
        for j in range(len(self._table)):
            if k == self._table[j]._key:  # found a match
                self._table.pop(j)  # remove item
                return   # quit
        raise KeyError('Key Error: ' + repr(k))

    def __len__(self):
        """
        return number of items in the map
        :return:
        """
        return len(self._table)

    def __iter__(self):
        """
        generate iteration of the map's keys
        :return:
        """
        for item in self._table:
            yield item._key  # yield the KEY 


