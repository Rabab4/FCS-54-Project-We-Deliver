# -*- coding: utf-8 -*-
# Drivers' Menu
def driversMenu():
    stop=False
    while not stop:
        print("Hello! This is the Drivers' Menu.")
        print("Please enter:")
        print("    1. To view all drives")
        print("    2. To add a driver")
        print("    3. To go back to the main menu")
        choice=int(input())
        choices=[1,2,3]
        while choice not in choices:
            print("Invalid input! Please try again: ")
            choice=int(input())
        if choice==1:
            print(viewDrivers())
        elif choice ==2:
            print(addDriver())
        else:
            print("Back to main menu")
            stop= True
            
#View Drivers
def viewDrivers():
    message="this function shows a list of all the drivers and their detail is printed to the users"
    return message

#Add a Driver
def addDriver():
    message="this function enables the user to add the name and start city of the driver to the system"
    return message

# Cities' Menu
def citiesMenu():
    message="This is the cities' menu"
    return message

#Menu Function
def menu():
    stop=False
    while not stop:
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
            driversMenu()
        elif choice ==2:
            print(citiesMenu())
        else:
            print("The system is exiting. Good bye!")
            stop= True


menu()
