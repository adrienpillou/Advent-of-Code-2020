# Author : Adrien Pillou
# Date : 12/17/2020
#--- Day 17: Conway Cubes ---
# Answer : ?

# Rules :
# - active and 2 or 3 active around => remains active, else inactive
# - inactive and 3 active aroun => becomes active
 
import math
import numpy as np
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

cycles = 3
pocket = dict()

# Display the entire pocket (7 layers from z = -6 to z = 6)
def display_pocket():
    for k in range(-cycles+1, cycles):
        print(f"z = {k}")
        print(pocket[k])

# Count active cubes in the pocket
def count_active():
    count = 0
    for k in range(-cycles+1, cycles):
        #indices = [i for i, row in enumerate(pocket[k][i]) if x == "whatever"]
        for row in pocket[k]:
            indices = [i for i, x in enumerate(row) if x == "#"]
            count+=len(indices)
    return count

# 3D space
def create_space():
    space = {}
    for c in range(-cycles+1, cycles):
        space[c] = create_layer()
    return space

# 2D layer
def create_layer():
    layer = np.chararray(shape, 1, True) # Layer 0
    layer[:] = '.'
    return layer

def get_neighboors(_x, _y, _z):
    neighboors = 0
    for l in pocket.keys(): # Layers
        for j in [-1, 0, 1]: # Rows
            for i in [-1, 0, 1]: # Columns
                z = _z+l
                y = _y+j
                x = _x+i
                if l==0 and j==0 and i==0: # Avoid self checking
                    continue
                if z not in list(pocket.keys()):
                    continue
                if y < 0 or y>=shape[0]:
                    continue
                if x < 0 or x>=shape[1]:
                    continue
                if pocket[z][y, x] == '#':
                    neighboors += 1
    return neighboors

# Check if a cube is active
def is_active(x, y, z):
    if pocket[z][y, x] == '#':
        return True
    else:
        return False

# Apply rules over one cycle
def perform_cycle(cycle):
    global pocket
    blank_space = create_space()# Empty 3d space to write in
    for z in pocket.keys():# Looping through z pocket layers
        for j in range(shape[0]):
            for i in range(shape[1]):
                active = is_active(i, j, z)
                n = get_neighboors(i, j, z)
                if active:
                    if n in (2,3):
                        blank_space[z][j, i] = '#'
                    else:
                        blank_space[z][j, i] = '.'
                elif not active:
                    if n==3:
                        blank_space[z][j, i] = '#'
                    else:
                        blank_space[z][j, i] = '.'
    pocket = blank_space
    return pocket

if __name__ == "__main__":
    # Reading input
    with open('in.txt', 'r') as f:
        x = f.readlines()
    x = [l.strip()for l in x]
    shape = (len(x), len(x[0])) # (h, w)

    # Creating the initial pocket space
    pocket = create_space()

    # Inserting input matrix in layer 0
    for j in range(shape[0]):
        lt = list(x[j])
        for i, c in enumerate(lt):
            pocket[0][j, i] = c

    print(f"Initial pocket")
    display_pocket()
    for c in range(1, cycles+1):
        print(f"\nCycle n°{c}")
        perform_cycle(c)
        display_pocket()

    print(f"Answer : {count_active()}")