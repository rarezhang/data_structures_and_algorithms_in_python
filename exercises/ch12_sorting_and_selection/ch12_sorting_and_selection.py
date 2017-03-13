"""
chapter 12
sorting and selection
"""
import sys, os, math
sys.path.append(os.path.abspath("D:\Projects\data_structures_and_algorithms_in_python\exercises\ch7_linked_lists"))
from LinkedQueue import LinkedQueue
sys.path.append(os.path.abspath("D:\Projects\data_structures_and_algorithms_in_python\exercises\ch9_priority_queues"))
from PriorityQueueBase import PriorityQueueBase
Item = PriorityQueueBase._Item

# P 565
# array based implementation of merge sort
def merge(S1, S2, S):
    """
    merge two sorted python lists S1 and S2 into properly sized list S
    :param S1:
    :param S2:
    :param S:
    :return:
    """
    i = j = 0
    while i + j < len(S):
        if j == len(S2) or (i < len(S1) and S1[i]<S2[j]):
            S[i+j] = S1[i]  # copy ith element of S1 as next item of S
            i += 1
        else:
            S[i+j] = S2[j]  # copy jth element of S2 as next item of S
            j += 1


def merge_sort(S):
    """
    sort the elements of Python list S using the merge sort algorithm
    :param S:
    :return:
    """
    n = len(S)
    if n < 2: return   # already sorted
    # divide
    mid = n//2
    S1 = S[:mid]  # copy of first half
    S2 = S[mid:]  # copy of second half
    # conquer with recursion
    merge_sort(S1)
    merge_sort(S2)
    merge(S1, S2, S)

l = [1,4,9,6,3,7,8]
merge_sort(l)
print(l)


# merge sort using a basic linked queue
# P 569
def merge_linked(S1, S2, S):
    """
    merge two sorted queue instances S1 and S2 into empty queue S
    :param S1:
    :param S2:
    :param S:
    :return:
    """
    while not S1.is_empty() and not S2.is_empty():
        if S1.first() < S2.first():
            S.enqueue(S1.dequeue())
        else:
            S.enqueue(S2.dequeue())
    while not S1.is_empty():  # move remaining elements of S1 to S
        S.enqueue(S1.dequeue())
    while not S2.is_empty():  # move remaining elements of S2 to S
        S.enqueue(S2.dequeue())



def merge_sort_linked(S):
    """
    sort the elements fo queue S using the merge sort algorithm
    :param S:
    :return:
    """
    n = len(S)
    if n < 2:  # already sorted
        return
    # divide
    S1 = LinkedQueue()
    S2 = LinkedQueue()
    while len(S1) < n//2:  # move the first n//2 elements to S1
        S1.enqueue(S.dequeue())
    while not S.is_empty():  # move the rest to S2
        S2.enqueue(S.dequeue())
    # conquer with recursion
    merge_sort_linked(S1)  # sort first half
    merge_sort_linked(S2)  # sort second half
    merge_linked(S1, S2, S)  # merge sorted halves back into S

l = [1,4,9,6,3,7,8]
L = LinkedQueue()
for i in l: L.enqueue(i)
merge_sort_linked(L)
print(L)


# a bottom-up (non-recursive) merge sort
# faster than recursive merge-sort: avoids the extra overheads of recursive calls and temporary memory at each level
# P 571
def merge_bottom_up(src, result, start, inc):
    """
    merge src[start:(start+inc)] and src[(start+inc):(start+2*inc)] into result
    :param src:
    :param result:
    :param start:
    :param inc:
    :return:
    """
    end1 = start + inc  # boundary for run 1
    end2 = min(start+2*inc, len(src))  # boundary for run 2
    x, y, z = start, start+inc, start  # index of run1, run2, result
    while x < end1 and y < end2:
        if src[x] < src[y]:
            result[z] = src[x]  # copy from run1 and increment x
            x += 1
        else:
            result[z] = src[y]  # copy from run 2 and increment y
            y += 1
        z += 1  # increment z to reflect new result
    if x < end1:
        result[z:end2] = src[x:end1]  # copy remainder of run1 to output
    elif y < end2:
        result[z:end2] = src[y:end2]  # copy remainder of run2 to output


def merge_sort_bottom_up(S):
    """
    sort the elements fo python list S using the merge sort algorithm
    :param S:
    :return:
    """
    n = len(S)
    logn = math.ceil(math.log(n,2))
    src, dest = S, [None] * n  # make temporary storage for dest
    for i in (2**k for k in range(logn)):  # pass i creates all runs of length 2i
        for j in range(0, n, 2*i):  # each pass merges two length i runs
            merge_bottom_up(src, dest, j, i)
        src, dest = dest, src  # reverse roles of lists
    if S is not src:
        S[:n] = src[:n]  # additional copy to get results to S

l = [1,4,9,6,3,7,8]
merge_sort_bottom_up(l)
print(l)


# quick sort
# quick sort for a sequence S implemented as a queue
# O(n**2) worst case; O(nlogn) average
# P 577
def quick_sort(S):
    """
    sort the elements of queue S using the quick-sort algorithm
    :param S:
    :return:
    """
    n = len(S)
    if n < 2:
        return  # list is already sorted
    # divide
    pivot = S.first()  # using first as arbitrary pivot
    L = LinkedQueue()
    E = LinkedQueue()
    G = LinkedQueue()
    while not S.is_empty():  # divide S into L, E and G
        if S.first() < pivot:
            L.enqueue(S.dequeue())
        elif S.first() > pivot:
            G.enqueue(S.dequeue())
        else:  # S.first() must equal pivot
            E.enqueue(S.dequeue())
    # conquer with recursion
    quick_sort(L)  # sort elements less than pivot
    quick_sort(G)  # sort elements greater than pivot
    # concatenate results
    while not L.is_empty():
        S.enqueue(L.dequeue())
    while not E.is_empty():
        S.enqueue(E.dequeue())
    while not G.is_empty():
        S.enqueue(G.dequeue())

l = [1,4,9,6,3,7,8]
S = LinkedQueue()
for x in l:
    S.enqueue(x)
print(S)
quick_sort(S)
print(S)


# inplace quick sort
# a sub-sequence of the input sequence is implicitly represented by a range of positions specified by a leftmost index A
# and a right most index B
# use the input sequence itself to store the sub-sequences for all the recursive calls
# stack depth can be O(n-1), expected stack depth is O(logn)
# -> design a non-recursive version of in-place quick-sort using an explicit stack to iteratively process sub-problem
# P 581
def inplace_quick_sort(S, a, b):
    """
    sort the list from S[a] to S[b] inclusive using the quick-sort algorithm
    :param S:
    :param a:
    :param b:
    :return:
    """
    if a >= b:
        return  # range is trivially sorted
    pivot = S[b]  # last element of range if pivot
    left, right = a, b-1
    while left <= right:
        # scan until reaching value equal or larger than pivot (or right marker)
        while left <= right and S[left]<pivot:
            left += 1
        # scan until reaching value equal or smaller than pivot (or left marker)
        while left <= right and pivot < S[right]:
            right -= 1
        if left <= right:  # scans did not strictly cross
            S[left], S[right] = S[right], S[left]  # swap values
            left, right = left+1, right-1  # shrink range

    # put pivot into its final place (currently marked by left index)
    S[left], S[b] = S[b], S[left]
    # make recursive calls
    # There is no explicit “combine” step, because the
    # concatenation of the two sublists is implicit to the in-place use of the original list
    inplace_quick_sort(S, a, left-1)
    inplace_quick_sort(S, left+1, b)

l = [1,4,9,6,3,7,8]
print(l)
inplace_quick_sort(l, 0, len(l)-1)
print(l)


# an implementing the decorate-sort-undecorate pattern based on the array-based mege-sort 
# P 592
def decorated_merge_sort(data, key=None):
    """
    demonstration of the decorate-sort-undecorate pattern 
    """
    if key is not None:
        for j in range(len(data)):
            data[j] = Item(key(data[j]), data[j])  # decorate each element
    merge_sort(data)  # sort with existing algorithm 
    if key is not None:
        for j in range(len(data)):
            data[j] = data[j]._value  # undecorate each element 
            
alist = ['yellow', 'blue', 'cyan', 'green', 'red']
print(alist)
decorated_merge_sort(alist, key=len)
print(alist)


# prune-and-search || decrease-and-conquer  
# select first k (find median) --> O(n)  [if sort O(nlogn)]
# randomized quick-select: O(n) expected time; O(n**2) worst case 
# P 594 
import random

def quick_select(S, k):
    """
    return the kth smallest element of list S, for k from 1 to len(S)
    """
    if len(S) == 1:
        return S[0]
    pivot = random.choice(S)  # pick random pivot element from S
    L = [x for x in S if x < pivot]  # elements less than pivot 
    E = [x for x in S if x == pivot]  # elements equal to pivot
    G = [x for x in S if x > pivot]  # elements greater than pivot
    if k <= len(L):
        return quick_select(L, k)  # kth smallest lies in L 
    elif k <= len(L) + len(E):  # kth smallest equal to pivot 
        return pivot
    else:
        j = k - len(L) - len(E)  # new k: new selection parameter j
        return quick_select(G, j)  # kth smallest is is jth in G

alist = [random.randint(1,10) for _ in range(10)]
print([x for x in alist], 'median:', quick_select(alist, len(alist)//2))
