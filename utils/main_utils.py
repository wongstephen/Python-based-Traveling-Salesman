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

def get_all_by_time():
    valid_input = False
    while not valid_input:
        time_str = input("Please enter a time in the following format (HH:MM am/pm): ")
        try:
            time_obj = datetime.datetime.strptime(time_str, "%I:%M %p")
            valid_input = True
        except ValueError:
            print('Invalid input')
            
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


