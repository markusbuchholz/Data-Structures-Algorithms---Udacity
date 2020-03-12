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
        #print(sha.hexdigest())

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
            new_block_data = Blockdata(datetime.now(timezone('UTC')),data, None)
            new_node = Block(new_block_data) 
            self.head = new_node
            self.tail = self.head
        else:

            prev_data_hash = self.tail.block_data.hash
            new_block_data = Blockdata(datetime.now(timezone('UTC')),data,prev_data_hash )
            new_node = Block(new_block_data) 
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node


    
    def traverse_chain(self):
        
        current_block = self.head
        while current_block is not None:
            # print(current_block.block_data.data)
            # print(current_block.block_data.hash)
            current_block = current_block.next
            self.counter += 1
        return (self.counter)

    def get_blockdata (self, dataset):
        current_block = self.head
        flag = False
        while current_block is not None:
            if current_block.block_data.data == dataset:
                flag = True
                return current_block.block_data #.data, current_block.block_data.timestamp

            if current_block is None:
                return None

            if flag == True:
                break
            
            current_block = current_block.next


if __name__ == '__main__':

    def test_1():

        print('*************************************************************')
        blockchain = Blockchain()
        block1 = blockchain.add_block('Block_data_1')
        block2 = blockchain.add_block('Block_data_2')
        block3 = blockchain.add_block('Block_data_3')

        dataset1 = blockchain.get_blockdata("Block_data_1")             # 
        print("Block_data 1 timestemp :: ", dataset1.timestamp, " generated hash :::", dataset1.previous_hash )
        #Block_data 1 timestemp ::  2020-03-11 23:48:59.633645+00:00  generated hash ::: None

        dataset2 = blockchain.get_blockdata("Block_data_2")             # 
        print("Block_data 2 timestemp :: ", dataset2.timestamp, " generated hash :::", dataset2.hash )
        #Block_data 2 timestemp ::  2020-03-11 23:48:59.633942+00:00  generated hash ::: 1dbda1eed9c22000ad5e36dddf68964f4cc96454be526fc6f80f32057238995c

        dataset3 = blockchain.get_blockdata("Block_data_3")             # 
        print("Block_data 3 timestemp :: ", dataset3.timestamp, " generated hash :::", dataset3.hash )
        #Block_data 3 timestemp ::  2020-03-11 23:48:59.634035+00:00  generated hash ::: 0ad46359b3d83f01fdcb3c6e0ea6f369e18da517007d8565289b7724e05d4ad8

    def test_2():
        print('*************************************************************')
        blockchain = Blockchain()
        print("length of blockchain :: ", blockchain.traverse_chain())
        #length of blockchain ::  0  

    def test_3():

        print('*************************************************************')
        blockchain = Blockchain()
    
        for n in range(50):
            blockchain.add_block('Block_data_{}'.format(n))

        print("length of blockchain :: ", blockchain.traverse_chain())      
        #length of blockchain ::  50  

    test_1()
    test_2()
    test_3()

