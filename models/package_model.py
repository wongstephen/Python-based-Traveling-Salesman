class Package_model:
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
        self.status = "At Hub" #At Hub, Out for Delivery, Delivered
        self.departure = None
        self.delivery_time = None

    def get_id(self):
        return self.id
    
    def get_address(self):
        return self.address
    
    def set_address(self, address):
        self.address = address
    
    def get_city(self):
        return self.city
    
    def set_city(self, city):
        self.city = city
            
    def get_state(self):
        return self.state
    
    def set_state(self, state):
        self.state = state

    def get_zip(self):
        return self.zip
    
    def set_zip(self, zip):
        self.zip = zip
    
    def get_deadline(self):
        return self.deadline
    
    def get_weight(self):
        return self.weight
    
    def get_notes(self):
        return self.notes
    
    def get_status(self):
        return self.status
    
    def get_truck(self):
        return self.truck
    
    def get_departure(self):
        return self.departure
    
    def get_delivery_time(self):
        return self.delivery_time
    
    def set_status(self, status):
        self.status = status

    def set_truck(self, truck):
        self.truck = truck

    def set_departure(self, departure):
        self.departure = departure

    def set_delivery_time(self, delivery_time):
        self.delivery_time = delivery_time

    def __str__(self):
        return f"{self.id}, {self.address}, {self.city}, {self.state}, {self.zip}, {self.deadline}, {self.weight}, {self.notes if self.notes else 'N/A'}, {self.status}, {self.delivery_time.strftime('%I:%M %p') if self.delivery_time else 'N/A'}"