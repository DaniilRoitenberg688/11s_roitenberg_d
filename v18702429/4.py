from itertools import product


l = "00 1001 1010 110 0101 011 111 0100 1000"
l = l.split()
for i in range(2, 5):
    for v in product("01", repeat=i):
        r = [j[:i] != ''.join(v) for j in l]
        if all(r):
            print(v)
