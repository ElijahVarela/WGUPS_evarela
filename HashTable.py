class HashTable(object):
    def __init__(self,length = 10):
        self.length = length
        self.hasharray = []
        for i in range(self.length):
            self.hasharray.append([])
        return

    def insert(self, unique_id, package):
        key = hash(unique_id) % self.length
        if [unique_id, package] not in self.hasharray[key]:
            self.hasharray[key].append([unique_id, package])
        return

    def print_hash_table(self):
        print(self.hasharray)
        return

    def update(self, unique_id, package):
        key = hash(unique_id) % self.length
        for x in self.hasharray[key]:
            if x[0] == unique_id:
                x[1] = package
        return

    def find(self, unique_id):
        key = hash(unique_id) % self.length
        for x in self.hasharray[key]:
            if x[0] == unique_id:
                return x[1]
                break
        return None

