import itertools
from ast import Continue


def f(x, y, w, z):
    return (x == (not (w == y))) and (w == (y <= z))


for a1, a2, a3, a4, a5, a6, a7 in itertools.product((0, 1), repeat=7):
    t = [(0, 0, a1, a2), (a3, 0, a4, 0), (0, a5, a6, a7)]
    if len(set(t)) != len(t):
        continue
    for v in itertools.permutations("xywz"):
        if [f(**dict(zip(v, i))) for i in t] == [1, 1, 1]:
            print(*v)
