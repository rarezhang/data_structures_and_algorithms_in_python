"""
sequence containers that allow constant time insert
and delete operations anywhere within the sequence
based on a singly linked list
"""


class ForwardList:
    """
    singly linked list based forward list
    """

    # -------------- nested nonpublic Node class ------------------------
    class _Node:
        """
        nonpublic class for storing a singly linked list
        """
        __slots__ = '_element', '_next'  # streamline memory

        def __init__(self, element, next):
            """
            initialize node's fields
            :param element:
            :param next:
            """
            self._element = element
            self._next = next

    # ----------------- nested Position class -----------------------------
    class Position:
        """
        an abstraction representing the location of a single element
        """

        def __init__(self, container, node):
            """
            constructor should not be invoked by user
            :param container:
            :param node:
            """
            self._container = container
            self._node = node

        def element(self):
            """
            return the element stored at this position
            :return:
            """
            return self._node._element

        def __eq__(self, other):
            """
            return True if other is a Position representing the same location
            :param other:
            :return:
            """
            # basically just need to check if the Position is associated with same Node object
            # same Node may have multiple Position container
            return type(other) is type(self) and other._node is self._node

        def __ne__(self, other):
            """
            return True if other does not represent the same location
            :param other:
            :return:
            """
            return not (self == other)  # opposite of __eq__

    # ----------------------------------------------------------------------
    def __init__(self):
        """
        create an empty list
        """
        self._head = None
        self._tail = None
        self._size = 0

    def __len__(self):
        """
        return the number of element in the list
        :return:
        """
        return self._size

    def is_empty(self):
        """
        return True if list is empty
        :return:
        """
        return self._size == 0

    def __iter__(self):
        """
        generate a forward iteration of the element in the doubly linked list
        :return:
        """
        cursor = self._head
        while cursor is not None:
            yield cursor._element
            cursor = cursor._next

    def __str__(self):
        """
        print out the doubly linked list
        :return:
        """
        s = '{ '
        for i in self:
            s += str(i) + ' '
        s += '}'
        return s

    # ------------------------------------------------------------------

    def _validate(self, position):
        """
        return position's node or raise appropriate error if invalid
        :param position:
        :return:
        """
        if not isinstance(position, self.Position):
            raise TypeError('position must be proper Position type')
        if position._container is not self:
            raise ValueError('position does not belong to this container')
        if position._node._next is None:  # convention for deprecated nodes
            raise ValueError('position is no longer valid')
        return position._node

    def _make_position(self, node):
        """
        return Position instance for given node
        :param node:
        :return:
        """
        return self.Position(self, node)  # legitimate position

    def first(self):
        """
        return the first position in the list
        or None if list is empty
        :return:
        """
        if not self.is_empty():
            return self._make_position(self._head)

    def last(self):
        """
        return the last position in the list
        or None if list is empty
        :return:
        """
        if not self.is_empty():
            return self._make_position(self._tail)

    def after(self, position):
        """
        return the position just after position
        or None if position is last
        :param position:
        :return:
        """
        node = self._validate(position)
        return self._make_position(node._next)

    def add_last(self, element):
        """
        insert element at the end of the list and return new position
        :param element:
        :return:
        """
        node = self._Node(element, None)
        if self.is_empty():  # special case previously empty
            self._head = node  # update reference to head node
        else:  # do not change head node
            self._tail._next = node
        self._tail = node  # update reference to tail node
        self._size += 1
        return self._make_position(node)

    def delete_first(self):
        """
        delete element at the end of the list and return the element
        :return:
        """
        if not self.is_empty():
            old_head = self._head
            element = old_head._element
            if old_head._next is not None:
                self._head = old_head._next
            else:
                self._head = self._tail = None
            self._size -= 1
            return element

    def add_first(self, element):
        """
        insert element at the front of the list and return new position
        :param element:
        :return:
        """
        node = self._Node(element, None)
        if self.is_empty():   # special case previously empty
            self._tail = node  # update reference to tail node
        else:
            old_head = self._head
            node._next = old_head
        self._head = node  # update reference to head node
        self._size += 1
        return self._make_position(node)

    def _add_after(self, predecessor, element):
        """
        add element after an existing nodes and return new node
        :param element:
        :param predecessor: node object
        :return:
        """
        successor = predecessor._next
        new_node = self._Node(element, predecessor)
        predecessor._next = new_node
        new_node._next = successor
        self._size += 1
        return self._make_position(new_node)

    def add_after(self, position, element):
        """
        insert element after a position
        :param position:
        :param element:
        :return:
        """
        predecessor = self._validate(position)
        return self._add_after(predecessor, element)

    def _delete_after(self, predecessor):
        """
        delete node from the list and return its element
        :param predecessor:
        :return:
        """
        node = predecessor._next
        successor = predecessor._next._next
        element = node._element
        predecessor._next = successor
        node._element = node._next = None  # deprecate node
        self._size -= 1
        return element

    def delete_after(self, position):
        predecessor = self._validate(position)
        if predecessor is not self._tail:
            return self._delete_after(predecessor)