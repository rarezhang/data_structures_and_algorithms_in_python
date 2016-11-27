"""
exercises
"""
import sys
import ctypes
import random
# R-5.4
# Our DynamicArray class, as given in Code Fragment 5.3, does not support
# use of negative indices with getitem . Update that method to better
# match the semantics of a Python list.

# R-5.6
# Give an improved implementation
# of the insert method, so that, in the case of a resize, the elements are
# shifted into their final position during that operation, thereby avoiding the
# subsequent shifting

# C-5.16
# Implement a pop method for the DynamicArray class, given in Code Fragment
# 5.3, that removes the last element of the array, and that shrinks the
# capacity, N, of the array by half any time the number of elements in the
# array goes below N / 4.


class DynamicArray:
    """
    a dynamic array class akin to a simplified python list
    """
    def __init__(self):
        """
        create an empty array
        :return:
        """
        self._n = 0  # count actual elements
        self._capacity = 1  # default array capacity
        self._A = self._make_array(self._capacity)  # low-level array

    def __len__(self):
        """
        return # of elements stored in the array
        :return:
        """
        return self._n

    def __getitem__(self, k):
        """
        # R-5.4
        return element at index k
        :param k: index k
        :return:
        """
        if 0 <= k < self._n:
            return self._A[k]  # retrieve from array
        elif -self._n <= k <= -1:
            return self._A[k + self._n]
        else:
            raise IndexError('Invalid Index')

    def append(self, obj):
        """
        add object to end of the array
        :param obj:
        :return:
        """
        if self._n == self._capacity:  # not enough room
            self._resize(2*self._capacity)  # double capacity
        self._A[self._n] = obj
        self._n += 1

    def _resize(self, c):  # nonpublic utity
        """
        # C-5.16
        resize internal array to capacity c
        :param c:
        :return:
        """
        B = self._make_array(c)  # new (bigger) array
        for k in range(self._n):  # for each existing value
            B[k] = self._A[k]
        self._A = B  # use the bigger array
        self._capacity = c

    def insert(self, k, value):
        """
        # R 5.6
        need two (non-nested) loops.
        :param k:
        :param value:
        :return:
        """
        if self._n == self._capacity:
            B = self._make_array(2 * self._capacity)
            for j in range(0, k):
                B[j] = self._A[j]
            for j in range(self._n, k, -1):
                B[j] = self._A[j - 1]
            self._A = B
            self._capacity = 2 * self._capacity
        else:
            for j in range(self._n, k, -1):
                self._A[j] = self._A[j-1]
        self._A[k] = value
        self._n += 1

    def remove(self, value):
        """
        remove first occurrence of value (or raise ValueError)
        do not consider shrinking the dynamic array in this version
        :param value:
        :return:
        """
        for k in range(self._n):
            if self._A[k] == value:
                for j in range(k, self._n -1):
                    self._A[j] = self._A[j+1]
                self._A[self._n - 1] = None  # garbage collection
                self._n -= 1
                return   # exit immediately if find one
        raise ValueError('vale not found')  # only reached if no match

    def remove_all(self, value):
        """
        # C-5.25
        removes all occurrences of value from the given list
        :param value:
        :return:
        """
        B = self._make_array(self._capacity)
        count = 0
        for k in range(self._n):
            if self._A[k] != value:
                B[count] = self._A[k]
                count += 1
        self._A = B
        self._n = count

    def pop(self):
        """
        # C-5.16
        removes the last element of the array
        shrinks the capacity of the array
        :return: last element of the array
        """
        p = self._A[self._n - 1]  # the last element of the array
        self._A[self._n - 1] = None  # garbage collection
        self._n -= 1
        if 0 < self._n < self._capacity * 0.25:
            self._resize(int(0.5 * self._capacity))  # shrink capacity
        return p

    def _make_array(self, c):    # nonpublic utility
        """
        return new array with capacity c
        :param c:
        :return:
        """
        return (c * ctypes.py_object)()  # see ctypes documentation

dynamic_array = DynamicArray()
print("create dynamic array object", dynamic_array, dynamic_array._n, dynamic_array._capacity)
dynamic_array.append(4)
print("append a new element", dynamic_array, dynamic_array._n, dynamic_array._capacity)
dynamic_array.insert(0, 489)
dynamic_array.insert(0, 21)
dynamic_array.insert(1, 25)
dynamic_array.insert(1, 23)
dynamic_array.insert(1, 23)
print("insert a new element at index:0", dynamic_array, dynamic_array._n, dynamic_array._capacity)
print("test positive indices:", dynamic_array[0], dynamic_array[1])
print("test negative indices:", dynamic_array[-1], dynamic_array[-2])
print("remove all occurrences of value", dynamic_array.remove_all(23))
# [21,25,489,4]

print("pop out last item:", dynamic_array.pop())
print("pop out last item:", dynamic_array.pop())
print("pop out last item:", dynamic_array.pop())
print("pop out last item:", dynamic_array.pop())


# R-5.7
# Let A be an array of size n ≥ 2 containing integers from 1 to n − 1, inclusive,
# with exactly one repeated. Describe a fast algorithm for finding the
# integer in A that is repeated.
def find_1_repeat(A):
    """

    :param A: an array of size n>=2
    :return:
    """
    len_A = len(A)
    assert len_A >= 2, 'A should be an array of size n>=2'
    sum_real = (len_A -1 ) * len_A / 2  # n(n+1)/2
    sum_A = sum(A)
    return sum_A - sum_real

ay = [1,2,3,2]
print('the integer that is repeated: {}'.format(find_1_repeat(ay)))

# R-5.10
# Caesar cipher
class CaesarCipher:
    """
    class for doing encryption and decryption using a Caesar cipher
    """
    def __init__(self, shift):
        """
        construct Caesar cipher using given integer shift for rotation
        :param shift:
        :return:
        """
        self._forward = "".join([chr((k+shift)%26 + ord('A')) for k in range(26)])  # will store as string
        self._backward = "".join([chr((k-shift)%26 + ord('A')) for k in range(26)])  # since fixed

cc_test = CaesarCipher(1)
print(cc_test._forward, cc_test._backward)

# R-5.11
def sum_standard_control(A):
    """

    :param A: python list of lists
    :return:
    """
    n = len(A)
    sum_A = 0
    for a in A:
        if len(a) != n:
            raise ValueError('should be n x n list')
        for aa in a:
            sum_A += aa
    return sum_A

A = [[1,2,3],[4,5,6],[7,8,0]]
print('the sum of A: {}'.format(sum_standard_control(A)))


# R-5.12
def sum_list_comprehension(A):
    """

    :param A: python list of lists
    :return:
    """
    return sum([sum(a) for a in A])

print('the sum of A: {}'.format(sum_list_comprehension(A)))

# C-5.14
# takes a Python list and rearranges it so that every possible ordering is equally likely
A = [1,2,3,4,5]
print(A)
random.shuffle(A)  # shuffle from random module, return None
print(A)


# you own version of shuffle:
# Consider randomly shuffling the deck one card at a time
def random_shuffle(A):
    """

    :param A: python list
    :return: shuffled A
    """
    len_A = len(A)
    for i in range(len_A):
        j = random.randrange(len_A)
        A[i], A[j] = A[j], A[i]
    return A

random_shuffle(A)
print(A)


# C-5.26
#  Let B be an array of size n ≥ 6 containing integers from 1 to n − 5, inclusive,
#  with exactly five repeated. Describe a good algorithm for finding the
#  five integers in B that are repeated
#  hints:  It might help to sort B.
def find_n_repeat(B):
    """

    :param B: python list, n>=6, with exactly five repeated
    :return:
    """
    B = sorted(B)
    for i in range(len(B)-1):
        if B[i] == B[i+1]:
            return B[i]

B = [1,1,1,1,1,1]
print('find n repeat:', find_n_repeat(B))
B = [2,2,2,2,2,2,1,3]
print('find n repeat:', find_n_repeat(B))


# C-5.27
# Given a Python list L of n positive integers, each represented with k =
#  ceiling(log n) + 1 bits, describe an O ( n ) -time method for finding a k-bit integer
# not in L.


# C-5.29
# natural join
def natural_join(A, B):
    """

    :param A: table A (x, y)
    :param B: table B (y, z)
    :return: (x, y, z)
    """
    C = list()
    for a in A:
        for b in B:
            if a[1] == b[0]:
                C.append((a[0], a[1], b[1]))
    return C

table_A = [('wenli', '001'), ('alex', '002'), ('cate', '003')]
table_B = [('001', 'A'), ('002', 'B'), ('003', 'D')]
print(natural_join(table_A, table_B))
# Be sure to allow for the case where every pair (x , y) in A and
# every pair (y , z) in B have the same y value.
table_A = [('wenli', '001'), ('alex', '001'), ('cate', '001')]
table_B = [('001', 'A'), ('001', 'B'), ('001', 'D')]
print(natural_join(table_A, table_B))


# C-5.31
def sum_recursion(A):
    """

    :param A: python list of lists
    :return:
    """
    pass
