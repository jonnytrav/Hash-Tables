
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

        # Part 1: Hash collisions should be handled with an error warning. (Think about and
        # investigate the impact this will have on the tests)

        # Part 2: Change this so that hash collisions are handled with Linked List Chaining.

        Fill this in.
        '''
        # 1) take the key and pass into _hash_mod... returns index
        # create a reference to the index
        # 2)
        # if node at index is None:
        # --insert key/value as a LinkedPair() at the index
        # elif value at index is not None:
        # --if next value at this index is None:
        # ----insert at the next slot
        # --else:
        # ----loop until we find an open spot
        index = self._hash_mod(key)
        if self.storage[index] is None:
            self.storage[index] = LinkedPair(key, value)
        elif self.storage[index] is not None:
            if self.storage[index].next is None:
                self.storage[index].next = LinkedPair(key, value)
            else:
                curr_node = self.storage[index]
                while curr_node.next is not None:
                    curr_node = curr_node.next
                curr_node.next = LinkedPair(key, value)
                print('smoke test')

    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''
        index = self._hash_mod(key)
        # if first pair matches
        if self.storage[index].next is None:
            self.storage[index] = None
        elif self.storage[index].key != key:
            prev = None
            curr_node = self.storage[index]
            # loop through chain until match is found
            while curr_node is not None:
                if curr_node.key == key:
                    prev.next = curr_node.next
                    return
                prev = curr_node
                curr_node = curr_node.next

    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''
        # 1) create a reference to the index where pair is stored
        # using the _hash_mod(key) function
        # 2) check the key in the pair that corresponds with the index
        # 3)
        # if the key arg matches the key at the index
        # --return pair at the index
        # else:
        # --if next pair at this index is none:
        # ---- return None
        # --while loop that returns the pair with matching key

        index = self._hash_mod(key)
        if self.storage[index].key == key:
            return self.storage[index].value
        else:
            if self.storage[index].next is None:
                return None
            else:
                curr_node = self.storage[index]
                while curr_node.next is not None:
                    if curr_node.key == key:
                        return curr_node.value

                return None

    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''
        # for each value:
        # --if curr_node.next is None:
        # ----insert curr_node pair and continue
        # --else:
        # ----add each pair while .next is not None
        old_storage = self.storage
        self.storage = self.storage * 2
        for pair in old_storage:
            # if there's a single pair
            if pair.next is None:
                index = self._hash_mod(pair.key)
                self.storage[index] = LinkedPair(pair.key, pair.value)
            # if there's multiple linked pairs
            else:
                curr_node = pair
                while curr_node.next is not None:
                    index = self._hash_mod(curr_node.key)
                    self.storage[index] = LinkedPair(
                        curr_node.key, curr_node.value)
                    curr_node = curr_node.next


if __name__ == "__main__":
    ht = HashTable(2)

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")
    # print(ht.storage[0].value)
    # print(ht.storage[1].value)
    # print(ht.storage[2].value)

    print(ht._hash_mod("line_3"))

    # Test storing beyond capacity
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    print("")
