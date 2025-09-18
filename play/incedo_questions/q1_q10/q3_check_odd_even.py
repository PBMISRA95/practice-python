"""
3. Write a function that takes an integer and returns "even" if it's even, "odd" if it's odd.
Example: check_even_odd(5) → "odd"
"""

# input_num = int(input("Enter an integer - "))


def check_even_odd(input_num: int) -> str:
    if input_num % 2 == 0:
        return "even"
    else:
        return "odd"


# print(f"The integer {input_num} is {check_even_odd(input_num)}")

# Logic 2 - Use of ternary operator
"""
def check_even_odd(input_num:int) -> str:
    return "even" if input_num % 2 == 0 else "odd"
    """
