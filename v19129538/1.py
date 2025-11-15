import itertools

t = "15 18 23 25 34 35 39 47 49 67 68 69 89"

g = "аб аг ад бв бд ве гж дж ди ек еи жи ик"


t = t + " " + t[::-1]
g = g + " " + g[::-1]


l = "абвгдежик"

print(*range(1, len(l) + 1))

for i in itertools.permutations(l):
    k = g
    for n in i:
        k = k.replace(n, str(i.index(n) + 1))
    if set(k.split()) == set(t.split()):
        print(*i)