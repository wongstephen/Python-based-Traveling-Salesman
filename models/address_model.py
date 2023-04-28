class Address_model:
    def __init__(self, id, name, address, zip):
        self.id = id
        self.name = name
        self.address = address
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
    
    def __str__(self):
        return f"{self.name}, {self.address}, {self.zip}"