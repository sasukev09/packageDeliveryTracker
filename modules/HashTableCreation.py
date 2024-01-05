"""
HashTableCreation.py
~

Western Governors University
C950: Data Structures & Algorithms II

~

Kevin Salazar
Student ID: 010303855

~

December 21st 2023

"""


class HashMapCreation:
    def __init__(self, initial_capacity=20):
        # Initializing the hash map as a list of empty lists
        self.list = []
        for i in range(initial_capacity):
            self.list.append([])

    def insert(self, key, item):
        # Determine the bucket index using the hash of the key
        bucket = hash(key) % len(self.list)
        # Access the bucket list at the calculated index
        bucket_list = self.list[bucket]

        for kv in bucket_list:
            # Check if the key already exists in the bucket
            if kv[0] == key:
                # If found, update the value associated with the key
                kv[1] = item
                return True

        # If the key doesn't exist in the bucket, add a new key-value pair
        key_value = [key, item]
        bucket_list.append(key_value)
        return True

    def lookup(self, key):
        # Determine the bucket index using the hash of the key
        bucket = hash(key) % len(self.list)
        # Access the bucket list at the calculated index
        bucket_list = self.list[bucket]
        for pair in bucket_list:
            # Check if the key matches the key in the current key-value pair
            if key == pair[0]:
                # Return the associated value if the key is found
                return pair[1]
        # Return None if the key is not found in the hash map
        return None

    def hash_remove(self, key):
        # Determine the bucket index using the hash of the key
        slot = hash(key) % len(self.list)
        # Access the bucket list at the calculated index
        destination = self.list[slot]

        if key in destination:
            destination.remove(key)
