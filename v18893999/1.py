import itertools


t = "12 14 18 23 36 38 47 56 57 58 68" 

#g = "аб бд дк аг ав бг гд ве ел ге лк"
g = "аб ав аг бг бд ве гд ге дк ел кл"

g = g + " " + g[::-1]
t = t + " " + t[::-1]


l = "абвгдекл"

print(*range(1, len(l) + 1))

for i in itertools.permutations(l):
    k = g
    for j in i:
        k = k.replace(j, str(i.index(j) + 1))
    if set(k.split()) == set(t.split()):
        print(*i)

