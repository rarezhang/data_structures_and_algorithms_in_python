"""
exceptions
"""

class Empty(Exception):
    """
    error attempting to access an element from an empty container
    """
    pass


class Full(Exception):
    """
     when the stack is at full capacity
    """
    pass