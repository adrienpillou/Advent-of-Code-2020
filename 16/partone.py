# Author : Adrien Pillou
# Date : 12/16/2020
#--- Day 16: Ticket Translation ---
# Answer : 21978

'''
.--------------------------------------------------------.
| ????: 101    ?????: 102   ??????????: 103     ???: 104 |
|                                                        |
| ??: 301  ??: 302             ???????: 303      ??????? |
| ??: 401  ??: 402           ???? ????: 403    ????????? |
'--------------------------------------------------------'
'''

import os
import math
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Check if a value is within at least one range
def is_valid(value:int):
    global ranges
    for r in ranges:
        if value >= r[0] and value <= r[1]:
            return True
    return False

ranges = []
my_ticket = tuple()
tickets = []
error_rate = 0

if __name__ == "__main__":
    with open('in.txt') as f:
        x = f.readlines()
    x = [l.strip() for l in x]

    # Gathering fields and ranges
    fields = x[0:20]
    for f in fields:
        f = f.split(':')
        values = f[1]
        values = values.split('or')
        ranges.append(values[0])
        ranges.append(values[1])

    for i in range(len(ranges)):
        ranges[i] = ranges[i].split('-')
        ranges[i] = (int(ranges[i][0]), int(ranges[i][1]))

    # Gathering my ticket
    my_ticket = x[22].split(',')
    for i in range(len(my_ticket)):
        my_ticket[i] = int(my_ticket[i])

    # Gathering all tickets
    tickets = x[25:]
    for i, t in enumerate(tickets):
        tickets[i] = tickets[i].split(',')
        for v in range(len(tickets[i])):
            tickets[i][v] = int(tickets[i][v])
        tickets[i] = tuple(tickets[i])

    # Sum up error rate
    for t in tickets:
        for v in t:
            if not is_valid(v):
                error_rate += v
    print(error_rate)

    