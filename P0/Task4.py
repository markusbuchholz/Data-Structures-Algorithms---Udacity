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

def remove_telemarketer_gather_incomming_from_call_list (calls):
    cleared_list_callers = []
    called_numbers = []
    

    for line in calls:
        called_numbers.append(line[1])
        if ((line[0].find(" "))>-1) and ((line[0].find('140')) > -1):
            pass
        else:
            cleared_list_callers.append(line[0])
    return cleared_list_callers, called_numbers

def gather_text_numbers (texts):

    texts_sender = []
    texts_receiver = []

    for line in texts:
        texts_sender.append(line[0])
        texts_receiver.append(line[1])

    return texts_sender, texts_receiver


def remove_duplicants (messed_list): #for calls and texts
    unmessed_list = list((Counter(messed_list)).keys())
    return unmessed_list

def compare_lists (outgoing_calls, unmessed_list):

    never_received = list(set(outgoing_calls)^set(unmessed_list))
    return never_received

def sort_and_print(list_to_sort_and_print):
    list_to_sort_and_print.sort()  
    print("These numbers could be telemarketers:")
    for line in list_to_sort_and_print:
        print(line)
    return 0

def main():
    cleared_list_callers, called_numbers = remove_telemarketer_gather_incomming_from_call_list (calls)
    list_callers_unmessed = remove_duplicants(cleared_list_callers)
    called_numbers_unmessed = remove_duplicants(called_numbers)
    texts_sender, texts_receiver = gather_text_numbers (texts)
    texts_sender_unmessed = remove_duplicants(texts_sender)
    texts_receiver_unmessed = remove_duplicants(texts_receiver)
    never_received_call = compare_lists(list_callers_unmessed,called_numbers_unmessed)
    never_received_text = compare_lists(list_callers_unmessed,texts_receiver_unmessed)
    never_send_text = compare_lists(list_callers_unmessed,texts_sender_unmessed)
    removed_duplicnt_from_never_lists = remove_duplicants(never_received_call + never_received_text + never_send_text)
    sort_and_print(removed_duplicnt_from_never_lists)



if __name__ == "__main__":
    main()






