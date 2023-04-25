class HashMap:
    def __init__(self,size,length, key, value):
        self.length = length
        self.key = key
        self.value = value
        self.data = []*size
        
    def __hash(self, key):
        hashed = key + 1
        return hashed
         

    def __str__(self):
        return f"{self.key} {self.value}"
