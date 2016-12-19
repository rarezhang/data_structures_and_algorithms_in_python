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
