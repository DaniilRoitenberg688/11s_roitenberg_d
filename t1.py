from itertools import permutations

table = "69 357 249 367 28 1489 248 567 136".split()
connections = "ав аб аг бв вк гд ге дж еи еж жк ик".split()

print(*range(1, 10))
for line in permutations("абвгдежик"):
    c = [str(line.index(b) + 1) in  table[line.index(a)] for a, b in connections]
    if all(c):
        print(*line)

print()
table = "16 19 23 25 27 34 39 46 47 58 68 69 78"
connections = "ав аб аг бв вк гд ге дж еи еж жк ик"
print(len(table.split()))
print(len(connections.split()))
for line in permutations("абвгдежик"):
    e = connections
    for i, s in enumerate(line):
        e = e.replace(s, str(i + 1))
    print(e)
    if set(e.split()) == set(table.split()):
        print(line)
        print('exit because done')
        break
