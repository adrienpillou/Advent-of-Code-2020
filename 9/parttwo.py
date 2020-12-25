# Author : Adrien Pillou
# Date : 12/24/2020
# Answer : 4023754

x = open('day09.txt').readlines()
x = [int(l.strip()) for l in x]

invalid_number = 27911108
sample_count = 2
while sample_count < len(x):
    for l in range(len(x)-sample_count):
        sample = x[l:l+sample_count]
        if sum(sample) == invalid_number:
            break
    if sum(sample) == invalid_number:
        print(sample)
        print(min(sample)+max(sample))
        break
    sample_count += 1