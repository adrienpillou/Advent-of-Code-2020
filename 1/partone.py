# Author : Adrien Pillou
# Date : 12/18/2020
#--- Day 1: Report Repair ---
# Answer = 935419

with open('day01.txt') as f:
    x = f.readlines()

x = [int(i.strip()) for i in x]

entries = []

for n in x:
    d = 2020 - n
    if d in x:
        c = x[x.index(d)]
        entries.append(c)
    else : continue

print(entries[0]*entries[1])
