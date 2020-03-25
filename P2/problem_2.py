
#https://www.geeksforgeeks.org/search-an-element-in-a-sorted-and-pivoted-array/

def findPivot(arr, low, high): 
      
    # base cases 
    if high < low: 
        return -1
    if high == low: 
        return low 
      
    #low + (high - low)/2; 
    mid = int((low + high)/2) 
      
    if mid < high and arr[mid] > arr[mid + 1]: 
        return mid 
    if mid > low and arr[mid] < arr[mid - 1]: 
        return (mid-1) 
    if arr[low] >= arr[mid]: 
        return findPivot(arr, low, mid-1) 
    return findPivot(arr, mid + 1, high) 


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
    low = 0
    high = len(input_list) - 1

    pivot = findPivot(input_list  ,low, high)
    #print("pivot ::", pivot)

    rotated = rotate_array(input_list, pivot)
    
    index = find_target_index(rotated,number,0, len(input_list)-1)
    

    if index == -1:
        return -1

    if input_list[pivot]== number :
        return pivot

    if rotated[pivot] == number:
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
            return index
    return -1

def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")

test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])

test_function([[], 1])
test_function([[-2, 90, 100, -2, 2, 3, 4], 2])
test_function([[-2, 90, 100, -2, 2, 3, 4], 0])


# Pass
# Pass
# Pass
# Pass
# Pass
# Pass
# Pass
# Pass

