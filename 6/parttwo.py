# Author : Adrien Pillou
# Date : 12/22/2020
#--- Day 6: Custom Customs ---
# Answer : 3512

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
    else:
        groups[n].append(l)

count = 0

for k,v in groups.items():
    answered = []
    for c in list(v[0]):
        answered.append(c)
        for q in range(1, len(v)):
            if not c in v[q]:
                answered.pop()
                break
    count += len(answered)

print(count)

    
