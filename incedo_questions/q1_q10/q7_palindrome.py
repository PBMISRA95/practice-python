"""
Q7. Write a function that checks if a string is a palindrome (case-insensitive)
Example - is_palindrome("Racecar") -> True
"""


def is_palindrome(input_str: str) -> bool:
    if len(input_str) % 2 == 0:
        return input_str == input_str[::-1]
    else:
        return False
