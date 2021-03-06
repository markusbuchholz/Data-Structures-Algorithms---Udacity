from collections import Counter
import sys


class LinkedListNode:
    
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashMap:
    
    def __init__(self, initial_size = 10):
        self.bucket_array = [None for _ in range(initial_size)]
        self.p = 31
        self.num_entries = 0
        
    def put(self, key, value):
        bucket_index = self.get_bucket_index(key)

        new_node = LinkedListNode(key, value)
        head = self.bucket_array[bucket_index]

        while head is not None:
            if head.key == key:
                head.value = value
                return
            head = head.next

        head = self.bucket_array[bucket_index]
        new_node.next = head
        self.bucket_array[bucket_index] = new_node
        self.num_entries += 1
        
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
            hash_code = hash_code % num_buckets                       
            current_coefficient *= self.p
            current_coefficient = current_coefficient % num_buckets  

        return hash_code % num_buckets                                
    
    def size(self):
        return self.num_entries



h_tree = []

def find_min(freq):
    item = min(freq, key=lambda i: i[0])
    freq.remove(item)
    return item

def compute_frequencies (data):


    freq = [(i, x) for x, i in Counter(data).items()]
    if len(freq) == 1:
        freq.append(tuple((0, 'None')))
  
    

    return freq




def huffman_codes(text):

    freq = compute_frequencies(text)


    while len(freq) > 1:
        left_i, left_j = find_min(freq)
        right_i, right_j = find_min(freq)
        freq.append((left_i + right_i, (left_j, right_j)))
    try:
        binary_coding(freq.pop()[1])
    except:
        print("No data to encode!")

def binary_coding(tree, prefix=''):
    
    if isinstance(tree, tuple):
        binary_coding(tree[0], prefix + '0')
        binary_coding(tree[1], prefix + '1')
    else:
        h_tree.append([tree, prefix])


def huffman_encoding(data):
    global h_tree
    h_tree = []
    tree = huffman_codes (data)
    hash_map = HashMap()

    for i in h_tree:
        hash_map.put(i[0], i[1])

    c = ''
    sum_c = ''
    for ch in data:
        c = hash_map.get(ch)
        sum_c = sum_c + c
    return sum_c, h_tree


def huffman_decoding(data, tree):

    hash_map = HashMap()
    for i in h_tree:
        hash_map.put(i[1], i[0])

    ijk = data 
    sum_ch=str('')
    decoding = ''

    for i in range(len(ijk)):
        sum_ch = ijk[i] + sum_ch
        sum_ch_rot = sum_ch[len(sum_ch)::-1]
        if hash_map.get(sum_ch_rot):
           
            d = hash_map.get(sum_ch_rot)
            decoding = decoding + d
            sum_ch=str('')
    
    return decoding




if __name__ == "__main__":
   
    def test_1():
        print("**************************************************")
        a_great_sentence = 'The Terminator and Michael Jordan AIR'
        
        encoded_data, tree = huffman_encoding(a_great_sentence)

        if encoded_data:
        
            print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
            print ("The content of the data is: {}\n".format(a_great_sentence))


            print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
            print ("The content of the encoded data is: {}\n".format(encoded_data))

            decoded_data = huffman_decoding(encoded_data, tree)

            print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
            print ("The content of the encoded data is: {}\n".format(decoded_data))

    def test_2():
        print("**************************************************")
        a_great_sentence = 'Markus Buchholz, Norway, 4032 Stavanger'

        encoded_data, tree = huffman_encoding(a_great_sentence)

        if encoded_data:

            print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
            print ("The content of the data is: {}\n".format(a_great_sentence))


            print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
            print ("The content of the encoded data is: {}\n".format(encoded_data))

            decoded_data = huffman_decoding(encoded_data, tree)

            print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
            print ("The content of the encoded data is: {}\n".format(decoded_data))


    def test_3():
        print("**************************************************")
        a_great_sentence = 'aaabbbbbcccccddddddddeeeeeeeefffffffffffffffffgggggggggggggggggggggggggggggåååååååøøøøøøøøøøøæææææææææ'

        encoded_data, tree = huffman_encoding(a_great_sentence)

        if encoded_data:

            print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
            print ("The content of the data is: {}\n".format(a_great_sentence))


            print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
            print ("The content of the encoded data is: {}\n".format(encoded_data))

            decoded_data = huffman_decoding(encoded_data, tree)

            print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
            print ("The content of the encoded data is: {}\n".format(decoded_data))


    def test_4():
        print("**************************************************")
       
        a_great_sentence = 'AAAAAAA'

        encoded_data, tree = huffman_encoding(a_great_sentence)

        if encoded_data:

            print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
            print ("The content of the data is: {}\n".format(a_great_sentence))

          

            print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
            print ("The content of the encoded data is: {}\n".format(encoded_data))

            decoded_data = huffman_decoding(encoded_data, tree)

            print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
            print ("The content of the encoded data is: {}\n".format(decoded_data))


    def test_5():
        print("**************************************************")
        
        a_great_sentence = '1111111'

        encoded_data, tree = huffman_encoding(a_great_sentence)

        if encoded_data:

            print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
            print ("The content of the data is: {}\n".format(a_great_sentence))


            print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
            print ("The content of the encoded data is: {}\n".format(encoded_data))

            decoded_data = huffman_decoding(encoded_data, tree)

            print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
            print ("The content of the encoded data is: {}\n".format(decoded_data))

    def test_6():
        print("**************************************************")
        
        a_great_sentence = ''

        encoded_data, tree = huffman_encoding(a_great_sentence)

        if encoded_data:

            print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
            print ("The content of the data is: {}\n".format(a_great_sentence))

            

            #print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
            print ("The content of the encoded data is: {}\n".format(encoded_data))

            decoded_data = huffman_decoding(encoded_data, tree)

            print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
            print ("The content of the encoded data is: {}\n".format(decoded_data))



    test_1()
    test_2()
    test_3()
    test_4()
    test_5()
    test_6()