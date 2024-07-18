#class DriverDb
#This class has methods to add drivers with unique IDs and view them
class DriverDb:
    #constructor 
    def __init__(self): #O(1)
        #drivers saved in the program
        self.drivers=[["ID001","Alex","Jounieh"],["ID002","Ali","Nabatieh"],["ID003","Rim","Tripoli"],["ID004","Mohammad","Beirut"],["ID005","Jana","Saida"],["ID006","Taj","Tyre"],["ID007","Joe","Byblos"],["ID008","Faten","Alay"]]
        self.driver_count=len(self.drivers)   #number of drivers saved in program

    #method: generates ID for new driver based on his/her number in the list
    def generateDriverID(self): #O(1)
        self.driver_count += 1  #add on to driver count representing new driver
        self.driver_id=f"ID{self.driver_count:03}"   #ID format: ID with 3 digits of 0s and drivers number
        return self.driver_id
    

    #method: add new drivers to the program
    def addDriver(self,driver_name, start_city): #O(n) n: nb of cities
        if C.cityNotExists(start_city): #if city is not already saved 
            #ask user if he/she wants to add it
            add_city = input(f"City '{start_city}' is not in the database. Do you want to add it? (yes/no): ") 
            if add_city.lower() == "yes": #if yes: case insensitive
                C.addCity(start_city) #add city to cities list
                print(f"City '{start_city}' added to the database.") #inform user that city was added 
            else:
                print("City not added. Driver not added.") #if user chose no, city and driver are not added
                return

        self.driver_id = self.generateDriverID() # id generted for new driver
        new_driver = [self.driver_id, driver_name, start_city] #new driver list formed
        self.drivers.append(new_driver) #new driver appended to drivers list
        return new_driver
    
    #method: print all drivers in the database in form: id, name, start city
    def viewDrivers(self): #O(n) n:nb of drivers
        if not self.drivers: #if no drivers available
            print("No drivers in the database.") 
        else:
            for driver in self.drivers: #iterate over the elements of the list of lists (drivers)
                print(driver) #print the iterator (each driver's info)

#used to call the class
driver=DriverDb()


# Class Cities
#This class has methods to view cities saved in the program, add to the cities after checking duplicates, 
# and creating graphs representing links between cities with ditances being weighs
class Cities():
    def __init__(self): #constructor O(1)
        self.cities_db=["Saida", "Beirut", "Tyre", "Nabatieh", "Tripoli", "Jounieh", "Byblos", "Alay","ghazieh"] #list of cities
        self.graph = {city: [] for city in self.cities_db} #graph of cities
    

    #method: check if a new city is NOT in the cities list
    def cityNotExists(self,city): #O(n) n:nb of cities
        #case insensitive
        return city.lower() not in (existing_city.lower() for existing_city in self.cities_db) #generator expression
   

    #method: add city to cities db
    def addCity(self, city): #O(1)
        self.cities_db.append(city)  #add new city by appending the list
        self.graph = {city: [] for city in self.cities_db} #update graph with new city
    
    #method: print cities in db
    def showCity(self): #O(n) n:nb of cities
        print("The cities in the program are: ")
        #iterate over all elements in db
        for i in self.cities_db:
            print(i) #print iterator
    
    #method: add edges to graph
    def addEdge(self, city1, city2, distance): #O(n) n: nb of cities
        #if 2 cities are available in db
        if city1 in self.cities_db and city2 in self.cities_db: #Case Sensitive
            #weighted (distance) undirected (works both ways) graph
            self.graph[city1].append((city2,distance)) #add neighboring relationship (thru edge) from C1 to C2 with dist(weight)
            self.graph[city2].append((city1,distance))#add neighboring relationship (thru edge) from C2 to C1 with dist(weight)
    

    #method: for an input city, print all neighboring cities (having edges connecting them)
    def printNeighboringCities(self, city): #O(n*m)
        #check if input city is in db
        if city in self.cities_db: # Case Sensitive   O(n) n:nb of cities
            print(f"Neighboring cities for {city} with distances:")
            #iterate over the elements of the graph
            if (self.graph[city]):
                for neighbor, distance in self.graph[city]: #O(m) m:edges related to city
                    print(f"{neighbor}: {distance} Km") #print neighbors with relative dist
            else:
                print(f"No neighbors found for {city}.") #no neighbors message
        else:
                print(f" {city} not is database.") #no neighbors message

    #method: print drivers in drop-off city and its neighbors
    def availableDrivers(self, city, drivers):
        #reachables: list of cities whose drivers can reach drop-off city
        reachables=[city] #initiatize the list with the drop-off city itself
        if city in self.graph: #Case Sensitive    O(n) n:nb of cities
            for neighbor in self.graph[city]: #iterate over neighbors   O(m) m: edges related to city
               reachables.append(neighbor[0]) #append neighboring cities to the reachables list (without distances)
            all_drivers = [] #list of available drives in the reachable cities
            for i in range (len (drivers)):  #loop over all drivers list    O(k) k:nb of drivers
                for reachable_city in reachables: #for every city in the list    O(j) j:nb of neighboring cities
                    if reachable_city in drivers[i]: #check if the drivers start city is same as rechable city  #O(k) k:nb of drivers
                        all_drivers.append(drivers[i]) #if yes, add the drivers info to the all drivers list
            #print availabe drives
            print(f"Drivers delivering to {city}:")
            for driver in all_drivers: #O(i) i: nb of drivers in reachable cities
                print(driver)
        else:
            #no drivers available
            print(f"No drivers found for {city}.")

#to call cities class
C=Cities()

#adding weighted edges to the cities graph
C.addEdge("Beirut", "Saida", 44)
C.addEdge("Saida", "Tyre", 38)
C.addEdge("Saida", "Nabatieh", 30)
C.addEdge("Beirut", "Tripoli", 82)
C.addEdge("Beirut", "Jounieh", 20)
C.addEdge("Jounieh", "Byblos", 18.5)
C.addEdge("Beirut", "Alay", 18.7)

##################### Menus of the Program #####################
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
            choice=int(input()) #does not work if user inputs other than digits
        if choice==1:
            driver.viewDrivers() 
        elif choice ==2:
            add= True
            while add:
                driver_name = input("Enter driver's name: ") #input new drivers name
                start_city = input("Enter driver's start city: ") #input new city name
                new_driver= driver.addDriver(driver_name, start_city) 
                print(new_driver)
                if new_driver:
                    print(f"Driver '{new_driver[1]}' with ID '{new_driver[0]}' added to the database.")
                #print(f"Driver '{new_driver['name']}' with ID '{new_driver['driver_id']}' added to the database.")
                add_choice=input("Do you want to add another driver? (yes/no): ").strip().lower() #add another driver
                if add_choice=="no":
                    add = False
                    print("Finished Adding drivers! Back to drivers' menu.")

        else:
            print("Back to main menu")
            stop= True #quit drivers menu, back to main menu
            

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
        choice=int(input("Enter your choice: ")) #error for input other than digits
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
            stop= True #quit cities menu back to main menu


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
            choice=int(input()) #error for input other than digits
        if choice==1:
            driversMenu()
        elif choice ==2:
            print(citiesMenu())
        else:
            print("The system is exiting. Good bye!")
            stop= True #quit program

mainMenu()

