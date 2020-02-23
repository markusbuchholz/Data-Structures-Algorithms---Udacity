# Solution
"""
double link list
hash table holds the key

*** set new velue is goes to the front of cache as a most recently used value. The other values are go back
*** get velue from cache move this value at the front as most recently used . Other value are pushed back
*** when wy add value wiith the same kay soio the valuue is updated (not the key because is the same) but only value is updated. The updated node is going at the front od f cache
*** if we go over the capacity so the new veleu is going at the front but last velue in cache is removed
*** if we woud like to get the vale with the key which is not exist so we return -1
"""

class LinkedListNode:
    
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashMap:
    
    def __init__(self, initial_size):
        self.bucket_array = [None for _ in range(initial_size)]
        self.p = 31
        self.num_entries = 0
        self.load_factor = 0.7
        self.capacity = initial_size
        
    def set(self, key, value):

        if self.capacity == 0:
            return -1
        bucket_index = self.get_bucket_index(key)

        new_node = LinkedListNode(key, value)
        head = self.bucket_array[bucket_index]

        # check if key is already present in the map, and update it's value
        while head is not None:
            if head.key == key:
                head.value = value
                return
            head = head.next

        # key not found in the chain --> create a new entry and place it at the head of the chain
        head = self.bucket_array[bucket_index]
        new_node.next = head
        self.bucket_array[bucket_index] = new_node
        self.num_entries += 1
        
        # check for load factor
        current_load_factor = self.num_entries / len(self.bucket_array)
        if current_load_factor > self.load_factor:
            self.num_entries = 0
            self._rehash()
        
    def get(self, key):
        bucket_index = self.get_hash_code(key)
        head = self.bucket_array[bucket_index]
        while head is not None:
            if head.key == key:
                return head.value
            head = head.next
        return None
        
    def get_bucket_index(self, key):
        bucket_index = self.get_hash_code(key)
        return bucket_index
    
    def get_hash_code(self, key):
        key = str(key)
        num_buckets = len(self.bucket_array)
        current_coefficient = 1
        hash_code = 0
        for character in key:
            hash_code += ord(character) * current_coefficient
            hash_code = hash_code % num_buckets                       # compress hash_code
            current_coefficient *= self.p
            current_coefficient = current_coefficient % num_buckets   # compress coefficient
        return hash_code % num_buckets                                # one last compression before returning
    
    def size(self):
        return self.num_entries

    def _rehash(self):
        old_num_buckets = len(self.bucket_array)
        old_bucket_array = self.bucket_array
        num_buckets = 2 * old_num_buckets
        self.bucket_array = [None for _ in range(num_buckets)]

        for head in old_bucket_array:
            while head is not None:
                key = head.key
                value = head.value
                self.set(key, value)         # we can use our set() method to rehash
                head = head.next
                
    def delete(self, key):
        bucket_index = self.get_bucket_index(key)
        head = self.bucket_array[bucket_index]

        previous = None
        while head is not None:
            if head.key == key:
                if previous is None:
                    self.bucket_array[bucket_index] = head.next
                else:
                    previous.next = head.next
                self.num_entries -= 1
                return
            else:
                previous = head
                head = head.next


hash_map = HashMap(5)

       
hash_map.set(1, 1)
hash_map.set(2, 2)
hash_map.set(3, 3)
hash_map.set(4, 4)

print(hash_map.get(1))     # 1
print(hash_map.get(2))
print(hash_map.get(9))     # 2
#print(cache.get(9))     # -1 because 9 is not present in the cache
#print(list(hash_map.hashtable.keys()))


hash_map.set(5, 5)
hash_map.set(6, 6)
print("******************'")
print(hash_map.get(3))     # -1 because the cache reached it's capacity and 3 was the least recently used entry
#print(list(cache.hashtable.keys()))  # [1, 2, 4, 5, 6]

# hash_map.set("one", 1)
# hash_map.set("two", 2)
# hash_map.set("three", 3)
# hash_map.set("neo", 11)
# hash_map.set(100,99)

# print("size: {}".format(hash_map.size()))


# print("one: {}".format(hash_map.get("one")))
# print("neo: {}".format(hash_map.get("neo")))
# print("three: {}".format(hash_map.get("three")))
# print("size: {}".format(hash_map.size()))

# hash_map.delete("one")

# print(hash_map.get("one"))
# print(hash_map.size())












































# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.next = None


# class LinkedList:
#     def __init__(self):
#         self.head = None

#     def prepend(self, value):
#         """ Prepend a node to the beginning of the list """

#         if self.head is None:
#             self.head = Node(value)
#             return

#         new_head = Node(value)
#         new_head.next = self.head
#         self.head = new_head

#     def append(self, value):
#         """ Append a node to the end of the list """
#         # Here I'm not keeping track of the tail. It's possible to store the tail
#         # as well as the head, which makes appending like this an O(1) operation.
#         # Otherwise, it's an O(N) operation as you have to iterate through the
#         # entire list to add a new tail.

#         if self.head is None:
#             self.head = Node(value)
#             return

#         node = self.head
#         while node.next:
#             node = node.next

#         node.next = Node(value)

#     def search(self, value):
#         """ Search the linked list for a node with the requested value and return the node. """
#         if self.head is None:
#             return None

#         node = self.head
#         while node:
#             if node.value == value:
#                 return node
#             node = node.next

#         raise ValueError("Value not found in the list.")


#     def remove(self, value):
#         """ Delete the first node with the desired data. """
#         if self.head is None:
#             return

#         if self.head.value == value:
#             self.head = self.head.next
#             return

#         node = self.head
#         while node.next:
#             if node.next.value == value:
#                 node.next = node.next.next
#                 return
#             node = node.next

#         raise ValueError("Value not found in the list.")


#     def pop(self):
#         """ Return the first node's value and remove it from the list. """
#         if self.head is None:
#             return None

#         node = self.head
#         self.head = self.head.next

#         return node.value

#     def insert(self, value, pos):
#         """ Insert value at pos position in the list. If pos is larger than the
#             length of the list, append to the end of the list. """
#         if pos == 0:
#             self.prepend(value)
#             return

#         index = 0
#         node = self.head
#         while node.next and index <= pos:
#             if (pos - 1) == index:
#                 new_node = Node(value)
#                 new_node.next = node.next
#                 node.next = new_node
#                 return

#             index += 1
#             node = node.next
#         else:
#             self.append(value)

#     def size(self):
#         """ Return the size or length of the linked list. """
#         size = 0
#         node = self.head
#         while node:
#             size += 1
#             node = node.next

#         return size

#     def to_list(self):
#         out = []
#         node = self.head
#         while node:
#             out.append(node.value)
#             node = node.next
#         return out


#         ## Test your implementation here

# # Test prepend
# linked_list = LinkedList()
# linked_list.prepend(1)
# assert linked_list.to_list() == [1], f"list contents: {linked_list.to_list()}"
# linked_list.append(3)
# linked_list.prepend(2)
# assert linked_list.to_list() == [2, 1, 3], f"list contents: {linked_list.to_list()}"
    
# # Test append
# linked_list = LinkedList()
# linked_list.append(1)
# assert linked_list.to_list() == [1], f"list contents: {linked_list.to_list()}"
# linked_list.append(3)
# assert linked_list.to_list() == [1, 3], f"list contents: {linked_list.to_list()}"

# # Test search
# linked_list.prepend(2)
# linked_list.prepend(1)
# linked_list.append(4)
# linked_list.append(3)
# assert linked_list.search(1).value == 1, f"list contents: {linked_list.to_list()}"
# assert linked_list.search(4).value == 4, f"list contents: {linked_list.to_list()}"

# # Test remove
# linked_list.remove(1)
# assert linked_list.to_list() == [2, 1, 3, 4, 3], f"list contents: {linked_list.to_list()}"
# linked_list.remove(3)
# assert linked_list.to_list() == [2, 1, 4, 3], f"list contents: {linked_list.to_list()}"
# linked_list.remove(3)
# assert linked_list.to_list() == [2, 1, 4], f"list contents: {linked_list.to_list()}"

# # Test pop
# value = linked_list.pop()
# assert value == 2, f"list contents: {linked_list.to_list()}"
# assert linked_list.head.value == 1, f"list contents: {linked_list.to_list()}"

# # Test insert 
# linked_list.insert(5, 0)
# assert linked_list.to_list() == [5, 1, 4], f"list contents: {linked_list.to_list()}"
# linked_list.insert(2, 1)
# assert linked_list.to_list() == [5, 2, 1, 4], f"list contents: {linked_list.to_list()}"
# linked_list.insert(3, 6)
# assert linked_list.to_list() == [5, 2, 1, 4, 3], f"list contents: {linked_list.to_list()}"

# # Test size
# assert linked_list.size() == 5, f"list contents: {linked_list.to_list()}"