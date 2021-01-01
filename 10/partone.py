# Author : Adrien Pillou
# Date : 12/24/2020
# --- Day 10: Adapter Array ---
# Answer : 2176

x=open('day10.txt').read().split('\n')
while '' in x : x.remove('')
x = [int(n) for n in x]

x.sort()
device = max(x)+3

diff = []

diff.append(x[0])
for i in range(len(x)):
    if(i<len(x)-1):
        diff.append(abs(x[i]-x[i+1]))
diff.append(device-x[-1])



print(diff, x)
print(diff.count(1)* diff.count(3))
