"""
Q8. Write a function that removes duplicates from a list and returns the result.
    Example - remove_duplicates([1, 2, 2, 3, 4, 4]) -> [1, 2, 3, 4]
"""


def remove_duplicates(input_nums: list[int]) -> list[int]:
    return list(set(input_nums))
