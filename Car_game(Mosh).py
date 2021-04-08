#Just a small game which takes input as start/stop and exit from the user. This is for understanding while loop.

import time
print("""\nWelcome to the game
\nMENU
\nEnter one of the following :
Start - To start the car
Stop - To stop the car
Exit - To exit the game
Help - To review the Menu""")
car_status_new = ""
car_status_old = ""

while True:
    car_status_new = input("\nEnter your input : ").upper()
   
    if car_status_new == "START":                       #Checks if the car is already started. If not then starts it if is said to.
        if car_status_new == car_status_old:
            print("\nHey!!The car is already started")
        else:
            print("\nThe car has been started now.")
            car_status_old = car_status_new
   
    elif car_status_new == "STOP":                      #Checks if the car is already stopped. If not then stops it if is said to.
        if car_status_new == car_status_old:
            print("\nHey!!The car is already stopped.")
        else:
            print("\nThe car has been stopped now.")
            car_status_old = car_status_new

    elif car_status_new == "HELP":
       print("""\nWelcome to the game
\nMENU
\nEnter one of the following :
Start - To start the car
Stop - To stop the car
Exit - To exit the game
Help - To review the Menu""")

    elif car_status_new == "EXIT":
        print("\nGoodBye! Exiting in few seconds.\n")
        time.sleep(2)                                   # Implementing a delay functionality
        break
    else:
        print("\nI don't Understand that ")
        
#End of Program. First Done on 07-04-2021.