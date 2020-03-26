Project Explanation


Problem 2

The solution of this problem has been divided by two parts. In first part the algorithm searching the pivot index number (divide the array in two sub-arrays) where the array was rotated and then rotate the given array back. Afterwards, the algorithm (second part) uses the binary search method to find the index of given target.
The binary search algorithm (the recursive type) has been deployed in both part of proposed solution so the final time complexity of the algorithm is O(log(n)), where the n is the length of input array. The data structure used to solve the problem is array which is recursively manipulated.
The space complexity of deployed algorithm can be estimated also for O(log(n)) - n is the length of input array, since the recursive type of binary search was used. Due to implementation of recursive approach of binary search, at each stage, the recursive call of stack is applied. That means leaving the current invocation on the stack, and calling a new one. In each recursion only the half on previous array has to be stored so the needed space is decreasing logarithmically.