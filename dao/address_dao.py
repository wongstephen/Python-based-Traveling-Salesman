from utils.Hashmap import Hashmap
from models.address_model import Address_model
import csv

#load the addresses csv into a Hashmap
#space complexity is O(n)
#time complexity is O(n)
addresses_map = Hashmap(100)
def load_addresses():
    with open('data/addresses.csv', encoding='utf-8-sig', newline='') as adddressFile:
        reader = csv.reader(adddressFile)
        addresses = list(reader)
    for i in range(len(addresses)):
        address_instance = Address_model(i, addresses[i][0], addresses[i][1], addresses[i][2])
        addresses_map.insert(address_instance.get_address(), address_instance)


