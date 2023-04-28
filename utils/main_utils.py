from utils.Colors import Colors
from dao.packages_dao import packages_map
import time

#prints main menu
def print_main_menu(color):
    print(color)
    print( "Possible Menu Options:")
    print( "***************************************")
    print( "1. Print All Package Status and Total Mileage")
    print( "2. Get a Single Package Status with a Time")
    print( "3. Get All Package Status with a Time ")
    print( "4. Exit the Program")
    print( "***************************************")
    print(Colors.default)

#prints all packages status
def print_packages_status():
    print()
    package_list = []
    packages_keys = packages_map.get_keys()
    for key in packages_keys:
        package_list.append(packages_map.get_value(key))
    package_list.sort(key=lambda x: x.get_delivery_time())
    print(Colors.green, "Package Status:")
    print(Colors.green, "PackageID, Address, City, State, Zip, Delivery Deadline, Mass KILO, PageSpecial Notes, Status, DeliveryTime")
    for package in package_list:
        truck_colors = {
            1: Colors.orange,
            2: Colors.cyan,
            3: Colors.red
        }
        time.sleep(.1)
        print(truck_colors.get(package.get_truck()), package)

#returns the total miles traveled by all trucks
def get_total_miles_traveled(truck1, truck2, truck3):
    return round(truck1.get_miles_traveled() + truck2.get_miles_traveled() + truck3.get_miles_traveled(),1)