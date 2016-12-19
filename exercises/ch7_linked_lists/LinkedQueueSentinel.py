from Excep import *
from SinglyLinkedBaseSentinel import _SinglyLinkedBaseSentinel


class LinkedQueueSentinel(_SinglyLinkedBaseSentinel):
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
        return self._header._next._element   # front aligned with head of list

    def dequeue(self):
        """
        remove and return the first element of the queue
        FIFO (first in first out)
        raise empty exception if the queue is empty
        :return:
        """
        if self.is_empty():
            raise Empty('Queue is empty')
        answer = self._header._next._element
        new_head = self._header._next._next
        self._header._next = new_head
        self._size -= 1
        if self.is_empty():
            self._trailer = self._Node(None, None)
        return answer

    def enqueue(self, element):
        """
        add an element to the back of queue
        :param element:
        :return:
        """
        newest = self._Node(element, None)  # node will be new tail node
        if self.is_empty():  # special case previously empty
            self._header._next = newest
        else:
            self._trailer._next = newest
        self._trailer = newest  # update reference to tail node
        self._size += 1

    def rotate(self):
        """
        rotate front element to the back of the queue
        :return:
        """
        if not self.is_empty():
            original_head = self._header._next
            original_head._next = None

            new_head = self._header._next._next
            self._header._next = new_head
            self._trailer._next = original_head
            self._trailer = original_head



