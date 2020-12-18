# Author : Adrien Pillou
# Date : 12/18/2020
#--- Day 18: Operation Order ---
# Answer : FAILURE

import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

def get_operators(operation:list): # Get * & + operators from a list
    operators = []
    for n, c in enumerate(operation):
        if c=="+" or c=='*':
            operators.append((int(n), c)) # Index , Char
    return operators

def calculate(line:list): # Estimate a portion of a line
    if '(' in line : line.remove('(')
    if ')' in line : line.remove(')')

    operators = get_operators(line)
    
    while len(operators) > 0:
        print(line)
        if '+' in operators: # While there is a + in the formula
            for o in operators:
                if o[1] == '+':
                    index = o[0]
                    a = int(line[index-1])
                    o = line[index]
                    b = int(line[index+1])

                    del line[index-1:index+1]# Deleting used elements to replace them all

                    line.insert(index-1, str(a+b))
                    operators = get_operators(line)      
        else: # Next procede to * operators
            index = line.index(operators[0][1])
            a = int(line[index-1])
            o = line[index]
            b = int(line[index+1])

            for i in range(3): # Deleting used elements to replace them all
                line.pop(0)

            line.insert(0, str(a*b))
            operators = get_operators(line)
        
        # Refreshing operators
        

    return line[0]


with open('day18.txt') as file:
    x = file.readlines()

x = [l.strip() for l in x]
print(len(x), ' operations to perform')
sum = 0

#for i, l in enumerate(x):
i=0
l = "1 + 2 * 3 + 4 * 5 + 6" # Input a line here
l = l.replace(' ', '')
l = list(l)

while '+' in l or '*' in l:
    start = 0
    end = 0
    for (c, char) in enumerate(l):
        if char == '(':
            start = c
        if char == ')':
            end = c+1
            break
    if start == end == 0:
        l = calculate(l) # Line result here
        #print(f"{x[i]} = {l}")
        sum += int(l) # Sum up
    else :
        res = calculate(l[start:end])
        del l[start:end]
        l.insert(start, res)

print(f"Answer : {l}")