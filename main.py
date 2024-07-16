# -*- coding: utf-8 -*-
#class Driver
class Driver:
    def __init__(self, driver_id, driver_name, start_city):
        self.driver_id = driver_id
        self.name = driver_name
        self.start_city = start_city
# Drivers' Menu
def driversMenu():
    stop=False
    while not stop:
        print("Hello! This is the Drivers' Menu.")
        print("Please enter:")
        print("    1. To view all drives")
        print("    2. To add a driver")
        print("    3. To go back to the main menu")
        choice=int(input("Enter your choice: "))
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
    if not drivers_db:
        print("No drivers in database")
    else:
        for driver in drivers_db:
            print(driver)

#Add a Driver
def addDriver():
    global driver_count
    add=True
    while add:
        driver_name = input("Enter the name of the driver: ")
        start_city = input("Enter the start city of the driver: ")

        if start_city.lower() not in [city.lower() for city in cities_db]:
            print(f"{start_city} is not in the database.")
            add_city_choice = input("Do you want to add this city to the database? (yes/no): ").strip().lower()
            #account for invalid input
            if add_city_choice == "yes":
                cities_db.append(start_city)
                print(f"{start_city} has been added to the database.")
                print("Update Cities Database: ")
                print(cities_db)
            else:
                print("Driver not added. Returning to Drivers' Menu.")
                return
        
        driver_count += 1
        driver_id = f"ID{driver_count:03}"
        new_driver=Driver(driver_id,driver_name,start_city)
        drivers_db.append(new_driver)
        print(f"Driver {driver_name} added successfully with ID {driver_id}.")
        add_choice=input("Do you want to add another driver? (yes/no): ").strip().lower()
        #account for invalid input
        if add_choice=="no":
            add = False
            print("Finished Adding drivers! Back to drivers' menu.")
            
            

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
        choice=int(input("Enter your choice: "))
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



driver_count = 0
cities_db=["Saida", "Beirut", "Tyre", "Nabatieh", "Tripoli", "Jounieh", "Byblos", "Alay"]
drivers_db=[]
menu()

