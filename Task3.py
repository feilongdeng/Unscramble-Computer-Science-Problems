"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

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

import re



#The prefixs dict of numbers

prefix_dict = {}



#Get the numbers called by people in Bangalore

for per_rec in calls:

    #Bangalore numbers

    if per_rec[0].startswith('(080)'):

        #Landline

        pre_1 = re.findall('^\(0.+\)',per_rec[1])

        #Mobile phone

        pre_2 = re.findall('^[7-9].+',per_rec[1])

        #Sales call

        pre_3 = re.findall('^140',per_rec[1])

        

        if len(pre_1) > 0:

            prefix_dict[pre_1[0]] = prefix_dict.get(pre_1[0], 0) + 1

        elif len(pre_2) > 0:

            prefix_dict[pre_2[0][:4]] = prefix_dict.get(pre_2[0][:4], 0) + 1

        elif len(pre_3) > 0:

            prefix_dict[pre_3[0]] = prefix_dict.get(pre_3[0], 0) + 1



#Sort the prefix_dict

sort_dict = sorted(prefix_dict.items(), key=lambda d:d[0])



#"The numbers called by people in Bangalore have codes:"

# <list of codes>

print("The numbers called by people in Bangalore have codes:")

for prefix in sort_dict:

    print(prefix[0])



'''

Second Part

'''

#Sum numbers called by people in Bangalore

sum_num = 0;

for key in prefix_dict:

    sum_num += prefix_dict[key]

    

percentage = (prefix_dict["(080)"] / sum_num) * 100

print("\n")

print("{} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.".format('%.2f'%percentage))
