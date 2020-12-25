# Author : Adrien Pillou
# Date : 12/23/2020
# --- Day 8: Handheld Halting ---
# Answer : 1727

from pprint import pprint

with open('day08.txt') as f:
    x=f.readlines()

x=[l.strip() for l in x]

instructions = list()
accumulator = 0
cursor = 0

class operation():
    def __init__(self, command, argument, index):
        self.command = command
        self.argument = argument
        self.index = index
        self.called = 0
    
    def execute(self):
        global accumulator
        global cursor
        if self.command == 'acc':
            accumulator += self.argument
            cursor += 1
        elif self.command == 'jmp':
            cursor += self.argument
        elif self.command == 'nop':
            cursor+=1 # Goes directly to the next operation
        self.called += 1
    
    def __repr__(self):
        return f"Command n°{self.index}: {self.command} [{self.argument}]"

for i, l in enumerate(x):
    ope = operation(l.split(' ')[0], int(l.split(' ')[1]), i)
    instructions.append(ope)

for i in range(2048):
    operation  = instructions[cursor]
    print( operation)
    operation.execute()
    if operation.called > 1:
        break

print(accumulator)
