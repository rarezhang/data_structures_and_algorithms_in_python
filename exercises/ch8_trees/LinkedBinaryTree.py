"""
linked representation of binary tree
"""


from BinaryTree import BinaryTree


class LinkedBinaryTree(BinaryTree):
    """
    linked representation of a binary tree structure
    """

    class _Node:
        """
        lightweight, nonpublic class for storing a node
        """
        __slots__ = '_element', '_parent', '_left', '_right'

        def __init__(self, element, parent=None, left=None, right=None):
            """

            :param element:
            :param parent:
            :param left:
            :param right:
            """
            self._element = element
            self._parent = parent
            self._left = left
            self._right = right

    class Position(BinaryTree.Position):
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
            return type(other) is type(self) and other._node is self._node

    def _validate(self, position):
        """
        return associated node, if position is valid
        :param position:
        :return:
        """
        if not isinstance(position, self.Position):
            raise TypeError('position must be proper Position type')
        if position._container is not self:
            raise  ValueError('position does not belong to this container')
        if position._node._parent is position._node:  # convention for deprecated nodes
            raise ValueError('position is o longer valid')
        return position._node

    def _make_position(self, node):
        """
        return position instance for given node
        or None if no node
        :param node:
        :return:
        """
        return self.Position(self, node) if node is not None else None

    # --------------------- binary tree constructor -------------------------
    def __init__(self):
        """
        create an initially empty binary tree
        """
        self._root = None
        self._size = 0

    # -------------------- public accessors -----------------------------------
    def __len__(self):
        """
        return the total number of elements in the tree
        :return:
        """
        return self._size

    def root(self):
        """
        return the root Position of the tree (or None if tree is empty)
        :return:
        """
        return self._make_position(self._root)

    def parent(self, position):
        """
        return the Position of p's parent
        or None if p is root
        :param position:
        :return:
        """
        node = self._validate(position)  # return node at position
        return self._make_position(node._parent)

    def left(self, position):
        """
        return the position of p's left child
        or None if no left child
        :param position:
        :return:
        """
        node = self._validate(position)
        return self._make_position(node._left)

    def right(self, position):
        """
        return the position of p's right child
        or none if no right child
        :param position:
        :return:
        """
        node = self._validate(position)
        return self._make_position(node._right)

    def num_children(self, position):
        """
        return the number of children of Position p
        :param position:
        :return:
        """
        node = self._validate(position)  # return node at position
        count = 0
        if node._left is not None:  # left child exists
            count += 1
        if node._right is not None:  # right child exists
            count += 1
        return count

    def _add_root(self, element):
        """
        place element at the root of an empty tree and return new Position
         raise ValueError if tree nonempty
        :param element:
        :return:
        """
        if self._root is not None: raise ValueError('root exists')
        self._size = 1
        self._root = self._Node(element)
        return self._make_position(self._root)

    def _add_left(self, position, element):
        """
        create a new left child for Position, storing element
        return the Position of new node
        raise ValueError if Position is invalid or already has a left child
        :param position:
        :param element:
        :return:
        """
        node = self._validate(position)  # return node at position
        if node._left is not None:
            raise ValueError('Left child exists')
        self._size += 1
        node._left = self._Node(element, node)  # Node->element, parent=None, left=None, right=None)
        return self._make_position(node._left)

    def _add_right(self, position, element):
        """
        create a new right child for position, storing element
        return the Position of new node
        Raise ValueError if Position is invalid or already has a right child
        :param position:
        :param element:
        :return:
        """
        node = self._validate(position)  # return node at position
        if node._right is not None:
            raise ValueError('right child exists')
        self._size += 1
        node._right = self._Node(element, node)  # Node->element, parent=None, left=None, right=None)
        return self._make_position(node._right)

    def _replace(self, position, element):
        """
        replace the element at position wit element and return old element
        :param position:
        :param element:
        :return:
        """
        node = self._validate(position)
        old = node._element
        node._element = element
        return old

    def _delete(self, position):
        """
        delete the node at position and replace it with its child (if only one child) if any
        return the element that had been stored at position
        :param position:
        :return:
        """
        node = self._validate(position)
        if self.num_children(position) == 2:
            raise ValueError('position has two children')
        child = node._left if node._left else node._right
        if child is not None:
            child._parent = node._parent  # child's grandparent becomes parent
        if node is self._root:
            self._root = child  # child becomes root
        else:
            parent = node._parent
            if node is parent._left:
                parent._left = child
            else:
                parent._right = child
        self._size -= 1
        node._parent = node  # convention for deprecated node
        return node._element

    def _attach(self, position, t1, t2):
        """
        attach trees t1 and t2 as left and right sub-trees of external position
        :param position:
        :param t1:
        :param t2:
        :return:
        """
        node = self._validate(position)
        if not self.is_leaf(position):
            raise ValueError('position must be leaf')
        self._size += len(t1) + len(t2)
        if not t1.is_empty():  # attach t1 as left subtree of node
            t1._root._parent = node
            node._left = t1._root
            t1._root = None  # set t1 instance to empty
            t1._size = 0
        if not t2.is_empty():  # attach t2 as right subtree of node
            t2._root._parent = node
            node._right = t2._root
            t2._root = None  # set t2 instance to empty
            t2._size = 0
