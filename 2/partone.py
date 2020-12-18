# Author : Adrien Pillou
# Date : 12/18/2020
#--- Day 2: Password Philosophy ---
# Answer = 519

import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

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
    occ = t['pwd'].count(t['letter'])
    if t['policy'][0] <= occ <= t['policy'][1]:
        valid_pwds +=1

print(valid_pwds)
