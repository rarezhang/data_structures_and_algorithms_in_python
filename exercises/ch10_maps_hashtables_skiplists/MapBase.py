"""
extending the MutableMapping abstract base class to provide a nonpublic
_Item class for use in our various map implementation

MutableMapping class provides concrete implementations for all behaviors other than the
first five outlined in Section 10.1.1: getitem , setitem , delitem , len , and
iter
"""
from collections import MutableMapping


class MapBase(MutableMapping):
    """
    abstract base class that includes a non public _Item class
    """

    # ---------------- nested _Item class -------------------
    class _Item:
        """
        light weight composite to store key-value pairs as map items
        """
        __slots__ = '_key', '_value'

        def __init__(self, k, v):
            self._key = k
            self._value = v

        def __eq__(self, other):
            """
            compare items based on their keys
            :param other:
            :return:
            """
            return self._key == other._key

        def __ne__(self, other):
            """
            opposite of __eq__
            :param other:
            :return:
            """
            return not (self == other)

        def __lt__(self, other):
            """
            compare items based on their keys
            :param other:
            :return:
            """
            return self._key < other._key

        def __gt__(self, other):
            """
            compare items based on their keys
            :param other:
            :return:
            """
            return self._key > other._key