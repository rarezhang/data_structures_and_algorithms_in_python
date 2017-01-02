"""
ch8 exercises
"""

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
