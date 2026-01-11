import itertools


t = "15 16 17 23 25 27 34 36 46 57"
g = "аб ав бв бд ве гд ге гк дк ек"


t = t + " " +  t[::-1]
g = g + " " + g[::-1]

l = "абвгдек"
print(*range(1, len(l) + 1))
for v in itertools.permutations(l):
    k = g
    for i in v:
        k = k.replace(i, str(v.index(i) + 1))
    if set(k.split()) == set(t.split()):
        print(*v)
