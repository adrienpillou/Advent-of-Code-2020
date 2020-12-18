# Author : Adrien Pillou
# Date : 12/18/2020
#--- Day 3: Toboggan Trajectory ---
# Answer = 3521829480

import os
import numpy as np

os.chdir(os.path.dirname(os.path.abspath(__file__)))

with open('day03.txt') as f:
    x=f.readlines()

x = [l.strip() for l in x]
shape = (len(x), len(x[0]))


trees = 0
forest = np.chararray(shape, 1, True)

for r in range(shape[0]):
    row = list(x[r])
    for c in range(shape[1]):
        forest[r, c] = row[c]

pos = [0, 0]
slope = (3, 1)
total_trees = 1
for slope in [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]:
    while pos[1] < shape[0]:
        pos = [pos[0]+slope[0], pos[1]+slope[1]]
        if pos[0]>=shape[1]:
            pos[0] = pos[0] - shape[1]
        if pos[1]>=shape[0]:
            break
        if forest[pos[1], pos[0]] == '#':
            trees += 1
    total_trees*=trees
    trees = 0
    pos =[0, 0]
    

print(total_trees)