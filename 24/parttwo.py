# Answer : 4036

x = open('day24.txt').read().split("\n")
while '' in x:x.remove('')

black_tiles = set() # set of flipped tiles (x, y) (white facing up by default)
day = 0

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
            j-=1
        elif m == 'ne':
            i+=1
            j-=1
        elif m == "se":
            j+=1
        elif m == 'sw':
            i-=1
            j+=1
           
    # Check if the hex cell is already flipped
    coords= (i, j)
    if coords in black_tiles:
        black_tiles.discard(coords)
    else :
        black_tiles.add(coords)

print(len(black_tiles))

def get_neighboors(i, j):
    n = 0
    if (i, j-1) in black_tiles:
        n+=1
    if (i+1, j-1) in black_tiles:
        n+=1
    if (i+1, j) in black_tiles:
        n+=1
    if (i, j+1) in black_tiles:
        n+=1
    if (i-1, j+1) in black_tiles:
        n+=1
    if (i-1, j) in black_tiles:
        n+=1
    return n

def cycle():
    global black_tiles
    blank = set()
    r = 256
    for j in range(-r, r+1):
        for i in range(-r, r+1):
            n = get_neighboors(i, j)
            pos = (i, j)
            if pos in black_tiles:
                if (n > 2 or n == 0):
                    pass
                else:
                    blank.add(pos)
            elif n == 2:
                blank.add(pos)
    black_tiles = blank

while(day<100):
    cycle()
    print(f"-- Day {day+1} --") 
    print(len(black_tiles))
    day+=1