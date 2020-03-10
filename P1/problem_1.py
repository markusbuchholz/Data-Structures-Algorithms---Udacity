"""
double link list
hash table holds the key

*** set new velue is goes to the front of cache as a most recently used value. The other values are go back
*** get velue from cache move this value at the front as most recently used . Other value are pushed back
*** when wy add value wiith the same kay soio the valuue is updated (not the key because is the same) but only value is updated. The updated node is going at the front od f cache
*** if we go over the capacity so the new veleu is going at the front but last velue in cache is removed
*** if we woud like to get the vale with the key which is not exist so we return -1
"""



class Node:

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None


class LRU_Cache:

    def __init__(self, capacity):
        self.capacity = capacity
        self.hashtable = {} 
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def _update_head_and_remove_node(self, node):
        
        _prev = node.prev
        _next = node.next

        _prev.next = _next
        _next.prev = _prev

        node.prev = self.head
        node.next = self.head.next

        self.head.next.prev = node
        self.head.next = node


    def get(self, key):

        if key not in self.hashtable:
            return -1

        node = self.hashtable[key]
        self._update_head_and_remove_node(node)

        return node.value

    def set(self, key, value):


        if key in self.hashtable:
            node = self.hashtable[key]
            node.value = value
   
            self._update_head_and_remove_node(node)

        else:
            node = Node(key, value)
           
            node.prev = self.head
            node.next = self.head.next

            self.head.next.prev = node
            self.head.next = node
            
            
            
            self.hashtable[key] = node


        if len(self.hashtable) > self.capacity:
            #self._remove_lru()
            node = self.tail.prev
            #self._remove(node)
            _prev = node.prev
            _next = node.next

            _prev.next = _next
            _next.prev = _prev
            del self.hashtable[node.key]



if __name__ == '__main__':

    def test_1(): # test from the course
        print("***********************************************")
        cache = LRU_Cache(5)
        cache.set(1, 1)
        cache.set(2, 2)
        cache.set(3, 3)
        cache.set(4, 4)

        print(cache.get(1)) 
        # 1
        print(cache.get(2)) 
        # 2
        print(cache.get(9))
        # -1 because 9 is not present in the cache
        cache.set(5, 5)
        cache.set(6, 6)
        print(cache.get(3))     
        # -1 because the cache reached it's capacity and 3 was the least recently used entry
        print(list(cache.hashtable.keys()))  
        # [1, 2, 4, 5, 6]

    def test_2(): #capacity test on cache
        print("***********************************************")
        cache = LRU_Cache(5)
        cache.set(1, 1)
        cache.set(2, 2)
        cache.set(3, 3)
        cache.set(4, 4)

        cache.set(5, 5)
        cache.set(6, 6)
        print(cache.get(1))         
        # -1
        print(cache.get(2))         
        # 2
        print(cache.get(3))         
        # 3

    def test_3(): #input testing
        print("***********************************************")
        cache = LRU_Cache(5)
        cache.set(1, 1)
        cache.set(2, 2)
        cache.set(3, 3)
        cache.set(4, 4)

        
        print(cache.get(99)) 
        # -1
        print(cache.get('abc'))         
        # -1
        print(cache.get(-10*2))     
        # -1
        print(cache.get(False))     
        # -1

    

    test_1() #from course
    test_2() #edge_test
    test_3() #edge_test
  