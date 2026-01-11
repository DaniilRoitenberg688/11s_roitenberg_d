with open("27_A.txt") as f:
    a = f.readlines()

clA = [[], []]

for p in a:
    x, y = list(map(float, p.strip().split()))
    if x > 5:
        clA[0].append((x, y))
    else:
        clA[1].append((x, y))


with open("27_B.txt") as f:
    b = f.readlines()

clB = [[], [], []]

for p in b:
    x, y = list(map(float, p.strip().split()))
    if x < 0 or y > 32:
        continue
    if y < 12:
        clB[0].append((x, y))
    elif y < 21:
        clB[1].append((x, y))
    else:
        clB[2].append((x, y))


from random import random
from turtle import *

tracer(0)
up()
for cl in clB:
    color = (random(), random(), random())
    for x, y in cl:
        goto(x * 20, y * 20)
        dot(3, color)


update()


def dist(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5


def center(cl):
    m = []
    for p in cl:
        s = 0
        for x in cl:
            s += dist(p, x)
        m.append([s, p])
    return min(m)


cenA = [center(i)[1] for i in clA]
x = max(cenA)
y = max(cenA, key=lambda z: z[1])
print(x[0], y[1])

cenB = [center(i)[1] for i in clB]
ma, mi = max(clB, key=len), min(clB, key=len)
mx, my = cenB[clB.index(ma)]
mix, miy = cenB[clB.index(mi)]
print(mx - mix, my - miy)
