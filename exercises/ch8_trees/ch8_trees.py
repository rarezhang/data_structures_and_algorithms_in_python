"""
ch8 trees
"""
from LinkedBinaryTree import LinkedBinaryTree
from EulerTour import EulerTour, BinaryEulerTour

# applications of tree traversals
# create a tree
T = LinkedBinaryTree()
root = T._add_root('Electronics RUs')  # return position
ch1 = T._add_left(root, 'R&D')
ch2 = T._add_right(root, 'Sales')
ch21 = T._add_left(ch2, 'Domestic')
ch22 = T._add_right(ch2, 'International')
ch221 = T._add_left(ch22, 'Canada')
ch222 = T._add_right(ch22, 'America')


# P 359
# table of contents
# When using a tree to represent the hierarchical structure of a document, a preorder
# traversal of the tree can naturally be used to produce a table of contents for the document.
def preorder_indent(T, position, depth):
    """
    print preorder representation of subtree of T rooted at position at depth d
    :param T:
    :param position:
    :param depth:
    :return:
    """
    if not T.is_empty():
        print(2 * depth * ' ' + str(position.element()))  # use depth for indentation
        for c in T.children(position):
            preorder_indent(T, c, depth+1)  # child depth is d+1


preorder_indent(T, T.root(), 0)  # depth start with 0
# Electronics RUs
#   R&D
#   Sales
#     Domestic
#     International
#       Canada
#       America


# P361
#  Efficient recursion for printing an indented and labeled presentation
#  of a preorder traversal.
def preorder_label(T, p, d, path):
    """
    print labeled representation of subtree of T rooted at p at depth d
    :param T: tree
    :param p: position
    :param d: depth
    :param path:  share the same list instance throughout the recursion.
    :return:
    """
    label = '.'.join(str(j+1) for j in path)  # displayed labels are on-indexed
    print(2*d*' ' + label, p.element())
    path.append(0)
    for c in T.children(p):
        preorder_label(T, c, d+1, path)  # child depth: d+1
        path[-1] += 1
    path.pop()   # v.s. path.append(0)


preorder_label(T, T.root(), 0, [])
#  Electronics RUs
#   1 R&D
#   2 Sales
#     2.1 Domestic
#     2.2 International
#       2.2.1 Canada
#       2.2.2 America


# P 361
# parenthetic representations of a tree
def parenthesize(T, position):
    """
    print parenthesized representation of subtree of T
    rooted at position
    :param T:
    :param position:
    :return:
    """
    print(position.element(), end='')  # use of end avoids trailing newline
    if not T.is_leaf(position):
        first_time = True
        for c in T.children(position):
            sep = ' (' if first_time else ', '  # determine proper separator
            print(sep, end='')
            first_time = False   # any future passes will not be the first
            parenthesize(T, c)  # recur on child
        print(')', end='')  # include closing parenthesis


parenthesize(T, T.root())
# Electronics RUs (R&D, Sales (Domestic, International (Canada, America)))


# P 362
# disk space: postorder traversal
# children returns information to the parent
# Recursive computation of disk space for a tree. We assume
# that a space() method of each tree element reports the local space used at that
# position.
def disk_space(T, p):
    """
    return total disk space for subtree of T rooted at p
    :param T:
    :param p:
    :return:
    """
    subtotal = p.element().space()  # space used at position p
    for c in T.children(p):
        subtotal += disk_space(T, c)  # add child's space to subtotal
    return subtotal


# P 366 - P 367
# using the Euler tour Framework
class PreorderPrintIndentedTour(EulerTour):
    def _hook_previsit(self, p, d, path):
        print(2*d*' '+str(p.element))

tour = PreorderPrintIndentedTour(T)
tour.execute()


class PreorderPrintIndentedLabeledTour(EulerTour):
    def _hook_previsit(self, p, d, path):
        label = '.'.join(str(j+1) for j in path)  # labels are one-indexed
        print(2*d*' ' + label, p.element())

tour = PreorderPrintIndentedLabeledTour(T)
tour.execute()


class ParenthesizeTour(EulerTour):
    def _hook_previsit(self, p, d, path):
        if path and path[-1] > 0:  # p follows a sibling
            print(', ', end='')  # so preface with comma
        print(p.element(), end='')  # then print element
        if not self.tree().is_leaf(p):  # if p has children
            print(' (', end='')  # print opening parenthesis

    def _hook_postvisit(self, p, d, path, results):
        if not self.tree().is_leaf(p):  # if p has children
            print(')', end='')

tour = ParenthesizeTour(T)
tour.execute()


class DiskSpaceTour(EulerTour):
    def _hook_postvisit(self, p, d, path, results):
        """
        simply add space associated with p to that of its subtrees
        :param p:
        :param d:
        :param path:
        :param results:
        :return:
        """
        return p.element().space() + sum(results)


# P 369
class BinaryLayout(BinaryEulerTour):
    """
    class for computing (x,y) coordinates for each node of a binary tree
    """
    def __init__(self, tree):
        super().__init__(tree)  # must call the parent constructor
        self._count = 0  # initialize count of processed nodes

    def _hook_invisit(self, p, d, path):
        p.element().setX(self._count)  # x-coordinate serialized by count
        p.element().setY(d)  # y-coordinate is depth
        self._count += 1  # advance count of processed nodes

bl = BinaryLayout(T)
