# a = 11/2
# b = 11//2
# c= 11%2
# print (a, " :: ", b, " :: ", c )

# d = 'number'
# d = 0
# try:
#     dd = d/1
# except:
#     print("string")
# print(dd)


def test_wrong(input_list):

    index0 = 0
    index1 = 1
    index2 = len(input_list) - 1

    list_sorted  = [0] * (len(input_list))
    temp = [] 

    for i in range (len(input_list)):
        if input_list[i] == 0:
            list_sorted[index0] = 0
            index0 = index0 + 1
            print(":0: ", list_sorted)
        if input_list[i] == 2:
            list_sorted[index2] = 2
            index2 = index2 -1
            print(":2: ", list_sorted)
        if input_list[i] == 1:
            temp.append(1)

    for j in range (len(temp)):
        list_sorted[index0 + j] = 1
        print(":1: ", list_sorted) 

    return list_sorted


def test (input_list):
    index0 = 0
    index2 = len(input_list) - 1

    list_sorted  = [1] * (len(input_list))

    for i in range(len(input_list)):
        if input_list[i]==0:
            list_sorted[index0] = 0
            index0 = index0+1
            print(":0: ", list_sorted)
        if input_list[i]==2:
            list_sorted[index2] = 2
            index2 = index2 -1
            print(":2: ", list_sorted)
    return list_sorted
        # if input_list[i] ==1:
        #     index


#data = ([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
data = ([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])
#       [0, 0, 0, 1, 1, 1, 2, 2, 2, 2, 2]]

list_sorted = test(data)
test = sorted(data)
print(list_sorted == test)
#print(list_sorted)

# list_2 = [0]*10
# list_2 [5] = 99
# print(list_2)