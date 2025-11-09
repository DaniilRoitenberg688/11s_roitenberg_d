from itertools import product


res = 0
word = "ПАРАБОЛА".lower()
g = "ао"
s = "прбл"
for var in product(g + s, repeat=8):
    for n, i in enumerate(var):
        if var.count(i) == word.count(i):
            if n != 7:
                if i in g and var[n + 1] not in g or i in s and var[n + 1] not in s:
                    res += 1


print(res)
