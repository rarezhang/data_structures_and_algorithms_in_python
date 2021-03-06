"""
base class for singly linked list
LinkedStack and LinkedQueue
singly linked list includes a header sentinel
"""


class _SinglyLinkedBaseSentinel:
    """
    a base class providing a singly linked list
    """

    class _Node:
        """
        nested _Node class
        light weight, non public class for storing a singly linked node
        """
        __slots__ = '_element', '_next'  # streamline memory usage

        def __init__(self, element, next):
            """
            initialize node's fields
            :param element:
            :param next:
            """
            self._element = element  # reference to user's element
            self._next = next  # reference to next node

    def __init__(self):
        """
        create an empty queue
        """
        self._header = self._Node(None, None)
        self._trailer = None
        self._header._next = self._trailer  # trailer is after header
        self._size = 0  # number of queue elements

    def __len__(self):
        """
        return the number of elements in the queue
        :return:
        """
        return self._size

    def is_empty(self):
        """
        return True if the stack is empty
        :return:
        """
        return self._size == 0

    def __iter__(self):
        """
        generate a forward iteration of the element in the stack
        :return:
        """
        cursor = self._header._next
        while cursor is not None:
            yield cursor._element
            cursor = cursor._next

    def __str__(self):
        """
        print out the singl
        :return:
        """
        s = '{ '
        for i in self:
            s += str(i) + ' '
        s += '}'
        return s