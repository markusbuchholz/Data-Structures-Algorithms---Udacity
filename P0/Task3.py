"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
import numpy as np
from collections import Counter 



with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""


def find_lines_called_from_bangladore(calls):

  calls_bangladore = []
  
  for record in calls:
    if ((record[0].find('(080)'))> -1):
      calls_bangladore.append(record[1])
  
  return calls_bangladore



def grab_area_codes (calls_bangladore):

  area_codes = []
  code_str = ""

  for lines in calls_bangladore:
    
    i = lines.find('(')
    j = lines.find(')')
    
    if (i and j ) > -1:

      number = []
      for k in range(len(lines)):
        if (k > i and k < j):
            number.append(lines[k])

      area_codes.append(code_str.join(number))
    
    if ((lines.find(" ")!=-1) and (lines[0] == 7 or 8 or 9)):
      area_codes.append(lines[0:4])
      
  return area_codes
    
def sorting_area_code_list(list_to_sort):

  occurence_in_incomming_list = list(set(list_to_sort))
  occurence_in_incomming_list.sort()
  return occurence_in_incomming_list
  
def internal_fix_lines(fix_lines):

  total_calls = len(fix_lines)
  line_counter = 0
  for internal_line in fix_lines:
    if ((internal_line.find('(080)'))!= -1):
      line_counter +=1
  print(format((line_counter/total_calls)*100,'.2f'), "percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.")

  return 0

def main():

  calls_bangladore = find_lines_called_from_bangladore (calls)
  area_codes = grab_area_codes (calls_bangladore) 
  sorted_list = sorting_area_code_list(area_codes)
  print("The numbers called by people in Bangalore have codes: " , *sorted_list, sep='\n')
  internal_fix_lines(calls_bangladore)


if __name__ == "__main__":
  
  main()