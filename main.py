# Stephen Wong Student ID 011031716

import csv
from utils.Hashmap import Hashmap
from utils.Colors import Colors
from models.package_model import PackageModel

#credit to https://stackoverflow.com/questions/72466218/ufeff-is-appearing-while-reading-csv-using-unicodecsv-module for the encoding fix

       #load the distances csv into a Hashmap
distances_map = Hashmap(100)
def load_distances():
    with open('csv/distance.csv', encoding='utf-8-sig', newline='') as distFile:
        reader = csv.reader(distFile)
        distances = list(reader)

#load the addresses csv into a Hashmap
addresses_map = Hashmap(100)
def load_addresses():
    with open('csv/addresses.csv', encoding='utf-8-sig', newline='') as adddressFile:
        reader = csv.reader(adddressFile)
        addresses = list(reader)

#load the packages csv into a Hashmap
packages_map = Hashmap(100)
def load_packages():
    with open('csv/packages.csv', encoding='utf-8-sig', newline='') as packagesFile:
        reader = csv.reader(packagesFile)
        packages = list(reader)
    # create packages as an instance
    # self.id = id
    # self.address = address
    # self.city = city
    # self.state = state
    # self.zip = zip
    # self.deadline = deadline
    # self.weight = weight
    # self.notes = notes
    # self.truck = None
    # self.departure = None
    # self.delivery = None
    for package in packages:
        packageInstance = PackageModel(package[0], package[1], package[2], package[3], package[4], package[5], package[6], package[7])
        packages_map.insert(package[0], packageInstance.__str__())

gameOver = False
while not gameOver:
    load_packages()
    load_distances()
    load_addresses()
    print(Colors.red, packages_map.get_value("1"))
    # print(packages_map.__str__())

    #get the user input to restart the app
    restart = input(f"{Colors.green}Would you like to restart the program? (y/n): ")
    if restart == "y":
        gameOver = False
    else:
        gameOver = True
        print("Goodbye!")