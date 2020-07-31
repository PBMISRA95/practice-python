
""" Exercise 5 :- List Overlap (PracticePython.org)

Problem Statement :- The following has to be implemented in Python

1) Take two user-input lists 
2) Find the common elements in exisiting in both the lists
3) Print the common elements existing in both the lists. Note no repition of common elements should be printed

"""

userlist1_raw = input("Enter the first list =")        #For taking user input as string
userlist2_raw = input("Enter the second list")         # Same as above

userlist1 =userlist1_raw.split()                        #.split makes each word in a string into element                          
userlist2 = userlist2_raw.split()                       # Same as above

list_of_duplicates =[]

print("\n The first list entered is :-" + str(userlist1))       
print("\n The second List entered is \n " + str(userlist2))

for element1 in userlist1:
    for element2 in userlist2:
        if(element2 == element1):
            list_of_duplicates.append(element1)

list_of_duplicates = list(dict.fromkeys(list_of_duplicates))   

 # How the above line 28 works :- first convert list into dictionery (which removes duplicate by keys) then convert back into list

print("\n The list of duplicates in both the list are as follows :- " + str(list_of_duplicates))


# End of Progam. Developed on 31-07-2020 by Priyabrat Mishra