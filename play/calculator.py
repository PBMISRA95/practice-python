"""
Program to make a simple calculator using Python.

It takes two numbers and an operator as input from the user and returns the result.
The calculator supports the following operations:
1. Addition (+)
2. Subtraction (-)
3. Multiplication (*)
4. Division (/)

"""

# calculator program
print("\n\nWelcome to the Simple Calculator!")


def calculator(number1: int, number2: int, option: int) -> int:
    if option == 1:
        result = number1 + number2
    elif option == 2:
        result = number1 - number2
    elif option == 3:
        result = number1 * number2
    elif option == 4:
        result = number1 / number2
    return result


while True:
    option = 10
    result = -1
    print("\nMenu:\n1. Addition \n2. Subtraction \n3. Multiplication \n4. Division \n0. Exit\n")
    option = int(input("Select operator option:  "))

    if option == 0:
        break
    elif option == 1 or option == 2 or option == 3 or option == 4:
        number1 = int(input("Enter first number: "))
        number2 = int(input("Enter second number: "))
        result = calculator(number1, number2, option)
        print(f"\nThe result of selected operation is: {result}")
    else:
        print("Incorrect option selected!")
