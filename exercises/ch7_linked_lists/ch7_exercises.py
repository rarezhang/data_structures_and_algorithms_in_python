"""
ch7 exercises
"""

from LinkedQueue import LinkedQueue
from LinkedStack import LinkedStack
from CircularQueue import CircularQueue
from LinkedDeque import LinkedDeque
from PositionalList import PositionalList
import random


# R-7.1
# Give an algorithm for finding the second-to-last node in a singly linked
# list in which the last node is indicated by a next reference of None
# create a singly linked queue
def second_to_last(SL):
    """
    find the second-to-last node in a singly linked queue or stack
    :param SL: singly linked queue or stack
    :return:
    """
    assert isinstance(SL, (LinkedQueue, LinkedStack)), 'should be a singly linked queue or stack'
    current = None
    for i in SL:
        pre_current = current
        current = i
    return pre_current

q = LinkedQueue()
s = LinkedStack()
for i in range(5):
    q.enqueue(i)
    s.push(i)
print(q, s)
print(second_to_last(q), second_to_last(s))


# R-7.2
# Describe a good algorithm for concatenating two singly linked lists L and
# M, given only references to the first node of each list, into a single list LL
# that contains all the nodes of L followed by all the nodes of M.
def concatenate_linked_list(L, M):
    """

    :param L: singly linked lists
    :param M: singly linked lists
    :return:
    """
    assert isinstance(L, (LinkedQueue, LinkedStack)) and isinstance(M, (LinkedQueue, LinkedStack))
    cursor = L._head
    while cursor != None:
        pre = cursor
        cursor = cursor._next
    pre._next = M._head
    return L


l = LinkedQueue()
for i in range(5): l.enqueue(i)
m = LinkedQueue()
for i in range(3): m.enqueue(i)
print("L:", l)
print("M:", m)
print("L+M:", concatenate_linked_list(l, m))


# R-7.3
# Describe a recursive algorithm that counts the number of nodes in a singly
# linked list.
def recursive_count(L):
    """

    :param L: singly linked list
    :return:
    """
    assert isinstance(L, (LinkedQueue, LinkedStack))

    def _recursive_count(node):
        """
        Consider passing a node as a parameter.
        :param node:
        :return:
        """
        if node is None:
            return 0
        else:
            return 1 + _recursive_count(node._next)

    n = L._head
    return _recursive_count(n)


print("size L:", len(l))
print("recursive_count:", recursive_count(l))


# R-7.5
# Implement a function that counts the number of nodes in a circularly linked list.
def counts_circularly_list(C):
    """
    counts the number of nodes in a circularly linked list.
    :param C: circularly linked list
    :return: the number of nodes
    """
    assert isinstance(C, CircularQueue)
    count = 1  # tail count 1
    cursor = C._tail._next  # head node
    while cursor is not C._tail:
        count += 1
        cursor = cursor._next
    return count


c = CircularQueue()
for i in range(5): c.enqueue(i)
print("size C:", len(c))
print("number of nodes in C:", counts_circularly_list(c))


# Suppose that x and y are references to nodes of circularly linked lists,
# although not necessarily the same list. Describe a fast algorithm for telling
# if x and y belong to the same list
def select_node(C):
    """
    select a random node from a circularly linked list
    :param C: circularly linked list
    :return:
    """
    assert isinstance(C, CircularQueue)
    node = C._tail
    for _ in range(random.randrange(len(C))):
        node = node._next
    return node


def same_circular_list(C1, C2):
    """

    :param C1: circularly linked list
    :param C2: circularly linked list
    :return: True if two nodes are from the same list
    """
    def loop_circular_list(C, node):
        """

        :param C: circularly linked list
        :param node:
        :return:
        """
        flag = False
        cursor = C._tail._next  # head node
        while cursor is not C._tail:  # all nodes except tail node
            if cursor is node:
                flag = True
                return flag
            cursor = cursor._next
        if cursor is node: flag = True   # tail node
        return flag

    assert isinstance(C1, CircularQueue) and isinstance(C2, CircularQueue)
    # x and y are references to nodes of circularly linked lists
    x = select_node(C1)
    y = select_node(C2)
    if len(C1) < len(C2):
        result = loop_circular_list(C1, y)
    else:
        result = loop_circular_list(C2, x)
    return result

c = CircularQueue()
for i in range(5): c.enqueue(i)
d = CircularQueue()
for i in range(10): d.enqueue(i)
print("same circularly linked list:", same_circular_list(c, c))
print("different circularly linked list:", same_circular_list(c, d))


# R-7.7
# Our CircularQueue class of Section 7.2.2 provides a rotate() method that
# has semantics equivalent to Q.enqueue(Q.dequeue()), for a nonempty
# queue. Implement such a method for the LinkedQueue class of Section
# 7.1.2 without the creation of any new nodes.
q = LinkedQueue()
for i in range(5): q.enqueue(i)
print(q)
q.rotate()
print(q)


# R-7.8
# Describe a non-recursive method for finding, by link hopping, the middle
# node of a doubly linked list with header and trailer sentinels. In the case
# of an even number of nodes, report the node slightly left of center as the
# “middle.” (Note: This method must only use link hopping; it cannot use a
# counter.) What is the running time of this method?
def find_middle_node(D):
    """

    :param D: doubly linked list
    :return: middle node or node slightly left of center for even number of nodes
    """
    assert isinstance(D, LinkedDeque)
    if not D.is_empty():
        front = D._header._next
        back = D._trailer._prev
        # odd number of node: front._next != back._prev
        # even number of node: front._next != back
        while front._next != back._prev and front._next != back:
            front, back = front._next, back._prev
        return back._prev._element


d = LinkedDeque()
for i in range(5): d.insert_last(i)
print(d, "middle node:", find_middle_node(d))
d = LinkedDeque()
for i in range(4): d.insert_last(i)
print(d, "middle node:", find_middle_node(d))
d = LinkedDeque()
print(d, "middle node:", find_middle_node(d))


# R - 7.9
# Give a fast algorithm for concatenating two doubly linked lists L and M,
# with header and trailer sentinel nodes, into a single list LL
def concatenate_doubly_linked_list(L, M):
    """

    :param L: doubly linked list
    :param M: doubly linked list
    :return:
    """
    assert isinstance(L, LinkedDeque) and isinstance(M, LinkedDeque)
    L_last, M_first = L._trailer._prev, M._header._next
    L_last._next, M_first._prev = M_first, L_last
    L._trailer = M._trailer
    # L._trailer._prev, M._header._next, L._trailer, M._header = None
    return L

l = LinkedDeque()
for i in range(4): l.insert_last(i)
m = LinkedDeque()
for i in range(5): m.insert_last(i)
print("L+M", concatenate_doubly_linked_list(l, m))


# R-7.10
# There seems to be some redundancy in the repertoire of the positional
# list ADT, as the operation L.add first(e) could be enacted by the alter-
# native L.add before(L.first(), e). Likewise, L.add last(e) might be per-
# formed as L.add after(L.last(), e). Explain why the methods add first
# and add last are necessary.
pp = PositionalList()
pp.add_first(1)
# if PositionalList is empty, raise TypeError('position must be proper Position type')
pp.add_before(pp.first(), 2)
print(pp)


# R-7.11
# Implement a function, with calling syntax max(L), that returns the maximum
# element from a PositionalList instance L containing comparable
# elements.
def max_PositionalList(L):
    """
    return the maximum element from a PositionalList
    :param L:
    :return:
    """
    if not L.is_empty():
        cursor = L.first()  # return the first position in the list
        max_element = cursor.element()
        while cursor is not None:
            if cursor.element() > max_element:   # element() return the element stored at this position
                max_element = cursor.element()
            cursor = L.after(cursor)  # return position after cursor
        return max_element


pp = PositionalList()
print(pp, "max:", max_PositionalList(pp))  # empty list
for _ in range(10):
    pp.add_first(random.randint(0, 100))
print(pp, "max:", max_PositionalList(pp))


# R-7.12
# Redo the previously problem with max as a method of the PositionalList
# class, so that calling syntax L.max() is supported.
pp = PositionalList()
print(pp, "max:", pp.max())  # empty list
for _ in range(10):
    pp.add_first(random.randint(0, 100))
print(pp, "max:", pp.max())

# recursion version
pp = PositionalList()
print(pp, "max:", pp.max_recursion())  # empty list
for _ in range(5):
    pp.add_first(random.randint(0, 100))
print(pp, "max:", pp.max_recursion().element())


# R-7.13
# Update the PositionalList class to support an additional method ﬁnd(e),
# which returns the position of the (first occurrence of) element e in the list
# (or None if not found).
e = 3
pp = PositionalList()
print(pp, "find {}:".format(e), pp.find(e))  # empty list
for _ in range(10):
    pp.add_first(random.randint(0, 5))
result = pp.find(e)
print(pp, "find {}:".format(e), result, result.element()) if result is not None else print(pp, "find {}:".format(e), result)


# R-7.14
# Repeat the previous process using recursion. Your method should not
# contain any loops. How much space does your method use in addition to
e = 3
pp = PositionalList()
print(pp, "find {}:".format(e), pp.find_recursion(e))  # empty list
for _ in range(10):
    pp.add_first(random.randint(0, 5))
result = pp.find_recursion(e)
print(pp, "find {}:".format(e), result, result.element()) if result is not None else print(pp, "find {}:".format(e), result)


# R-7.15
# Provide support for a reversed method of the PositionalList class that
# is similar to the given iter , but that iterates the elements in reversed
# order.
pp = PositionalList()
for _ in range(10):
    pp.add_first(random.randint(0, 100))
print(pp)
rp = reversed(pp)
for i in rp: print(i, end=" ")
