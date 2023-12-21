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


# Creating a Hash table, used "Let's Go Hashing!" webinar for reference
class HashTableCreate:
    def __init__(self, initial_capacity=20):
        # Initializing the hash as a list of empty lists
        self.list = []
        for i in range(initial_capacity):
            self.list.append([])

    # Inserting an item into the hash table
    def insert(self, key, item):
        # Getting the bucket list where key will go (point of insertion)
        bucket = hash(key) % len(self.list)
        point_of_insertion = self.list[bucket]

        # Updating the key if its already in the bucket
        for kv in point_of_insertion:
            if kv[0] == key:
                # If found, print(key_value)
                kv[1] = item
                return True

            # If key is not in bucket, insert the new key-value item at the end of the list
            key_value = [key, item]
            point_of_insertion.append(key_value)
            return True


# Looking up an item with a matching key in the hash table
def lookup(self, key):
    # Getting the bucket list (niche) where this key would be located, the index is the 'point of lookup'
    niche = hash(key) % len(self.list)
    point_of_lookup = self.list[niche]

    # Search of the pair in the bucket list (niche)
    for pair in point_of_lookup:
        if key == pair[0]:
            return pair[1]

        return None


# Removing an item with a matching key in the hash table
def hash_remove(self, key):
    # Determining the 'point of deletion' the item will be removed from
    niche = hash(key) % len(self.list)
    point_of_deletion = self.list[niche]
# If item is in point of deletion, the item will be removed
    if key in point_of_deletion:
        point_of_deletion.remove(key)
