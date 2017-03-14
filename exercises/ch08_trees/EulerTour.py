class EulerTour:
    """
    abstract base class for performing Euler tour of a tree
    _hook_previsit and _hook_postvisit may be overridden by subclasses
    """
    def __init__(self, tree):
        """
        prepare an Euler tour template for given tree
        :param tree:
        """
        self._tree = tree

    def tree(self):
        """
        return reference to the tree being traversed
        :return:
        """
        return self._tree

    def execute(self):
        """
        perform the tour and return any result from post visit of root
        :return:
        """
        if len(self._tree) > 0:
            return self._tour(self._tree.root(), 0, [])  # start the recursion

    def _tour(self, p, d, path):
        """
        perform tour of subtree rooted at position p
        :param p: Position of current node being visited
        :param d: depth of p in the tree
        :param path: list of indices of children on path from root to p
        :return:
        """
        self._hook_previsit(p, d, path)  # pre visit p
        results = []
        path.append(0)  # add new index to end of path before recursion
        for c in self._tree.children(p):
            results.append(self._tour(c, d+1, path))  # recur on child's subtree
            path[-1] += 1  # increment index
        path.pop()  # remove extraneous index from end of path
        answer = self._hook_postvisit(p, d, path, results)  # post visit p
        return answer

    def _hook_previsit(self, p, d, path):  # can be overridden
        pass

    def _hook_postvisit(self, p, d, path, results):  # can be overridden
        pass


class BinaryEulerTour(EulerTour):
    """
    abstract base class for performing Euler tour of a binary tree

    This version includes an additional _hook_invisit that is called after the tour
    of the left subtree if any, yet before the tour of the right subtree if any

    Note: right child is always assigned index 1 in path even if no left sibling
    """
    def _tour(self, p, d, path):
        results = [None, None]   # will update with results of recursions
        self._hook_previsit(p, d, path)  # pre visit for p
        if self._tree.left(p) is not None:  # consider left child
            path.append(0)
            results[0] = self._tour(self._tree.left(p), d+1, path)
            path.pop()
        self._hook_invisit(p, d, path)  # in visit for p
        if self._tree.right(p) is not None:  # consider right child
            path.append(1)
            results[1] = self._tour(self._tree.right(p), d+1, path)
            path.pop()
        answer = self._hook_postvisit(p, d, path, results)  # post visit p
        return answer

    def _hook_invisit(self, p, d, path):  # can be overridden
        pass