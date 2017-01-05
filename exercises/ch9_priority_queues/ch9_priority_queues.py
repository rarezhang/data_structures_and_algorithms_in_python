"""
chapter 9
priority queues
"""

import heapq as hq
from random import randint
from HeapPriorityQueue import HeapPriorityQueue
import sys, os
sys.path.append(os.path.abspath("D:\\Projects\\data_structures_and_algorithms_in_python\\exercises\\ch7_linked_lists"))
from PositionalList import PositionalList

# P 406
# python's heapq module
L = list()
for e in range(10): hq.heappush(L, randint(1,100))  # heappush: O(log(n))
print(L)
i = hq.heappop(L)  # heappop: O(log(n)) -> reestablish the heap-order property
print(i, L)
i = hq.heappushpop(L, 500)  # heappushpop: O(log(n)) -> push element to L, pop the smallest item
print(i, L)
i = hq.heapreplace(L, 1000)  # heapreplace: O(log(n)) -> pop smallest item, push element to L
print(i, L)

L = [randint(1, 100) for i in range(10)]
print(L)
hq.heapify(L)
print(L)  # O(n) -> bottom-up construction
i = hq.nlargest(5, L)  # O(n+k*log(n)) -> k largest value
print(i, L)
i = hq.nsmallest(5, L)  # O(n+k*log(n)) -> k smallest value
print(i, L)

# P 407
def pq_sort(C):
    """
    sort a collection of elements stored in a positional list
    :param C:
    :return:
    """
    assert isinstance(C, PositionalList)
    n = len(C)
    P = HeapPriorityQueue()  # could be any PriorityQueue
    for j in range(n):
        element = C.delete(C.first())
        P.add(element, element)  # use element as key and value
    for j in range(n):
        (k,v) = P.remove_min()
        C.add_last(v)  # store smallest remaining element in C


p = PositionalList()
for i in range(10): p.add_last(randint(1, 100))
print(p)
pq_sort(p)
print(p)
