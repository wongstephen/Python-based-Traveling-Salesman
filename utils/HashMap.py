#space complexity: O(n)
#time complexity: O(n)
class Hashmap:
    #initializes the size of the hashmap. recommended to be a prime number
    def __init__(self, size):
        self.data = [None]*size
    
    #hashing fuction. returns the hashed key
    def __hash(self, key):
        hashed = 0
        for i in range(len(key)):
            hashed = hashed + ord(key[i])
        return hashed % len(self.data)

    #inserts a key value pair into the hashmap
    def insert(self, key, value):
        #hashes the key to find the index
        hashed = self.__hash(key)
        #checks if index is null. 
        if self.data[hashed] is None:
            #if there is no list at the index, one is created with the key value
            self.data[hashed] = [[key, value]]
            return
        #check the list to see if the key is in the list
        for i in range(len(self.data[hashed])):
            if self.data[hashed][i][0] == key:
                self.data[hashed][i][1] = value
                return
        #if there is a list at the index, a list with key, value is appended
        self.data[hashed].append([key, value])

    def delete(self, key):
        #hashes the key to find index
        hashed = self.__hash(key)
        #iterates through the list at the hashed index and delete the key value pair if found
        for i in range(len(self.data[hashed])):
            if self.data[hashed][i][0] == key:
                del self.data[hashed][i]
                return
        return None

    #returns all keys in the hashmap
    def get_keys(self):
        keys = []
        for i in range(len(self.data)):
            if self.data[i] is not None:
                for j in range(len(self.data[i])):
                    keys.append(self.data[i][j][0])
        return keys
    
    #returns the value of the key
    def get_value(self, key):
        #hashes the key to find index
        hashed = self.__hash(key)
        #iterates through the list at the hashed index and returns the value if found
        for i in range(len(self.data[hashed])):
            if self.data[hashed][i][0] == key:
                return self.data[hashed][i][1]
        return None

    #returns entire list in the hast table
    def get_list(self):
        return self.data
    
    #returns the size of the hashmap
    def size(self):
        return len(self.data)
    
    def __str__(self):
        string = ""
        for i in range(len(self.data)):
            if self.data[i] is not None:
                string += str(i) + ": " + str(self.data[i]) + "\n"
        return string