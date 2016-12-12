from DoublyLinkedBase import _DoublyLinkedBase
from Excep import Empty

class LinkedDeque(_DoublyLinkedBase):
    """
    double-ended queue implementation based on a doubly linked list
    achieve all operations in O(1)
    """

    # def __init__(self): pass
    # def __len__(self): pass
    # def is_empty(self): pass
    # do not provide explicit __init__ __len__ and is_empty method
    # as the inherited version of the methods suffices to initialize a new instance

    def first(self):
        """
        return __but do not remove__ the element at the front of the deque
        :return:
        """
        if self.is_empty():
            raise Empty('Deque is empty')
        return self._header._next._element  # real item just after header

    def last(self):
        """
        return __but do not remove__ the element at the back of the deque
        :return:
        """
        if self.is_empty():
            raise Empty('Deque is empty')
        return self._trailer._prev._element  # real item just before trailer

    def insert_first(self, element):
        """
        add an element to the front of the deque
        :param element:
        :return:
        """
        self._insert_between(element, self._header, self._header._next)  # after header

    def insert_last(self, element):
        """
        add an element to the back of the deque
        :param element:
        :return:
        """
        self._insert_between(element, self._trailer._prev, self._trailer)  # before trailer

    def delete_first(self):
        """
        remove and return the element from the front of the deque
        raise Empty exception if the deque is empty
        :return:
        """
        if self.is_empty():
            raise Empty('Deque is empty')
        return self._delete_node(self._header._next)  # use inherited mehtod

    def delete_last(self):
        """
        remove and return the element from the back of the deque
        raise empty exception if the deque is empty
        :return:
        """
        if self.is_empty():
            raise Empty('Deque is empty')
        return self._delete_node(self._trailer._prev)  # use inherited method

