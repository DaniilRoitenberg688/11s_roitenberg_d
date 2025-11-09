from itertools import product
r = 0
l = "алгоритм"
l = sorted(l)
for n, i in enumerate(product(l, repeat=5)):
    if (n + 1) % 2 != 1:
        continue
    if i[0] == "г":
        continue
    if i.count("и") < 2:
        continue
    r += 1
print(r)
