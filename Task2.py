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

# a dictionary for each phone number and their time-spent
time_spent = {}

# add up all time for each one
for call in calls:
    # calling out
    time_spent[call[0]] = time_spent.get(call[0], 0) + int(call[3])
    # answering
    time_spent[call[1]] = time_spent.get(call[1], 0) + int(call[3])

# sort
results = sorted(time_spent.items(), reverse=True, key=lambda x:x[1])    
longest = results[0]

# print result
print(f"{longest[0]} spent the longest time, {longest[1]} seconds, on the phone during September 2016.")