"""
5. Write a function that counts the number of vowels and
   returns the maximum value.
Example: count_vowels("h e l l o") -> 2
"""


def count_vowels(input_str: str) -> tuple[int, str]:
    vowels_dict = {
        "a": 0,
        "A": 0,
        "e": 0,
        "E": 0,
        "i": 0,
        "I": 0,
        "o": 0,
        "O": 0,
        "u": 0,
        "U": 0,
    }
    for char in input_str:
        if char in vowels_dict:
            vowels_dict[char] += 1
    max_value = max(vowels_dict.values())
    max_vowel = max(vowels_dict, key=vowels_dict.get)
    return max_value, max_vowel
