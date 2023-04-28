class Address_model:
    def __init__(self, id, name, address, zip):
        self.id = id
        self.name = name
        self.address = address
        self.city = None
        self.state = None
        self.zip = zip

    def get_id(self):
        return self.id

    def get_address(self):
        return self.address
    
    def set_address(self, address):
        self.address = address
    
    def get_zip(self):
        return self.zip
    
    def set_zip(self, zip):
        self.zip = zip

    def get_name(self):
        return self.name
    
    def get_state(self):
        return self.state
    
    def set_state(self, state):
        self.state = state

    def get_city(self):
        return self.city
    
    def set_city(self, city):
        self.city = city
    
    def __str__(self):
        return f"{self.name}, {self.address}, {self.zip}"