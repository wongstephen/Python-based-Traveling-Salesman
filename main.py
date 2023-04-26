# Stephen Wong Student ID 011031716

import csv
from utils.HashMap import HashMap

#load the package data into a hashmap
packages = HashMap(40)
with open('csv/packages.csv') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        packages.insert(row[0], row[1:])

#load the distance data into a hashmap
distances = HashMap(40)
with open('csv/distance.csv') as csvfile:
    reader = csv.reader(csvfile)
    distance = list(reader)

print(distance)
