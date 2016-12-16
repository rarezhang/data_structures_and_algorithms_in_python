"""
ch7 exercises
"""

from LinkedQueue import LinkedQueue
from LinkedStack import LinkedStack

# R-7.1
# Give an algorithm for finding the second-to-last node in a singly linked
# list in which the last node is indicated by a next reference of None
# create a singly linked queue
q = LinkedQueue()
s = LinkedStack()
for i in range(5):
    q.enqueue(i)
    s.push(i)
print(q, s)


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

print(second_to_last(q), second_to_last(s))



