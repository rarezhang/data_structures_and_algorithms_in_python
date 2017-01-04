"""
Priority Queue Base
"""


class PriorityQueueBase:
    """
    abstract base class for a priority queue
    """

    class _Item:
        """
        lightweight composite to store priority queue items
        """
        __slots__ = '_key', '_value'

        def __init__(self, k, v):
            self._key = k
            self._value = v

        def __lt__(self, other):
            """
            compare items based on their keys
            :param other:
            :return:
            """
            return self._key < other._key

    def is_empty(self):
        """
        concrete method assuming abstract len
        return true if the priority queue is empty
        :return:
        """
        return len(self) == 0