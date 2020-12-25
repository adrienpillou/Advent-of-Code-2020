# Author : Adrien Pillou
# Date : 12/21/2020

from pprint import pprint

with open ('day21.txt') as f:
    x=f.read()

data = []
ingredients = dict()
allergens = dict()

x=x.replace('\n', '')
x= x.split(')')

# Split products/list of ingredients and allergens
for i in x:
    obj = {}
    if '(' in i:
        values = i.split('(')
        obj['products'] = values[0]
        obj['allergens'] = values[1]
    else:
        obj['products'] = i
        obj['allergens'] = ""
    data.append(obj)

# Casting products and allergens into lists
for i in data:
    if i['allergens']!="":
        values = i['allergens']
        values = values.split(' ')
        values.remove('contains')
        values = [v.strip(' ,')for v in values]
        i['allergens'] = values
    i['products'] = i['products'].split(' ')
    while '' in i['products']:
        i['products'].remove('')

# Gathering all types of allergens
for i in data:
    for a in i['allergens']:
        if not a in allergens.keys():
            allergens[a] = None # Dict of all allergens contained in the products

# Make an inventory of all listed ingredients
for l in data:
    for i in l['products']:
        if not i in ingredients.keys():
            ingredients[i] = list()

# Set possible allergens to each ingredient 
for l in data:
    for i in l['products']:
        for a in l['allergens']:
            ingredients[i].append(a)

# Count all occurences of allergens types list((ingredient, count), ...)
for k  in ingredients:
    structured_allergens = dict()
    for a in ingredients[k]:
        if not a in structured_allergens.keys():
            occ = ingredients[k].count(a) # Counting allergens
            structured_allergens[a] = occ
    ingredients[k] = structured_allergens

# Figure out which ingredient comes up the most when an allergen is mentioned
for a in allergens.keys():
    max = 0
    match = ""
    for i in ingredients.keys():
        if i in list(allergens.values()):
            continue
        if a in ingredients[i].keys():
            if ingredients[i][a] > max :
                max = ingredients[i][a]
                match = i
    allergens[a] = match



count = 0
for d in data:
    for p in d['products']:
        if not p in list(allergens.values()):
            count += 1
pprint(allergens)

dangerous = []
for key, value in sorted(allergens.items()):
    print(f"{value}:{ingredients[value]}")
    dangerous.append(value)

print(','.join(dangerous))

#pprint(allergens)
#for k, v in ingredients.items():
#    print(k," :\n",v)