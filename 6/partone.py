# Author : Adrien Pillou
# Date : 12/22/2020
#--- Day 6: Custom Customs ---
# Answer : 6763

from pprint import pprint

with open('day06.txt') as f:
    x=f.readlines()
x = [l.strip() for l in x]

groups = dict()

n = 0
for i, l in enumerate(x):
    if l == '' or i==0:
        n+=1
        groups[n] = []
    for c in list(l): # Check if a question is already answered by this group
        if not c in groups[n]:
            groups[n].append(c)

sum = 0
for k, v in groups.items():
    sum+=len(v)

print(sum)
    
