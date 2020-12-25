# Author : Adrien Pillou
# Date : 12/24/2020
# Answer : 27911108

x = open('day09.txt').readlines()
x = [int(l.strip()) for l in x]

sample_count = 25

for l in range(sample_count, len(x)):
    sample = x[l-sample_count:l]
    sample.reverse()
    valid = False
    for s in range(1, len(sample)):
        if x[l]-sample[s] in sample:
            valid = True
    if not valid:
        invalid_number = x[l]
        break
print(x[l])




