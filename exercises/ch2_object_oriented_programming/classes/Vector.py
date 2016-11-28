class Vector:
    """represent a vector in a multidimensional space"""
    def __init__(self,d):
        """
        d: int: create d-dimensional vector of 0
        d: list: create vector with the sequence value
        :param d: int or list
        :return: create a new vector
        """
        if isinstance(d, int):
            """create d-dimensional vector of 0"""
            self._coords = [0]*d # a list
        elif isinstance(d, list):
            """create vector with the sequence value"""
            self._coords = [0]*len(d)
            for j in range(len(d)):
                self[j] = d[j]
        else:
            raise TypeError('the input must be an int or a list.')

    def __len__(self):
        """return the dimension of the vecotr"""
        return len(self._coords) # the len of the list

    def __getitem__(self,j):
        """return j th coordinate of vector"""
        return self._coords[j]

    def __setitem__(self,j,val):
        """set j th coordinate of vector"""
        self._coords[j] = val

    def __add__(self,other):
        """return sum of two vector"""
        if len(self)!=len(other):
            raise ValueError('dimensions must be agree')
        result = Vector(len(self))  # a vector
        for j in range(len(self)):
            result[j]=self[j]+other[j]
        return result

    def __radd__(self, other):
        """
        return sum of list + vector
        :param other: list
        :return:
        """
        if len(self)!=len(other):
            raise ValueError('dimensions must be agree')
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = self[j]+other[j]
        return result

    def __sub__(self, other):
        """
        return difference between two vector.
        :param other: another vector.
        :return: difference between two vector.
        """
        if len(self) != len(other):
            raise ValueError('dimensions must be agree')
        result = Vector(len(self)) # a vector
        for j in range(len(self)):
            result[j] = self[j] - other[j]
        return result

    def __neg__(self):
        """
        returns a new vector instance
        :return: coordinates are all the negated values of the respective coordinates
        """
        if len(self) == 0:
            return self
        else:
            result = Vector(len(self))
            for j in range(len(self)):
                result[j] = self[j] * -1
            return result

    def __mul__(self, other):
        """
        vector * int, returns a new vector with coordinates that are x times the respective coordinates of v.
        vector * vector, dot product.
        :param other: number or vector
        :return: vector or number
        """
        if isinstance(other, (int,float)):
            result = Vector(len(self))
            for j in range(len(self)):
                result[j] = self[j] * other
        elif isinstance(other, (Vector)):
            if len(self)!=len(other):
                raise ValueError('dimension must be agree')
            result = 0
            for j in range(len(self)):
                result += self[j] * other[j]
        else:
            raise TypeError('multiple must be a number or a Vector')
        return result


        return result

    def __rmul__(self, multiple):
        if not isinstance(multiple, (int,float)):
            raise TypeError('multiple must be a number')
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = self[j] * multiple
        return result

    def __eq__(self,other):
        """return True if vetor has same coordinate"""
        # == belong to list
        return self._coords == other._coords  # _coords is a list

    def __ne__(self,other):
        """return true if vector differs from other"""
        # == is from the __eq__ defined above
        return not self == other

    def __str__(self):
        """produce string representation of vector"""
        return '<'+str(self._coords)[1:-1]+'>' # adapt list representation

"""
    def __mul__(self, multiple):
        if not isinstance(multiple, (int,float)):
            raise TypeError('multiple must be a number')
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = self[j] * multiple
        return result"""




