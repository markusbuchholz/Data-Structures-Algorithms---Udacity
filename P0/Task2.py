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

def find_longest_call (list_of_records):

    list_of_calls_duration = []

    for call in list_of_records:
        list_of_calls_duration.append(int(call[3]))

    return max(list_of_calls_duration)

def check_how_many_numbers_spent_longest_time(longest_call, list_of_records):
    
    number_of_phones_with_longest_call = 0
    for record in list_of_records:
        if int(record[3]) == longest_call:
            number_of_phones_with_longest_call+=1
    return number_of_phones_with_longest_call


def find_phone_number_for_the_longest_call(longest_call, list_of_records):

    for record in list_of_records:
        if int(record[3]) == longest_call:
            return record[0]

def main():
    longest_call = find_longest_call(calls)
    telephone_number_with_longest_call = find_phone_number_for_the_longest_call (longest_call, calls)
    print(telephone_number_with_longest_call," spent the longest time,", longest_call ,"seconds, on the phone during September 2016.")



if __name__ == "__main__":
    main()

