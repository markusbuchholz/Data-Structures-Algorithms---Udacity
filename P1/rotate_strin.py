my_string= ' markus'
temp_string = ' '
temp_string += my_string[-len(my_string)+1]

print(temp_string)

def rotate_string(input_string):

    temp_str = ' '
    i = 1
    for ch in input_string:
        temp_str +=input_string[-i]
        i+=1
        if i > len(input_string):
            break
    print(temp_str)


rotate_string ('retaw')