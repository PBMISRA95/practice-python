"""
Q19. Write a function that returns the greatest common divisor (GCD) of two integers.
Example - gcd(48, 18) -> 6
"""


def gcd(num1: int, num2: int) -> int:
    """Calculate GCD using Euclidean algorithm"""
    i = 1
    while num2 != 0:
        remainder = num1 % num2
        num1 = num2
        num2 = remainder

        print(f"Iteration no {i} | num1 = {num1} | num2 = {num2}")
        i += 1
    return num1


if __name__ == "__main__":
    num1 = 48
    num2 = 18
    print(f"The GCD of {num1} and {num2} is {gcd(num1, num2)}")
