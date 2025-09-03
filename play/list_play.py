"""
Title: My experiments with List and for loop
Date : 03rd Sept 2025
Author : Priyabrat Mishra
"""

print("Hello World!")

for num in range(0, 10):
    print(f"Number 1 is - {num}")

integers = [1, 2, 3, 4, 5]
list_of_integers = list(range(0, 10))

for num in list_of_integers:
    print(f"INteger list: {num}")
print(f"The list of integers is as follows : \n{list_of_integers}")
print(f"The integers is as : {integers}")

for i, n in enumerate(list_of_integers):
    print(f"The index is : {i} and the associated number is: {n}")
