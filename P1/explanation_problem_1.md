### Problem 1. Explanation ####

The project requires to develop solution which has to secure time operation for the range of complexity estimated to O(1) time. Due to the project constraint the solution (data structure) had to be take into account.
The solution strategy for LRU cache can be displayed as follows:
a. when set a new value goes to the front of cache as a most recently used value. The other values move back
b. when get value from cache operation moves this value at the front as most recently used. Other value are move back
c. when add value with the same key so the value is updated (not the key) - only value is updated. The updated node is going at the front of the cache
d. if we go over the capacity so the new value is going at the front but last value in cache is removed
e. if we would like to get the value with the key which is not exist so we return -1

Deployed design was based on hash table and doubly linked list. Hash table holds the node address (hash key) and serves a direct access to the linked list. Nodes (memory blocks in memory) as mentioned were organised in doubled linked list which holds the pointers to previous and next node.

As it was discussed in course the time complexity for hash table can be estimated for O(1) - we follow the project constraint and the complexity for deployed linked list also for O(1) - the nodes are only moved or removed from the list . Based on presented analysis we can estimated final complexity for presented algorithm for O(1). Space complexity (total and partial: for hash table and double linked list) can be estimated as 0(n)