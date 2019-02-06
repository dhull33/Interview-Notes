"""
Given an array of integers, return indices of the two numbers such
that they add up to a specific target.

You may assume that each input would have exactly one solution, and
you may not use the same element twice.
"""

def two_sum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    indices = []
    for i in range(0, len(nums)):
        for j in range(1, len(nums)):
            if i != j:
                if nums[j] == target - nums[i]:
                    indices.append(i)
                    indices.append(j)
                    return indices
