"""
Write a function that returns a dictionary of character counts in a string.
Example : count_chars("hello") -> {'h': 1, 'e' : 1, 'l' : 2, 'o' : 1}
"""


def count_chars(input_str: str) -> dict:
    char_dict = {}
    for char in input_str:
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    return char_dict


"""
Steps I need to do:
1. Make a char_dict which I will return
2. iterate through the each char of input_str
    2.1. check if the character exists in char_dict
        if yes then increment the value by 1
        if not then add char as key and value as 1
2. return the char_dict
"""
