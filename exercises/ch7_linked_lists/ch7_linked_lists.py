"""
ch7 linked lists
"""
from PositionalList import PositionalList


# P 307
def insertion_sort(L):
    """
    sort PostitionalList of comparable elements into non-decreasing order
    important variable:
    - marker: the rightmost position of the currently sorted portion of a list
    - pivot: the position just past the marker
    - walk: move leftward from the marker, as long as there remains a preceding element with value larger than the pivot's
    e.g.,
    {  [15, 22, 25, 29, 36]       23, 53, 11, 42}
               walk    marker    pivot
       -- sorted portion --

    :param L: PositionalList
    :return:
    """
    assert isinstance(L, PositionalList), "L is not a PositionalList"

    if len(L) > 1:  # otherwise, no need to sort it
        marker = L.first()
        while marker != L.last():
            pivot = L.after(marker)  # next item to place
            value = pivot.element()
            if value > marker.element():  # pivot is already sorted
                marker = pivot
            else:  # must relocate pivot
                walk = marker  # find leftmost item greater than value
                while walk != L.first() and L.before(walk).element() > value:
                    walk = L.before(walk)
                L.delete(pivot)
                L.add_before(walk, value)  # reinsert value before walk


pl = PositionalList()
num = [15,22,25,29,36,23,53,11,42]
for n in num:
    pl.add_last(n)

print('PositionalList before sorting: ', pl)
insertion_sort(pl)
print('PositionalList after sorting: ', pl)


# P 309
class FavoritesList:
    """
    list of elements ordered from most frequently accessed to lest
    """

    # ------------ nested _Item class ---------------------------
    class _Item:
        __slots__ = '_value', '_count'  # streamline memory usage

        def __init__(self, element):
            self._value = element  # the user's element
            self._count = 0  # access count initially zero

    # ------------ non-public utilities --------------------------
    def _find_position(self, element):
        """
        search for element and return its Position (or None if not found)
        :param element:
        :return:
        """
        walk = self._data.first()
        while walk is not None and walk.element()._value != element:
            walk = self._data.after(walk)
        return walk

    def _move_up(self, position):
        """
        move item at position earlier in the list based on access count
        :param position:
        :return:
        """
        if position != self._data.first():  # consider moving
            cnt = position.element()._count
            walk = self._data.before(position)
            if cnt > walk.element()._count:  # must shift forward
                while (walk != self._data.first() and cnt > self._data.before(walk).element()._count):
                    walk = self._data.before(walk)
                self._data.add_before(walk, self._data.delete(position))  # delete / reinsert

    # ------------ public methods ---------------------------------
    def __init__(self):
        """
        create an empty list of favorites
        """
        self._data = PositionalList()  # list of _Item instances

    def __len__(self):
        """
        return number of entries on favorites list
        :return:
        """
        return len(self._data)

    def is_empty(self):
        """
        return True if list is empty
        :return:
        """
        return len(self._data) == 0

    def access(self, element):
        """
        access element, thereby increasing its access count
        :param element:
        :return:
        """
        position = self._find_position(element)  # try to locate existing element
        if position is None:
            position = self._data.add_last(self._Item(element))  # if new, place at end
        position.element()._count += 1  # always increment count
        self._move_up(position)  # consider moving forward

    def remove(self, element):
        """
        remove element from the list of favorites
        :param element:
        :return:
        """
        position = self._find_position(element)  # try to locate existing element
        if position is not None:  # delete if found
            self._data.delete(position)

    def top(self, k):
        """
        generate sequence of top k elements in terms of access count
        :param k:
        :return:
        """
        if not 1 <= k <= len(self):
            raise ValueError('Illegal value for k')
        walk = self._data.first()
        for j in range(k):
            item = walk.element()  # element of list is _Item
            yield item._value
            walk = self._data.after(walk)

    def clear(self):
        """
        returns the list to empty.
        :return:
        """
        self._data = PositionalList()

    def reset_counts(self):
        """
         resets all elements’ access counts to zero (while leaving the order of
         he list unchanged).
        :return:
        """
        cursor = self._data.first()
        while cursor is not None:
            cursor.element()._count = 0
            cursor = self._data.after(cursor)


# P 313
class FavoritesListMTF(FavoritesList):
    """
    List of elements ordered with move-to-front heuristic
    """

    # override _move_up to provide move-to-front semantics
    def _move_up(self, position):
        """
        move accessed item at Position to front of list
        :param position:
        :return:
        """
        if position != self._data.first():
            self._data.add_first(self._data.delete(position))

    # override top() -> list is no longer sorted
    def top(self, k):
        """
        generate sequence of top k elements in terms of access count
        :param k:
        :return:
        """
        if not 1 <= k <= len(self):
            raise ValueError('illegal value for k')

        # making a copy of the original list
        temp = PositionalList()
        for item in self._data:  # positional lists support iteration
            temp.add_last(item)

        # repeatedly find, report and remove element with largest count
        for j in range(k):
            # find and report next highest from temp
            highPos = temp.first()
            walk = temp.after(highPos)
            while walk is not None:
                if walk.element()._count > highPos.element()._count:
                    highPos = walk
                walk = temp.after(walk)
            # found the element with highest count
            yield highPos.element()._value  # report element to user
            temp.delete(highPos)  # remove from temp list




