# Author : Adrien Pillou
# Date : 12/21/2020
#
# Answer : 

from pprint import pprint

def is_valid(id:int):
    for k in fields:
        if not k in passports[id].keys():
            return False
    return True


with open('day04.txt') as f:
    x=f.readlines()
x=[l.strip() for l in x]

fields = ("byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid") # cid is optional
passports = []

obj = dict()
for i, l in enumerate(x):
    if len(passports) == 0 or l == '':
        if not obj is None:
            passports.append(obj)
        obj={}

    for f in fields:
        values = l.split(' ')
        for v in values:
            if f in v:
                obj[f] = v[v.index(":")+1:]
    
    if i == len(x)-1:
        passports.append(obj)

valids = 0

for i in range(len(passports)):
    if is_valid(i):
        valids+=1

#pprint(passports)
print(x[-1])
print(valids, len(passports))


