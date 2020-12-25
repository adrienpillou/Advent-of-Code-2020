# Answer : 394

x = open('day24.txt').read().split("\n")
while '' in x:x.remove('')

directions = ('e', 'w', 'ne', 'se', 'nw', 'sw')

black_tiles = set() # set of flipped tiles (x, y) (white facing up by default)
count = 0

i = 0
j = 0

#t = "ewnwnwsenwnwnwwnweswnwnenwnwesenwwnww"
for t in x:
    moves = [] # Spliting all the moves contained in the string
    n=0
    while n < len(t):
        chars = list(t)
        c = chars[n]
        if c == 'n' or c == 's':
            c+=chars[n+1]
        moves.append(c)
        n+=len(c)

    i = 0
    j = 0
    for m in moves: # Applying all the moves from reference cell (0, 0)
        if m =='e':
            i+=1
        elif m == 'w':
            i-=1
        elif m == 'nw':
            i-=1
            j+=1
        elif m == 'ne':
            j+=1
        elif m == "se":
            i+=1
            j-=1
        elif m == 'sw':
            j-=1
           
    # Check if the hex cell is already flipped
    coords= (i, j)
    if coords in black_tiles:
        black_tiles.discard(coords)
    else :
        black_tiles.add(coords)
    print(coords)

print(black_tiles)
print(len(black_tiles))