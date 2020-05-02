
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
        curr_pair = self.storage[index]
        prev_pair = None

        while curr_pair is not None and curr_pair.key != key:
            prev_pair = curr_pair
            curr_pair = prev_pair.next

        # after loop breaks, check if keys match/if there's an opening
        # (that's what keeps the loop going so one of those is true)
        if curr_pair is not None:
            curr_pair.value = value
        else:
            new_pair = LinkedPair(key, value)
            new_pair.next = self.storage[index]
            self.storage[index] = new_pair

        # if self.storage[index] is None:
        #     self.storage[index] = LinkedPair(key, value)
        # elif self.storage[index] is not None:
        #     if self.storage[index].next is None:
        #         self.storage[index].next = LinkedPair(key, value)
        #     else:
        #         curr_node = self.storage[index]
        #         while curr_node.next is not None:
        #             curr_node = curr_node.next
        #         curr_node.next = LinkedPair(key, value)
        #         print('smoke test')

    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''
        index = self._hash_mod(key)
        curr_pair = self.storage[index]
        most_recent = None
        while curr_pair is not None and curr_pair.key != key:
            most_recent = curr_pair
            curr_pair = most_recent.next

        if curr_pair is None:
            print("Value does not exist. Sorry!")
        else:
            if most_recent is None:
                self.storage[index] = None
            else:
                most_recent.next = None

            # if first pair matches
            # if self.storage[index].next is None:
            #     self.storage[index] = None
            # elif self.storage[index].key != key:
            #     prev = None
            #     curr_node = self.storage[index]
            #     # loop through chain until match is found
            #     while curr_node is not None:
            #         if curr_node.key == key:
            #             prev.next = curr_node.next
            #             return
            #         prev = curr_node
            #         curr_node = curr_node.next

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
        curr_pair = self.storage[index]
        while curr_pair is not None:
            if curr_pair.key == key:
                return curr_pair.value
            curr_pair = curr_pair.next
        # if self.storage[key] is not None and self.storage[index].key == key:
        #     return self.storage[index].value
        # else:
        #     if self.storage[index].next is None:
        #         return None
        #     else:
        #         curr_node = self.storage[index]
        #         while curr_node.next is not None:
        #             if curr_node.key == key:
        #                 return curr_node.value
        #             curr_node = curr_node.next

        #         return None

    def resize(self):
        old_storage = self.storage
        self.capacity = self.capacity * 2
        self.storage = [None] * self.capacity

        for pair in old_storage:
            curr_node = pair
            while curr_node is not None:
                self.insert(curr_node.key, curr_node.value)
                # print(curr_node.key, curr_node.value,
                #       "smoke test for insubscriptable int")
                curr_node = curr_node.next


if __name__ == "__main__":
    ht = HashTable(2)

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")

    # print(ht._hash_mod("line_1"))
    # print(ht._hash_mod("line_2"))
    # print(ht._hash_mod("line_3"))

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
