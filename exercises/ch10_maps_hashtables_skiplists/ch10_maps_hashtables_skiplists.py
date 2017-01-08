"""
chapter 10
Maps, Hash Tables and Skip Lists
"""
from SortedTableMap import SortedTableMap

# P 427
def word_count(file_path):
    """
    word count
    determine which word has the most occurrences
    :param file_path:
    :return:
    """
    freq = {}
    for piece in open(file_path, encoding='utf-8').read().lower().split():
        # only consider alphabetic characters within this piece
        word = ''.join(c for c in piece if c.isalpha())
        if word:  # require at least one alphabetic character
            freq[word] = 1 + freq.get(word, 0)  # dic.get(key, default value)

    max_word = ''
    max_count = 0
    for (w, c) in freq.items():  # (key, value) tuples represent (word, count)
        if c > max_count:
            max_word = w
            max_count = c
    print('the most frequent word is:', max_word)
    print('its number of occurrences is: ', max_count)
    return max_word, max_count


path = '..\\..\\README.md'
# word_count(path)


# P 436
# cyclic-shift hash code computation for character string
def hash_code(s):
    """
    cyclic-shift hash code computation for character string
    :param s: string
    :return:
    """
    mask = (1 << 32) - 1  # limit to 32-bit integers
    h = 0
    for character in s:
        h = (h << 5 & mask) | (h >> 27)  # 5-bit cyclic shift of running sum
        h += ord(character)  # add in value of next character
    return h

s = 'apple'
print(hash_code(s))
print(hash(s))  # python built in hash function, return the hash value of the object
print(hash(5), hash(5.0))


# P 458
# dominates pair (a,b):
# - (c,d) != (a,b)
# - a >= c and b >= d
# maximum pair: it is not dominated by any other pair
# an implementation of a class maintaining a set of maximum cost-performance pairs using a sorted map
class CostPerformanceDatabase:
    """
    maintain a database of maximal (cost,performance) pairs
    """

    def __init__(self):
        """
        create an empty database
        """
        self._M = SortedTableMap()  # or a more efficient sorted map

    def best(self, c):
        """
        return (cost, performance) pair with largest cost not exceeding c
        :param c: cost as key
        :return:
        """
        return self._M.find_le(c)

    def add(self, c, p):
        """
        add new entry with cost c and performance p
        worst case: O(n)
        :param c:
        :param p:
        :return:
        """
        # determine if (c,p) is dominated by an existing pair
        # other = (key, value) = (cost, performance)
        other = self._M.find_le(c)  # other is at least as cheap as c
        if other is not None and other[1] >= p:  # if other performance is as good as p, other[1]->performance
            return  # (c,p) is dominated, so ignore
        self._M[c] = p   # else, add (c,p) to database
        # remove any pairs that are dominated by (c,p)
        other = self._M.find_gt(c)  # other more expensive than c
        while other is not None and other[1] <= p:
            del self._M[other[0]]  # other[0] -> key
            other = self._M.find_gt(c)
