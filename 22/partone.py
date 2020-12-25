# Author : Adrien Pillou
# Date : 12/22/2020
# --- Day 22: Crab Combat ---
# Answer : 32856

def count_score(p:list):
    score = 0
    for i in range(len(p)):
        score += (len(p)-i) * p[i]
    return score

def play_round():
    if len(p1) == 0 or len(p2)==0:
        return
    c1 = p1[0]
    c2 = p2[0]
    if c1>c2:
        p1.pop(0)
        p2.pop(0)
        p1.append(c1)
        p1.append(c2)
    elif c2>c1:
        p1.pop(0)
        p2.pop(0)
        p2.append(c2)
        p2.append(c1)


with open('day22.txt', 'r') as f:
    x=f.readlines()
x=[l.strip() for l in x]

p1 = x[1:x.index('')]
p2 = x[x.index('')+2:]

p1 = [int(x) for x in p1]
p2 = [int(x) for x in p2]

print(f"Total cards:{len(p1)+len(p2)}")
r = 0
while True:
    play_round()
    r+=1
    print(f"\n-- Round {r}: --")
    print(f"Player 1:{p1}")
    print(f"Player 2:{p2}")
    if r > 2**12:
        break
    if len(p1)==0 or len(p2)==0:
        break

if len(p1) == 0:
    print(count_score(p2))
else : 
    print(count_score(p1))
