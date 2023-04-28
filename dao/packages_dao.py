from models.package_model import Package_model
from utils.Hashmap import Hashmap
import csv

#load the packages csv into a Hashmap
packages_map = Hashmap(100)

def load_packages():
    with open('data/packages.csv', encoding='utf-8-sig', newline='') as packagesFile:
        reader = csv.reader(packagesFile)
        packages = list(reader)
    for package in packages:
        packageInstance = Package_model(package[0], package[1], package[2], package[3], package[4], package[5], package[6], package[7])
        packages_map.insert(package[0], packageInstance)