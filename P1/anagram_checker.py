from collections import Counter



def anagram_checker(str1, str2):
    str3 = str1
    str1_key = list((Counter(str1)).keys())
    str1_value =list((Counter(str1)).values())
    str2_key = list((Counter(str2)).keys())
    str2_value =list((Counter(str2)).values())

    # print(list(str1_key))
    # print(str1_value)
    # str1 = Counter(str1)
    # str2 = Counter(str2)
    # print(str3.find("a"))
    #print(str2)

    for s2_k in str2_key:
        print(str1.find(s2_k))
        # for s1_k in str1_key:
        #     if (str1['s1_k']>=str2['s2_k']) :
        #         print("")
        #     if (s2_k==s1_k):
        #         pass #print("OK")
        #     else:
        #         pass #print("bad")
    


sort_test = [45,67,3,5,6,22,1,9,8,7,544,33,0,7,5,3,77,55,77,45,43,45,67,44,22,11,22,55,771,6,7,8,9,3,4,5,6,7,8,9]
test_values = (Counter(sort_test)).values()
#print(occurence_test_values)
test_keys = (Counter(sort_test)).keys()

anagram_checker('Slot machines', 'Slot machines')

#print(test_values)


