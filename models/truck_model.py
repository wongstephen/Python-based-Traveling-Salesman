class Truck:
    def __init__(self, id):
        self.id = id
        self.packages = []

    def getId(self):
        return self.id
    
    def getPackage(self, id):
        return self.packages