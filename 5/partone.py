# Author : Adrien Pillou
# Date : 12/22/2020 
# --- Day 5: Binary Boarding ---
# Answer : 801

import math

def calculate_id(r, c):
    return r*8+c

with open('day05.txt') as f:
    x=f.readlines()

x=[l.strip() for l in x]

rows = 128
cols = 8
highest_id = 0

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

    seat_id = calculate_id(r, c)
    if seat_id > highest_id:
        highest_id = seat_id
print(highest_id)
