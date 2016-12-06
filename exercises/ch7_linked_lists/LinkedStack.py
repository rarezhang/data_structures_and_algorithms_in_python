from Excep import *


class LinkedStack:
    """
    LIFO (last in first out) Stack
    implementation using a singly linked list for storage
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
        create an empty stack
        """
        self._head = None  # reference to the head node
        self._size = 0  # number of stack elements

    def __len__(self):
        """
        return the number of elements in the stack
        :return:
        """
        return self._size

    def is_empty(self):
        """
        return True if the stack is empty
        :return:
        """
        return self._size == 0

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