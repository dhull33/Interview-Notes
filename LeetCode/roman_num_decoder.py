"""
Create a function that takes a Roman numeral as its argument and returns its
value as a numeric decimal integer. You don't need to validate the form of the
Roman numeral.

Modern Roman numerals are written by expressing each decimal digit of the
number to be encoded separately, starting with the leftmost digit and skipping
any 0s. So 1990 is rendered "MCMXC" (1000 = M, 900 = CM, 90 = XC) and 2008 is
rendered "MMVIII" (2000 = MM, 8 = VIII). The Roman numeral for 1666, "MDCLXVI",
 uses each letter in descending order.
"""

def solution(roman):
    """
    :param roman: string
    :return: int
    """
    if roman == "IV":
        return 4

    roman_nums = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }

    count_roman = {}
    for char in roman:
        if not char in count_roman:
            count_roman[char] = 1
        else:
            count_roman[char] += 1

    returned_int = 0
    for char in count_roman:
        if char in roman_nums:
            returned_int = returned_int + count_roman[char]*roman_nums[char]
    return returned_int
