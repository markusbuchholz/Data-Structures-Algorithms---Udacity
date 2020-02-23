"""
double link list
hash table holds the key

*** set new velue is goes to the front of cache as a most recently used value. The other values are go back
*** get velue from cache move this value at the front as most recently used . Other value are pushed back
*** when wy add value wiith the same kay soio the valuue is updated (not the key because is the same) but only value is updated. The updated node is going at the front od f cache
*** if we go over the capacity so the new veleu is going at the front but last velue in cache is removed
*** if we woud like to get the vale with the key which is not exist so we return -1
"""


class CacheItem:
    def __init__(self, key, value):
        self.key = key
        self.value = value

class LRU_Cache(object):
    def __init__(self, capacity):
        self.size = capacity
        self.backet_array = [None for i in range(self.size)]
        self.count = 0
        self.p = 37
        self.recently_used = None
        self.head = None
        self.tail = None
        self.next = None
        self.prev = None

    def _hash(self, key):
        mult = 1
        hash_value = 0
        if type(key) == int:
            key = str(key)
        for ch in key:
            hash_value += mult * ord(ch)
            mult += 1
        #print("hash_value:::", hash_value )

        hash_code = 0
        mpx = 1
        for char in key:
            hash_code =  mpx * ord(char) 
            mpx *= self.p
            mpx = mpx
        #print("hash_code :::", hash_code)
        return hash_code % self.size
        #return hash_value % self.size

    def set(self, key, value):
        if self.count == self.size:
            return -1
        item = CacheItem(key, value)
        h = self._hash(key)

        #while self.backet_array[h] is not None:
        if self.backet_array[h].key is key:
            item.value = value
            #now move to the front
                



            #h = (h + 1) % self.size
        # if self.backet_array[h] is None:
        #     self.count += 1
        # self.backet_array[h] = item
        #print("from set c:", self.count)
       # print(" ===  ", self.backet_array[h].value)
        #self.recently_uded = item

    def get(self, key):
        h = self._hash(key)
        while self.backet_array[h] is not None:
            if self.backet_array[h].key is key:
                return_actual_value = self.backet_array[h].value
                self.backet_array[h] = return_actual_value
                self.count -=1
               # print("from get :", self.count)
                return return_actual_value
            h = (h + 1) % self.size
        return -1

##%% 
our_cache = LRU_Cache(6)
our_cache.set(1, 1);
our_cache.set(2, 2);
our_cache.set(3, 3);
our_cache.set(4, 4);


print(our_cache.get(1))       # returns 1
print(our_cache.get(2))       # returns 2
print("from 9 ", our_cache.get(9))      # returns -1 because 9 is not present in the cache

our_cache.set(5, 5)
our_cache.set(6, 6)

print(our_cache.get(3))      # returns -1 because the cache reached it's capacity and 3 was the least recently used entry