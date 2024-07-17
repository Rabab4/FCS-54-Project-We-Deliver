# -*- coding: utf-8 -*-
#class Driver
class DriverDb:
    def __init__(self):
        self.drivers=[["ID001","Alex","Jounieh"],["ID002","Ali","Nabatieh"],["ID003","Rim","Tripoli"],["ID004","Mohammad","Beirut"],["ID005","Jana","Saida"],["ID006","Taj","Tyre"],["ID007","Joe","Byblos"],["ID008","Faten","Alay"]]
        self.driver_count=len(self.drivers)

    def generateDriverID(self):
        self.driver_count += 1
        self.driver_id=f"ID{self.driver_count:03}"
        return self.driver_id
    
    def addDriver(self,driver_name, start_city, cities_db):
        if C.cityNotExists(start_city):
            add_city = input(f"City '{start_city}' is not in the database. Do you want to add it? (yes/no): ")
            if add_city.lower() == "yes":
                C.addCity(start_city)
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
        self.graph = {city: [] for city in self.cities_db}
    
    def cityNotExists(self,city):
        return city.lower() not in (existing_city.lower() for existing_city in self.cities_db)
   

    def addCity(self, city):
        self.cities_db.append(city)
    
    def showCity(self):
        print("The cities in the program are: ")
        for i in self.cities_db:
            print(i)
    
    def addEdge(self, city1, city2, distance):
        if city1 in self.cities_db and city2 in self.cities_db: #Case Sensitive
            self.graph[city1].append((city2,distance))
            self.graph[city2].append((city1,distance))
    
    def printNeighboringCities(self, city):
        
        if city in self.cities_db: # Case Sensitive
            print(f"Neighboring cities for {city} with distances:")
            for neighbor, distance in self.graph[city]:
                print(f"{neighbor}: {distance} Km")
        else:
            print(f"No neighbors found for {city}.")

    def availableDrivers(self, city, drivers):
        reachables=[city]
        if city in self.graph: #Case Sensitive
            for neighbor in self.graph[city]:
               reachables.append(neighbor[0])
            all_drivers = []
            for i in range (len (drivers)):
                for reachable_city in reachables:
                    if reachable_city in drivers[i]:
                        all_drivers.append(drivers[i])
            print(f"Drivers delivering to {city}:")
            for driver in all_drivers:
                print(driver)
        else:
            print(f"No drivers found for {city}.")


C=Cities()


C.addEdge("Beirut", "Saida", 44)
C.addEdge("Saida", "Tyre", 38)
C.addEdge("Saida", "Nabatieh", 30)
C.addEdge("Beirut", "Tripoli", 82)
C.addEdge("Beirut", "Jounieh", 20)
C.addEdge("Jounieh", "Byblos", 18.5)
C.addEdge("Beirut", "Alay", 18.7)


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
                new_driver= driver.addDriver(driver_name, start_city, C.cities_db)
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
            C.showCity()
        elif choice ==2:
            city=input("Enter the city name: ")
            C.printNeighboringCities(city)
        elif choice ==3:
            city=input("Enter the drop-off city name: ")
            C.availableDrivers(city, driver.drivers)
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

