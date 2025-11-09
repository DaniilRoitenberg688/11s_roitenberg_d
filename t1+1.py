from itertools import permutations


c = "12 14 24 26 35 36 46 47 56 76"
g = "аб ав бв вд де вг ег ек гк ве"

c = c + " " + c[::-1]
g = g + " " + g[::-1]

l = "абвгдек"

print(*range(1, len(l) + 1))
for var in permutations(l):
    n = g
    for i, s in enumerate(var):
        n = n.replace(s, str(i + 1))
    if set(n.split()) == set(c.split()):
        print(*var)
