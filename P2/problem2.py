
nums = [27,29,32,33,88,4,7,6,8,12,13,16,22,23]
#nums = [1,2,3,4,5,6]


def find_pivot(data):
    for i in range (len(data)-1):
        if data[i+1]<data[i]:
            return i    
    return -1

def rotate_array(data, pivot):
    rotated = data[pivot+1:]+ data[0:pivot+1]
    return rotated


def find_target_index(array, target, start_index, end_index):
    if start_index > end_index:
        return -1
    
    mid_index = (start_index + end_index)//2
    mid_element = array[mid_index]
    
    if mid_element == target:
        return mid_index
    elif target < mid_element:
        return find_target_index(array, target, start_index, mid_index - 1)
    else:
        return find_target_index(array, target, mid_index + 1, end_index)


def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """
    pivot = find_pivot(input_list)
    print("pivot index ::", pivot, "element :: ", input_list[pivot])
    rotated = rotate_array(input_list, pivot)
    print("rotated :: ", rotated)
    index = find_target_index(rotated,number,0, len(input_list)-1)
    print("index in rotated ::: ", index)

    if index == -1:
        return -1

    #nums = [27,29,32,33,88,4,7,6,8,12,13,16,22,23]
    #print("check ::", rotated[pivot])
   # print("check :: ", input_list[len(input_list)-1])
    if input_list[pivot]== number :
        return pivot

    if rotated[pivot] == number:
        print("check ::", rotated[pivot])
        return 0
    if number > input_list[len(input_list)-1]:
        return index - pivot + 1 
    if number < input_list[len(input_list)-1]:
        return index + pivot + 1
    else:
        return 0

def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            #print("linear :: ", index)
            return index
    return -1

def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    lin = linear_search(input_list, number)
    rot = rotated_array_search(input_list, number)

    print( "lin ::", lin, " rot :: ", rot)
    if lin == rot:
        print("Pass")
    else:
        print("Fail")

test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])

# 2 => pivot + index = 4 + 1 + 1
# 6 => pivot + index = 4 + 1 + 1
# 6, 7, 8, 9, 10,-- 1, 2, 3, 4
# 1, 2, 3, 4 ----- 6, 7, 8, 9, 10

# 9 => index - pivot + 1 = 5-3+1
# 6 => 4
# 6, 7, 8, 9, 10,-- 1, 2, 3, 4
# 1, 2, 3, 4 ----- 6, 7, 8, 9, 10

