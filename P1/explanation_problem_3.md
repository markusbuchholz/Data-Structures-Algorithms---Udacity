## Problem 3. Explanation ####

Solution for the Huffman coding includes two data structure - dictionary (build a binary tree) for holding characters and frequencies on each level of the tree, and hash table (uses while encoding and decoding)
which keeps the as a value: binary string of zeros and ones and as a key: a character of provided sentence. Hash table secures time complexity as 0(1).
The slowest data structure deployed in proposed solution is a dictionary which in each iteration chooses (from sorted list) minimum 2 frequencies values (and characters).
This two frequencies values (and characters) are then merged creating new node. The time complexity for this operation can be estimated for O(n log n) which defines the final worst algorithm complexity.
The space complexity partial and as a final solution can be estimated for O(n), 