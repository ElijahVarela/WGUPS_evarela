class hashTable(object):
    def __init__(self,length = 10):
        self.length = length
        self.hasharray = []
        for i in range(self.length):
            self.hasharray.append([])
        return

    def insert(self, ID, Package):
        key = hash(ID) % self.length
        if [ID, Package] not in self.hasharray[key]:
            self.hasharray[key].append([ID, Package])
        return

    def printHashTable(self):
        print(self.hasharray)
        return

    def update(self, ID, Package):
        key = hash(ID) % self.length
        for x in self.hasharray[key]:
            if x[0] == ID:
                x[1] = Package
        return

    def find(self, ID):
        key = hash(ID) % self.length
        for x in self.hasharray[key]:
            if x[0] == ID:
                return x[1]
                break
        return None

