from itertools import permutations


t = "12 14 24 26 35 36 37 46 47 56 67"
g = "аб вб бд де вд ве вг ав ге ек гк"

t = t + " " + t[::-1]
g = g + " " + g[::-1]

l = "абвгдек"
print(*range(len(l)))
for v in permutations(l):
    s = g
    for i in v:
        s = s.replace(i, str(v.index(i) + 1))
    if set(s.split()) == set(t.split()):
        print(*v)
