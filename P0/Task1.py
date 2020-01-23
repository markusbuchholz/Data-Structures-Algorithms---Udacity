"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
import numpy as np
from collections import Counter
#import Counter

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""


def merge_telephone_numbers (list1, list2):

    telephone_numbers = []
    telephone_list = [list1, list2]
    for _list in telephone_list:

        for tel in _list:
            telephone_numbers.append(tel[0])
            telephone_numbers.append(tel[1])
    return telephone_numbers

def check_different_numbers(all_telephone_numbers):
    
    different_telephone_occurence = (Counter(all_telephone_numbers)).values()
    return len(different_telephone_occurence)


def main():

    merged_list_of_telephones = merge_telephone_numbers(texts,calls)
    different_telephone_numbers = check_different_numbers(merged_list_of_telephones)
    print("There are ", different_telephone_numbers," different telephone numbers in the records.")
 

if __name__ == "__main__":
    main()


