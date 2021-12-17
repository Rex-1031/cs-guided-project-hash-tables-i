"""
Your task is create your own HashTable without using a built-in library, using chaining to resolve collisions.

Your HashTable needs to have the following functions:

- put(key, value): Use a hashing function to calculate an index at which to store this data. At that index in the hash table, append a new ListNode(key,value) to the linked list. Or if this key already exists in the table, update the value

- get(key): Figure out where to look in the hash table by plugging in the given key to the hashing function. The result is the index in the hash table storage where we'll find the desired data. Search through the linked list at that location to find the right one, and return that node.value

- remove(key) : Remove the mapping for the given key if it exists in the hash table. Similar logic to the get(key) method as far as hashing and list searching, then we just remove the node from the linked list

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
class ListNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class MyHashTable:
    def __init__(self, capacity):
        # Initialize the hash table with storage array of specified capacity
        self.capacity = capacity
        self.storage = [None] * capacity
        self.count = 0

    def hash_index(self, key):
        # Take an arbitrary key and return a valid integer index at which to store the (key,value)
        # A standard hashing function: DJB2
        # Cast the key to a string and get bytes
        str_key = str(key).encode()

        # Start from an arbitrary large prime
        hash_value = 5381

        # Bit-shift and sum value for each character
        for b in str_key:
            hash_value = ((hash_value << 5) + hash_value) + b
            hash_value &= 0xffffffff  # DJB2 is a 32-bit hash, only keep 32 bits

        return hash_value % self.capacity


    def put(self, key, value):
        # Store the value with the given key.
        # In the event of a collision, simply overwrite the previous value

        # calculate the index:
        index = self.hash_index(key)

        # Look through the linked list at storage[index] to see if this key is already in the table
        currentNode = self.storage[index]
        while currentNode:
            if currentNode.key == key: # if key found in list:
                currentNode.value = value # update value
                return
            currentNode = currentNode.next

        # Otherwise, append a new ListNode(key,value) to the linked list
        self.count += 1
        newNode = ListNode(key,value)
        newNode.next = self.storage[index]
        self.storage[index] = newNode
        
        return


    def get(self, key):
        # Retrieve the value stored with the given key.
        # Return -1 if the key is not found

        # calculate the index:
        index = self.hash_index(key)

        # Look for the given key in the list at storage[index]
        currentNode = self.storage[index]
        while currentNode:
            # If it's found, return the value
            if currentNode.key == key:
                return currentNode.value
            currentNode = currentNode.next # move to the next, keep searching

        # Otherwise, return -1
        return -1


    def remove(self, key: int) -> None:
        # calculate the index:
        index = self.hash_index(key)

        # initialize some variables to help with linked list navigation
        currentNode = prev_node = self.storage[index]

        # If the storage bin is already empty, just return
        if not currentNode: return

        if currentNode.key == key:
            # We found the node to delete immediately, we can now skip over it 
            self.storage[index] = currentNode.next
        else:
            # We did not find the node to delete we must now traverse the bin
            currentNode = currentNode.next

            while currentNode:
                if currentNode.key == key:
                    prev_node.next = currentNode.next
                    break
                else:
                    prev_node, currentNode = prev_node.next, currentNode.next

# Test it!
hash_table = MyHashTable(1000);
hash_table.put("a", 1);
hash_table.put("b", 2);
print(hash_table.get("a"));            # returns 1
print(hash_table.get("c"));            # returns -1 (not found)
hash_table.put("b", 1);         # update the existing value
print(hash_table.get("b"));            # returns 1
hash_table.remove("b");         # remove the mapping for 2
print(hash_table.get("b"));            # returns -1 (not found)