"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
import numpy as np

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
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

    joined_dict = {}

    for line in calls:
        if line[0] in joined_dict:
            joined_dict[line[0]] += int(line[3])
        else:
            joined_dict[line[0]] = int(line[3])
        if line[1] in joined_dict :
            joined_dict[line[1]] += int(line[3])
        else:
            joined_dict[line[1]] = int(line[3])

    return joined_dict

def find_longest_time_and_user(record_dict):

    user_with_max_time = max(record_dict, key=record_dict.get)
    max_time_for_user = max(record_dict.values())

    return max_time_for_user, user_with_max_time

def main():
    record_dict = prepare_dict_for_input_record(calls)
    max_time_for_user, user_with_max_time = find_longest_time_and_user(record_dict)
    print(user_with_max_time, " spent the longest time, " , max_time_for_user, " seconds, on the phone during September 2016.")


if __name__ == "__main__":
    main()
 
  
