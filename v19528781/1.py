import itertools

t = "13 14 16 25 27 34 47 56 57"
g = "аб ад бв бд вг ге гж де еж"

t = t + " " + t[::-1]
g = g + " " + g[::-1]

l = "абвгдеж"

print(*range(1, len(l) + 1))

for v in itertools.permutations(l):
    k = g
    for i in v:
        k = k.replace(i, str(v.index(i) + 1))
    if set(k.split()) == set(t.split()):
        print(*v)

