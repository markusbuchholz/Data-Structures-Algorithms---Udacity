
#By Udacity

def sort_012(data):
    
    next_pos_0 = 0
    next_pos_2 = len(data) - 1

    front_index = 0

    while front_index <= next_pos_2:
        if data[front_index] == 0:
            data[front_index] = data[next_pos_0]
            data[next_pos_0] = 0
            next_pos_0 += 1
            front_index += 1
        elif data[front_index] == 2:           
            data[front_index] = data[next_pos_2] 
            data[next_pos_2] = 2
            next_pos_2 -= 1
        else:
            front_index += 1

    return data


def test_function(test_case):
    sorted_array = sort_012(test_case)
    print(sorted_array)
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")

test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])
test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])
test_function([0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2])
test_function([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1])
test_function([2, 0, 1])
test_function([1,2,0])
test_function([0,2,1])
test_function([1,1,0,0,1,1,2,2])

# [0, 0, 0, 1, 1, 1, 2, 2, 2, 2, 2]
# Pass
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2]
# Pass
# [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2]
# Pass
# [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2]
# Pass
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
# Pass
# [0, 1, 2]
# Pass
# [0, 1, 2]
# Pass
# [0, 1, 2]
# Pass
# [0, 0, 1, 1, 1, 1, 2, 2]
# Pass

