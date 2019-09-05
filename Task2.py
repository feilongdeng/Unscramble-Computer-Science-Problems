"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
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

time_dict = {}


for per_rec in calls:

    for per_num in per_rec[:2]:

        time_dict[per_num] = time_dict.get(per_num, 0) +  int(per_rec[3])


sort_time = sorted(time_dict.items(), key=lambda d:d[1], reverse=True)


print("{} spent the longest time, {} seconds, on the phone during September 2016.".format(sort_time[0][0], sort_time[0][1]))
