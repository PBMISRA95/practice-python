"""
14. Write a function that takes a list of dictionaries and sorts it by the "name" key
ascending order.
Example -
data = [{"name": "Bob", "age": 25},
        {"name": "Alice", "age" : 30}]
Date - 03rd November 2025, Monday
Author - Priyabrat Mishra
"""


def sort_dict(input_list: list[dict]) -> list[dict]:
    output_sorted_list = sorted(input_list, key=lambda item: item["name"])
    return output_sorted_list
