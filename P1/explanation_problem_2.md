### Problem 2. Explanation ####

Given problem has been solved by deploying recursion algorithm. The algorithm is exhausted (finishes checks) when the potential list of the file paths is empty.
For this algorithm, we can consider to have two different aspects to analyze: the number of files in each directory (N) within the given directory path and the depth of the directory tree that will be analyzed (D) which represents the number of calls of function find_files().
Based on given definition we are able to estimated the time complexity as O(N*D).
For the space complexity, the efficiency is directly dependent on the number of returns the function performs. It means the number of files N which match suffix in given path. The total space efficiency can be estimated as O(N).
