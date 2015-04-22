class Range:
    """a class that mimic the built-in range calass"""

    def __init__(self,start,stop=None,step=1):
        """initialize a Range instance.
        Semantics is similar to built-in range class."""
        if step == 0:
            raise ValueError('step cannot be 0')
        if stop is None:  # spacial case of range(n)
            start, stop = 0, start
        # calculate the effective length
        self._length = max(0,(stop - start + step -1))
        # need start and step for the __getitem__ method
        self._start = start
        self._step = step

        def __len__(self):
            """return number of entries in the range"""
            return self._length

        def __getitem__(self, k):
            """return entry at index k """
            if k < 0:   # convert negative index
                k += len(self)
            if not 0 <= k < self._length:
                raise IndentationError('index out of range')
            return self._start + k * self._step
