
""" Exercise 6 :- String Lists (PracticePython.org)

Problem Statement :- The following has to be implemented in Python

1) To take user input string
2) Check whether the string is Palindrome

"""
str_input = input("Enter a string :- ")
str_input_rev = str_input[len(str_input)::-1]

print("The entered String is "+str_input)
print("The reverse of the String is "+ str_input_rev)
flag =False

#Both the logics have been commented below. To use them add #(hash) symbol in front of (""") symbol one of either of logics.

"""
if(str_input == str_input_rev):
    flag = True                                     #1st logic of palidrome checking
"""

"""
for i in range(0,int(len(str_input))):
    if(str_input[i] != str_input_rev[i]):
        flag = False                                #2nd Logic of Palindrome checking using loop
        break
    else:
        flag = True
"""

if flag:
    print(str_input + " is a palindrome")
else:
    print(str_input + " is not a palindrome")


# End of Progam. Developed on 01-08-2020 by Priyabrat Mishra