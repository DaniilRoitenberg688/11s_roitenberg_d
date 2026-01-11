import itertools


l = sorted("парус")

n = 0
for i in itertools.product(l, repeat=4):
    n += 1
    if 'а' not in i:
        print(i)
        print(n)
        break
        
