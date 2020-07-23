
""" Exercise 2 :- Odd or Even (PracticePython.org)

Problem Statement :- It accepts two numbers. Then it checks the following

1) Whether it is a multiple of 4.
2) Whether the first number is divisible by the second number.
3) Whether the first number is off or even.

"""

num = int(input("Enter the first number = "))
num2 = int(input("Enter the second number = "))

# This is the first part of the program.
if num%4 == 0:
    print(str(num) + " is divisible by 4")
else:
    print(str(num) + " is not divisible by 4")

# This is the second part of the program.

if num%num2 == 0:
    print(str(num) +" is divisible by " + str(num2))
else:
    print(str(num) +" is not divisible by " + str(num2))

# This is the 3rd part of the program.

if num%2 == 0:
    print(str(num) +" is even" )
else:
    print(str(num) +" is odd")