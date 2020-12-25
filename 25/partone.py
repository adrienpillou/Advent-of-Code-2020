# Author : Adrien Pillou
# Date : 12/25/2020
# Answer : 6421487

keys = [12320657, 9659666]
#keys = [5764801, 17807724]
loop_sizes = []
modulus = 20201227

for k in keys:
    value = 1
    for i in range(2**32):
        value *= 7
        value = value % modulus
        if value == k :
            print(value, i+1)
            loop_sizes.append(i+1)
            break


# [6527904, 75188]
for i, k in enumerate(keys):
    if i == 0:
        l = 1
    else:
        l = 0
    value = 1
    for i in range(loop_sizes[l]):
        value *= k
        value = value % modulus
    print(value)





            