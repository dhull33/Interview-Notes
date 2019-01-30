# -*- coding: utf-8 -*-
"""This module implements quick sort"""
def quicksort(array):
    """ Input a list.
        Output a sorted list."""
    quicksort_helper(array, 0, len(array) - 1)
    return array

def quicksort_helper(array, first, last):
    if first < last:
        split_point = partition(array, first, last)

        quicksort_helper(array, first, split_point - 1)
        quicksort_helper(array, split_point + 1, last)

def partition(array, first, last):
    pivot_value = array[first]

    left_point = first + 1
    right_point = last

    done = False
    while not done:
        while (left_point <= right_point) and (array[left_point] <= pivot_value):
            left_point = left_point + 1

        while (array[right_point] >= pivot_value) and (right_point >= left_point):
            right_point = right_point - 1

        if right_point < left_point:
            done = True
        else:
            temp = array[left_point]
            array[left_point] = array[right_point]
            array[right_point] = temp

    temp = array[first]
    array[first] = array[right_point]
    array[right_point] = temp
    return right_point
