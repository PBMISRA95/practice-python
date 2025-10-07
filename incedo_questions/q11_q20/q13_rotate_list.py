"""
13. Write a function that rotates a list to the right by k steps using slicing.
Example: rotate_list([1, 2, 3, 4, 5], 2) → [4, 5, 1, 2, 3]
"""


def rotate_list(input_list: list[int], k: int) -> list[int]:
    first_chunk = input_list[-k::]
    second_chunk = input_list[: len(input_list) + 1 - k :]
    output = first_chunk + second_chunk
    return output
