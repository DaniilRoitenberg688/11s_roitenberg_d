from itertools import permutations


g = "ab bd ag bc cd ce cg cf de ef fg"
t = "13 14 16 26 27 34 35 45 46 47 67"

g = g + " " + g[::-1]
t = t + " " + t[::-1]

l = "abcdefg"
print(*range(1, len(l) + 1))
for i in permutations(l):
    k = g
    for j in i:
        k = k.replace(j, str(i.index(j) + 1))
    if set(k.split()) == set(t.split()):
        print(*i)

