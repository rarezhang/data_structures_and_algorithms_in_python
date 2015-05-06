class Progression:
    """iterator producing a generic progression.
    default iterator produces the whole number 0,1,2"""
    def __init__(self,start=0):
         """
         initialize current to the first value of the progression
         :return:
         """
         self._current = start

    def _advance(self):
         """
         update self._current to a new value.
         This should be overidden by a subclass to customize progreesion
         :return:
         """
         self._current += 1

    def __next__(self):
         """
         :return:the next element, or else raise StopIteration error
         """
         if self._current is None:
             raise StopIteration()
         else:
             answer = self._current
             self._advance()
             return answer

    def __iter__(self):
         """an iterator return itself as an iterator"""
         return self

    def print_progression(self, n):
         """Print next n values of the progression."""
         print(' '.join(str(next(self)) for j in range(n)))



class ArithmeticProgression(Progression):
    """
    iterator producing an arithmetic progression
    inherit from Progression
    """
    def __init__(self, increment= 1, start =0):
        """

        :param increment: the fixed constant to add to each item (default 1)
        :param start: the first term of the progression (default 0)
        :return:
        """
        super().__init__(start)   # initialize base class
        self._increment = increment

    def _advance(self):
        """
        update current value by adding the fixed increment.
        override inherited version
        :return:
        """
        self._current += self._increment


class GeometricProgression(Progression):
    """
    iterator producing a geometric progression.
    inherit from Progression
    """
    def __init__(self, base = 2, start = 1):
        """
        create a new geometric progression
        :param base: the fixed constant multiplied to each term(default 2)
        :param start: the first term of the progression (default 1)
        :return:
        """
        super().__init__(start)
        self._base = base

    def _advance(self):
        """
        update current value by multiplying it by the base value
        :return:
        """
        self._current *= self._base

class FibonacciProgression(Progression):
    """
    iterator producing a generalized Fibonacci progression
    """

    def __init__(self, first=0, second = 1):
        """
        create a new fibonacci progression
        :param first: the first term of the progression (default 0)
        :param second: the second term of the progression (default 1)
        :return:
        """
        super().__init__(first) # start progression at first
        self._prev = second - first

    def _advance(self):
        """
        update current value by taking sum of previous two
        :return:
        """
        self._prev, self._current = self._current, self._prev + self._current

class AbsoluteProgression(Progression):
    """
    each value in the progression is the absolute value of the difference between the
    previous two values.
    """
    def __init__(self, first= 2, second = 200):
        """
        :param first: the first term of the progression (default 2)
        :param second: the second term of the progression (default 200)
        :return:
        """
        super().__init__(first) # start progression at first
        self._prev = first+second
        self._current = first

    def _advance(self):
        """
        update current value by taking sum of previous two
        :return:
        """
        self._prev, self._current = self._current, abs(self._prev - self._current)


class SquarerootProgression(Progression):
    """
     each value in the progression is the square root of the previous value
    inherit from Progression
    """
    def __init__(self, start = 65536):
        """

        :param start: the first term of the progression (default 1)
        :return:
        """
        super().__init__(start)
        self._current = start

    def _advance(self):
        import math
        """
        update current value by multiplying it by the base value
        :return:
        """
        self._current = math.sqrt(self._current)