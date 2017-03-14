"""
chapter 5. array-based sequences
"""


import sys
import ctypes  # proves low-level arrays
from time import time  # import  time function from time module

# P215
# explore the relationship between a list's length and its underlying size in python
data = []
n = 26
for k in range(n):
    a = len(data)
    # getsizeof() only includes the size for representing its primary structure
    # does not account for memory used by the objects that are elements fo the list
    b = sys.getsizeof(data)
    print('Length: {0:3d}; Size in bytes: {1:4d}'.format(a, b))
    data.append(None)  # list is a referential structure


# P218
class DynamicArray:
    """
    a dynamic array class akin to a simplified python list
    """
    def __init__(self):
        """
        create an empty array
        :return:
        """
        self._n = 0  # count actural elements
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
        return element at index k
        :param k: index k
        :return:
        """
        if not 0 <= k < self._n:
            raise IndexError('Invalid Index')
        return self._A[k]   # retrieve from array

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
        insert value at index k
        shifting subsequent values rightward
        assume 0<= k <= n
        :param k:
        :param value:
        :return:
        """
        if self._n == self._capacity:
            self._resize(2 * self._capacity)
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

    def _make_array(self, c):    # nonpublic utitity
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
print("insert a new element at index:0", dynamic_array, dynamic_array._n, dynamic_array._capacity)


# P223
# measuring the amortized cost of append for python's list class
def compute_average(n):
    """
    perform n appends to an empty list and return average time elapsed
    :param n:
    :return:
    """
    data = []
    start = time()  # record the start time
    for k in range(n):
        data.append(None)
    end = time()  # record the end time
    return (end-start)/n  # compute average per operation

for num in range(100, 10000, 1000):
    print('compute average, n: {0}  average per operation: {1}'.format(num, compute_average(num)))

# P229
# list comprehension
n = 5
squares = [k*k for k in range(1, n+1)]
print(squares)


# P232
class GameEntry:
    """
    represents one entry of a list of high scores
    """
    def __init__(self,name,score):
        """
        constructor
        :param name:
        :param score:
        :return:
        """
        self._name = name
        self._score = score

    def get_name(self):
        return self._name

    def get_score(self):
        return self._score

    def __str__(self):
        return '({0}, {1})'.format(self._name, self._score)   # e.g.,(Bob, 98)


print("test GameEntry class")
kate = GameEntry('Cate Zhang', 100)
print("get name", kate.get_name())
print("get score", kate.get_score())
print("__str__ method", kate)   # (Cate Zhang, 100)


# P234
class Scoreboard:
    """
    fixed-length sequence of high scores in nondecreasing order
    """
    def __init__(self, capacity=10):
        """
        initialize scoreboard with given maximum capacity. all entries are initially None
        :param capacity:
        :return:
        """
        self._board = [None]*capacity  # reserve space for future scores
        self._n = 0  # number of actual entries

    def __getitem__(self, k):
        """
        return entry at index k
        :param k:
        :return:
        """
        return self._board[k]

    def __str__(self):
        """
        return string representation of the high score list
        :return:
        """
        return '\n'.join(str(self._board[j]) for j in range(self._n))

    def add(self, entry):
        """
        consider adding entry to high scores
        :param entry:
        :return:
        """
        score = entry.get_score()
        # does new entry qualify as a high score
        # answer is yes if board not full or score is higher than last entry
        good = self._n < len(self._board) or score > self._board[-1].get_score()

        if good:
            if self._n < len(self._board):  # no score drops from list
                self._n += 1  # so overall number increases
            # shift lower scores rightward to make roo for new entry
            j = self._n - 1
            while j > 0 and self._board[j-1].get_score() < score:
                self._board[j] = self._board[j-1]  # shift entry from j-1 to j
                j -= 1  # add decrement j
            self._board[j] = entry  # when done, add new entry


# P237
def insertion_sort(A):
    """
    sort list of comparable elements into non-decreasing order
    :param A: numerical list
    :return:
    """
    for k in range(1,len(A)):  # from 1 to n-1
        cur = A[k]  # current element to be inserted
        j = k  # find correct index j for current
        while j > 0 and A[j-1] > cur:  # element A[j-1] must be after current
            A[j] = A[j-1]
            j -= 1
        A[j] = cur  # cur is now in the right place


# P 240
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
        encoder = [None] * 26  # temp array for encryption
        decoder = [None] * 26  # temp array for decryption
        for k in range(26):
            encoder[k] = chr((k+shift)%26 + ord('A'))
            decoder[k] = chr((k-shift)%26 + ord('A'))
        self._forward = "".join(encoder)  # will store as string
        self._backward = "".join(decoder)  # since fixed

    def encrypt(self, message):
        """
        return string representing encrypted message
        :param message:
        :return:
        """
        return self._transform(message, self._forward)

    def decrypt(self, secret):
        """
        return decrypted message given encrypted secret
        :param secret:
        :return:
        """
        return self._transform(secret, self._backward)

    def _transform(self, original, code):
        """
        utility to perform transformation based on given code string
        :param orginal:
        :param code:
        :return:
        """
        msg = list(original)
        for k in range(len(msg)):
            if msg[k].isupper():
                j = ord(msg[k]) - ord('A')  # index form 0 to 25
                msg[k] = code[j]
        return ''.join(msg)

cipher = CaesarCipher(3)  # class CaesarCipher, shift=3
message = "THE EAGLE IS IN PLAY; MEET AT JOE S."  # original message
coded = cipher.encrypt(message)
print('secret: ', coded)
answer = cipher.decrypt(coded)
print('answer: ', answer)


# P243
# create a two dimensional list
column = 3
row = 3
data = ([0]*column)*row  # can only get 1 dimension list with column*row elements
print(data)  # [0, 0, 0, 0, 0, 0, 0, 0, 0]
data = [[0]*column]*row  # all row entries of the list know as data are references to the same instance of a list of column zero
data[2][0] = 100  # e.g., will get [[100, 0, 0], [100, 0, 0], [100, 0, 0]]
print(data)
# [[100, 0, 0], [100, 0, 0], [100, 0, 0]]
data = [[0] * column for j in range(row)]
data[2][0] = 100  # will get [[0, 0, 0], [0, 0, 0], [100, 0, 0]]
print(data)
# [[0, 0, 0], [0, 0, 0], [100, 0, 0]]


# P 245
# multidimensional data set
class TicTacToe:
    """
    management of a Tic Tac toe game
    does not do strategy
    """

    def __init__(self):
        """
        start a new game
        """
        self._board = [[' '] * 3 for j in range(3)]
        self._player = 'X'

    def mark(self, i, j):
        """
        put an X or O mark at position (i,j) for next player's turn
        :param i:
        :param j:
        :return:
        """
        if not (0 <= i <= 2 and 0<= j <= 2):
            raise ValueError("invalid board position")
        if self._board[i][j] != ' ':
            raise ValueError("board position occupied")
        if self.winner() is not None:
            raise ValueError("Game is already complete")
        self._board[i][j] = self._player
        if self._player == "X":
            self.player = "O"
        else:
            self._player = "X"

    def _is_win(self, mark):
        """
        Check whether the board configuration is a win for the given player.
        :param mark:
        :return:
        """
        board = self._board  # local variable for shorthand
        return (mark == board[0][0] == board[0][1] == board[0][2] or # row 0
                mark == board[1][0] == board[1][1] == board[1][2] or # row 1
                mark == board[2][0] == board[2][1] == board[2][2] or # row 2
                mark == board[0][0] == board[1][0] == board[2][0] or # column 0
                mark == board[0][1] == board[1][1] == board[2][1] or # column 1
                mark == board[0][2] == board[1][2] == board[2][2] or # column 2
                mark == board[0][0] == board[1][1] == board[2][2] or # diagonal
                mark == board[0][2] == board[1][1] == board[2][0]) # rev diagonal

    def winner(self):
        """

        :return: mark of winning player or None to indicate a tie
        """
        for mark in 'XO':
            if self._is_win(mark):
                return mark
            return None

    def __str__(self):
        """

        :return: string representation of current game board
        """
        rows = ['|'.join(self._board[r]) for r in range(3)]
        return '\n-----\n'.join(rows)



