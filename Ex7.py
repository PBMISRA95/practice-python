"""Exercise 7 :- List Comprehension (PracticePython.org)

Problem Statement :- The following has to be implemented in Python

1) To take user input list
2) Generate a new list containing only even numbers entered in the user-input list

"""

input_str = input("Enter the list")
usr_input_list = list(input_str.split())
print("The entered user input list is :- ")
print(usr_input_list)

only_even_list = [
    num for num in usr_input_list if int(num) % 2 == 0
]  # Logic of obtain even numbers using List comprehension

print("The list with only even numbers are as follow : \n" + str(only_even_list))

"""Line 16 can also be written as:-

only_even_list = []
for num in usr_input_list:
    if int(num)%2 == 0:
        only_even_list.append(num)

"""


# End of Progam. Developed on 01-08-2020 by Priyabrat Mishra
