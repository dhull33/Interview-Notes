# -*- coding: utf-8 -*-
"""This module demonstrates recursion with the Fibonacci sequence"""
def get_fib(position):
    """
    Calculates the nth fibonacci number where n=position
    Args:
        position (int): Fibonacci number to be calculated
    Returns:
        int: the nth fibonacci number
    """
    if position == 0:
        return 0
    if position == 1:
        return 1
    return get_fib(position - 1) + get_fib(position - 2)
