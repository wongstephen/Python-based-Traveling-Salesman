from dao.address_dao import addresses_map
from dao.distances_dao import distances

def find_distance (address1, address2):
    # params are a string of the address
    # get the address with the address as the key
    # returns the distance between the two addresses
    address_1 = addresses_map.get_value(address1).get_id()
    address_2 = addresses_map.get_value(address2).get_id()
    if (distances[address_1][address_2]):
        return round(float(distances[address_1][address_2]),1)
    else:
        return round(float(distances[address_2][address_1]),1)
    
def get_shortest_distance(truck):
    # get the shortest distance from the current address
    # returns package object with shortest distance
    current_address = truck.get_current_location()
    package_load = truck.get_package_load()
    shortest_dist = None
    shortest_package = None
    for package in package_load:
        distance = find_distance(current_address, package.get_address())
        if shortest_dist == None and shortest_package == None:
            shortest_dist = distance
            shortest_package = package
        elif distance < shortest_dist:
            shortest_dist = distance
            shortest_package = package
    object = {"package": shortest_package, "distance": shortest_dist}
    return object