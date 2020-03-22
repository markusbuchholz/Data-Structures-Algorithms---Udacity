"""
[38,27,43,3,9,82,10]
[38,27,43,3][9,82,10]
[38,27][43,3][9,82][10]
[38][27] [43][3] [9][82][10]

-------------------------------
[27,38][3,43] [9,82][10]
take 27 and compare with other list (if lower) - with 3 and 43 if lower put on the list if not put 27 on te list. Next take a 38.
If it is done tke next 
[3,27,38,43] [9,10,82]

3<9 - 3
9<27 - 9
27<10 - 10
27<82 -27
82<38 - 38
82<43 -43


[3,9,10,27,38,43,82]


#######

[4, 6, 2, 5, 9, 8]

[9, 8, 6, 5, 4, 2]

[964][852]
"""






def mergesort(items):

    if len(items) <= 1:
        return items
    
    mid = len(items) // 2
    left = items[:mid]
    right = items[mid:]
    
    left = mergesort(left)
    right = mergesort(right)
    
    return merge(left, right)
    
def merge(left, right):
    
    merged = []
    left_index = 0
    right_index = 0
    
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            merged.append(right[right_index])
            right_index += 1
        else:
            merged.append(left[left_index])
            left_index += 1

    merged += left[left_index:]
    merged += right[right_index:]
        
    return merged


def compute_numbers(data):
    number1 = []
    number2 = []

    while data:

        number1.append(data.pop())
        if data:
            number2.append(data.pop())

    # for i in range (len(data)):
    #     number1.append(data[2*i])
    #     number2.append(data[2*i+1])

    return number1, number2


nr1, nr2 = compute_numbers([9, 8, 6, 5, 4, 2])
print(nr1, " :: ", nr2)

nr1, nr2 = compute_numbers([2, 4, 5, 6, 8, 9])
print(nr1, " :: ", nr2)

nr1, nr2 = compute_numbers([2,3, 4, 5, 6, 8, 9])
print(nr1, " :: ", nr2)

# test_list_1 = [8, 3, 1, 7, 0, 10, 2]
# test_list_2 = [1, 0]
# test_list_3 = [97, 98, 99]
# test_list_4 = [38,27,43,3,9,82,10]
# print('{} to {}'.format(test_list_1, mergesort(test_list_1)))
# print('{} to {}'.format(test_list_2, mergesort(test_list_2)))
# print('{} to {}'.format(test_list_3, mergesort(test_list_3)))
# print('{} to {}'.format(test_list_4, mergesort(test_list_4)))