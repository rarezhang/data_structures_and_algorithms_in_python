"""
Abstract base Binary Tree class
"""

from Tree import Tree

class BinaryTree(Tree):
    """
    abstract base class representing a binary tree structure
    """
    # -------------------- additional abstract methods ----------------------
    def left(self, position):
        """
        return a Position representing p's left child
        return None if p does not have left child
        :param position:
        :return:
        """
        raise NotImplementedError('must be implemented by subclass')

    def right(self, position):
        """
        return a Position representing p's right child
        return None if p does not have right child
        :param position:
        :return:
        """
        raise NotImplementedError('must be implemented by subclass')

    # ------------------ concrete methods ---------------------------
    def sibling(self, position):
        """
        return a Position representing p's sibling
        or None if no sibling
        :param position:
        :return:
        """
        parent = self.parent(position)
        if parent is None:  # position must be the root
            return None  # root has no sibling
        else:
            if position == self.left(parent):
                return self.right(parent)  # possibly None
            else:
                return self.left(parent)  # possibly None

    def children(self, position):
        """
        generate an iteration of Positions representing p's children
        :param position:
        :return:
        """
        if self.left(position) is not None:
            yield self.left(position)
        if self.right(position) is not None:
            yield self.right(position)

    # override inherited version to make inorder the default
    def positions(self):
        """
        generate an iteration of the tree's positions
        :return:
        """
        return self.inorder()  # make inorder the default

    def _subtree_inorder(self, position):
        """
        generate an inorder iteration of positions in subtree rooted at p
        :param position:
        :return:
        """
        if self.left(position) is not None:  # if left child exists, traverse its subtree
            for other in self._subtree_inorder(self.left(position)):
                yield other
        yield position  # visit position between its subtrees
        if self.right(position) is not None:  # if right child exists, traverse its subtree
            for other in self._subtree_inorder(self.right(position)):
                yield other

    def inorder(self):
        """
        generate an inorder iteration of positions in the ree
        :return:
        """
        if not self.is_empty():
            for p in self._subtree_inorder(self.root()):
                yield p
