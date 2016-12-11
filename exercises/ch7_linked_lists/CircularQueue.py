from Excep import *


class CircularQueue:
    """
    Queue implementation using circularly linked list for storage
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
        self._tail = None  # will represent tail of queue
        self._size = 0  # number of queue elements

    def __len__(self):
        """
        return the number of elements in the queue
        :return:
        """
        return self._size

    def is_empty(self):
        """
        return True if the queue is empty
        :return:
        """
        return self._size == 0

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


