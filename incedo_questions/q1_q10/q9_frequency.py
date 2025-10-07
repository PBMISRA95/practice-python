"""
Q9. Write a function that takes a string and returns a dictionary with frequency of each word.
Example - word_frequency("the cat the dog") -> {"the": 2, "cat": 1, "dog" : 1}
"""


def frequency_of_words(input_str: str) -> dict[str, int]:
    frequency_dict = {}
    """                 LOGIC 1
    return {word: input_str.count(word) for word in input_str.split()}
    """

    # """                 LOGIC 2
    for word in input_str.split():
        frequency_dict[word] = input_str.count(word)
    return frequency_dict
    # """


# print(frequency_of_words("the cat the dog"))
