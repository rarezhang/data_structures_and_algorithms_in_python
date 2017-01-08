"""
an implementation of a SortedTableMap class
"""

from MapBase import MapBase


class SortedTableMap(MapBase):
    """
    map implementation using a sorted table
    """

    # ------------------- nonpublic methods -----------------------
    def _find_index(self, k, low, high):
        """
        return index of the left most item with key greater than or equal to k

        return high+1 if no such item qualifies
        j will be returned such that:
        - all items of slice table[low:j] have key<k
        - all items of slice table[j:high+1] have key>=k

        :param k:
        :param low:
        :param high:
        :return:
        """
        if high < low:
            return high + 1  # no element qualifies
        else:
            mid = (low+high) // 2
            if k == self._table[mid]._key:
                return mid  # find exact match
            elif k < self._table[mid]._key:
                return self._find_index(k, low, mid-1)  # Note: may return mid
            else:
                return self._find_index(k, mid+1, high)  # answer is right of mid

    # ------------------- public behaviors ------------------------------
    def __init__(self):
        """
        create an empty map
        """
        self._table = []

    def __len__(self):
        """
        return number of items in the map
        :return:
        """
        return len(self._table)

    def __getitem__(self, k):
        """
        return value associated with key k (raise KeyError if not found)
        :param k:
        :return:
        """
        j = self._find_index(k, 0, len(self._table)-1)
        if j == len(self._table) or self._table[j]._key != k:
            raise KeyError('Key Error: ' + repr(k))
        return self._table[j]._value

    def __setitem__(self, k, v):
        """
        assign value v to key k, overwriting existing value if present
        :param k:
        :param v:
        :return:
        """
        j = self._find_index(k, 0, len(self._table)-1)
        if j < len(self._table) and self._table[j]._key == k:
            self._table[j]._value = v  # reassign value
        else:
            self._table.insert(j, self._Item(k,v))  # adds new item

    def __delitem__(self, k):
        """
        remove item associated with key k (raise KeyError if not found)
        :param k:
        :return:
        """
        j = self._find_index(k, 0, len(self._table)-1)
        if j == len(self._table) or self._table[j]._key != k:
            raise KeyError('Key Error: ' + repr(k))
        self._table.pop(j)  # delete item

    def __iter__(self):
        """
        generate keys of the map ordered from minimum to maximum
        :return:
        """
        for item in self._table:
            yield item._key

    def __reversed__(self):
        """
        generate keys of the map ordered from maximum to minimum
        :return:
        """
        for item in reversed(self._table):
            yield item._key

    def find_min(self):
        """
        return (key,value) pair with minimum key or None if empty
        :return:
        """
        if len(self._table) > 0:
            return (self._table[0]._key, self._table[0]._value)
        else:
            return None

    def find_max(self):
        """
        return (key,value) pair with maximum key or None if empty
        :return:
        """
        if len(self._table) > 0:
            return (self._table[-1]._key, self._table[-1]._value)
        else:
            return None

    def find_ge(self, k):
        """
        return (key,value) pair wit least key greater than or equal to k
        :param k:
        :return:
        """
        j = self._find_index(k, 0, len(self._table)-1)  # j's key >= k
        if j < len(self._table):
            return (self._table[j]._key, self._table[j]._value)
        else:
            return None

    def find_lt(self, k):
        """
        :return (key, value) pair with greatest key strictly less than k
        :param k:
        :return:
        """
        j = self._find_index(k, 0, len(self._table)-1)
        if j > 0:
            return (self._table[j-1]._key, self._table[j-1]._value)  # use of j-1
        else:
            return None

    def find_gt(self, k):
        """
        return (key,value) pair with least key strictly greater than k
        :param k:
        :return:
        """
        j = self._find_index(k, 0, len(self._table)-1)  # j's key >= k
        if j < len(self._table) and self._table[j]._key == k:
            j += 1
        if j < len(self._table):
            return (self._table[j]._key, self._table[j]._value)
        else:
            return None

    def find_range(self, start, stop):
        """
        iterate all (key,value) pairs such that start<=key<stop

        if start is None, iteration begins with minimum key of map
        if stop is None, iteration continues through the maximum key of map
        :param start:
        :param stop:
        :return:
        """
        if start is None:
            j = 0
        else:
            j = self._find_index(start, 0, len(self._table)-1)  # find first result
        while j < len(self._table) and (stop is None or self._table[j]._key < stop):
            yield (self._table[j]._key, self._table[j]._value)
            j += 1

            