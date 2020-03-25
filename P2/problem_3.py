

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
        if left[left_index] > right[right_index]:
            merged.append(right[right_index])
            right_index += 1
        else:
            merged.append(left[left_index])
            left_index += 1

    merged += left[left_index:]
    merged += right[right_index:]
        
    return merged

def convert(list): 
      
    s = [str(i) for i in list] 
      
    res = int("".join(s)) 
      
    return(res) 
  


def compute_numbers(data):
    number1 = []
    number2 = []

    while data:

        number1.append(data.pop())
        if data:
            number2.append(data.pop())


    number1 = convert(number1)
    number2= convert(number2)

    
    return number1, number2


def rearrange_digits(input_list):

    number1, number2 = compute_numbers(mergesort(input_list))
  

    return [number1, number2]



def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    #print(output)
    #print(solution)
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")

test_function([[1, 2, 3, 4, 5], [531, 42]])

test_function([[4, 6, 2, 5, 9, 8], [964, 852]])
test_function([[0, 0, 9, 9, 8, 2], [980, 920]])
test_function([[0, 0, 0, 0, 9, 9, 9, 9], [9900, 9900]])

test_function([[1, 9, 8, 2, 6, 3, 5, 4, 0], [96420, 8531]])

# Pass
# Pass
# Pass
# Pass
# Pass