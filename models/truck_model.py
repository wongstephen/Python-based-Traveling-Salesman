# attributes: id, max_packages, prev_address, next_address, distance, depart_time
class Truck_model:
    def __init__(self):
        self.id = None
        self.max_packages = 16
        self.package_load = []
        self.current_location = "4001 South 700 East"
        self.miles_traveled = 0.0
        self.departure = None #time
        self.status = 'not departed' # not departed, departed,returned
    
    def get_id(self):
        return self.id
    
    def set_id(self, id):
        self.id = id

    def set_departure(self, departure):
        self.set_departure = departure

    def get_departure(self):
        return self.set_departure
    
    def set_miles_traveled(self, miles):
        self.miles_traveled = self.miles_traveled + miles

    def get_miles_traveled(self):
        return self.miles_traveled
    
    def set_status(self, status):
        self.status = status

    def get_status(self):
        return self.status
    
    #accepts a list of packages or a single package
    def load_package(self, package):
        if package is list:
            for p in package:
                self.package_load.append(p)
        else:
            self.package_load.append(package)
    
    def get_package_load(self):
        return self.package_load

    def get_current_location(self):
        return self.current_location
    
    def set_current_location(self, location):
        self.current_location = location

    def get_package_load(self):
        return self.package_load

    def deliver_package(self, package):
        self.package_load.remove(package)

    def __str__(self):
        return f"Truck {self.id} has {len(self.package_load)} packages and is at {self.current_location} and has traveled {round(self.miles_traveled,1)} and is {self.status}"