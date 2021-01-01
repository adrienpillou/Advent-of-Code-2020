# Author : Adrien Pillou
# Date : 12/24/2020
# --- Day 10: Adapter Array ---
# Answer : 18512297918464

x=open('day10.txt').read().split('\n')
while '' in x : x.remove('')
x = [int(n) for n in x]

x.sort()
device = max(x)+3

x.append(device)
x.insert(0, 0)


def combinations(adapters, cache = {}, index=0):
    if index in cache.keys():
        return cache[index]

    if index == len(adapters)-1:
        return 1
    
    total = 0
    if (index < len(adapters)-1) and (adapters[index+1]-adapters[index])<=3:
        total += combinations(adapters, cache, index+1)
    
    if (index < len(adapters)-2) and (adapters[index+2]-adapters[index])<=3:
        total += combinations(adapters, cache, index+2)
    
    if (index < len(adapters)-3) and (adapters[index+3]-adapters[index])<=3:
        total += combinations(adapters, cache, index+3)
    
    cache[index] = total
    return total
    
print(combinations(x))
