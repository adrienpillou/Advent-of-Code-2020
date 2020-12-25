# Author : Adrien Pillou
# Date : 12/21/2020
#
# Answer : 

from pprint import pprint

def is_valid(id:int):
    for k in fields:
        
        if not k in passports[id].keys():
            return False
        else:
            value = passports[id][k]
            if k == "byr" or k == "iyr" or k == "eyr":

                if not value.isdecimal() or len(value)!=4:
                    return False

                year = int(value)
                if k == "byr":
                    if year < 1920 or year > 2002:
                        return False

                elif k == "iyr":
                    if year < 2010 or year > 2020:
                        return False

                elif k == "eyr":
                    if year < 2020 or year > 2030:
                        return False

            if k == "hgt":
                if not (value.endswith("cm") or value.endswith("in")):
                    return False
                else:
                    if "cm" in value:
                        height = int(value.rstrip('cm'))
                        if height < 150 or height > 193:
                            return False
                    else: 
                        height = int(value.rstrip('in'))
                        if height < 59 or height > 76:
                            return False
                    
            if k == "hcl":
                if not value.startswith('#') and len(value)!=7:
                    return False
                else:
                    value = value.upper()
                    chars = list("0123456789ABCDEF")
                    for c in list(value[1:]):
                        if not c in chars:
                            return False

            if k == "ecl":
                if not value in ("amb", "blu", "brn", "gry", "grn", "hzl", "oth"):
                    return False

            if k == "pid":
                if len(value) != 9 or not value.isnumeric():
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

print(valids)