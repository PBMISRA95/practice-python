"""
1. Write a function that takes a string as input and returns it reversed.
Example: reverse_string("hello") → "olleh"
"""

input_string = input("Enter a string - ")
# output_string = reverse_string(input_string)


def reverse_string(input_string: str) -> str:
    return input_string[::-1]


output_string = reverse_string(input_string)
print(f"The reverse of {input_string} is {output_string}")
# print(reverse_string("hello"))
