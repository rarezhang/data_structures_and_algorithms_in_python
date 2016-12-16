from Excep import *
from SinglyLinkedBase import _SinglyLinkedBase


class LinkedStack(_SinglyLinkedBase):
    """
    LIFO (last in first out) Stack
    implementation using a singly linked list for storage
    """

    def push(self, element):
        """
        add element to the top of the stack
        :param element:
        :return:
        """
        self._head = self._Node(element, self._head)  # create and link a new node
        self._size += 1

    def top(self):
        """
        return __but do not remove__ the element at the top of the stack
        raise empty exception if the stack is empty
        :return:
        """
        if self.is_empty():
            raise Empty('stack is empty')
        return self._head._element  # top of the stack is at head of list

    def pop(self):
        """
        remove and return the element from the top of the stack
        LIFO (last in first out)
        raise empty exception if the stack is empty
        :return:
        """
        if self.is_empty():
            raise Empty('stack is empty')
        answer = self._head._element
        self._head = self._head._next  # bypass the former top node
        return answer
