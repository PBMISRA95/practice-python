"""
14. Write a function that takes a list of numbers and return the arithmetic mean
(return None in ascending order)
Example -
average_list([4,8]) -> 6.0
Date - 10th November 2025, Monday
Author - Priyabrat Mishra
"""


def average_list(input_list: list[int] = None) -> int | None:
    if input_list:
        return int(sum(input_list) / len(input_list))
    else:
        return None


# print(average_list([1,2,3,4,5]))
# print(average_list())
