"""
chapter 10
Maps, Hash Tables and Skip Lists
"""


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