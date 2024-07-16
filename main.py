# -*- coding: utf-8 -*-
#class Driver
class DriverDb:
    def __init__(self):
        self.drivers=[]
        self.driver_count=0

    def generate_driver_id(self):
        self.driver_count += 1
        self.driver_id=f"ID{self.driver_count:03}"
        return self.driver_id
    
    def add_driver(self,driver_name, start_city, cities_db):
        if start_city.lower() not in [city.lower() for city in cities_db]:
            add_city = input(f"City '{start_city}' is not in the database. Do you want to add it? (yes/no): ")
            if add_city.lower() == "yes":
                cities_db.append(start_city)
                print(f"City '{start_city}' added to the database.")
            else:
                print("City not added. Driver not added.")
                return

        self.driver_id = self.generate_driver_id()
        new_driver = [self.driver_id, driver_name, start_city]
        self.drivers.append(new_driver)
        return new_driver
    
    def view_drivers(self):
        if not self.drivers:
            print("No drivers in the database.")
        else:
            for driver in self.drivers:
                print(driver)

driver=DriverDb()

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
            driver.view_drivers()
        elif choice ==2:
            add= True
            while add:
                driver_name = input("Enter driver's name: ")
                start_city = input("Enter driver's start city: ")
                new_driver= driver.add_driver(driver_name, start_city, cities_db)
                print(new_driver)
                if new_driver:
                    print(f"Driver '{new_driver[1]}' with ID '{new_driver[0]}' added to the database.")
                #print(f"Driver '{new_driver['name']}' with ID '{new_driver['driver_id']}' added to the database.")
                add_choice=input("Do you want to add another driver? (yes/no): ").strip().lower() 
                if add_choice=="no":
                    add = False
                    print("Finished Adding drivers! Back to drivers' menu.")

        else:
            print("Back to main menu")
            stop= True
            
#View Drivers
'''
def viewDrivers():
    if not drivers_db:
        print("No drivers in database")
    else:
        for driver in drivers_db:
            print(driver)
'''

#Add a Driver
'''
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
            
'''           

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



#driver_count = 0
cities_db=["Saida", "Beirut", "Tyre", "Nabatieh", "Tripoli", "Jounieh", "Byblos", "Alay"]
#drivers_db=[]
menu()

