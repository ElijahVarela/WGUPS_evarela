# Class for Creating a Hash Map with Chaining for Collision Resolution.
class HashTable:
    def __init__(self, initial_capacity=20):
        # Initialize the hash map with empty buckets.
        self.buckets = []
        for _ in range(initial_capacity):
            self.buckets.append([])

    # Inserts a new key-value pair into the hash map or updates an existing one.
    def insert(self, key, value):
        # Determine the bucket index for the given key using the hash function.
        bucket_index = hash(key) % len(self.buckets)
        bucket = self.buckets[bucket_index]
        # Verify if the key already exists in the bucket.
        for key_value_pair in bucket:
            # If the key is found, update its value and return the updated result.
            if key_value_pair[0] == key:
                key_value_pair[1] = value
                return True
        # If the key is not found, append the new key-value pair to the bucket.
        key_value_pair = [key, value]
        bucket.append(key_value_pair)
        return True

    # Searches for a value in the hash map using its key.
    def lookup(self, key):
        # Determine the bucket index for the given key using the hash function.
        bucket_index = hash(key) % len(self.buckets)
        bucket = self.buckets[bucket_index]
        # Searches for the key in the bucket.
        for key_value_pair in bucket:
            # If the key is found, return its associated value.
            if key_value_pair[0] == key:
                return key_value_pair[1]
        # If the key is not found, return None.
        return None

    # Removes a key-value pair from the hash map using its key.
    def hash_remove(self, key):
        # Determine the bucket index for the given key using the hash function.
        bucket_index = hash(key) % len(self.buckets)
        bucket = self.buckets[bucket_index]
        # Search for the key in the bucket and remove it if found.
        for key_value_pair in bucket:
            if key_value_pair[0] == key:
                bucket.remove(key_value_pair)
                return True
        # If the key is not found, return False.
        return False



