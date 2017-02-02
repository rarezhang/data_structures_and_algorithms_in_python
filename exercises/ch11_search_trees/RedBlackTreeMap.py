"""
red black tree map
"""

from TreeMap import TreeMap

class RedBlackTreeMap(TreeMap):
    """
    sorted map implementation using a red-black tree
    """

    class _Node(TreeMap._Node):
        """
        node class for red-black tree maintains bit that denotes color
        """
        __slots__ = '_red'  # add additional data member to the Node class

        def __init__(self, element, parent=None, left=None, right=None):
            """

            :param element:
            :param parent:
            :param left:
            :param right:
            """
            super().__init__(element, parent, left, right)
            self._red = True  # new node red by default

    # -------------------- positional-based utility methods --------------------
    # consider a non-existent child to be trivially black
    def _set_red(self, p):
        """

        :param p: position
        :return:
        """
        p._node._red = True

    def _set_black(self, p):
        """

        :param p: position
        :return:
        """
        p._node._black = False

    def _set_color(self, p, make_red):
        """

        :param p:
        :param make_red:
        :return:
        """
        p._node._red = make_red

    def _is_red(self, p):
        """

        :param p: position
        :return:
        """
        return p is not None and p._node._red

    def _is_red_leaf(self, p):
        """

        :param p: position
        :return:
        """
        return self._is_red(p) and self.is_leaf(p)

    def _get_red_child(self, p):
        """
        return a red child of p or None if no such child
        :param p:
        :return:
        """
        for child in (self.left(p), self.right(p)):
            if self._is_red(child):
                return child
        return None

    # ----------------- support for insertions -----------------------
    # insert x: if x is the only node -> root -> black; else color x red
    # double red at node x: violate "red property" -> red property: the children of a red node are black
    def _rebalance_insert(self, p):
        """

        :param p:
        :return:
        """
        self._resolve_red(p)  # new node is always red

    def _resolve_red(self, p):
        """

        :param p:
        :return:
        """
        if self.is_root(p):
            self._set_black(p)   # make root black
        else:
            parent = self.parent(p)
            if self._is_red(parent):  # double red problem
                uncle = self.sibling(parent)
                if not self._is_red(uncle):  # case 1: misshapen 4 nodes
                    middle = self._restructure(p)  # do tri-node restructuring
                    self._set_black(middle)
                    self._set_red(self.left(middle))
                    self._set_red(self.right(middle))
                else:   # overfull 5 nodes
                    grand = self.parent(parent)
                    self._set_red(grand)  # grandparent becomes red
                    self._set_black(self.left(grand))
                    self._set_black(self.right(grand))
                    self._resolve_red(grand)