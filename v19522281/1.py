import itertools

t = "16 19 23 25 27 34 39 46 47 58 68 69 78"
g = "аб аг аи ав бв вк ге гд дж еи еж жк ик"

g = g + " " + g[::-1]
t = t + " " + t[::-1]

l = "абвгдежик"
print(*range(1, len(l) + 1))

for i in itertools.permutations(l):
    k = g
    for j in i:
        k = k.replace(j, str(i.index(j) + 1))
    if set(k.split()) == set(t.split()):
        print(*i)
