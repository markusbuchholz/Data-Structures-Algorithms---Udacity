### Problem 5. Explanation ###

The problem was solved in similar way to problem 1 where doubly linked list and has table were used. It this case the hash table hold hashed data, timestamp and previous hash (which was computed for previous block).
Doubled linked list holds the data block. It provides also methods to traverse the list and add a block. Time complexity is O(1) because the list holds tail pointer.
However traversing the list can be estimated as O(n).
The space complexity is relevant with the number of block to hold a data so the space complexity can be estimated for O(n)