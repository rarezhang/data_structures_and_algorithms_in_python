"""
base class for singly linked list
recursive version
reference: UC Berkeley CS61A
"""


class _SinglyLinkedBaseRecursive:
    """
    a base class for singly linked list
    recursive version
    """
    empty = ()

    def __init__(self, head, rest=empty):
        """

        :param head:
        :param rest:
        """
        assert rest is _SinglyLinkedBaseRecursive.empty or isinstance(rest, _SinglyLinkedBaseRecursive)
        self._head = head
        self._rest = rest

    def __getitem__(self, item):
        """
        implicit recursive
        :param item:
        :return:
        """
        if item == 0:
            return self._head
        else:
            return self._rest[item-1]  # will invoke the same __getitem__ method

    def __len__(self):
        """
        implicit recursive
        :return:
        """
        return 1 + len(self._rest)  # len(empty)=0

    def is_empty(self):
        """
        return True if the list is empty
        :return:
        """
        return len(self) == 0

    def __str__(self):
        """

        :return:
        """
        if self._rest:  # rest is not empty
            rest_str = ' ' + str(self._rest)
        else:  # rest is empty
            rest_str = ''
        return '{{ {0} {1}}}'.format(self._head, rest_str)

    def _extend(self, L, element):
        """
        help method for extend()
        :param L:
        :param element:
        :return:
        """
        if L is self.empty:
            return _SinglyLinkedBaseRecursive(element)
        else:
            return _SinglyLinkedBaseRecursive(self._head, self._extend(L._rest, element))

    def extend(self, element):
        """
        return link followed by new element
        :param element: new element
        :return:
        """
        return self._extend(self, element)

    def _map_link(self, L, fun):
        """
        helper function for map_link
        :return:
        """
        if L is self.empty:
            return L
        else:
            return _SinglyLinkedBaseRecursive(fun(L._head), self._map_link(L._rest, fun))

    def map_link(self, fun):
        """
        apply fun to each element of list
        :param fun:
        :return:
        """
        return self._map_link(self, fun)

    def _filter_link(self, L, fun):
        """
        helper function for filter_link
        :param L:
        :param fun:
        :return:
        """
        if L is self.empty:
            return L
        else:
            filtered = self._filter_link(L._rest, fun)
            if fun(L._head):
                return _SinglyLinkedBaseRecursive(L._head, filtered)
            else:
                return filtered

    def filter_link(self, fun):
        """
        return a link with element of link for which fun return true
        :param fun:
        :return:
        """
        return self._filter_link(self, fun)
