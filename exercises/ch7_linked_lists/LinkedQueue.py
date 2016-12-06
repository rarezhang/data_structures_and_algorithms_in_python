from Excep import *


class LinkedQueue:
    """
    FIFO (first in first out)
    queue implementation using a singly linked list for storage

    enqueue elements at the back and dequeue them from the front
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
        self._head = None
        self._tail = None
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

    # enqueue elements at the back and dequeue them from the front
    def first(self):
        """
        return __but do not remove__ the element at the front of the queue
        :return:
        """
        if self.is_empty():
            raise Empty('Queue is empty')
        return self._head._element   # front aligned with head of list

    def dequeue(self):
        """
        remove and return the first element of the queue
        FIFO (first in first out)
        raise empty exception if the queue is empty
        :return:
        """
        if self.is_empty():
            raise Empty('Queue is empty')
        answer = self._head._element
        self._head = self._head._next
        self._size -= 1
        if self.is_empty():  # special case as queue is empty
            self._tail = None   # removed head had been the tail
        return answer

    def enqueue(self, element):
        """
        add an element to the back of queue
        :param element:
        :return:
        """
        newest = self._Node(element, None)  # node will be new tail node
        if self.is_empty():  # special case previously empty
            self._head = newest
        else:
            self._tail._next = newest
        self._tail = newest  # update reference to tail node
        self._size += 1