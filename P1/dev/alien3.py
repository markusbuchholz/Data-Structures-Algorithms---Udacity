
class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None
    
    
class LRU_Cache(object):

    def __init__(self, capacity):
        # Initialize class variables
        self.capacity = capacity
        self.hash_map = {}
        self.current_size = 0
        
        # initialize the queue 
        self.head = None
        self.tail = None
        
        pass
    
    def enqueue_at_head(self, node):
        if not self.head:
            self.head = node
            self.tail = node 
        else:
            node.prev = self.head
            self.head.next = node
            self.head = node
        self.current_size += 1
        
    def dequeue(self, node):
        if not self.head:
            return
        
        if node.prev:
            node.prev.next=node.next
            
        if node.next:
            node.next.prev=node.prev
            
        if not node.next and not node.prev:
            self.head = None
            self.tail = None
            
        if self.tail == node:
            self.tail = node.next
            
        self.current_size-=1
        
        return node
    
    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent. 
        if key not in self.hash_map:
            return -1
        
        node = self.hash_map[key]
        if self.head == node:
            return node.value
        
        self.dequeue(node)
        self.enqueue_at_head(node)
        
        return node.value
        pass

    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item. 
        if key in self.hash_map:
            node = self.hash_map[key]
            
            if self.head != node:
                self.dequeue(node)
                self.enqueue_at_head(node)
                
        else:
            new_node = Node(key,value)
            if self.current_size == self.capacity:
                del self.hash_map[self.tail.key]
                self.dequeue(self.tail)
            self.enqueue_at_head(new_node)
            self.hash_map[key]= new_node
        pass




our_cache = LRU_Cache(5)

our_cache.set(1, 1);
our_cache.set(2, 2);
our_cache.set(3, 3);
our_cache.set(4, 4);


our_cache.get(1)       # returns 1
our_cache.get(2)       # returns 2
our_cache.get(9)      # returns -1 because 9 is not present in the cache

our_cache.set(5, 5) 
our_cache.set(6, 6)

print(our_cache.get(3))      # returns -1 because the cache reached it's capacity and 3 was the least recently used entry



# In[ ]:



