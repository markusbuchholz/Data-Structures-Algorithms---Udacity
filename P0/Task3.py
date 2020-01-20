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


def find_fix_lines_mobile_tele_called_from_bangladore(calls):
  fix_lines = []
  mobile = []
  telemarketers = []
  for record in calls:
    if ((record[0].find('(080)'))!= -1):
      fix_lines.append(record[1])
    if ((record[0].find(" "))> -1):
      mobile.append(record[1])
    if ((record[0].find(" "))==-1) and ((record[0].find('140'))!= -1):
      telemarketers.append(record[1])
  return fix_lines, mobile, telemarketers



def grab_area_codes (fix_lines, mobile, telemarketers):

  codes_fix_lines = []
  codes_mobile = []
  codes_telemarketers = []
  area_codes = []
  code_str = ""

  for lines in fix_lines + mobile + telemarketers:
    
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
  occurence_in_incomming_list = list((Counter(list_to_sort)).keys())
  occurence_in_incomming_list.sort()
  return occurence_in_incomming_list


def printing_output_per_line(list_to_print):
  
  print("The numbers called by people in Bangalore have codes:")
  for line in list_to_print:
    print(line)
  return 0

  
def banglador_internal_fix_line_calls(fix_lines):

  total_calls = len(fix_lines)
  line_counter = 0
  for internal_line in fix_lines:
    if ((internal_line.find('(080)'))!= -1):
      line_counter +=1
  print(round((line_counter/total_calls)*100), "percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.")

  return 0

def main():
  fix_lines, mobile, telemarketers = find_fix_lines_mobile_tele_called_from_bangladore (calls)
  area_codes = grab_area_codes (fix_lines, mobile, telemarketers)
  sorted_list_of_area_codes = sorting_area_code_list(area_codes)
  printing_output_per_line(sorted_list_of_area_codes)
  banglador_internal_fix_line_calls(fix_lines)


if __name__ == "__main__":
  main()











