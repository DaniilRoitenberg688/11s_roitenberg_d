from itertools import permutations

table = "69 357 249 367 28 1489 248 567 136".split()
connections = "ав аб аг бв вк гд ге дж еи еж жк ик".split()

print(*range(1, 10))
for line in permutations("абвгдежик"):
    c = [str(line.index(b) + 1) in  table[line.index(a)] for a, b in connections]
    if all(c):
        print(*line)
