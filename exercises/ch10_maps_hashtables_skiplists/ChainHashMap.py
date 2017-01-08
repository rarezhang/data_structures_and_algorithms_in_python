"""
concrete hash map class with separate chaining
"""

from HashMapBase import HashMapBase
from UnsortedTableMap import UnsortedTableMap


class ChainHashMap(HashMapBase):
    """
    hash map implemented with separate chaining for collision resolution
    """

    def _bucket_getitem(self, j, k):
        """
        self._table[j][k]
        :param j:
        :param k:
        :return:
        """
        bucket = self._table[j]
        if bucket is None:
            raise KeyError('Key Error: ' + repr(k))  # no match found
        return bucket[k]  # may raise KeyError

    def _bucket_setitem(self, j, k, v):
        """

        :param j:
        :param k:
        :param v:
        :return:
        """
        if self._table[j] is None:
            self._table[j] = UnsortedTableMap()  # bucket is new to the table
        oldsize = len(self._table[j])
        self._table[j][k] = v
        if len(self._table[j]) > oldsize:  # key is new to the table
            self._n += 1  # increase overall map size

    def _bucket_delitem(self, j, k):
        """

        :param j:
        :param k:
        :return:
        """
        bucket = self._table[j]
        if bucket is None:
            raise KeyError('Key Error: '+ repr(k))  # no match found
        del bucket[k]

    def __iter__(self):
        """

        :return:
        """
        for bucket in self._table:
            if bucket is not None:  # a non-empty slot 
                for key in bucket:
                    yield key