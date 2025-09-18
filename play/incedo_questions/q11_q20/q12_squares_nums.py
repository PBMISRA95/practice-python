"""
12. Write a function that squares numbers in a list if they are odd, using a list comprehension with a conditional.
Example: square_odds([1, 2, 3, 4]) -> [1, 2, 9, 4]
"""


def square_odds(input_list: list[int]) -> list[int]:
    result = []
    for num in input_list:
        if num % 2 != 0:
            result.append(num**2)  # Square the number
        else:
            result.append(num)  # Keep even numbers as is
    return result
