# Author : Adrien Pillou
# Date : 12/18/2020
#--- Day 2: Password Philosophy ---
# Answer = 708

import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

def is_valid(pwd:str, letter:str, pos:tuple):
    if not letter in pwd:
        return False
    occ_index = [i for i, x in enumerate(list(pwd)) if x == letter]
    if pos[0]-1 in occ_index != pos[1]-1 in occ_index:
        return False
    if pos[0]-1 in occ_index:
        return True
    elif pos[1]-1 in occ_index:
        return True
    return False

with open('day02.txt') as f:
    x=f.readlines()

x = [l.strip() for l in x]

tuples = []
valid_pwds = 0

for l in x:
    obj = dict()
    obj['pwd'] = l.split(':')[1].replace(' ', '')
    complete_policy = l.split(':')[0]
    letter = complete_policy.split(' ')[1]
    policy = complete_policy.split(' ')[0]
    policy = (int(policy.split('-')[0]), int(policy.split('-')[1]))
    obj['policy'] = policy
    obj['letter'] = letter
    tuples.append(obj)

for t in tuples:
    if is_valid(t['pwd'], t['letter'], t['policy']):
        valid_pwds +=1

print(valid_pwds)
