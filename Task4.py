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

#sum_num_dict include never text, receive text messages or receive calls

sum_num_dict = {}

#get sum_num_dict from calls

for per_call in calls:

    sum_num_dict[per_call[1]] = sum_num_dict.get(per_call[1], 0) + 1

#get sum_num_dict from texts

for per_text in texts:

    sum_num_dict[per_text[1]] = sum_num_dict.get(per_text[1], 0) + 1



#call_dict include num which make a call

call_dict = {}

for per_rec in calls:

    call_dict[per_rec[0]] = call_dict.get(per_rec[0], 0) + 1



#Sort the call_dict

sort_dict = sorted(call_dict.items(), key=lambda d:d[0])



#Get the number that meets the requirements and print it

print("These numbers could be telemarketers: ")

for sort_num in sort_dict:

    if sort_num[0] not in sum_num_dict:

        print(sort_num[0])
