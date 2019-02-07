"""
You might know some pretty large perfect squares. But what about the NEXT one?

Complete the findNextSquare method that finds the next integral perfect
square after the one passed as a parameter. Recall that an integral perfect
square is an integer n such that sqrt(n) is also an integer.

If the parameter is itself not a perfect square, than -1 should be returned.
You may assume the parameter is positive.
"""
import math

def find_next_square(sq):
    """
    :param sq: an integer
    :return: the next perfect square or -1 if sq is not a perfect square
    """
    found = False
    if str(math.sqrt(sq)) != "{}.0".format(str(math.sqrt(sq))[:-2]):
        return -1
    while not found:
        sq += 1
        if str(math.sqrt(sq)) == "{}.0".format(str(math.sqrt(sq))[:-2]):
            found = True
    return sq
