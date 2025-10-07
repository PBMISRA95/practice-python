"""
2. Write a function that takes a list of numbers and returns their sum.
Example: sum_list([1, 2, 3, 4]) → 10
"""

# Logic 1 - Using the built function sum()


def sum_list(input_list: list) -> int:
    output = sum(input_list)
    return output


# print(f"The sum of {input_list} is {sum_list(input_list)}")
"""
 Logic 2 - Using For loop

def sum_list(input_list: list) -> int:
    for num in input_list:
        sum += num
    return sum
"""
