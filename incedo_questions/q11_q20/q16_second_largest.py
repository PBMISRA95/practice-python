"""
16. Write a function that returns the second-largest unique number in a list
(raise an error if the list has fewer than two unique values).
Example:
second_largest([4, 1, 7, 7, 3]) → 4
Date - 14th November 2025
Author - Priyabrat Mishra
"""


def second_largest(input_list: list[int]) -> int:
    largest = max(input_list)
    second_large = 0
    for num in input_list:
        if num < largest:
            if second_large < num:
                second_large = num
    return second_large


if __name__ == "__main__":
    print(second_largest([1, 2, 3, 4, 5]))
