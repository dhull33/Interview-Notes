"""
Given a non-empty array of integers, every element appears three times except
for one, which appears exactly once. Find that single one.
"""
def single_number(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    count_of_nums = {}
    # Put elements in dictionary and count them
    for num in nums:
        if not num in count_of_nums:
            count_of_nums[num] = 1
        else:
            count_of_nums[num] += 1
    # Iterates through elements in count_of_nums and returns element with 1
    for number in count_of_nums:
        if count_of_nums[number] == 1:
            return number

# A faster implementation that uses Counter
def single_number2(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    from collections import Counter
    counts = Counter(nums)
    for number, count in counts.items():
        if count != 3:
            return number
