"""Exercise 1 :- Odd or Even (PracticePython.org)

Create a program that asks the user to enter their name and their age.
Print out a message addressed to them that tells them the year that they will turn 100 years old.
Note: for this exercise, the expectation is that you explicitly write out the year (and therefore be out of date the next year).

"""

# Importing modules
from datetime import date

# from dateutil.relativedelta import relativedelta

# Accepting inputs
name = input("Enter your Name - ")
age = input("Enter your Age - ")
# Computational logic
todays_date = date.today().year
year_of_100 = todays_date + 100 - int(age)

# Output
print(f"{name} with age {age} will turn 100 years old in {year_of_100}")


"""
___________________________________________________________
                        ROUGH WORK
___________________________________________________________

Logic of the code -
Accept input
    1. Name
    2. Age string
Output - Print the year they will turn 100
Computation logic -  todays date + age = year_of_100
___________________________________________________________
"""
