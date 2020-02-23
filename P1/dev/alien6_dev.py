#!/usr/bin/env python3


class Node:

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None


class LRU_Cache:

    def __init__(self, capacity):
        self.capacity = capacity
        self.hashtable = {} #dict()
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
            #self._add(node)
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





    def run_test_last_recently_used():
        print('\nRunning multiple tests....')
        # Initialize
        cache = LRU_Cache(5)
        cache.set(1, 1)
        cache.set(2, 2)
        cache.set(3, 3)
        cache.set(4, 4)
        # cache.set(5, 5)
        # print(cache.set(6, 6))
        # print(cache.set(7, 7))
        # print(cache.set(8, 8))
        # print(cache.set(9, 9))
        # print(cache.set(10, 10))

        print(cache.get(1))     # 1
        print(cache.get(2))
        print(cache.get(9))     # 2
        #print(cache.get(9))     # -1 because 9 is not present in the cache
       # print(list(cache.hashtable.keys()))
    

        cache.set(5, 5)
        cache.set(6, 6)
        print("******************'")
        print(cache.get(3))     # -1 because the cache reached it's capacity and 3 was the least recently used entry
        print(list(cache.hashtable.keys()))  # [1, 2, 4, 5, 6]


    run_test_last_recently_used()