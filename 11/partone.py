# Author : Adrien Pillou
# Date : 12/22/2020
# --- Day 11: Seating System ---
# Answer : 2448


import numpy as np
from pprint import pprint
# # : occupied seat
# L : empty seat
# . : floor

def get_neighboors(c, r):
    neighs = 0
    for j in [-1, 0, 1]:
        for i in [-1, 0, 1]:
            x = c+i
            y = r+j
            if j==i==0:
                continue
            if y<0 or y>=room_shape[0]:
                continue
            if x<0 or x>=room_shape[1]:
                continue
            if room[y, x] == '#':
                neighs += 1
    return neighs

def perform_round():
    global room
    blank = np.chararray(room_shape, 1, True)
    blank[:] = '.'
    for j in range(room_shape[0]):
        for i in range(room_shape[1]):
            if room[j, i] == '.':
                blank[j, i] = '.'
                continue
            n = get_neighboors(i, j)
            if room[j, i] == 'L' and n ==0:
                    blank[j, i] = '#'
            elif room[j, i] == '#' and n>=4:
                blank[j, i] = 'L'
            else: blank[j, i] = room[j, i]
    room = blank

with open('day11.txt') as f:
    x=f.readlines()
x=[l.strip() for l in x]

room_shape = (len(x), len(x[0]))
room = np.chararray(room_shape, 1, True)
occupied = []

for j, l in enumerate(x):
    room[j] = list(l)
c = 0

while True:
    perform_round()
    occupied.append(np.count_nonzero(room == '#')) # Count all occupied seats
    if len(occupied) >2:
        if(occupied[-1] == occupied[-2]): # When occupied seat count is stable, break the loop
            break

print(room)
print(f"There is {occupied[-1]} occupied seats in the waiting room at iteration n°{len(occupied)}.")
