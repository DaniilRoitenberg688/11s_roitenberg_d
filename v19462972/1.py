import itertools


t = "12 13 14 23 26 54 47 56 57"
g = "ad ae bd bf ce cg df eg fg"

t = t + " " + t[::-1]
g = g + " " + g[::-1]


l = "abcdefg"

print(*range(1, len(l) + 1))

for i in itertools.permutations(l):
    k = g
    for b in i:
        k = k.replace(b, str(i.index(b) + 1))
        
    if set(k.split()) == set(t.split()):
        print(*i)