class SequenceIterator:
    """an iterator for any of Python's sequence type"""

    def __init__(self,sequence):
        """create an iterator for the given sequence"""
        self._seq = sequence   # keep a reference to the underlying data
        self._k  = -1 #will increment to 0 on first call to next

    def __next__(self):
        """return the next element, or stop iteration"""
        self._k += 1     # to next index
        if self._k < len(self._seq):
            return(self._seq[self._k])  # return the data element
        else:
            raise StopIteration()  # no more element

    def __iter__(self):
        """an iterator must return itself"""
        return self
