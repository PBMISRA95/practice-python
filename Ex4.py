"""Exercise 4 :- List all the divisors of a number (PracticePython.org)

Problem Statement :- The following has to be implemented in Python

1) Take a user input number
2) Find all the divisors of that number
3) Print all the divisors of that number

"""

num = int(input("Enter the number = "))
print("The number entered is " + str(num))
num_check_div_list = range(1, num + 1)  # Will have all number 1 to n
num_div_list = []  # Will have the divisors after checking condition 1
for element in num_check_div_list:
    if num % element == 0:  # Condition 1
        num_div_list.append(element)

print("The list of divisors are:- " + str(num_div_list))


# End of Progam. Developed on 31-07-2020 by Priyabrat Mishra
