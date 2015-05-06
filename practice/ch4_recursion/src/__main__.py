__author__ = 'wlz'

#P172 factorial
def factorial(n):
    """
    implementation of a factorial function
    :param n: input integer
    :return:

    >>> factorial(0)
    1
    >>> factorial(5)
    120
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)


# P175 English ruler
def draw_line(tick_length,tick_label=''):
    """
    draw one line with given tick length (followed by tick label)
    :param tick_length:
    :param tick_label:
    :return:
    """
    line = '-'*tick_length
    if tick_label:
        line += ' '+tick_label
    print(line)

def draw_interval(center_length):
    """
    draw tick interval based on a central tick length
    :param center_length:
    :return:
    """
    if center_length >0: # stop when length drops to 0
        draw_interval(center_length-1) # recursively draw top ticks
        draw_line(center_length) # draw center tick
        draw_interval(center_length-1) #recurively draw bottom ticks


def draw_ruler(num_inches, major_length):
    """
    draw english ruler with given number of inches, major tick length
    :param num_inches:
    :param major_length:
    :return:
    """
    draw_line(major_length, '0') # draw inch 0 line
    for j in range(1,1+num_inches):
        draw_interval(major_length-1)  # draw interior ticks for inch
        draw_line(major_length,str(j)) # draw inch j line and label






if __name__ == "__main__":
    import doctest
    # factorial
    doctest.testmod(verbose=True)
    # draw ruler
    draw_ruler(2,4)