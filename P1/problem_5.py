import hashlib
from datetime import datetime
from pytz import timezone



class Blockdata:
    def __init__(self, timestamp, data, previous_hash):
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash(self.data)

    def calc_hash(self, data):
        
        sha = hashlib.sha256()
        hash_str = data.encode('utf-8') + str(self.timestamp).encode('utf-8') + str(self.previous_hash).encode('utf-8')
        sha.update(hash_str)
        print(sha.hexdigest())

        return sha.hexdigest()


class Block: #Block -> Block!!!!!

    def __init__(self, block_data):
        self.block_data = block_data
        self.next = None
        self.prev = None


class Blockchain:

    def __init__(self):
        self.head = None
        self.tail = None
        self.counter = 0

    def take_UTC_time(self):
        utc = timezone('UTC')
        return datetime.now(utc)

    def add_block(self, data):

        if self.head is None:
            new_block_data = Blockdata(self.take_UTC_time,data, 0)
            new_node = Block(new_block_data) 
            self.head = new_node
            self.tail = self.head
        else:

            prev_data_hash = self.tail.block_data.hash
            new_block_data = Blockdata(self.take_UTC_time(),data,prev_data_hash )
            new_node = Block(new_block_data) 
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

        self.counter += 1
    
    def traverse_chain(self):
        
        current_block = self.head
        while current_block is not None:
            print(current_block.block_data.data)
            print(current_block.block_data.hash)
            current_block = current_block.next

    def get_blockdata (self, dataset):
        current_block = self.head
        flag = False
        while current_block is not None:
            if current_block.block_data.data == dataset:
                flag = True
                return current_block.block_data 

            if current_block is None:
                return None

            if flag == True:
                break
            
            current_block = current_block.next




chain1 = Blockchain()
chain1.add_block('markus')
chain1.add_block('buchholz')
chain1.add_block('stavanger') 
print(chain1.counter)
chain1.traverse_chain()
yourdata = chain1.get_blockdata('buchholz1')
if yourdata:
    print("data ::::", yourdata.data) #[0], " :: ", yourdata[1])
if not yourdata:
    print("there is not the block for given dataset")
#print(get_block_data)
#print(get_block_timestamp)

if __name__ == '__main__':
    def run_test_1():
        print('Running test 1....')
        blockchain = Blockchain()
        block1 = blockchain.insert('Block 1')
        block2 = blockchain.insert('Block 2')

        print(blockchain.get(block1.hash))              # Should print block1.
        print(blockchain.get(block1.previous_hash))     # Should print None (as it's the dummy head block.
        print(blockchain.get(block2.hash))              # Should print block2.
        print(blockchain.get(block2.previous_hash))     # Should print block1.
        print()

    def run_test_2():
        print('\nRunning test 2....')
        blockchain = Blockchain()
        print(blockchain)       # Should print "Blockchain is empty."
        for n in range(50):
            blockchain.insert('Some information {}'.format(n))

        print(blockchain)       # Should print the entire blockchain.

        # Walk the blockchain.
        for block in blockchain:
            print('{}: {}'.format(block.index, block.hash)) # Should print each block's index and hash.

    def run_test_3():
        print('\nRunning test 3....')
        blockchain = Blockchain()
        print(blockchain)       # Should print "Blockchain is empty."

    run_test_1()
    run_test_2()
    run_test_3()



















#     def iter(self):
#         """ Iterate through the list. """
#         current = self.head #note subtle change
#         while current:
#             val = current.data
#             current = current.next
#             yield val

#     def reverse_iter(self):
#         """ Iterate backwards through the list. """
#         current = self.tail
#         while current:
#             val = current.data
#             current = current.prev
#             yield val

#     def delete(self, data):
#         """ Delete a node from the list. """
#         current = self.head
#         node_deleted = False
#         if current is None:
#             node_deleted = False

#         elif current.data == data:
#             self.head = current.next
#             self.head.prev = None
#             node_deleted = True

#         elif self.tail.data == data:
#             self.tail = self.tail.prev
#             self.tail.next = None
#             node_deleted = True

#         else:
#             while current:
#                 if current.data == data:
#                     current.prev.next = current.next
#                     current.next.prev = current.prev
#                     node_deleted = True
#                 current = current.next

#         if node_deleted:
#             self.count -= 1

#     def search(self, data):
#         """Search through the list. Return True if data is found, otherwise False."""
#         for node in self.iter():
#             if data == node:
#                 return True
#         return False

#     def print_foward(self):
#         """ Print nodes in list from first node inserted to the last . """
#         for node in self.iter():
#             print(node)

#     def print_backward(self):
#         """ Print nodes in list from latest to first node. """
#         current = self.tail
#         while current:
#             print(current.data)
#             current = current.prev

#     def insert_head(self, data):
#         """ Insert new node at the head of linked list. """

#         if self.head is not None:
#             new_node = Node(data, None, None)
#             new_node.next = self.head
#             self.head.prev = new_node
#             self.head = new_node
#             self.count += 1

#     def reverse(self):
#         """ Reverse linked list. """
#         current = self.head
#         while current:
#             temp = current.next
#             current.next = current.prev
#             current.prev = temp
#             current = current.prev

#         # Now reverse the order of head and tail
#         temp = self.head
#         self.head = self.tail
#         self.tail = temp

#     def __getitem__(self, index):
#         if index > self.count - 1:
#             raise Exception("Index out of range.")
#         current = self.head # Note subtle change
#         for n in range(index):
#             current = current.next
#         return current.data

#     def __setitem__(self, index, value):
#         if index > self.count - 1:
#             raise Exception("Index out of range.")
#         current = self.head # Note subtle change
#         for n in range(index):
#             current = current.next
#         current.data = value


# dll = DoublyLinkedList()
# dll.append("foo")
# dll.append("bar")
# dll.append("biz")
# dll.append("whew")
# print("Items in List : ")
# dll.print_foward()
# print("List after deleting node with data whew")
# dll.delete("whew")
# dll.print_foward()

# print("List count: {}".format(dll.count))
# print("Print list backwards")
# dll.print_backward()

# print("Reverse list ")
# dll.reverse()
# dll.print_foward()

# print("Append item to front of list")
# dll.insert_head(55)
# dll.print_foward()

# print("Get First element: {}".format(dll[0]))