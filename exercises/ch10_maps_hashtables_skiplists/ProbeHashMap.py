"""
concrete ProbeHashMap class that uses linear probing for collision resolution
"""

from HashMapBase import HashMapBase


class ProbeHashMap(HashMapBase):
    """
    hash map implemented with linear probing for collision resolution
    """

    _AVAIL = object()  # sentinal marks locations of previous deletions

    def _is_available(self, j):
        """
        return true if index j is available in table
        :param j:
        :return:
        """
        return self._table[j] is None or self._table[j] is ProbeHashMap._AVAIL

    def _find_slot(self, j, k):
        """
        search for key k in bucket at index j
        return (success, index) tuple, described as follows:
        - if match was found, success is True and index denotes its location
        - if no match found, success is False and index denotes first available slot
        :param j:
        :param k:
        :return:
        """
        first_avail = None
        while True:
            if self._is_available(j):
                # cannot stop the search upon reaching an AVAIL sentinel, because it represents a location
                # that may have been filled when the desired item was once inserted
                if first_avail is None:
                    first_avail = j  # mark this as first avail
                if self._table[j] is None:
                    return (False, first_avail)  # search has failed
            elif k == self._table[j]._key:
                return (True, j)  # found a match
            j = (j+1) % len(self._table)  # keep looking cyclically

    def _bucket_getitem(self, j, k):
        """

        :param j:
        :param k:
        :return:
        """
        found, s = self._find_slot(j, k)
        if not found:
            raise KeyError('Key Error: ' + repr(k))   # no match found
        return self._table[s]._value  # _Item: (key, value)

    def _bucket_setitem(self, j, k, v):
        found, s = self._find_slot(j, k)
        if not found:
            self._table[s] = self._Item(k,v)  # insert new item
            self._n += 1  # size has increased
        else:  # find a match
            self._table[s]._value = v  # overwrite existing

    def _bucket_delitem(self, j, k):
        found, s = self._find_slot(j, k)
        if not found:  # no match found
            raise KeyError('Key Error: ' + repr(k))
        self._table[s] = ProbeHashMap._AVAIL  # mark as vacated

    def __iter__(self):
        for j in range(len(self._table)):  # scan entire table
            if not self._is_available(j):
                yield self._table[j]._key
