# '''
# Linked List hash table key/value pair
# '''
class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''
    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity
    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.
        You may replace the Python hash with DJB2 as a stretch goal.
        '''
        return hash(key)
    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash
        OPTIONAL STRETCH: Research and implement DJB2
        '''
        pass
    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        return self._hash(key) % self.capacity
    def insert(self, key, value):
        '''
        Store the value with the given key.
        Hash collisions should be handled with Linked List Chaining.
        Fill this in.
        '''
        index = self._hash_mod(key)
        current = self.storage[index]
        last = None
        while (current is not None and current.key != key):
         last = current
         current = last.next

        if (current is not None):
            current.value = value
        else:
            new = LinkedPair(key, value)
            new.next = self.storage[index]
            self.storage[index] = new
       
    def remove(self, key):
        '''
        Remove the value stored with the given key.
        Print a warning if the key is not found.
        Fill this in.

        '''
        index = self._hash_mod(key)
        # floating
        last = None
        current = self.storage[index]
        # That the current is not None meaning it has been found
        # and the current key is not the same key.
        while current is not None and current.key != key:
            last = current
            current = current.next
        if (self.storage[index] is None):
            # doesn't exist
            print("Error")
        else:
            # hasn't been found 
            if (last is None):
                self.storage[index] = current.next
            else:
                # equal to it's next go around by deleteing it
                last.next = current.next
    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.
        Returns None if the key is not found.
        Fill this in.
        '''
        index = self._hash_mod(key)
        # Find the node/current
        current = self.storage[index]

        while current is not None:
            # Making sure the key matches the key of the retrieved
            if (current.key == key):
                # If it doesn't the return it 
                return current.value
                # continues on the list
            current = current.next

    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.
        and we continue down the line of key value pairs going 
        back and fourth through the for loop with the whole object then the 
        while loop through the object itself.
        Fill this in.
        '''
        old_storage = self.storage
        self.capacity *= 2
        self.storage = [None] * self.capacity
        for item in old_storage:
            current = item
            while (current is not None):
                self.insert(current.key, current.value)
                current = current.next

if __name__ == "__main__":
    ht1 = HashTable(2)
    ht1.insert("key1", "hello")
    ht1.insert("unicorn", "goodbye")
    ht1.remove("key1")
    print(ht1.storage)
    # ht = HashTable(2)
    # ht.insert("line_1", "Tiny hash table")
    # ht.insert("line_2", "Filled beyond capacity")
    # ht.insert("line_3", "Linked list saves the day!")
    # print("")
    # # Test storing beyond capacity
    # print(ht.retrieve("line_1"))
    # print(ht.retrieve("line_2"))
    # print(ht.retrieve("line_3"))
    # # Test resizing
    # old_capacity = len(ht.storage)
    # ht.resize()
    # new_capacity = len(ht.storage)
    # print(f"\nResized from {old_capacity} to {new_capacity}.\n")
    # # Test if data intact after resizing
    # print(ht.retrieve("line_1"))
    # print(ht.retrieve("line_2"))
    # print(ht.retrieve("line_3"))
    # print("")