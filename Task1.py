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
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""

# use set structure to store all unique telephone numbers
numbers = {x[0] for x in calls}
numbers |= {x[1] for x in calls}
numbers |= {x[0] for x in texts}
numbers |= {x[1] for x in texts}
# output the length of the set
print(f"There are {len(numbers)} different telephone numbers in the records.")
