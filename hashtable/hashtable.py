class HashTableEntry:
    """
    Linked List hash table key/value pair
    """

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

    def __str__(self):
        return self.value


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8

# Minimum and maximum desired load factors
MIN_LOAD_FACTOR = 0.2
MAX_LOAD_FACTOR = 0.7


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity):
        if capacity >= MIN_CAPACITY:
            self.capacity = capacity
        else:
            print(
                f"Error: the specified capacity ({capacity}) is too small -- initializing with minimum capacity of {MIN_CAPACITY}...")
            self.capacity = MIN_CAPACITY
        self.data = [None] * self.capacity
        self.num_keys = 0

    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        return self.capacity

    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        return self.num_keys / self.capacity

    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """

        # Your code here

    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        hash_ = 5381
        for c in key:
            hash_ = (hash_ * 33) + ord(c)
        return hash_

    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        # return self.fnv1(key) % self.capacity
        return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        if self.num_keys / self.capacity > MAX_LOAD_FACTOR:
            self.resize(self.capacity * 2)

        index = self.hash_index(key)
        entry = self.data[index]
        if not entry:
            self.data[index] = HashTableEntry(key, value)
        else:
            previous = None
            while entry:
                if entry.key == key:
                    entry.value = value
                    return
                previous, entry = entry, entry.next

            entry = HashTableEntry(key, value)
            previous.next = entry
        self.num_keys += 1

    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        if self.num_keys / self.capacity < MIN_LOAD_FACTOR and self.capacity // 2 >= 8:
            self.resize(self.capacity // 2)

        index = self.hash_index(key)
        entry = self.data[index]
        if not entry:
            raise KeyError('Error: key not found!')
        else:
            previous = None
            while entry:
                if entry.key == key:
                    if previous:
                        entry.value = None
                        return
                    else:
                        entry.value = None
                        return
                previous, entry = entry, entry.next
            raise KeyError('Error: key not found!')

        self.num_keys -= 1

    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        index = self.hash_index(key)
        entry = self.data[index]
        if entry:
            while entry:
                if entry.key == key:
                    return entry.value
                entry = entry.next
        return None

    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        self.capacity = new_capacity
        old_data, self.data = self.data, [None] * self.capacity
        for entry in old_data:
            while entry:
                self.put(entry.key, entry.value)
                entry = entry.next


if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")

    print("")

    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print("")
