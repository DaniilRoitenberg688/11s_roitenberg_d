# import itertools
#
#
# def f1(x, y, z, w):
#     return (x == y) and (w <= z)
#
#
# def f2(x, y, z, w):
#     return (x <= y) <= (w == z)
#
#
# for v in itertools.product((0, 1), repeat=5):
#     t = [(1, v[0], 1, 1),
#          (0, 1, 0, v[1]),
#          (v[2], 0, 0, v[3])]
#     if len(t) != len(set(t)):
#         continue
#     for l in itertools.permutations("xywz"):
#         if [f1(**dict(zip(l, k))) for k in t] == [1, 1, 0] and [f2(**dict(zip(l, k))) for k in t] == [0, v[4], 0]:
#             print(*l)
# import itertools
#
#
# def f(x, y, w, z):
#     return ((x <= y) and (y <= w)) or (z == (x or y))
#
# for a in itertools.product([0, 1], repeat=7):
#     t = [
#         (1, a[0], a[1], 1),
#         (1, a[2], a[3], a[4]),
#         (a[5], 1, a[6], 1),
#     ]
#     if len(set(t)) != len(t):
#         continue
#     for v in itertools.permutations("xwzy"):
#         if [f(**dict(zip(v, p))) for p in t] == [0, 0, 0]:
#             print(*v)



import itertools
from itertools import repeat


def f1(x, y, w, z):
    return (x <= y) == (w or (not z))

def f2(x, y, w, z):
    return (x <= y) and ((not w) == z)



for a1, a2, a3, a4, a5 in itertools.product((0, 1), repeat=5):
    t = [
        (a1, 1, 0, 1),
        (a2, 0, 0, 0),
        (0, a3, 0, 0)
    ]
    if len(set(t)) != len(t):
        continue

    for v in itertools.permutations("wyxz"):
        if [f1(**dict(zip(v, p))) for p in t] == [a4, 0, 0] and [f2(**dict(zip(v, p))) for p in t] == [0, a5, 1]:
            print(*v)




