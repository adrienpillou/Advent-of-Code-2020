# Advent of Code 2020
# Author : Adrien Pillou
# Date : 12/13/2020

# ---Day 13: Shuttle Search--- : https://adventofcode.com/2020/day/13

import math
import numpy as np

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
    could_depart = 1000067 # Earliest timestamp you could depart on a bus
    stamp = (could_depart-10, could_depart+10) # Time interval
    wait = math.inf # Waiting time
    goto_bus = None # The bus you need to take to go to the airport
    schedule = np.chararray((21, len(buses)+1), 9, unicode = True) # Schedule char array
    header = ["time"] # Schedule header

    for i,b in enumerate(buses): # Looping through all buses
        header.append(f"bus {b}")
        for t in range(stamp[0], stamp[1]+1): # Iterating through time interval
            schedule[t-stamp[0], 0] = str(t)
            if t%b == 0: # Using modulus to know buses departure
                schedule[t-stamp[0], i+1] = 'D'
                if(could_depart<=t):
                    if(wait>=t-could_depart): # Minimizing the waiting time
                        goto_bus = b # Selecting a bus 
                        wait = t-could_depart
            else:
                schedule[t-stamp[0], i+1] = '.'# The bus is on his way
                        
    print("*** AIRPORT SHUTTLE SERVICE ***")
    show_schedule(schedule, header)
    if wait == 0:
        print(f"\nBus {goto_bus} is on departure !")
    else:
        print(f"\nYou should take bus {goto_bus}.\nEstimated waiting time of {wait} minutes.")
    print(f"Answer : {wait*goto_bus}")# Answering statement question
