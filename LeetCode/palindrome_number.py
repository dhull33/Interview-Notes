"""
Determine whether an integer is a palindrome. An integer is a palindrome
when it reads the same backward as forward.
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

def isPalindrome(x: 'int') -> 'bool':
    if x >= 0:
        if reverse(x) == x:
            return True
    return False
