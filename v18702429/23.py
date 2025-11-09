from itertools import product

r = 0
for i in range(4, 13):
    for v in product("12", repeat=i):
        if 10 + 1 * v.count("1") + 10 * v.count("2") == 32:
            r += 1

print(r)
