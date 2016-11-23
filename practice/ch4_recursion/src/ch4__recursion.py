__author__ = 'wlz'

import os, sys
#import doctest


# P172 factorial
def factorial(n):
    """
    implementation of a factorial function
    :param n: input integer
    :return:
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)


# P175 English ruler
def draw_line(tick_length,tick_label=''):
    """
    draw one line with given tick length (followed by tick label)
    :param tick_length:
    :param tick_label:
    :return:
    """
    line = '-'*tick_length
    if tick_label:
        line += ' '+tick_label
    print(line)


def draw_interval(center_length):
    """
    draw tick interval based on a central tick length
    :param center_length:
    :return:
    """
    if center_length >0: # stop when length drops to 0
        draw_interval(center_length-1) # recursively draw top ticks
        draw_line(center_length) # draw center tick
        draw_interval(center_length-1) #recurively draw bottom ticks


def draw_ruler(num_inches, major_length):
    """
    draw english ruler with given number of inches, major tick length
    :param num_inches:
    :param major_length:
    :return:
    """
    draw_line(major_length, '0') # draw inch 0 line
    for j in range(1,1+num_inches):
        draw_interval(major_length-1)  # draw interior ticks for inch
        draw_line(major_length,str(j)) # draw inch j line and label


# P178 binary search
def binary_search(data, target, low, high):
    """
    return True if target is found in indicated portion of a Python list.
    the search only considers the portion from data[low] to data[high] inclusive
    :param data: python list
    :param target:
    :param low: low index of the list
    :param high: high index of the list
    :return: True or False
    """
    #print(data[low:high])
    #print(target)
    if low > high:
        return False
    else:
        mid = (low + high) // 2
        if target == data[mid]:   # found a match, mid is an index
            return True
        elif target < data[mid]:
            # recur on the portion left of the middle
            return binary_search(data, target, low, mid-1)
        else:
            # recur on the portion right of the middle
            return binary_search(data, target, mid+1, high)


# P201
def binary_search_iterative(data, target):
    """
    return True if target is found in given list
    :param data:
    :param target:
    :return:
    """
    low = 0
    high = len(data) - 1
    while low <= high:
        mid = (low + high) // 2
        if target == data[mid]:  # found a match
            return True
        elif target < data[mid]:  # only consider values left of mid
            high = mid - 1
        else:   # only consider value right of mid
            low = mid + 1
    return False


# P181 computing the total disk usage for all files and directories

def disk_usage(path):
    """
    return the number of bytes used by a file/folder and any descendants
    :param path:
    :return:
    """
    total = os.path.getsize(path)   # get direct usage
    if os.path.isdir(path):  # if this is a directory
        for filename in os.listdir(path):  # for each child
            childpath = os.path.join(path, filename)  # compose full path to child
            total += disk_usage(childpath)  # add child's usage to total
    print('{0:<7}'.format(total), path)  # descriptive output
    return total  # return the grand total


# P189 efficient fibonacci --> return two values
def good_fibonacci(n):
    """
    return pair of fibonacci numbers F(n) and F(n-1)
    :param n:
    :return:
    """
    if n <= 1:
        return (n, 0)
    else:
        (fa, fb) = good_fibonacci(n-1)
        return (fa+fb, fa)


# P192 linear recursion to calculate sum
def linear_sum(S, n):
    """
    return the sum of the first n numbers of sequence S
    :param S: sequence
    :param n:
    :return:
    """
    if n == 0:
        return 0
    else:
        return linear_sum(S, n-1) + S[n-1]


# P193
# reversing a sequence with recursion
def reverse(S, start, stop):
    """
    reverse elements in implicit slice S[start:stop]
    :param S:
    :param start:
    :param stop:
    :return:
    """
    if start < stop -1: # if at least 2 elements
        S[start], S[stop-1] = S[stop-1], S[start]  # swap first and last
        reverse(S, start+1, stop-1)  # recur on rest


# P201
def revers_interative(S):
    """
    reverse elements in sequence S
    :param S:
    :return:
    """
    start, stop = 0, len(S)
    while start < stop - 1:
        S[start], S[stop-1] = S[stop-1], S[start]  # swap first and last
        start, stop = start+1, stop-1  # narrow the range


# P194
# recursive algorithms for computing power
def power1(x, n):
    """
    compute the value x**n for integer n
    O(n)
    :param x:
    :param n:
    :return:
    """
    if n == 0:
        return 1
    else:
        return x*power1(x, n-1)


# p195
def power2(x, n):
    """
    compute the value x**n for integer n
    O(log n)
    :param x:
    :param n:
    :return:
    """
    if n == 0:
        return 1
    else:
        partial = power2(x, n//2)  # rely on truncated division
        result = partial * partial  # even
        if n % 2 == 1:  # odd, include extra factor of x
            result *= x
        return result


# p196
def binary_sum(S, start, stop):
    """
    return the sum of the number in implicit slice S[start:stop]
    :param S:
    :param start:
    :param stop:
    :return:
    """
    if start >= stop:  # 0 element in slice
        return 0
    elif start == stop-1:  # 1 element in slice
        return S[start]
    else:    # more than 2 elements in slice
        mid = (start + stop) // 2
        return binary_sum(S, start, mid) + binary_sum(S, mid, stop)


# main

# factorial
# print("factorial")
# doctest.testmod(verbose=True)

# draw ruler
print("draw ruler")
draw_ruler(2, 4)
# binary search
print("binary search")
data = [2,4,5,7,8,9,12,14,17,19,22,25,27,28,33,37]
low, high = 0, len(data)
target = 22
bs = binary_search(data, target, low, high)
print(bs)
# disk usage
print("disk usage ")
path = "..\\..\\..\\sourceCode\\ch02"
disk_usage(path)
# linear sum
print("linear search")
S = range(10)
print(linear_sum(S, 5))
# print recursion limit
old = sys.getrecursionlimit()
print("old recursion limit is: {}".format(old))
sys.setrecursionlimit(50000)
print("new recursion limit is: {}".format(sys.getrecursionlimit()))
# binary sum
print("binary sum")
print(binary_sum(data, 0, len(data)))







