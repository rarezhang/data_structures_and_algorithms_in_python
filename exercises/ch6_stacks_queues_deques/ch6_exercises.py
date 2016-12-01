"""
Exercises
"""
from ArrayStack import *
from ArrayQueue import *
from ArrayDeque import *
from collections import deque

def init_stack(S, n):
    """

    :param S: Stack
    :param n: number of elements
    :return:
    """
    for i in range(n):
        S.push(i)
    return S


# R-6.1
stack = ArrayStack()
stack.push(5)  # [5]
stack.push(3)  # [5,3]
stack.pop()  # [5]
stack.push(2)  # [5,2]
stack.push(8)  # [5,2,8]
stack.pop()  # [5,2]
stack.pop()  # [5]
stack.push(9)  # [5,9]
stack.push(1)  # [5,9,1]
stack.pop()  # [5,9]
stack.push(7)  # [5,9,7]
stack.push(6)  # [5,9,7,6]
stack.pop()  # [5,9,7]
stack.pop()  # [5,9]
stack.push(4)  # [5,9,4]
stack.pop()  # [5,9]
stack.pop()  # [5]
print(stack._data)

# R-6.2
# total of 25 push | 12 top | 10 pop
# 3 Empty errors
# If a stack is empty when pop is called, its size does not change.
# 0 on pop: 25- 10 = 15
# 1 on pop: 25-(10-1) = 16
# 2 on pop: 25-(10-2) = 17
# 3 on pop: 25-(10-3) = 18
# current size of S: 15-18

# R-6.3
# stack: Last in first out
# Transfer items one at a time.
def transfer(S, T):
    """
    transfers all element from stack S onto stack T
    the element that starts at the top of S is the first to be inserted onto T
    :param S:
    :param T:
    :return:
    """
    for _ in range(len(S)):
        s = S.pop()
        T.push(s)
    return T

SS = ArrayStack()
init_stack(SS, 3)
print(SS._data)  # [0, 1, 2]
TT = ArrayStack()
TT = transfer(SS, TT)
print(TT._data)  # [2, 1, 0]


# R-6.4
def remove_elements(S):
    """
    a recursive method for removing all the elements from a stack.
    :param S:
    :return:
    """
    if S.is_empty():  # First check if the stack is already empty.
        return S
    else:
        S.pop()
        return remove_elements(S)

init_stack(SS, 4)
print(SS._data)  # [0, 1, 2, 3]
remove_elements(SS)
print(SS._data)  # []


# R-6.5
def reverse_list(ll):
    """
    reverses a list of elements
    writing them back to the list in reversed order
    :param ll:
    :return:
    """
    S = ArrayStack()
    L = list()
    for i in range(len(ll)):
        S.push(ll[i])
    for _ in range(len(S)):
        L.append(S.pop())
    return L

test = 'a b c d e'.split()  # ['a', 'b', 'c', 'd', 'e']
reverse_test = reverse_list(test)
print(reverse_test)


# R-6.7
# First in first out
q = ArrayQueue()
q.enqueue(5)  # [5]
q.enqueue(3)  # [5,3]
q.dequeue()  # [3]
q.enqueue(2)  # [3,2]
q.enqueue(8)  # [3,2,8]
q.dequeue()  # [2,8]
q.dequeue()  # [8]
q.enqueue(9)  # [8,9]
q.enqueue(1)  # [8,9,1]
q.dequeue()  # [9,1]
q.enqueue(7)  # [9,1,7]
q.enqueue(6)  # [9,1,7,6]
q.dequeue()  # [1,7,6]
q.dequeue()  # [7,6]
q.enqueue(4)  # [7,6,4]
q.dequeue()  # [6,4]
q.dequeue()  # [4]
print(q._data)  # [None, None, None, None, None, None, None, None, 4, None]


# R-6.11

class QueueDQ:
    """
    queue ADT based on collections.deque
    first in first out
    """
    DEFAULT_CAPACITY = None  # Maximum size of a deque or None if unbounded.

    def __init__(self):
        """
        empty queue
        """
        self._data = deque(maxlen=QueueDQ.DEFAULT_CAPACITY)


    def __len__(self):
        """

        :return:
        """
        return len(self._data)

    def is_empty(self):
        """
        return True if it is empty
        :return: True | False
        """
        return len(self._data) == 0

    def first(self):
        """
        return the front element (do not remove)
        :return:
        """
        if self.is_empty():
            raise Empty('queue is empty')
        return self._data[0]

    def enqueue(self, element):
        """
        add an element to the back of queue
        :return:
        """
        self._data.append(element)

    def dequeue(self):
        """
        remove and return the first elemtn of the queue
        :return:
        """
        if self.is_empty():
            raise Empty('queue is empty')
        return self._data.popleft()

q_dq = QueueDQ()
q_dq.enqueue(1);q_dq.enqueue(2);q_dq.enqueue(3)
print(q_dq.first())
print(q_dq._data)
q_dq.dequeue()
print(q_dq.first())
print(q_dq._data)


# R-6.12
d = ArrayDeque()
d.add_first(4)  # [4]
d.add_last(8)  # [4,8]
d.add_last(9)  # [4,8,9]
d.add_first(5)  # [5,4,8,9]
d.delete_first()  # [4,8,9]
d.delete_last()  # [4,8]
d.add_last(7)  # [4,8,7]
d.first()  # 4
d.last()  # 7
d.add_last(6)  # [4,8,7,6]
d.delete_first()  # [8,7,6]
d.delete_first()  # [7,6]
print(d._data)

# R-6.13
print("R-6.13:")
d = ArrayDeque()
for i in range(1,9):
    d.add_last(i)
# deque([1,2,3,4,5,6,7,8])
q = ArrayQueue()  # initial empty queue
d.add_last(d.delete_first())
d.add_last(d.delete_first())
d.add_last(d.delete_first())
print(d._data)  # d [4, 5, 6, 7, 8, 1, 2, 3]
q.enqueue(d.delete_first())
q.enqueue(d.delete_first())
print(q._data)  # q [4, 5]
print(d._data)  # d [6, 7, 8, 1, 2, 3]
d.add_first(q.dequeue())  # d [4, 6, 7, 8, 1, 2, 3]
d.add_last(q.dequeue())  # d [4, 6, 7, 8, 1, 2, 3, 5]
q.enqueue(d.delete_first())
d.add_last(q.dequeue())
d.add_last(d.delete_first())
d.add_last(d.delete_first())
d.add_last(d.delete_first())
# results in D storing the elements in the order
# ( 1 , 2 , 3 , 5 , 4 , 6 , 7 , 8 ) .

# R-6.14
print("R-6.14:")
d = ArrayDeque()
for i in range(1,9):
    d.add_last(i)
# deque([1,2,3,4,5,6,7,8])
s = ArrayStack()  # initial empty queue
d.add_last(d.delete_first())
d.add_last(d.delete_first())
d.add_last(d.delete_first())
s.push(d.delete_first())
s.push(d.delete_first())
d.add_last(s.pop())
d.add_last(s.pop())
d.add_last(d.delete_first())
d.add_last(d.delete_first())
d.add_last(d.delete_first())
print(d._data)