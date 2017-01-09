"""
TreeMap class based on a binary search tree
"""

import sys, os
sys.path.append(os.path.abspath("D:\\Projects\\data_structures_and_algorithms_in_python\\exercises\\ch8_trees"))
from LinkedBinryTree import LinkedBinaryTree
sys.path.append(os.path.abspath("D:\Projects\data_structures_and_algorithms_in_python\exercises\ch10_maps_hashtables_skiplists"))
from MapBase import MapBase
sys.path.append(os.path.abspath("D:\Projects\data_structures_and_algorithms_in_python\exercises\ch7_linked_lists"))
from Excep import Empty

class TreeMap(LinkedBinaryTree, MapBase):
    """
    sorted map implementation using a binary search tree
    """

    # -------------- override Position class ------------------------
    class Position(LinkedBinaryTree.Position):
        """
        override Position class from LinkedBinaryTree
        """
        def key(self):
            """
            return key of map's key-value pair
            :return:
            """
            return self.element()._key

        def value(self):
            """
            return value of map's key-value pair
            :return:
            """
            return self.elment()._value

    # -------------- nonpublic method -----------------------------
    def _subtree_search(self, p, k):
        """
        return position of p's subtree having key k
        or last node searched
        :param p:
        :param k:
        :return:
        """
        if k == p.key():   # find match
            return p
        elif k < p.key():  # search left subtree
            if self.left(p) is not None:
                return self._subtree_search(self.left(p), k)
        else:  # k > p.key() ->  search right subtree
            if self.right(p) is not None:
                return self._subtree_search(self.right(p), k)
        return p   # unsuccessful search, return last node searched

    def _subtree_first_position(self, p):
        """
        return Position of first item in subtree rooted at p
        :param p:
        :return:
        """
        walk = p
        while self.left(walk) is not None:  # keep walking left
            walk = self.left(walk)
        return walk

    def _subtree_last_position(self, p):
        """
        return Position of last item in subtree rooted at p
        :param p:
        :return:
        """
        walk = p
        while self.right(walk) is not None:  # keep walking right
            walk = self.right(walk)
        return walk

    def first(self):
        """
        return the first Position in the tree
        or None if empty
        :return:
        """
        return self._subtree_first_position(self.root()) if len(self) > 0 else None

    def last(self):
        """
        return the last Position in the tree
        or None if empty
        :return:
        """
        return self._subtree_last_position(self.root()) if len(self) > 0 else None

    def before(self, p):
        """
        return the Position just before p in the natural order
        return None if p is the first position
        :param p:
        :return:
        """
        self._validate(p)  # inherited from LinkedBinaryTree
        if self.left(p):
            return self._subtree_last_position(self.left(p))
        else:  # walk upward
            walk = p
            above = self.parent(walk)
            while above is not None and walk == self.left(above):
                walk = above
                above = self.parent(walk)
            return above

    def after(self, p):
        """
        return the Position just after p in the natural order
        return None if p is the last position
        :param p:
        :return:
        """
        self._validate(p)  # inherited from LinkedBinaryTree
        if self.right(p):
            return self._subtree_first_position(self.right(p))
        else:  # walk upward
            walk = p
            above = self.parent(walk)
            while above is not None and walk == self.right(above):
                walk = above
                above = self.parent(walk)
        return above

    def find_position(self, k):
        """
        return position with key k or else neighbor
        or None if empty
        :param k:
        :return:
        """
        if self.is_empty():
            return None
        else:
            p = self._subtree_search(self.root(), k)  # find match or last node searched
            self._rebalance_access(p)  # hook for balanced tree subclasses
            return p

    def find_min(self):
        """
        return (key,value) pair with minimum key (or None if empty)
        :return:
        """
        if self.is_empty():
            return None
        else:
            p = self.first()
            return (p.key(), p.value())

    def find_ge(self, k):
        """
        return (key, value) pair with least key greater than or equal to k
        return None if there does not exist such a key
        :param k:
        :return:
        """
        if self.is_empty():
            return None
        else:
            p = self.find_position(k)  # may not find exact match
            if p.key() < k:
                p = self.after(p)
            return (p.key(), p.value()) if p is not None else None

    def find_range(self, start, stop):
        """
        iterate all (key,value) pairs such that start <= key <= stop
        if start is None, iteration begins with minimum key of map
        if stop is None, iteration continues through the maximum key of map
        :param start:
        :param stop:
        :return:
        """
        if not self.is_empty():
            if start is None:
                p = self.first()
            else:  # initialize p with logic similar to find_ge
                p = self.find_position(start)
                if p.key() < start:
                    p = self.after(p)
            while p is not None and (stop is None or p.key() < stop):
                yield (p.key(), p.value())
                p = self.after(p)

    # ------------- public method -------------------------
    def __getitem__(self, k):
        """
        return value associated with key k
        raise KeyError if not found
        :param k:
        :return:
        """
        if self.is_empty():
            raise Empty('the tree/map is empty')
        else:
            p = self._subtree_search(self.root(), k)  # find match or last node searched
            self._rebalance_access(p)  # hook for balanced tree subclasses
            if k != p.key():
                raise KeyError('Key Error: ' + repr(k))
            return p.value()

    def __setitem__(self, k, v):
        """
        assign value v to key k, overwriting existing value if present
        :param k:
        :param v:
        :return:
        """
        if self.is_empty():
            leaf = self._add_root(self._Item(k,v))  # from LinkedBinaryTree
        else:
            p = self._subtree_search(self.root(), k)  # find match or last node searched
            if p.key() == k:  # find existing node
                p.element()._value = v  # replace existing items's value
                self._rebalance_access(p)  # hook for balanced tree subclasses
                return
            else:  # no existing node
                item = self._Item(k,v)
                if p.key() < k:
                    leaf = self._add_right(p, item)  # from LinkedBinaryTree
                else:
                    leaf = self._add_left(p, item)
        self._rebalance_insert(leaf)  # hook for balanced tree subclasses

    def __iter__(self):
        """
        generate an iteration of all keys in the map in order
        :return:
        """
        p = self.first()
        while p is not None:
            yield p.key()
            p = self.after(p)

    def delete(self, p):
        """
        remove the item at given Position
        :param p:
        :return:
        """
        self._validate(p)  # from LinkedBinaryTree
        if self.left(p) and self.right(p):  # p has two children
            replacement = self._subtree_last_position(self.left(p))
            self._replace(p, replacement.element())   # from LinkedBinaryTree
            p = replacement
        # now p has at most one child
        parent = self.parent(p)
        self._delete(p)
        self._rebalance_delete(parent)  # if root deleted, parent is None

    def __delitem__(self, k):
        """
        remove item associated with key k
        raise KeyError if not found
        :param k:
        :return:
        """
        if not self.is_empty():
            p = self._subtree_search(self.root(), k)
            if k == p.key():
                self.delete(p)  # rely on positional version
                return  # successful deletion complete
            self._rebalance_access(p)   # hook for balanced tree subclasses
        raise KeyError('Key Error: ' + repr(k))
    