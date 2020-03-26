Project Explanation

Problem 3

Similarly to solution displayed while solving problem 2 the algorithm was divided by two parts (data structure used in this type of algorithm is an array). First by use of merge and sort the give input array is sorted. The time complexity for this part can be estimated for O(nlog(n)), where the n is the length of array digits. In second part the the required numbers are computed. In discussed art the while loop was used so the time complexity is O(n). Finally the time complexity of mentioned  above two parts of deployed algorithm can be estimated as O(nlog(n)) - merge and sort algorithm deployed in first part of presented solution.
The space complexity, based on deployed merge and sort algorithm can be estimated as O(n), since the applied algorithm copies frequently the given values into new arrays (auxiliary space/extra space). Only two new arrays at every recursive step are needed - one array where values are stored and one array where the values are copied into - it means that in every recursive step the function call stack and creates new array (merged = []) while the other arrays are deleted.

