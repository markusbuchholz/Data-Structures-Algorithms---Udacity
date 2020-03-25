def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    _min = 0
    _max = 0
    for i in range (len(ints) - 1):
        if _max < ints[i]:
            _max = ints[i]
        if ints[i]<_min:
            _min = ints[i]



    return (_min, _max)
## Example Test Case of Ten Integers
import random

l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)

print ("Pass" if ((0, 9) == get_min_max(l)) else "Fail")