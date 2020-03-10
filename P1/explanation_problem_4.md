### Problem 4. Explanation ###

Problem 4 was solved by implementing a recursive algorithm. which returns True when the user is in the group otherwise,
the checks is performed in other group for each sub group in the group, the function is called again and search the user.
The worst time complexity can be estimated considering the directly relation of numbers of group and subgroup to check. It this case the time complexity is O(n).
For deployed algorithm the space complexity is also O(n). Each group and subgroup are stored in array which grows lineary while number of group or subgroup increase.
