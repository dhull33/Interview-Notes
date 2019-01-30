# -*- coding: utf-8 -*-
"""
    Assume we are dealing with an environment which could only store integers
    within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose
    of this problem, assume that your function returns 0 when the reversed
    integer overflows.
"""
def reverse(x):
    """
    :type x: int
    :rtype: int
    """
    positive_x = abs(x)
    reversed_int = 0
    while positive_x > 0:
        remainder = positive_x % 10
        reversed_int = reversed_int * 10 + remainder
        positive_x = positive_x // 10
    if x < 0:
        reversed_int = reversed_int * -1
    if reversed_int < -2**31 or reversed_int > ((2**31) - 1):
        return 0
    return reversed_int
