"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
import numpy as np
from collections import Counter

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls_test.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""
def prepare_dict_for_input_record(calls):
    telephone_caller = []
    telephone_receiver = []
    call_duration1 = []
    call_duration2 = []
    joined_dict = {}

    for line in calls:
        #print(line[3])
        telephone_caller.append(str(line[0]))
        call_duration1.append(int(line[3]))
    print(telephone_caller)
    print(call_duration1)
    caller_dict = zip(list(telephone_caller), list(call_duration1))
    #print("1 ::", caller_dict)
    caller_dict = dict(caller_dict)
    print("2 ::", caller_dict)
    #print(telephone_caller)

        
    for line in calls:
        #print(line[3])
        telephone_receiver.append(str(line[1]))
        call_duration2.append(int(line[3]))

    receiver_dict = dict(zip(telephone_receiver, call_duration2))
    for d in (caller_dict, caller_dict): joined_dict.update(d)
   # print("1 ::", caller_dict)

    return joined_dict

def find_longest_time_and_user(record_dict):
    #print(record_dict)
    counter = Counter()
    for rec in record_dict:
        counter.update(rec)
    
    dict_sum = dict(counter)
    user_with_max_time = max(dict_sum, key=dict_sum.get)
    max_time_for_user = max(dict_sum.values())

    return max_time_for_user, user_with_max_time

def main():
    record_dict = prepare_dict_for_input_record(calls)
    max_time_for_user, user_with_max_time = find_longest_time_and_user(record_dict)
    #print(user_with_max_time, " spent the longest time, " , max_time_for_user, " seconds, on the phone during September 2016.")


if __name__ == "__main__":
    main()

    ini_dict = [{'a':5, 'b':10, 'c':90}, {'a':45, 'b':78}, {'a':90, 'c':10}] 
  
# printing initial dictionary 
    # print ("initial dictionary", str(ini_dict)) 
    
    # # sum the values with same keys 
    # counter = Counter() 
    # for d in ini_dict:  
    #     counter.update(d) 
        
    # result = dict(counter) 


# List of strings
    listOfStr = ["hello", "at" , "test" , "this" , "here" , "now", "now" ]
        
    # List of ints
    listOfInt = [56, 23, 43, 97, 43, 102,200000]
    zipbObj = zip(listOfStr, listOfInt)
    dictOfWords = dict(zipbObj)
    print(dictOfWords)
    
    
    # print("resultant dictionary : ", str(counter)) 