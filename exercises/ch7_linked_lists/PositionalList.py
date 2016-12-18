from DoublyLinkedBase import _DoublyLinkedBase


class PositionalList(_DoublyLinkedBase):
    """
    a sequential container of elements allowing positional access
    """

    ##################### nested Position class ########################
    class Position:
        """
        an abstraction representing the location af a single element
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
            return True if other is a position representing the same location
            :param other:
            :return:
            """
            return type(other) is type(self) and other._node is self._node

        def __ne__(self, other):
            """
            return True if other does not represent the same location
            :param other:
            :return:
            """
            return not (self == other)  # == -> __eq__ ==> __ne__ opposite of __eq__

    ##################### nested Position class ########################

    # ------------------------------- utility method -------------------------------
    def _validate(self, position):
        """
        return position's node,
        or raise appropriate error if invalide
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
        return Position instance for given node (or None if sentinel)
        :param node:
        :return:
        """
        if node is self._header or node is self._trailer:
            return None   # boundary violation
        else:
            return self.Position(self, node)   # legitimate position

    # ------------------------------- accessors -------------------------------
    def first(self):
        """
        return the first Position in the list (or None if list is empty)
        :return:
        """
        return self._make_position(self._header._next)

    def last(self):
        """
        return the last Position in the list (or None if list is empty)
        :return:
        """
        return self._make_position(self._trailer._prev)

    def before(self, position):
        """
        return the Position just before Position -> position (or None if position is first)
        :param position:
        :return:
        """
        node = self._validate(position)
        return self._make_position(node._prev)

    def after(self, position):
        """
        return the Position just after position (or None if position is last)
        :param position:
        :return:
        """
        node = self._validate(position)
        return self._make_position(node._next)

    def __iter__(self):
        """
        generate a forward iteration of the elements of the list
        :return:
        """
        cursor = self.first()
        while cursor is not None:
            yield cursor.element()
            cursor = self.after(cursor)



    # ------------------------------- mutators -------------------------------
    # override inherited version to return Position, rather than Node
    def _insert_between(self, element, predecessor, successor):
        """
        add element between existing nodes and return new Position
        :param element:
        :param predecessor:
        :param successor:
        :return:
        """
        node = super()._insert_between(element, predecessor, successor)
        return self._make_position(node)

    def add_first(self, element):
        """
        insert element at the front of the list and return new Position
        :param element:
        :return:
        """
        return self._insert_between(element, self._header, self._header._next)

    def add_last(self, element):
        """
        insert element at the back of the list and return new Position
        :param element:
        :return:
        """
        return self._insert_between(element, self._trailer._prev, self._trailer)

    def add_before(self, position, element):
        """
        insert element into list before Position and return new Position
        :param position:
        :param element:
        :return:
        """
        original = self._validate(position)  # return position._node
        return self._insert_between(element, original._prev, original)  # return self._make_position(node)

    def add_after(self, position, element):
        """
        insert element into list after Position and return new Position
        :param position:
        :param element:
        :return:
        """
        original = self._validate(position)
        return self._insert_between(element, original, original._next)

    def delete(self, position):
        """
        remove and return the element at position
        :param position:
        :return:
        """
        original = self._validate(position)  # return position._node
        return self._delete_node(original)  # inherited method form DoublyLinkedBase: return element

    def replace(self, position, element):
        """
        replace the element at position with element
        return the element formerly at position
        :param position:
        :param element:
        :return:
        """
        original = self._validate(position)  # return position._node
        old_value = original._elment  # temporarily store old element
        original._element = element  # replace with new element
        return old_value  # return the old element value




