# Author : Adrien Pillou
# Date : 12/15/2020
# --- Day 15: Rambunctious Recitation ---
# Answer = 24065124

import numpy as np

spokens = [1, 2, 16, 19, 18, 0]
last_index = {}

for i, n in enumerate(spokens):
    if i != len(spokens)-1:
        last_index[n] = i

while len(spokens) < 30000000:
    last_spoken = spokens[-1]
    previous_occurence = last_index.get(last_spoken, -1)
    last_index[last_spoken] = len(spokens)-1
    if previous_occurence == -1:
        to_spoke = 0
    else:
        to_spoke = len(spokens)-1-previous_occurence
    spokens.append(to_spoke)

print(f"Answer : {spokens[-1]}")

