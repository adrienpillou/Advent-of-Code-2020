# Author : Adrien Pillou
# Date : 12/23/2020
# --- Day 23: Crab Cups ---
# Answer : 98742365

from collections import deque

def display_move(n):
    print(f"\n--- Move {n} ---")

def display_cups():
    global cups, cur_cup
    msg = ""
    for c in cups:
        if c == cur_cup:
            msg+=f"({c}) "
        else:
            msg+=f"{c} "
    print(f"cups: {msg}")

def display_pickup(picked, dest):
    print(f"pick up: {picked}")
    print(f"destination: {dest}")

x = "792845136"
cups = [int(l) for l in list(x)]
index = 0
cur_cup = cups[0]
m=1

for moves in range(100):
    

    display_move(m)
    display_cups()

    pick = cups[1:4]
    cur_cup = cups[0]
    dest = cur_cup-1

    if dest == 0:
        dest = 9
    while dest in pick or not dest in cups:
        dest-=1
        if dest < 1:
            dest = 9
            
    without_pick = cups[:1] + cups[4:]
    dest_index = without_pick.index(dest)
    without_pick = without_pick[:dest_index+1] + pick + without_pick[dest_index+1:]
    cups = without_pick[1:] + without_pick[:1]
    m+=1

print("\nAnswer : ",''.join(str(c) for c in cups[cups.index(1)+1:] + cups[:cups.index(1)]))