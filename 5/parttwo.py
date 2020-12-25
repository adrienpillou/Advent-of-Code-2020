# Date : 12/22/2020 
# --- Day 5: Binary Boarding ---
# Answer : 597

import numpy as np

def calculate_id(r, c):
    return r*8+c

with open('day05.txt') as f:
    x=f.readlines()

x=[l.strip() for l in x]

seats = dict() # Seats info

for l in x:
    row_range = [0, 127]
    col_range = [0, 7]
    r=0
    c=0
    for i, char in enumerate(list(l)):
        if i<6:
            if char == 'B': # Take upper half
                mid = round((row_range[1]-row_range[0])/2)
                row_range[0] += mid
            elif char == 'F': # Take lower half
                mid = round((row_range[1]-row_range[0])/2)
                row_range[1] -= mid
        else:
            if char == 'R': # Take upper part
                mid = round((col_range[1]-col_range[0])/2)
                col_range[0] += mid
            elif char == 'L': # Take lower part
                mid = round((col_range[1]-col_range[0])/2)
                col_range[1] -= mid

    if list(l)[6] == 'F':
        r = min(row_range)
    else:
        r = max(row_range)

    if list(l)[-1] == 'L':
        c = min(col_range)
    else:
        c = max(col_range)

    seats[calculate_id(r, c)] = l

plan = [0]*1024

for i in range(len(plan)): # Place a 1 in all occupied seats
    if i in seats.keys():
        plan[i] = 1

empty_seats = [i for i, x in enumerate(plan) if x == 0] # Identify empty seats by their ids

prev = empty_seats[0] # Calculate the delta to find our seat
for e in empty_seats:
    d = e-prev
    prev = e
    if d>1:
        print (e)
        break
