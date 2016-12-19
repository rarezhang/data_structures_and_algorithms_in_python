"""
ch7 exercises
"""

from LinkedQueue import LinkedQueue
from LinkedStack import LinkedStack
from CircularQueue import CircularQueue
from LinkedDeque import LinkedDeque
from PositionalList import PositionalList
from ch7_linked_lists import FavoritesList
from LinkedStackSentinel import LinkedStackSentinel
from LinkedQueueSentinel import LinkedQueueSentinel
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
print()


# R-7.16
# Describe an implementation of the PositionalList methods add last and
# add before realized by using only methods in the set {is empty, first, last,
# prev, next, add after, and add first} .
pp = PositionalList()
pp.add_last2(500)
for _ in range(5):
    pp.add_first(random.randint(0, 3))
pp.add_last(1000); print(pp)
pp.add_last2(2000); print(pp)
pp.add_before(pp.first(), 3000); print(pp)
pp.add_before2(pp.first(), 4000); print(pp)
pp.add_before2(pp.last(), 5000); print(pp)


# R-7.17
# move an element of a list at position p to become the first
# element of the list, while keeping the relative order of the remaining elements
# unchanged.
# Augment the PositionalList
# class to support a new method, move to front(p), that accomplishes this
# goal more directly, by relinking the existing node.
pp = PositionalList()
for i in range(5):
    pp.add_first(i)
print(pp)
pp.move_to_front(pp.first()); print(pp)  # move first item
pp.move_to_front(pp.last()); print(pp)  # move last item
pp.move_to_front(pp.after(pp.first())); print(pp)  # move second item


# R-7.18
# Given the set of element { a , b , c , d , e , f } stored in a list, show the final state
# of the list, assuming we use the move-to-front heuristic and access the elements
# according to the following sequence: ( a , b , c , d , e , f , a , c , f , b , d , e ) .
s = 'abcdef'
pp = PositionalList()
for i in s:
    pp.add_last(i)
print(pp)  # {{ a b c d e f }}
# access sequence ( a , b , c , d , e , f , a , c , f , b , d , e )
seq = 'abcdefacfbde'
for i in seq:
    pp.move_to_front(pp.find(i))
    print("access: {}, list: {}".format(i, pp))
# access: a, list: {{ a b c d e f }}
# access: b, list: {{ b a c d e f }}
# access: c, list: {{ c b a d e f }}
# access: d, list: {{ d c b a e f }}
# access: e, list: {{ e d c b a f }}
# access: f, list: {{ f e d c b a }}
# access: a, list: {{ a f e d c b }}
# access: c, list: {{ c a f e d b }}
# access: f, list: {{ f c a e d b }}
# access: b, list: {{ b f c a e d }}
# access: d, list: {{ d b f c a e }}
# access: e, list: {{ e d b f c a }}

# R-7.20
# Let L be a list of n items maintained according to the move-to-front heuris-
# tic. Describe a series of O ( n ) accesses that will reverse L.
s = 'abc'
pp = PositionalList()
for i in s:
    pp.add_last(i)
print(pp)
# O(n)
pp.move_to_front(pp.first())
pp.move_to_front(pp.after(pp.first()))
pp.move_to_front(pp.after(pp.after(pp.first())))
print(pp)


# R-7.21
# Suppose we have an n-element list L maintained according to the move-
# to-front heuristic. Describe a sequence of n*n accesses that is guaranteed
# to take Ω( n*n*n) time to perform on L.
ele = 'a'
pp.move_to_front(pp.find(ele))
# For this lower bound, assume that when an element is accessed
# we search for it by traversing the list starting at the front.


# R-7.22
# Implement a clear() method for the FavoritesList class that returns the list
# to empty.
f = FavoritesList()
f.access(50)
print(f._data)
f.clear()
print(f._data)


# R-7.23
# Implement a reset counts() method for the FavoritesList class that resets
# all elements’ access counts to zero (while leaving the order of the list
# unchanged).
#  adjust instances of the nested Item class.
for i in range(9): f.access(i)
for i in range(4): f.access(i)
for i in f._data: print(i._value, i._count)
f.reset_counts()
for i in f._data: print(i._value, i._count)


# C-7.24
# Give a complete implementation of the stack ADT using a singly linked
# list that includes a header sentinel.
ls = LinkedStackSentinel()
for i in range(5): ls.push(i); print(ls)
for _ in range(5): ls.pop(); print(ls)


# C-7.25
# Give a complete implementation of the queue ADT using a singly linked
# list that includes a header sentinel.
qs = LinkedQueueSentinel()
for i in range(5,9): qs.enqueue(i); print(qs)
for _ in range(5,9): qs.dequeue(); print(qs)