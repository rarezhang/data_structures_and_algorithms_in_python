from Excep import *
from SinglyLinkedBase import _SinglyLinkedBase


class LinkedQueue(_SinglyLinkedBase):
    """
    FIFO (first in first out)
    queue implementation using a singly linked list for storage

    enqueue elements at the back and dequeue them from the front
    """

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
