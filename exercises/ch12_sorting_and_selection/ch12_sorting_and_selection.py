"""
chapter 12
sorting and selection
"""
import sys, os, math
sys.path.append(os.path.abspath("D:\Projects\data_structures_and_algorithms_in_python\exercises\ch7_linked_lists"))
from LinkedQueue import LinkedQueue

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