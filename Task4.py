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

# step 1: create a white list recording the numbers cannot be telemarketers
#         also record the suspect numbers
white_list = set()
suspect_list = set()
for item in texts:
    white_list.add(item[0])
    white_list.add(item[1])
for item in calls:
    suspect_list.add(item[0])
    white_list.add(item[1])

# step 2: find out the calling number that is not in the white list
telemarketers = suspect_list - white_list
        
# step 3: print
print("These numbers could be telemarketers: ")
telemarketers = list(telemarketers)
telemarketers.sort()
for item in telemarketers:
    print(item)
