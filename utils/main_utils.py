from utils.Colors import Colors
import datetime
from dao.packages_dao import packages_map
import time
from utils.log_utils import package_log

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
#packages are sorted by delivery time
#space complexity: O(n)
#time complexity: O(n)
def print_packages_status():
    print()
    package_list = []
    packages_keys = packages_map.get_keys()
    for key in packages_keys:
        package_list.append(packages_map.get_value(key))
    package_list.sort(key=lambda x: x.get_delivery_time())
    truck_legend()
    print(Colors.green, "Package Status:")
    print(Colors.green, "PackageID, Address, City, State, Zip, Delivery Deadline, Mass KILO, PageSpecial Notes, Status, DeliveryTime")
    for package in package_list:
        truck_colors = {
            1: Colors.orange,
            2: Colors.cyan,
            3: Colors.red
        }
        print(truck_colors.get(package.get_truck()), package)

#returns the total miles traveled by all trucks
def get_total_miles_traveled(truck1, truck2, truck3):
    print()
    print(Colors.default, "Miles Traveled")
    print()
    print(Colors.orange, f' Truck 1: {round(truck1.get_miles_traveled(), 1)} Miles')
    print(Colors.cyan, f' Truck 2: {round(truck2.get_miles_traveled(), 1)} Miles')
    print(Colors.red, f' Truck 3: {round(truck3.get_miles_traveled(), 1)} Miles')
    print()
    print(Colors.lightgreen, f'Total Miles Traveled {round(truck1.get_miles_traveled() + truck2.get_miles_traveled() + truck3.get_miles_traveled(),1)}')


def get_time_input():
    valid_input = False
    while not valid_input:
        time_str = input("Please enter a time in the following format (HH:MM am/pm): ")
        try:
            time_obj = datetime.datetime.strptime(time_str, "%I:%M %p")
            valid_input = True
            return time_obj
        except ValueError:
            print('Invalid input')

def get_package_input():
    package_sel = -1
    while package_sel < 1 or package_sel > len(packages_map.get_keys()):
        package_sel = int(input("Please select a package 1-40 by ID: "))
    return package_sel

def get_all_by_time(time_obj):
    print_package_legend()
    times = package_log.get_keys()
    sorted_times = sorted(times, key=lambda x: x, reverse=True)
    print(Colors.green, "PackageID, Address, City, State, Zip, Delivery Deadline, Mass KILO, PageSpecial Notes, Status, DeliveryTime")
    print(Colors.black, "--------------------------------------------------------------------------------------------------------------------")
    for time in sorted_times:
        if time_obj > datetime.datetime.strptime(time, "%I:%M %p"):
            for package in package_log.get_value(time):
                if package.get_status() == "Delivered":
                    print(Colors.green, package)
                elif package.get_status() == "Enroute":
                    print(Colors.yellow, package)
                else:
                    print(Colors.default, package) 
            break

def print_package_legend():
    print()
    print(Colors.darkgrey, 'Package status legend')
    print(Colors.default, 'At Hub')
    print(Colors.yellow, 'En Route')
    print(Colors.green, 'Delivered')
    print()

def truck_legend():
    print()
    print(Colors.darkgrey, 'Truck legend')
    print(Colors.orange, 'Truck 1')
    print(Colors.cyan, 'Truck 2')
    print(Colors.red, 'Truck 3')
    print()