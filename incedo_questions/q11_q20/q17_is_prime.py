"""
Q17. Write a function that checks whether an integer is prime.
Example: is_prime(11) -> True
Date - 02nd December 2025
Author - Priyabrat Mishra
"""


def is_prime(input_num: int) -> bool:
    if input_num <= 1:
        return False

    divisor_count = 0
    for num in range(1, input_num):
        if input_num % num == 0:
            divisor_count += 1

    if divisor_count > 2:
        return False
    else:
        return True


if __name__ == "__main__":
    num = 6
    print(f"{5} is a Prime Number {is_prime(5)}")
