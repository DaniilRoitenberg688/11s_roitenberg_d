import itertools

t = "12 14 24 26 35 36 37 46 47 56 67"
g = "аб ав бв бд вд ве вг ге гк де ек"

t = t + " " + t[::-1]
g = g + " " + g[::-1]

l = "абвгдек"

print(*range(1, len(l) + 1))


for i in itertools.permutations(l):
    k = g
    for j in i:
        k = k.replace(j, str(i.index(j) + 1))

    if set(k.split()) == set(t.split()):
        print(*i)