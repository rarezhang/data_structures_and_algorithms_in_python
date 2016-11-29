"""
Exercises
"""
from ArrayStack import *


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

