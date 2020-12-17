# From Robert Xiao
# https://www.youtube.com/watch?v=89SqNQKPVRI&t=367s

import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Reading input
with open('in.txt', 'r') as f:
    x = f.readlines()
x = [l.strip('\n')for l in x]

grid = [list(row) for row in x]
w = len(grid[0])
h = len(grid)

print(w, h)

cubes = set()
for y in range(h):
    for x in range(w):
        if grid[y][x] == '#':
            cubes.add((x, y, 0))

def neighboors(x, y, z):
    for dx in (-1, 0, 1):
        for dy in(-1, 0, 1):
            for dz in (-1, 0, 1):
                if dx == dy == dz == 0: continue
                yield(x+dx, y+dy, z+dz)

def countn(x, y, z):
    c = 0
    for p in neighboors(x, y, z):
        c += p in cubes
    return c

def step():
    ncubes = set()
    for p in cubes:
        for n in neighboors(*p):
            if n not in cubes and countn(*n) == 3:
                ncubes.add(n)
        if countn(*p) in (2, 3):
            ncubes.add(p)
    return ncubes
            
for iter in range(6):
    cubes = step()

print(len(cubes))