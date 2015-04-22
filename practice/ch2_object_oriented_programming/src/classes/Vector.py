class Vector:
    """represent a vector in a multidimensional space"""
    def __init__(self,d):
        """create d-dimensional vector of 0"""
        self._coords = [0]*d # a list

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






