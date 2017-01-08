"""
an implementation of a MultiMap using a dict for storage
"""


class MultiMap:
    """
    a multimap class built upon use of an underlying map for storage
    """
    _MapType = dict  # map type, can be redefined by subclass

    def __init__(self):
        """
        create a new empty multimap instance
        """
        self._map = self._MapType()  # create map instance for storage
        self._n = 0

    def __len__(self):
        """

        :return:
        """
        return self._n

    def __iter__(self):
        """
        iterate through all (k,v) pairs in multimap
        :return:
        """
        for k, secondary in self._map.items():  # secondary -> list
            for v in secondary:
                yield (k,v)

    def add(self, k, v):
        """
        add pair (k,v) to multimap
        :param k:
        :param v:
        :return:
        """
        container = self._map.setdefault(k, [])  # create empty list if needed
        container.append(v)
        self._n += 1

    def pop(self, k):
        """
        remove and return arbitrary (k,v) with key k
        or raise KeyError
        :param k:
        :return:
        """
        secondary = self._map[k]  # may raise KeyError
        v = secondary.pop()
        if len(secondary) == 0:
            del self._map[k]  # no pairs left
        self._n -= 1
        return (k,v)

    def find(self, k):
        """
        return arbitrary (k,v) pair with given key (or raise KeyError)
        :param k:
        :return:
        """
        secondary = self._map[k]  # may raise KeyError
        return (k, secondary[0])
    
    def find_all(self, k):
        """
        generate iteration of all (k,v) pairs with given key
        :param k:
        :return:
        """
        secondary = self._map.get(k, [])  # empty list by default
        for v in secondary:
            yield (k,v)