"""
4. Write a function to compute the factorial of a non-negative integer.
Example: factorial(5) -> 120
"""


def factorial(input_num: int) -> int:
    result = 1
    if input_num == 0:
        return result
    else:
        """
        for i in range(1,input_num+1):
            result = i * result
            i += 1
        return result
        """
        return input_num * factorial(input_num - 1)
