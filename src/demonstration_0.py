"""
Demonstration 0: basic HashTable implementation with a fixed capacity and no collision handling.

Example:

```plaintext
hash_table = MyHashTable();
hash_table.put("a", 1);
hash_table.put("b", 2);
hash_table.get("a");            // returns 1
hash_table.get("c");            // returns -1 (not found)
hash_table.put("b", 1);         // update the existing value
hash_table.get("b");            // returns 1
hash_table.remove("b");         // remove the mapping for 2
hash_table.get("b");            // returns -1 (not found)
```
"""

"""
A hash table with `capacity` buckets
that accepts string keys
"""
class HashTable:
    def __init__(self, capacity):
        # Initialize the hash table with storage array of specified capacity
        self.capacity = capacity
        self.storage = [None] * capacity
        self.count = 0

    def hash_index(self, key):
        # Take an arbitrary key and return a valid integer index at which to store the (key,value)
        # Naive simple hashing function: sum the bytes!
        bytes_representation = key.encode()

        sum = 0
        for byte in bytes_representation:
            sum += byte
        
        return sum % self.capacity # hashed index within storage array


    def put(self, key, value):
        # Store the value with the given key.
        # In the event of a collision, simply overwrite the previous value

        # calculate the index:
        index = self.hash_index(key)

        # Increment the item count (if there wasn't something there before)
        if self.storage[index] == None:
            self.count += 1

        # assign value to storage[index]
        self.storage[index] = value
        return


    def get(self, key):
        # Retrieve the value stored with the given key.
        # Return -1 if the key is not found

        # calculate the index:
        index = self.hash_index(key)

        # Return the value at that index, or -1 if None is there
        if self.storage[index] == None:
            return -1
        else:
            return self.storage[index]


    def remove(self, key: int) -> None:
        # calculate the index:
        index = self.hash_index(key)

        # Remove the value at that index and decrement the count if needed
        if self.storage[index] != None:
            self.count -= 1
            self.storage[index] = None


# Test it!
hash_table = HashTable(1000);
hash_table.put("a", 1);
hash_table.put("b", 2);
print(hash_table.get("a"));            # returns 1
print(hash_table.get("c"));            # returns -1 (not found)
hash_table.put("b", 1);         # update the existing value
print(hash_table.get("b"));            # returns 1
hash_table.remove("b");         # remove the mapping for 2
print(hash_table.get("b"));            # returns -1 (not found)