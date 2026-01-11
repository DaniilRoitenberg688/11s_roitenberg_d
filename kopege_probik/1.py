import itertools


t = "12 14 24 26 35 36 46 47 56 67"
g = "аб ав бв вд ве вг ге гк де ек"

t = t + " " + t[::-1]
g = g + " " + g[::-1]


l = "абвгдек"

print(*range(1, len(l) + 1))

for v in itertools.permutations(l):
    k = g
    for i in v:
        k = k.replace(i, str(v.index(i) + 1))
    if set(k.split()) == set(t.split()):
        print(*v)