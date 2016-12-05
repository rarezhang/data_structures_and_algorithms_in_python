"""
Exercises
"""
from ArrayStack import *
from ArrayQueue import *
from ArrayDeque import *
from collections import deque
from random import randrange
import itertools

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
print(d._data)
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


# C-6.15
s = ArrayStack()
s.push(randrange(10))
s.push(randrange(10))
s.push(randrange(10))
print("Alice's three integers:", s._data)
x = s.pop()
if x < s.top():
    x = s.pop()
print("the largest of Alice's three integers with probability 2/3: {}".format(x))

# C-6.16
s = ArrayStack(maxlen=2)
s.push(2)
s.push(3)
print(s._data)

# C-6.17

# C-6.18
# Show how to use the transfer function, described in Exercise R-6.3, and
# two temporary stacks, to replace the contents of a given stack S with those
# same elements, but in reversed order.
s1 = ArrayStack()
s2 = ArrayStack()
S = ArrayStack()
init_stack(S, 3)  # S = [0,1,2]
s1 = transfer(S, s1)  # s1 = [2, 1, 0]
s2 = transfer(s1, s2)
S = transfer(s2, S)
print(S._data)  # S = [2, 1, 0]

# C-6.19
#  After finding what’s between the < and > characters, the tag is
#  only the part before the first space (if any).
def is_matched_html(raw):
    """
    return True if all HTML tags are properly match
    False otherwise
    :param raw:
    :return:
    """
    S = ArrayStack()
    # string.find -> return index if found and -1 otherwise
    j = raw.find('<')  # find first '<' character if any
    while j != -1:
        k = raw.find('>', j+1)  # find next '>' character
        if k == -1:
            return False  # invalid tag
        tag = raw[j+1:k]  # strip away <>
        tag = tag.split()[0]  # the tag is only the part before the first space (if any)
        print(tag)
        if not tag.startswith('/'):  # this is opening tag
            S.push(tag)
        else:   # this is closing tag
            if S.is_empty():
                return False  # nothing to match with
            if tag[1:] != S.pop():
                return False  # mismatched delimiter
        j = raw.find('<', k+1)  # find next '<' character if any
    return S.is_empty()  # if all opening tags matched


raw_html = '''
<body>
<center>
<h1> The Little Boat </h1>
</center>
<p attribute1="value1" attribute2="value2"> The storm tossed the little
boat like a cheap sneaker in an
old washing machine. The three
drunken fishermen were used to
such treatment, of course, but
not the tree salesman, who even as
a stowaway now felt that he
had overpaid for the voyage. </p>
<ol>
<li> Will the salesman die? </li>
<li> What color is the boat? </li>
<li> And what about Naomi? </li>
</ol>
</body>
'''
print('matched html:', is_matched_html(raw_html))

# C-6.20
# Describe a non-recursive algorithm for enumerating all permutations of the
# numbers { 1 , 2 ,... , n } using an explicit stack.
num = [1,2,3]

p1 = itertools.permutations(num)
print(list(p1))


def permutations_recursive(num):
    """
    public method
    :param num: python list
    :return:
    """

    if len(num) == 1:
        return (num,)
    result = []
    for n in num:
        remaining = [x for x in num if x!=n]
        perms = permutations_recursive(remaining)
        for p in perms:
            result.append((n,) + tuple(p))
    return result

print(permutations_recursive(num))


def permutations_nonrecursive(num):
    """
    Use a stack to reduce the problem to that of enumerating all
    permutations of the numbers {1,2,...,n− 1}.

     replace a recursive algorithm by an iterative algorithm by pushing the parameters
     that would normally be passed to the recursive function onto a stack.
     In fact, you are replacing the program stack by one of your own.

    :param num: python list
    :return:
    """
    S = ArrayStack()
    for n in num:
        S.push(n)

    result = [(S.pop(),)]

    while len(S) != 0:
        c = (S.pop(),)
        new_result = []
        for w in result:
            for i in range(len(w) + 1):
                new_result.append(w[:i] + c + w[i:])
        result = new_result
    return result

print(permutations_nonrecursive(num))


# C-6.21
# Show how to use a stack S and a queue Q to generate all possible subsets
# of an n-element set T non-recursively.
num = [1,2,3]
result = []
for n in range(1, len(num)+1):
    result.extend(list(itertools.combinations(num, n)))
print(result)


def subsets_recursive(num):
    """

    :param num:
    :return:
    """
    if len(num) == 0:
        return ()

    result = []
    subs = subsets_recursive(num[0:-1])
    result += subs
    result.append((num[-1],))
    for s in subs:
        result.append(s + (num[-1],))
    return result

print(subsets_recursive(num))

# Use the stack to store the elements yet to be used to generate
# subsets and use the queue to store the subsets generated so far.
def subsets_nonrecursive(num):
    """
     use a stack S and a queue Q to generate all possible subsets
     of an n-element set T non-recursively.
    :param num:
    :return:
    """
    def copy_Q(Q, list_data):
        for l in list_data:
            Q.enqueue(l)

    result = []

    S = ArrayStack()
    for i in num:
        S.push(i)

    Q = ArrayQueue()

    for _ in range(len(S)):
        x = S.pop()
        sub = (x,)
        result.append(sub)
        if Q.is_empty():
            copy_Q(Q, result)  # copy result to Q
            continue
        else:
            for _ in range(len(Q)):
                q = Q.dequeue()
                result.append(q + sub)
            copy_Q(Q, result)  # copy result to Q
    return result


# C-6.22
# Postfix notation
from operator import add, sub, mul, truediv
op = {'+': add, '-': sub, '*': mul, '/': truediv}
op_str = op.keys()
def post_fix(expression):
    """

    :param expression:
    :return:
    """
    S = ArrayStack()

    expression = expression.split()
    try:
        for e in expression:
            if not e in op_str:
                S.push(int(e))
            else: # operator
                oper = op[e]
                b = S.pop()
                a = S.pop()
                S.push(oper(a,b))
        return S.pop()
    except Exception as e:
        print(e)
        print('Check expression --> if it is a valid postfix expression ')

exp = '5 2 + 8 3 - * 4 /'
# exp = '8 3 -'
print(post_fix(exp))


# C-6.23
# use R as temporary storage, as long as you never
# pop its original contents.
# original -> R=[1,2,3],S=[4,5],T=[6,7,8,9]
# goal -> R=[1,2,3], S=[6,7,8,9,4,5]
R,S,T = ArrayStack(), ArrayStack(), ArrayStack()
# initialize R, S and T
for i in range(1,10):
    if i < 4:
        R.push(i)
    elif i < 6:
        S.push(i)
    else:
        T.push(i)
print(R._data)
print(S._data)
print(T._data)
len_S = len(S); len_T = len(T)
for i in range(len_S):
    R.push(S.pop())
for i in range(len_T):
    R.push(T.pop())
for i in range(len_T+len_S):
    S.push(R.pop())

print(R._data)
print(S._data)
print(T._data)


# C-6.27
S = ArrayStack()
S = init_stack(S, 5)  # initialize stack 0-5

# Think of how you might use Q
# to process the elements of S twice.
def find_element(S, x):
    """
    scan S to see if it contains a certain element x
    your algorithm must return the elements back to S
    in their original order
    :param S:
    :param x:
    :return:
    """
    Q = ArrayQueue()
    len_S = len(S)
    flag = False
    for i in range(len_S):
        y = S.pop()
        Q.enqueue(y)
        if x == y:
            flag = True
    for i in range(len_S):
        S.push(Q.dequeue())

    for i in range(len_S):
        Q.enqueue(S.pop())
    for i in range(len_S):
        S.push(Q.dequeue())
    return flag
print('initial S: {}'.format(S._data))
print(S._data, find_element(S, 3))


# C-6.31
mazie, daisy, crazy, lazy = 2, 4, 10, 20
trip = []
trip.append(max(mazie, daisy))  # go: 4
trip.append(mazie)  # back: 2
trip.append(max(crazy, lazy))  # go: 20
trip.append(daisy)  # back: 4
trip.append(max(mazie, daisy))  # go: 4
print('all cows across the bridge in {} minutes'.format(sum(trip)))

