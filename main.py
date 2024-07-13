# -*- coding: utf-8 -*-
# Drivers' Menu
def driversMenu():
    message="This is the drivers' menu"
    return message


# Cities' Menu
def citiesMenu():
    message="This is the cities' menu"
    return message

#Menu Function
def menu():
    print("Hello! Please enter:")
    print("    1. To go to the drivers' menu")
    print("    2. To go to the cities' menu")
    print("    3. To exit the system")
    choice=int(input())
    choices=[1,2,3]
    while choice not in choices:
        print("Invalid input! Please try again: ")
        choice=int(input())
    if choice==1:
        print(driversMenu())
    elif choice ==2:
        print(citiesMenu())
    else:
        print("The system is exiting. Good bye!")
        stop= True

menu()

