"""
chapter 9
priority queues
"""

import heapq as hq
from random import randint

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