class ReversedSequenceIterator:
    """a reversed iterator for any of Python's sequence type"""

    def __init__(self,sequence):
        """create an iterator for the given sequence"""
        self._seq = sequence   # keep a reference to the underlying data
        self._k  = len(self._seq) # start from the last element

    def __next__(self):
        """return the next element, or stop iteration, reversed"""
        self._k -= 1     # to next index, reversed
        if self._k >= 0:
            return(self._seq[self._k])  # return the data element
        else:
            raise StopIteration()  # no more element

    def __iter__(self):
        """an iterator must return itself"""
        return self

