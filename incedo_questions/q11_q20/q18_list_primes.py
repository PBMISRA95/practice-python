"""
Q18. Write a function that returns a list of all prime numbers less than
or equal to a given limit.
Example: list_primes(10) -> [2, 3, 5, 7]
Author - Priyabrat Mishra
Date - 03rd December 2025
"""


def list_primes(input_num: str) -> list[int]:
    output_list = []
    if input_num == 1:
        return [1]
    else:
        for number in range(2, input_num):  # Iterating through each number until target
            divisor_count = 1
            for num in range(2, number):  # Iterating to find divisors of a certain number
                if number % num == 0:
                    divisor_count += 1

            if divisor_count < 2:
                output_list.append(number)

        return output_list


if __name__ == "__main__":
    input_num = 1
    print(f"The output of {input_num} is {list_primes(input_num)}")
