from itertools import product


l = "алгоритм"
l = sorted(l)

for n, i in enumerate(product(l, repeat=4)):
    if i[0] == "и" and i[1] == "г":
        print(n + 1)
        break
