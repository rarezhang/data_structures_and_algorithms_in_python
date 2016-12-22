"""
Abstract base Tree class
"""
from LinkedQueue import LinkedQueue


class Tree:
    """
    Abstract base class representing a tree structure
    """
    #---------------------nested Position class --------------------------
    class Position:
        """
        an abstraction representing the location of a single element
        """
        def element(self):
            """
            return the element stored at the Position
            :return:
            """
            raise NotImplementedError('must be implemented by subclass')

        def __eq__(self, other):
            """
            return True if other Position represents the same location
            :param other:
            :return:
            """
            raise NotImplementedError('must be implemented by subclass')

        def __ne__(self, other):
            """
            return True if other does not represent the same location
            :param other:
            :return:
            """
            return not (self == other)  # opposite of __eq__

    # ---------- abstract methods that concrete subclass must support -------------------
    def root(self):
        """
        return Position representing the tree's root (or None if empty)
        :return:
        """
        raise NotImplementedError('must be implemented by subclass')

    def parent(self, position):
        """
        return Position representing the p's parent (or None if p is root)
        :param position:
        :return:
        """
        raise NotImplementedError('must be implemented by subclass')

    def num_children(self, position):
        """
        return the number of children that Posiiton p has
        :param position:
        :return:
        """
        raise NotImplementedError('must be implemented by subclass')

    def children(self, position):
        """
        generate an iteration of Positions representing p's children
        :param position:
        :return:
        """
        raise NotImplementedError('must be implemented by subclass')

    def __len__(self):
        """
        return the total number of elements in the tree
        :return:
        """
        raise NotImplementedError('must be implemented by subclass')

    # ------------- concrete methods implemented in this class ----------------------------
    def is_root(self, position):
        """
        return True if Position p represents the root of the tree
        :param position:
        :return:
        """
        return self.root() == position

    def is_leaf(self, position):
        """
        return True if Position does not have any children
        :param position:
        :return:
        """
        return self.num_children(position) == 0

    def is_empty(self):
        """
        return True if the tree is empty
        :return:
        """
        return len(self) == 0

    def depth(self, position):
        """
        return the number of levels separating Position from the root
        :param position:
        :return:
        """
        if self.is_root(position):
            return 0
        else:
            return 1 + self.depth(self.parent(position))

    def _height(self, position):
        """
        return the height of the subtree rooted at Position
        time is linear in size of subtree
        O(n)
        :param position:
        :return:
        """
        if self.is_leaf(position):
            return 0
        else:
            return 1 + max(self._height(c) for c in self.children(position))

    def height(self, position=None):
        """
        return the height of the subtree rooted at Position p
        :param position:
        :return:
        """
        if position is None:
            position = self.root()
        return self._height(position)

    def __iter__(self):
        """
        generate an iteration of the tree's elements
        :return:
        """
        for p in self.positions():  # use same order as positions
            yield p.element()  # yield each element

    def positions(self):
        """
        generate an iteration of the tree's positions
        :return:
        """
        return self.preorder()  # return entire pre-order iteration

    # ----------------- pre-order traversal --------------------------------
    def _subtree_preorder(self, position):
        """
        helper function for preorder
        generate a pre-order iteration of positions in subtree rooted at position
        :param position:
        :return:
        """
        yield position  # visit p before its subtrees
        for c in self.children(position):  # for each child
            for other in self._subtree_preorder(c):  # do preorder of child's subtree
                yield other

    def preorder(self):
        """
        generate a preorder iteration fo positions in the tree
        :return:
        """
        if not self.is_empty():
            for p in self._subtree_preorder(self.root()):  # start recursion
                yield p

    # ----------------- post-order traversal --------------------------------
    def _subtree_postorder(self, position):
        """
        generate a postorder iteration of positions in subtree rooted at position
        :param position:
        :return:
        """
        for c in self.children(position):  # for each child c
            for other in self._subtree_postorder(c):  # postorder of child's subtree
                yield other  # yielding each to our caller
            yield position  # visit p after its subtrees

    def posordre(self):
        """
        generate a postorder iteration of positions in the tree
        :return:
        """
        if not self.is_empty():
            for p in self._subtree_postorder(self.root()):  # start recursion
                yield p

    def breadthfirst(self):
        """
        generate a breadth-first iteration of the positions of the tree
        :return:
        """
        if not self.is_empty():
            fringe = LinkedQueue()  # known positions not yet yielded
            fringe.enqueue(self.root())  # starting with the root
            while not fringe.is_empty():
                p = fringe.dequeue()  # remove from front of the queue
                yield p  # report this position
                for c in self.children(p):
                    fringe.enqueue(c)  # add children to back of queue

