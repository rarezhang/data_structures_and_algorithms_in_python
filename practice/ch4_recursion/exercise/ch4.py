__author__ = 'wlz'


# R-4.1
def maximum(S):
    """
    finding the maximum element in a sequence
    :param S: python list
    :return:
    """
    if len(S) == 1:
        return S[0]
    else:
        max_element = maximum(S[1:])
        if max_element > S[0]:  # value of S[0] will change through every recursion
            return max_element
        else:
            return S[0]

# R-4.6
def harmonic(n):
    """
    a recursive function for computing the nth harmonic number
    :param n:
    :return:
    """
    if n == 1:
        return 1
    else:
        return harmonic(n-1) + 1/n

# R-4.7
def str_to_int(string, accumulator):
    """
    recursive function for converting a string of digits into the integer it represents
    :param s: pyhon string
    :return:
    """
    if not string:
        return accumulator
    else:
        # value of accumulator changes through every recursion
        # ord(string[0]) --> ascii, 0:48; ord(string[0])-48 --> '0'-> 0
        # accumulator keep record the value, through every recursion, (10*already had + add string[0]), left -> right
        return str_to_int(string[1:], 10 * accumulator + ord(string[0]) - 48)

# C-4.9
def minimum_maximum(s):
    """
    recursive function finds the minimum and maximum values in a sequence
    :param s: python list
    :param start:
    :param end:
    :return:
    """
    if len(s) == 1:
        return s[0], s[0]
    else:
        max_min_element = minimum_maximum(s[1:])
        if max_min_element[0] > s[0]:  # max
            max = max_min_element[0]
        else:
            max = s[0]
        if max_min_element[1] < s[0]:  # min
            min = max_min_element[1]
        else:
            min = s[0]
        return max, min

# C-4.10
def base_two_log(n):
    """
    !!! can only process positive numbers
    recursive algorithm to compute the integer part of the base-two
    logarithm of n, using only addition and integer division
    log2(n)
    :param n:
    :return:
    """
    if n < 2:
        return 0
    else:
        return 1+base_two_log(n//2)

# C-4.11
def unique(s):
    """
    recursive function
    uniqueness of element: without using sorting
    :param s: python list
    :return:
    """
    if len(s) == 1:
        return True
    else:
        # s[0] changes through every recursion
        # (s[0] not in s[1:]) --> if current element is unique
        # unique(s[1:]) --> check next element is unique
        return (s[0] not in s[1:]) and unique(s[1:])

# C-4.12
def product(m, n):
    """
    recursive to compute the product of two positive integer m and n
    using only addition and subtraction
    :param m:
    :param n:
    :return:
    """
    if n == 1:
        return m
    else:
        return m + product(m, n-1)


# C-4.14
def hanoi(n, source, helper, target):
    """
    http://www.python-course.eu/towers_of_hanoi.php
    The following rules have to be obeyed:
    -Only one disk may be moved at a time.
    -Only the most upper disk from one of the rods can be moved in a move
    -It can be put on another rod, if this rod is empty or if the most upper disk of this rod is larger than the one which is moved.
    The number of moves necessary to move a tower with n disks can be calculated as: 2n - 1
    :param n:
    :return:
    """
    print("hanoi( ", n, source, helper, target, " called")
    if n > 0:
        # move tower of size n-1 to helper
        hanoi(n-1, source, target, helper)
        # move disk from source peg to target peg
        if source[0]:
            disk = source[0].pop()
            print("moving " + str(disk) + " from " + source[1] + " to " + target[1])
            target[0].append(disk)
        # move tower of size n-1 from helper to target
        hanoi(n-1, helper, source, target)


# C-4.15
def subset(s):
    """
    recursive function output all the subsets of a set of n elements
    without repeating any subsets
    :param s: python list
    :return:
    """
    if len(s) == 0:
        return [[]]
    else:
        result = []
        for sub in subset(s[1:]):
            result.append(sub+[s[0]])
        return result + subset(s[1:])


# C-4.16
def string_reverse(s):
    """
    recursive python function that takes a character string s and outputs its reverse
    s: python string
    """
    if len(s) == 0:
        return s
    else:
        return string_reverse(s[1:])+s[0]


# C-4.17
def palindrome(s):
    """
    recursive python function determines if a string s is a palindrome
    (the string is equal to its reverse)
    :param s: python string
    :return: True / False
    """
    if len(s) < 2:
        # 0 or 1 item left, s is a palindrome by identity
        return True
    elif s[0] != s[-1]:  # if first and last are not the same item is not a palindrome
        return False
    return palindrome(s[1:-1])  # remove first and last item


# c-4.18
def count_vowels(s):
    """
    python recursion: count how many vowels in a string
    :param s: python
    :return: # of vowels
    """
    vowels = 'aeiouAEIOU'
    if not s:
        return 0
    elif s[0] in vowels:
        return 1 + count_vowels(s[1:])
    else:
        return count_vowels(s[1:])

def vowels_than_consonants(s):
    """
    determining if a string s has more vowels than consonants (not vowel)
    :param s: python string
    :return: True if more vowels than consonants; False if not
    """
    return count_vowels(s) > (len(s)-count_vowels(s))


# C-4.19
def rearrange(s):
    """
    recursive python function: rearranges a sequence of integer values
    so that all teh even values appear before all the odd values
    :param s: s python sting (but just have 0-9)
    :return:
    """
    if len(s) < 2:
        return s
    elif s[-1] in '24680':
        return s[-1] + rearrange(s[:-1])
    else:
        return rearrange(s[:-1]) + s[-1]

# C-4.20
def rearrange_k(s, k):
    """
    recursive: rearranging the elements in s
    all elements less than or equal to k come before any elements larger than k
    :param s: unsorted sequence s of integers (string but just have 0-9)
    : k: integer k
    :return:
    """
    if len(s) < 2:  # if there are only 0 or 1 element, no need to rearrangement
        return s
    elif int(s[-1]) <= k:
        return s[-1] + rearrange_k(s[:-1], k)
    else:
        return rearrange_k(s[:-1], k) + s[-1]


# C-4.21
def sum_to_k(s, k):
    """
    recursive algorithm to fin 2 integers in S that sum to k, is such a pair exists
    s: n-element sequence (python list), distinct integers that are listed in increasing order
    k: a number k
    :return a pair if exists; False if not
    """
    if len(s) < 2:
        return False
    elif (k-s[0]) in s:
        return (s[0], k-s[0])
    return sum_to_k(s[1:], k)


# C-4.22
def power_nonrecursive(x, n):
    """
    compute the value x**n for integer n
    """
    if n < 0:
        x = 1 / x
        n = -n
    elif n == 0:
        return 1

    y = 1
    while n > 1:
        if n%2 == 0:
            x = x*x
            n = n/2
        else:
            y = x*y
            x = x*x
            n = (n-1)/2
    return x*y










################################################################
################################################################
################################################################
################################################################
# main
'''
# R-4.1
S = [1, 9]
print(maximum(S))
# R-4.6
print(harmonic(1))
print(harmonic(3))
# R-4.7
s = "13531"
i = str_to_int(s, 0)
print(i, type(i))
# C-4.9
s = [1,5,9]
print(minimum_maximum(s))
# C-4.10
n = 4
print(base_two_log(n))
# C-4.11
print(unique(s))
# C-4.12
print(product(4, 2))
# C-4.14
source = ([3,2,1], "source")
target = ([], "target")
helper = ([], "helper")
n = len(source[0])
hanoi(n, source, helper, target)

# C-4.15
s = [0,1,2]
subs = subset(s)
print(subs)

# C-4.16
s = "pots&pans"
rs = string_reverse(s)
print(rs)

# C-4.17
s = 'abc'
print(palindrome(s))

# C-4.18
s = 'abc'
print(count_vowels(s))
print(vowels_than_consonants(s))

# C-4.19
s = '1234567890'
rs = rearrange(s)
print(s, rs)

# C-4.20
s = '5896542315898546878963'
k = 5
rs = rearrange_k(s, k)
print(s, rs)

# C-4.21
s = [1,3,5]
k = 9
print(sum_to_k(s, k))
'''
# C-4.22
x = 2
n = 1
print(power_nonrecursive(x, n))