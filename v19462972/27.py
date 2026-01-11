with open("27A.txt") as f:
    d = f.readlines()
    d = list(map(lambda x: (float(x.split()[0]), float(x.split()[1])), d))

clA = [[], []]

for i in d:
    x, y = i
    if y < 10:
        clA[0].append(i)
    else:
        clA[1].append(i)


with open("27B.txt") as f:
    d = f.readlines()
    d = list(map(lambda x: (float(x.split()[0]), float(x.split()[1])), d))

clB = [[], [], []]

for i in d:
    x, y = i
    if x < 4 or y > 30:
        continue
    elif y < 20:
        clB[0].append(i)
    elif x < 19:
        clB[1].append(i)
    else:
        clB[2].append(i)

# from random import random
# from turtle import *

# tracer(0)
# up()

# for cl in clB:
#     color = (random(), random(), random())
#     for i in cl:
#         goto(i[0] * 20, i[1] * 20)
#         dot(3, color)

# update()
# while True:
#     pass


def dist(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5


def center(cl):
    r = []
    for i in cl:
        s = 0
        for j in cl:
            s += dist(i, j)
        r.append([s, i])
    return min(r)


cenA = [center(i)[1] for i in clA]
cenB = [center(i)[1] for i in clB]

print(cenA)
print(min(cenA)[0] * 10000)
print(min(cenA, key=lambda x: x[1])[1] * 10000)


ma = cenB[clB.index(max(clB, key=len))]
mi = cenB[clB.index(min(clB, key=len))]

print(dist(ma, mi) * 10_000)

r = []
for i in range(len(clB)):
    t = max(clB[i], key=lambda x: dist(x, cenB[i]))
    r.append(dist(t, cenB[i]))
    
    
print(max(r) * 10_000)
    