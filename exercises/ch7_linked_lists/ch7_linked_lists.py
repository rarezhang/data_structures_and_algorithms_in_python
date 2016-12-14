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