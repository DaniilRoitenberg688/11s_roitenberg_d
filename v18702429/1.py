from itertools import permutations


g = "ав вд вг бг ге ек"
t = "13 23 34 45 46 67"
t = t + " " + t[::-1]
g = g + " " + g[::-1]

l = "абвгдек"
print(*range(1, len(l) + 1))
for var in permutations(l): 
    c = g
    for i, s in enumerate(var):
        c = c.replace(s, str(i + 1))
    if set(c.split()) == set(t.split()):
        print(*var)
