"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
from collections import Counter

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

def collect_callers_receivers (calls):
    
    list_of_receivers = []
    list_of_callers = []

    for line in calls:
        list_of_receivers.append(line[1])
        if (((line[0].find(" "))>-1) and ((line[0].find('140')) > -1)) == False:
            list_of_callers.append(line[0])
    return list_of_callers, list_of_receivers

def gather_text_numbers (texts):
    
    texts_sender = []
    texts_receiver = []
    for line in texts:
        texts_sender.append(line[0])
        texts_receiver.append(line[1])
    return texts_sender, texts_receiver

def compare_lists (list_of_callers, combined_list):
    
    never_received = [x for x in list_of_callers if x not in combined_list]
    never_received.sort()
    never_received = list((Counter(never_received)).keys())
    return never_received


def main():
    list_of_callers, list_of_receivers = collect_callers_receivers(calls)
    texts_sender, texts_receiver = gather_text_numbers(texts)
    combined_list = list_of_receivers + texts_sender + texts_receiver
    never_received = compare_lists(list_of_callers, combined_list)
    print("These numbers could be telemarketers: " , *never_received, sep='\n')

    
if __name__ == "__main__":
    main()