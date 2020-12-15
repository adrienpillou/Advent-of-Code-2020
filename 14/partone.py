# Author : Adrien Pillou
# Date : 12/14/2020
# --- Day 14: Docking Data ---
# Answer = 8471403462063

# Docking command class
class Command():
    def __init__(self, id, mask="", instructions=[]):
        self.id = id
        self.mask = mask # binary string/list
        self.instructions = instructions # (index, value) list of tuple

    def __repr__(self):
        c = f"id : {self.id} ; "
        c += f"mask : {self.mask}"
        return c

if __name__ == "__main__":
    memory = [0 for i in range(2**16)]
    commands = []

    # Parsing the input file
    with open("in.txt", 'r') as f:
        content = f.readlines()
    content = [x.strip() for x in content]
    
    id = 0
    command = None
    for l in content:
        if l.startswith("mask"): # If this line starts with 'mask'
            command = Command(id)
            command.instructions = []
            id+=1
            mask = l.split(' = ')
            command.mask = mask[-1]
            commands.append(command)
        elif l.startswith("mem"): # Else if this line starts with 'mem'
            instruction = l.split(' = ')
            index = l[l.find("[")+1:l.find("]")]
            value = instruction[-1]
            command.instructions.append((int(index), int(value)))

    # Decoding the docking procedure
    print('*** DOCKING PROCEDURE ***')
    print(f'Total commands : {len(commands)}\n')
    
    for n in range(len(commands)): # Loopin through docking commands
        c = commands[n]
        for i in c.instructions: # Writing each instruction value in the memory
            cursor = i[0] # Memory buffer location 
            dec_value = i[1] # Gathering the value to write
            bin_value_str = bin(dec_value)[2:].zfill(36) # Converting it to binary
            bin_value_list = list(bin_value_str) # Converting this 4 bytes word to a list
            for i in range(0, len(c.mask)):
                if c.mask[i] != 'X':
                    bin_value_list[i] = c.mask[i] # Applying the mask
            bin_value_str = "".join(bin_value_list) # Converting back the binary list to a string
            dec_value = int(bin_value_str, 2) # Converting this string to an int
            memory[cursor] = dec_value # Storing this value in the memory where the cursor is

    answer = 0
    for i in range(len(memory)): # Sum up the entire memory
        answer += memory[i]
    print(f"Answer = {answer}")
