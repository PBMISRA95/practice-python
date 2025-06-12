"""Exercise 3 :- List less than Ten (PracticePython.org)

Problem Statement :- The following has to be implemented in Python

1) To read from a List and then display numbers below 5 in the sample list
2) To read a number from the user and then display numbers below that user input number in the sample list
3) To use a list to store the numbers in both 1) and 2) and use it to display rather than displaying it one by one

"""

# Part one accepts the user input list of number and checks for numbers less than 5
x_input = input("Enter the numbers in of list = ")
print("\n")
x_input_list = x_input.split()
print("\n The elements which were given as input as follows :- " + str(x_input_list))
print("\n The following elements of the given above list are less than 5 ")

x_input_less_5 = []

for element in x_input_list:
    if int(element) < 5:
        x_input_less_5.append(element)

print("\n " + str(x_input_less_5))

# Part two accepts a number from user and checks for numbers in the above list which are less than the user input number

x_new = int(input("Enter a number = "))
print("\n The number entered is " + str(x_new))

x_input_new = []

for i in x_input_list:
    if int(i) < x_new:
        x_input_new.append(i)

print(
    "\n The following elements of the given above user input list are less than "
    + str(x_new)
    + "\n "
    + str(x_input_new)
)

# End of Progam. Developed on 23-07-2020 by Priyabrat Mishra
