
class _DoublyLinkedBase:
    """
    a base class providing a doubly linked list representation
    """

    class _Node:
        """
        Light weight, nonpublic class for storing a doubly linked node
        """
        __slots__ = '_element', '_prev', '_next'  # streamline memory

        def __init__(self, element, prev, next):
            """
            initialize node's fields
            :param element: user's element
            :param prev: previous node reference
            :param next: next node reference
            """
            self._element = element
            self._prev = prev
            self._next = next

    def __init__(self):
        """
        create an empty list
        The constructor instantiates the two sentinel nodes and links them directly to each
        other.
        """
        self._header = self._Node(None, None, None)
        self._trailer = self._Node(None, None, None)
        self._header._next = self._trailer  # trailer is after header
        self._trailer._prev = self._header  # header is before trailer
        self._size = 0

    def __len__(self):
        """
        return the number of elements in the list
        :return:
        """
        return self._size

    def is_empty(self):
        """
        return True if list is empty
        :return:
        """
        return self._size == 0

    def _insert_between(self, element, predecessor, successor):
        """
        add element between two existing nodes and return new node
        :param element:
        :param predecessor:
        :param successor:
        :return:
        """
        newest = self._Node(element, predecessor, successor)
        predecessor._next = newest
        successor._prev = newest
        self._size += 1
        return newest

    def _delete_node(self, node):
        """
        delete non-sentinel node from the list and return its element
        :param node:
        :return:
        """
        predecessor = node._prev
        successor = node._next
        predecessor._next = successor
        successor._prev = predecessor
        self._size -= 1
        element = node._element  # record deleted element
        node._prev = node._next = node._element = None  # deprecate node
        return element

    def reverse(self):
        """
        reverses the order of the list
        :return:
        """
        if not self.is_empty():
            new_head, new_tail = self._trailer, self._header
            cursor = self._header
            while cursor is not None:
                temp = cursor
                cursor = temp._next
                temp._next = new_head
                new_head._prev = temp
                new_head = temp
            self._header, self._trailer = new_head, new_tail

    def __iter__(self):
        """
        generate a forward iteration of the element in the doubly linked list
        :return:
        """
        cursor = self._header._next
        while cursor is not self._trailer:
            yield cursor._element
            cursor = cursor._next

    def __str__(self):
        """
        print out the doubly linked list
        :return:
        """
        s = '{{ '
        for i in self:
            s += str(i) + ' '
        s += '}}'
        return s
