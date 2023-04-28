# Stephen Wong Student ID 011031716

import datetime
import math
import time
from dao.distances_dao import load_distances
from utils.main_utils import print_main_menu, print_packages_status
from utils.Hashmap import Hashmap
from utils.calc_utils import get_shortest_distance
from dao.packages_dao import packages_map, load_packages
from utils.Colors import Colors
from dao.address_dao import addresses_map, load_addresses
from models.package_model import Package_model
from models.address_model import Address_model
from models.truck_model import Truck_model
from utils.log_utils import package_log
from utils.main_utils import get_total_miles_traveled

#takes a snapshot of the packages at the current time and returns an array of package objects
#space complexity is O(n) 
#time complexity is O(n)
def package_snapshot():
    package_arr = []
    for package in packages_map.get_keys():
        el = packages_map.get_value(package)
        package_snap = Package_model(el.get_id(), el.get_address(), el.get_city(), el.get_state(), el.get_zip(), el.get_deadline(), el.get_weight(), el.get_notes())
        package_snap.set_truck(el.get_truck())
        package_snap.set_status(el.get_status())
        package_snap.set_delivery_time(el.get_delivery_time())
        package_arr.append(package_snap)
    return package_arr

running = True
while running:
    print("WELCOME TO THE WGUPS ROUTING PROGRAM")
    print()
    # time.sleep(1)
    print("Loading Packages from CSV to Hash Map...")
    load_packages()
    # time.sleep(1)
    print("Loading Distance Maps from CSV...")
    load_distances()
    # time.sleep(1)
    print("Loading Addresses from CSV to Hash Map...")
    load_addresses()
    # time.sleep(1)
    # instantiate and load trucks
    print()
    print("Creating Truck Instances...")
    time.sleep(1)
    truck1 = Truck_model()
    truck1.set_id(1)
    truck1.set_departure(datetime.datetime(1970, 1, 1, 8, 0, 0))
    truck2 = Truck_model()
    truck2.set_departure(datetime.datetime(1970, 1, 1, 9, 15, 0))
    truck2.set_id(2)
    truck3 = Truck_model()
    truck3.set_departure(datetime.datetime(1970, 1, 1, 10, 45, 0))
    truck3.set_id(3)
    print()
    print("Loading Trucks with Packages...")
    print()
    time.sleep(1)

    #literates through the hub_packages dictionary and loads the packages into the trucks
    hub_packages = {
        1:[1, 2, 4, 13, 14, 15, 16, 19, 20, 29, 30, 31, 34, 37, 40],
        2:[3, 6, 7, 8, 10, 11, 17, 18, 21, 22, 23, 25, 28, 32, 36, 38],
        3:[5, 9, 12, 24, 26, 27, 33, 35, 39]
    }
    for key in hub_packages.keys():
        trucks = {
            1: truck1,
            2: truck2,
            3: truck3
        }
        for hub_package in hub_packages.get(key):
            package_object = packages_map.get_value(str(hub_package))
            trucks.get(key).load_package(package_object)
            package_object.set_truck(key)
        print("Truck ", key, " loaded with packages: ", hub_packages.get(key))
    package_log.insert(str(datetime.time(8,0,0).strftime('%I:%M%p')), package_snapshot())

    print()

    # encapulates truck functions 
    # time complexity is O(n^2) it loops through trucks then through packages. 
    # space complexity is O(n)
    def run_truck(text_color, truck):
        #sets the truck status to in service
        truck.set_status("Delivering")

        #sets all packages in the truck to enroute
        for package in truck.get_package_load():
            # package.set_status("Enroute on Truck " + str(truck.get_id()))
            package.set_status("Enroute")

        #delivers the package to the next address that is closest to the current address
        while (len(truck.get_package_load()) > 0): 
            shortest_package = get_shortest_distance(truck) #returns dictionary with package and distance of closest package

            truck.set_miles_traveled(shortest_package.get('distance')) #add the distance traveled to the truck
            time_traveled = truck.get_miles_traveled()/18 * 60 #calculate the time traveled in minutes
            minutes_traveled = math.floor(time_traveled) #get the minutes traveled
            seconds_traveled = round((time_traveled - minutes_traveled) * 60) #get the seconds traveled
            package_delivery_time = truck.get_departure() + datetime.timedelta(minutes=minutes_traveled, seconds=seconds_traveled) #calculate the time of delivery

            shortest_package.get('package').set_delivery_time(package_delivery_time) #record the time of delivery to package object
            shortest_package.get('package').set_status("Delivered") #set the package status to delivered
                
            truck.deliver_package(shortest_package.get('package')) #deliver the package and remove from payload           
            truck.set_current_location(shortest_package.get('package').get_address()) #set truck to last known address
            
            package_log.insert(str(package_delivery_time.strftime('%I:%M%p')), package_snapshot())

        truck.set_status("Not in Service")

    print("Starting Deliveries...")

    run_truck(Colors.orange, truck1)
    run_truck(Colors.cyan, truck2)
    packages_map.get_value("9").set_address("410 S State St") # update 9 410 S State St., Salt Lake City, UT 84111
    run_truck(Colors.red, truck3)
    print()

    print(Colors.green, f"Total miles traveled by all trucks: {get_total_miles_traveled(truck1, truck2, truck3)}") #returns the total miles traveled by all trucks
    print()

    print_main_menu(Colors.default) #prints the main menu
    print()

    main_menu_input = None
    while main_menu_input != "1" and main_menu_input != "2" and main_menu_input != "3" and main_menu_input != "4":
        main_menu_input = input("Select menu option 1, 2, 3 or 4: ")
        if main_menu_input != "1" and main_menu_input != "2" and main_menu_input != "3" and main_menu_input != "4":
            print(Colors.red, "Invalid input. Please select menu option 1, 2, 3 or 4: ")
            print(Colors.default)
        print()

    if main_menu_input == "1":
        print_packages_status()
        print()

        print(Colors.darkgrey, f"Total miles traveled by all trucks: {get_total_miles_traveled(truck1, truck2, truck3)}")
        print()

    #prints the package status based on the time selected
    elif main_menu_input == "2":
        #prints the time selection menu
        for i in range(len(package_log.get_keys())):
            print(i + 1, ":", package_log.get_keys()[i])
            time.sleep(.05)
        print()

        time_sel = -1
        while time_sel < 1 or time_sel > len(package_log.get_keys()):
             time_sel = int(input("Please select a time: "))
        print()
        
        #prints the package selection menu
        package_sel = -1
        while package_sel < 1 or package_sel > len(package_log.get_value(package_log.get_keys()[time_sel - 1])):
            package_sel = int(input("Please select a package 1-40: "))
        print()
        
        #returns the package object based on the time and package selected
        selected_package = package_log.get_value(package_log.get_keys()[time_sel - 1])
        for package in selected_package:
            if package.get_id() == str(package_sel):
                print(Colors.green, "PackageID, Address, City, State, Zip, Delivery Deadline, Mass KILO, PageSpecial Notes, Status, DeliveryTime")
                print(Colors.black, "--------------------------------------------------------------------------------------------------------------------")
                print(Colors.default)
                print(package)
   
    #prints all packages at a specific time
    elif main_menu_input == "3":
        #print all times available to select
        for i in range(len(package_log.get_keys())):
            print(i + 1, ":", package_log.get_keys()[i])
        print()

        time_sel = -1
        while time_sel < 1 or time_sel > len(package_log.get_keys()):
            time_sel = int(input("Please select a time: ")) 
        print()

        print("You selected to view all packages at", package_log.get_keys()[time_sel - 1])
        print(Colors.green, "PackageID, Address, City, State, Zip, Delivery Deadline, Mass KILO, PageSpecial Notes, Status, DeliveryTime")
        print(Colors.black, "--------------------------------------------------------------------------------------------------------------------")
        print(Colors.default)
        for package in package_log.get_value(package_log.get_keys()[time_sel - 1]):
            if package.get_status() == "Delivered":
                print(Colors.green, package)
            elif package.get_status() == "Enroute":
                print(Colors.yellow, package)
            else:
                print(Colors.default, package)
        print(Colors.blue, "Total Packages:", len(package_log.get_value(package_log.get_keys()[time_sel - 1])))
        print(Colors.default)

    #exits program
    elif main_menu_input == "4":
        print("Goodbye!")
        exit(0)

    # get the user input to restart the app
    restart_input = None
    while restart_input != "y" and restart_input != "n":
        restart_input = input(f"{Colors.green}Would you like to restart the program? (y/n): ")
    if restart_input == "y":
        running = True
    else:
        running = False
        print("Exiting!")
    print(Colors.default)