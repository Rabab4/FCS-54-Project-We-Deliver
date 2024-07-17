# -*- coding: utf-8 -*-
#class Driver
class DriverDb:
    def __init__(self):
        self.drivers=[]
        self.driver_count=0

    def generateDriverID(self):
        self.driver_count += 1
        self.driver_id=f"ID{self.driver_count:03}"
        return self.driver_id
    
    def addDriver(self,driver_name, start_city, cities_db):
        if city.cityExists(start_city):
            add_city = input(f"City '{start_city}' is not in the database. Do you want to add it? (yes/no): ")
            if add_city.lower() == "yes":
                city.addCity(start_city)
                print(f"City '{start_city}' added to the database.")
            else:
                print("City not added. Driver not added.")
                return

        self.driver_id = self.generateDriverID()
        new_driver = [self.driver_id, driver_name, start_city]
        self.drivers.append(new_driver)
        return new_driver
    
    def viewDrivers(self):
        if not self.drivers:
            print("No drivers in the database.")
        else:
            for driver in self.drivers:
                print(driver)

driver=DriverDb()


# Class Cities

class Cities():
    def __init__(self):
        self.cities_db=["Saida", "Beirut", "Tyre", "Nabatieh", "Tripoli", "Jounieh", "Byblos", "Alay"]
    
    def cityExists(self,city):
        return city.lower() in (existing_city.lower() for existing_city in self.cities_db)

    def addCity(self, city):
        self.cities_db.append(city)
    
    def showCity(self):
        print("The cities in the program are: ")
        for i in self.cities_db:
            print(i)

city=Cities()

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
            driver.viewDrivers()
        elif choice ==2:
            add= True
            while add:
                driver_name = input("Enter driver's name: ")
                start_city = input("Enter driver's start city: ")
                new_driver= driver.addDriver(driver_name, start_city, cities_db)
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
            

# Cities' Menu
def citiesMenu():
    stop=False
    while not stop:
        print("Hello! This is the Cities' Menu.")
        print("Please enter:")
        print("    1. To show cities")
        print("    2. To print neighboring cities")
        print("    3. To print drivers delivering to city")
        print("    4. To go back to main menu")
        choice=int(input("Enter your choice: "))
        choices=[1,2,3,4]
        while choice not in choices:
            print("Invalid input! Please try again: ")
            choice=int(input())
        if choice==1:
            city.showCity()
        elif choice ==2:
            #neighboring
        elif choice ==3:
            #drivers delivering to city
        else:
            print("Back to main menu")
            stop= True


#Menu Function
def mainMenu():
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

mainMenu()

