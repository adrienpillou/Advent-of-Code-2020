# Author : Adrien Pillou
# Date : 12/18/2020
#--- Day 1: Report Repair ---
# Answer = ?

import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

with open('day01.txt') as f:
    x = f.readlines()

x = [int(i.strip()) for i in x]
x.sort()
entries = []

for n in x:
    for a in range(len(x)):
        for b in range(a+1, len(x)):
            for c in range(b+1, len(x)):
                print(x[a], x[b], x[c])
                if a!=b!=c:
                    if x[a] + x[b] + x[c] == 2020:
                        entries = (x[a], x[b], x[c])
if len(entries) > 0: 
    print(entries[0]*entries[1]*entries[2])