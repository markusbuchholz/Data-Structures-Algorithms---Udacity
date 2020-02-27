import sys
from collections import Counter


def compute_frequencies (data):

    data = data.replace(" ", "")
#    print(data)
    freq = Counter(data)
    freq = sorted(freq.items(), key=lambda pair: pair[1], reverse=False)
    return freq

def huffman_encoding(data):
    print("**********************")
    code = []
    ch = 'h'
    tree_to_code = []

    for i in range(len(data)):
        tree_to_code.append(data[-1-i])
        print(data[-1-i])
    check_node = []
    print("tree  ::::::::::::::::::::::::::::::::::::::::::: ",tree_to_code)
    flag = False
    for node in tree_to_code:
        print ("node ::: ", node)
        print ("node [0] ", node[0])
        print ("publish ::", node[1:])

        # if len(check_node) == 1:
        #     break
        # for sub in node[1:]:
        #     print("sub :::", sub)
        #     if ((sub.find(ch) > -1) and (len(sub) == 1)):
        #         flag = True
        #         break
        # if flag == True:
        #     break

        if node[0].find(ch) > -1:
            code.append(0)
            # check_node = node[0]
            # if len(check_node) == 1:
            #     break
        if node[0].find(ch) == -1:
            code.append(1)


        for sub in node:
            print("sub :::", sub)
            if ((sub.find(ch) > -1) and (len(sub) == 1)):
                flag = True
                break
        if flag == True:
            break


        # if flag == True:
        #     break


    print(code)
    
    # for j in range (len(tree_to_code) -1):
    #     compare = list(set(tree_to_code[j+1]) - set (tree_to_code[j]))
    #     compare2 = list(set(tree_to_code[j]) - set (tree_to_code[j+1]))
        #print("*********" )
        #print(compare)
        #print(compare2)
        # flag1 = False
        # flag2 = False
        # if compare[0].find(ch) > -1:
        #     code.append(0)
        #     flag1 = True
        # if compare[1].find(ch) > -1:
        #     code.append(1)
        #     flag2 = True
        # if flag1 == False and flag2 == False:
        #     code.append(1)
    
    #print(code)
        
        #print(compare)




def huffman_decoding(data,tree):
    pass



def build_binary_tree(freq):
    freq_tree = []
    freq_aux = []
    while(len(freq) > 1):
        
        freq_tree.append(list(freq))
        f_temp = []
        for i in freq:
            f_temp.append(i[0])

        freq_aux.append(f_temp)
        f0 = freq.pop(0)
        f1 = freq.pop(0)
        freq.insert(0,(f0[0] + f1[0], f0[1] + f1[1]))
        freq.sort(key=lambda tup: tup[1])
        #print(freq)
        
 
    return freq_tree, freq_aux



if __name__ == "__main__":
    codes = {}

    a_great_sentence = "The bird is the word"
    #a_great_sentence = "aabbbcccccdddddddd"


    # print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    # print ("The content of the data is: {}\n".format(a_great_sentence))

    # encoded_data, tree = huffman_encoding(a_great_sentence)

    # print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    # print ("The content of the encoded data is: {}\n".format(encoded_data))

    # decoded_data = huffman_decoding(encoded_data, tree)

    # print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    # print ("The content of the encoded data is: {}\n".format(decoded_data))
    freq = compute_frequencies(a_great_sentence)
    #print("type freq ", type(freq))
    f_t, f_aux =build_binary_tree(freq)
    # for i in range(len(f_aux)):
    #     print(f_aux[i])
    
    huffman_encoding (f_aux)
    



    # y = []

    # for i in range(len(f_aux)):
    #     y.append(f_aux[-1-i])
    
    # for jj in y:
    #     print(jj)

    # a1 = ['Tbh', 'wost', 'rdei']
    # a2 = ['rd', 'ei', 'Tbh', 'wost']
    # a1 = ['w', 'o', 'st', 'Tb', 'h', 'e', 'i', 'r', 'd']
    # a2 = ['s', 't', 'w', 'o', 'Tb', 'h', 'e', 'i', 'r', 'd']
    # for jk in range (len(a2)-1):
    #     print(a2[jk], a2[jk+1])

    # compare = list(set(a2) - set (a1))
    # print(compare)


    
    # q0 = []
    # q1 = [('e', 2), ('i', 2), ('r', 2), ('d', 2), ('Tbh', 4), ('wost', 4)]
    # q2 = [('e', 2), ('i', 2), ('r', 2), ('d', 2), ('Tbh', 4), ('wost', 4)]
    # q0.append(q1)
    # q0.append(q2)
    # print(q0)
    # print("1 :::", freq)
    # f0 = freq.pop(0)
    # f1 = freq.pop(0)

    # #print ("c :::", c)
    # #print("2 :::", a)
    # f2 = (f0[0] + f1[0], f0[1] + f1[1]) 
    # freq.insert(0,(f0[0] + f1[0], f0[1] + f1[1]))
    # print ("f ::: ", freq)
    # freq.sort(key=lambda tup: tup[1])
    # #freq = sorted(freq.items(), key=lambda pair: pair[1], reverse=False)
    # print ("f ::: ", freq)

    
    # #a.insert(0,c)
    # print("f2 :::", f2)


    # #print(a[0][0]+a[1][0])

    # x = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    #a[3:6] = [''.join(a[3:6])]
    #print(c)
    


    # for i in a:
    #     print(i[1])