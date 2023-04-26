class PackageModel:
    def __init__(self, id, address, city, state, zip, deadline, weight, notes):
        self.id = id
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip
        self.deadline = deadline
        self.weight = weight
        self.notes = notes
        self.truck = None
        self.status = "hub"
        self.departure = None
        self.delivery = None

    def getId(self):
        return self.id
    
    def getAddress(self):
        return self.address
    
    def getCity(self):
        return self.city
    
    def getState(self):
        return self.state
    
    def getZip(self):
        return self.zip
    
    def getDeadline(self):
        return self.deadline
    
    def getWeight(self):
        return self.weight
    
    def getNotes(self):
        return self.notes
    
    def getTruck(self):
        return self.truck
    
    def setTruck(self, truck):
        self.truck = truck

    def getStatus(self):
        return self.status
    
    def setStatus(self, status):
        self.status = status

    def getDeparture(self):
        return self.departure
    
    def setDeparture(self, departure):
        self.departure = departure

    def getDelivery(self):
        return self.delivery
    
    def setDelivery(self, delivery):
        self.delivery = delivery

    def __str__(self):
        return "Package ID: " + self.id + " Address: " + self.address + " City: " + self.city + " State: " + self.state + " Zip: " + self.zip + " Deadline: " + self.deadline + " Weight: " + self.weight + " Notes: " + self.notes + " Truck: " + str(self.truck) + " Departure: " + str(self.departure) + " Delivery: " + str(self.delivery)

