"""
ch6 stacks queues and deques
"""
from ArrayStack import *

# P 254
S = ArrayStack()
S.push(5)  # [5]
S.push(3)  # [5,3]
print(len(S))  # 2
print(S.pop())  # 3
print(S.is_empty())  # False
print(S.pop())  # 5
print(S.is_empty())  # True
S.push(7)  # [7]
S.push(9)  # [7,9]
print(S.pop())  # 9
S.push(4)  # [7,4]
print(len(S))  # 2
print(S.pop())  # 4
S.push(6)  # [7,6]


# P 257
def reverse_file(filename):
    """
    write given file with its contents line by line reversed
    :param filename:
    :return:
    """
    S = ArrayStack()
    original = open(filename)
    for line in original:
        # S.push(line.rstrip('\n'))
        S.push(line)
    original.close()
    # overwrite with contents in LIFO order
    output = open(filename, 'w')
    while not S.is_empty():
        # output.write(S.pop() + '\n')
        output.write(S.pop())
    output.close()

reverse_file('test.txt')


# P 258
def is_matched(expression):
    """
    return True if all delimiters are properly match
    False otherwise
    :param expression:
    :return:
    """
    lefty = '({['
    righty = ')}]'
    S = ArrayStack()
    for c in expression:
        if c in lefty:
            S.push(c)  # push left delimiter on stack
        elif c in righty:
            if S.is_empty():
                return False
            if righty.index(c) != lefty.index(S.pop()):
                return False  # mismatched
    return S.is_empty()  # all symbols matched

s = '()(()){([()])}'
print(is_matched(s))
s = '((()(()){([()])}))'
print(is_matched(s))
s = ')(()){([()])}'
print(is_matched(s))
s = '({[])}'
print(is_matched(s))