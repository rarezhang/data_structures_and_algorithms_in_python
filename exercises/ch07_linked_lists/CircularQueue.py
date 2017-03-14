from Excep import *
from SinglyLinkedBase import _SinglyLinkedBase


class CircularQueue(_SinglyLinkedBase):
    """
    Queue implementation using circularly linked list for storage
    """

    def __init__(self):
        """
        create an empty queue
        """
        self._tail = None  # will represent tail of queue
        self._size = 0  # number of queue elements

    def first(self):
        """
        return __but do not remove__ the element at the front of the queue
        raise empty exception if the queue is empty
        :return:
        """
        if self.is_empty():
            raise Empty('Queue is empty')
        head = self._tail._next
        return head._element

    def dequeue(self):
        """
        remove and return the first element of the queue
        FIFO (first in first out)
        Raise empty exception if the queue is empty
        :return:
        """
        if self.is_empty():
            raise Empty('Queue is empty')
        old_head = self._tail._next
        if self._size == 1:  # removing only element
            self._tail = None  # queue becomes empty
        else:
            self._tail._next = old_head._next  # bypass the old head
        self._size -= 1
        return old_head.element

    def enqueue(self, element):
        """
        add an element to the back of queue
        :param element:
        :return:
        """
        newest = self._Node(element, None)  # new node will be new tail node
        if self.is_empty():
            newest._next = newest  # initialize circularly
        else:
            newest._next = self._tail._next  # new node points to head
            self._tail._next = newest  # old tail points to new node
        self._tail = newest  # new node becomes the tail
        self._size += 1

    def rotate(self):
        """
        rotate front element to the back of the queue
        :return:
        """
        if self._size > 0:
            self._tail = self._tail._next   # old head becomes new tail

    def __iter__(self):
        """
        generate a forward iteration of the element is the stack
        :return:
        """
        cursor = self._tail._next  # head node
        while cursor is not self._tail:
            yield cursor._element
            cursor = cursor._next
        yield cursor._element  # tail node
