class HashItem:
    def __init__(self, key, value):
        self.key = key
        self.value = value

class LRU_Cache(object):
    def __init__(self, capacity):
        self.size = capacity
        self.backet_array = [None for i in range(self.size)]
        self.count = 0

    def _hash(self, key):
        mult = 1
        hash_value = 0
        if type(key) == int:
            key = str(key)
        for ch in key:
            hash_value += mult * ord(ch)
            mult += 1
        return hash_value % self.size

    def set(self, key, value):
        item = HashItem(key, value)
        h = self._hash(key)

        while self.backet_array[h] is not None:
            if self.backet_array[h].key is key:
                break
            h = (h + 1) % self.size
        if self.backet_array[h] is None:
            self.count += 1
        self.backet_array[h] = item

    def get(self, key):
        h = self._hash(key)
        while self.backet_array[h] is not None:
            if self.backet_array[h].key is key:
                return self.backet_array[h].value
            h = (h + 1) % self.size
        return None



our_cache = LRU_Cache(5)




#our_cache.set("abc", 1);
our_cache.set(2, 7772);
# our_cache.set(3, 3);
# our_cache.set(4, 4);


print(our_cache.get(2))       # returns 1
# our_cache.get(2)       # returns 2
# our_cache.get(9)      # returns -1 because 9 is not present in the cache

# our_cache.set(5, 5) 
# our_cache.set(6, 6)

# our_cache.get(3)  # returns -1


