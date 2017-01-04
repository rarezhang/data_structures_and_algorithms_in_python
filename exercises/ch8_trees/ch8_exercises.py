"""
ch8 exercises
"""

from BinaryTree import BinaryTree

# R-8.1
# The following questions refer to the tree of Figure 8.3.
# Figure 8.3: P 324
# a. Which node is the root?
# /user/rt/courses/

# b. What are the internal nodes?
# internal nodes: if it has one or more children: cs016/, cs252/, homework/, programs/, projects/, papers/ demos/

# c. How many descendants does node cs016/ have?
# node v is a descendant of a node u if u is an ancestor of v
# node u is an ancestor of a node v if u = v or u is an ancestor of the parent of v
# cs016/ has 10 descendants

# d. How many ancestors does node cs016/ have?
# cs016/ has 2 ancestors

# e. What are the siblings of node homework/?
# two nodes that are children of the same parent are siblings
# homework/ has 2 siblings

# f. Which nodes are in the subtree rooted at node projects/?
# /projects, /papers, /demos, buylow, sellhigh, market

# g. What is the depth of node papers/?
# depth of a position (p): the number of ancestors of p, excluding p itself
# depth of node papers/: 3

# h. What is the height of the tree?
# height(T) == max(depth(leaf))
# height of the tree: 4


# R-8.5
# Describe an algorithm, relying only on the BinaryTree operations, that
# counts the number of leaves in a binary tree that are the left child of their
# respective parent.
def count_left_child(T):
    """
    relying only on the BinaryTree operations
    :param T: binary tree
    :return:
    """
    assert isinstance(T, BinaryTree)
    count = 0
    pos = T.positions()  # generate an iteration of the tree's positions
    for p in pos:
        if p.left() is not None:
            # return a Position representing p's left child
            # return None if p does not have left child
            count += 1
    return count

# R-8.6
# Let T be an n-node binary tree that may be improper. Describe how to
# represent T by means of a proper binary tree T' with O(n) nodes.

# proper binary tree (full binary tree): each node has either zero or two children
# R-8.6) Consider using dummy nodes.
def proper_tree(T):
    """

    :param T:
    :return:
    """
    def add_dummy(position):
        pass

    assert isinstance(T, BinaryTree)
    pos = T.positions()  # generate an iteration of the tree's positions
    for p in pos:
        if (p.left() is not None) and (p.right() is None):
            add_dummy(p)  # add a dummy node as the right child
    return

# R-8.7
# What are the minimum and maximum number of internal and external
# nodes in an improper _binary tree_ with n nodes?

# internal nodes: if it has one or more children
# minimum: cell[(n-1)/2]  (a proper tree)
# maximum: n-1 (linked list)

# v is external if v has no children (known as leaves)
# minimum: 1 (linked list)
# maximum: floor[(n+1)/2]  (a proper tree)

# Proposition 8.8:
# T: a nonempty binary tree
# n: number of nodes
# nE: number of external nodes
# nI: number of internal nodes
# h: height of T
# T has following properties
# 1. h + 1 ≤ n ≤ 2^(h + 1) − 1
# 2. 1 ≤ nE ≤ 2^h
# 3. h ≤ nI ≤ 2^h − 1
# 4. log(n+1)− 1 ≤ h ≤ n − 1
# Also,if T is proper,then T has the following properties:
# 1. 2h + 1 ≤ n ≤ 2^(h+1) − 1
# 2. h + 1 ≤ nE ≤ 2^h
# 3. h ≤ nI ≤ 2^h − 1
# 4. log(n+1)− 1 ≤ h ≤ ( n − 1 )/ 2

# R-8.8
# Answer the following questions so as to justify Proposition 8.8.
# a. What is the minimum number of external nodes for a proper binary
# tree with height h? Justify your answer.

# b. What is the maximum number of external nodes for a proper binary
# tree with height h? Justify your answer.
# 2^h