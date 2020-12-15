# Author : Adrien Pillou
# Date : 12/15/2020
# --- Day 15: Rambunctious Recitation ---
# Answer = 536

x = [1, 2, 16, 19, 18, 0]
#x = [0, 3, 6]
spokens = []
turn = 1

def get_occurencies(v:int):
    global spokens
    occurencies = []
    for i in range(len(spokens)):
        if spokens[i] == v:
            occurencies.append(i)
    return occurencies

def get_spoken_number(num_turn:int):
    global turn, spokens, x
    while turn <= num_turn:
        # Starting numbers from input x
        if(turn<=len(x)):
            num = x[turn-1]
        # Taking le last spoken number
        else: 
            num = spokens[-1]
            # Nums are now how many turns apart
            occurencies = get_occurencies(num)
            if len(occurencies) == 1:
                num = 0
            elif len(occurencies) >= 2:
                num = occurencies[-1]-occurencies[-2]
            
        # Spoke this turn number
        spokens.append(num)
        turn += 1
    return spokens[-1]


ans  = get_spoken_number(30000000)
print(f"Answer : {ans}")
print(f"Spoken length : {len(spokens)}")