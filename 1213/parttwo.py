# Advent of Code 2020
# Author : Adrien Pillou
# Date : 12/13/2020

# ---Day 13: Shuttle Search--- : https://adventofcode.com/2020/day/13#part2
# Part two : What is the earliest timestamp such that all of the listed bus IDs depart at offsets matching their positions in the list ?
# Answer : 100023729388239 / FAILED

# To see : Chinese remainder theorem

import math
import numpy as np
import time

# Printing formatted bus schedule
def show_schedule(array, header_list):
    print("\t".join(header_list))
    row = ""
    for j, rows in enumerate(array):
        for i, cols in enumerate(array[j]):
            row += array[j,i] + '\t'
        print(row)
        row = ""
    pass

if __name__ == "__main__":
    buses = [17, 37, 439, 29, 13, 23, 787, 41, 19] # buses ids
    stamp = 3417 # current timestamp value
    interval = (stamp, stamp+20) # Time interval
    schedule = np.chararray((21, len(buses)+1), 9, unicode = True) # Schedule char array
    answer = None

    header = ["time"] # Schedule header
    for bus in buses:
        header.append(f"bus {bus}")

    # Finding the earliest occurence
    stamp = 0
    dt = 0
    offset = 0

    while answer is None:
       stamp+=buses[0]
       dt = 0
       offset = 0
       for b in range(1, len(buses)):
           while (stamp + offset + dt)%buses[b]!=0 or dt>3:
               dt+=1
           if (dt>3):
               break
           offset+=dt
           dt = 1
           if buses[b] == buses[-1]:
               answer = stamp
       if stamp > 500000000000000:
           answer = 0

    # Creating the schedule at specified time stamp
    stamp = answer
    interval = (stamp, stamp+20) # Updating time interval
    for i,b in enumerate(buses): # Looping through all buses
        for t in range(interval[0], interval[1]+1): # Iterating through time interval
            schedule[t-interval[0], 0] = str(t)
            if t%b == 0: # Using modulus to know buses departure
                schedule[t-interval[0], i+1] = 'D'
            elif t==stamp:
                schedule[t-interval[0], i+1] = '░'# The bus is on it's way
            else:
                schedule[t-interval[0], i+1] = '.'# The bus is on it's way

    print("*** AIRPORT SHUTTLE SERVICE ***")
    show_schedule(schedule, header)
    print (f"Answer : {answer}")



