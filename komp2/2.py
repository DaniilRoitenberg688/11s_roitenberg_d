import itertools


def f(x, y, w, z):
    return (x and not y) or (y == z) or w


for a1, a2, a3, a4, a5, a6, a7, a8 in itertools.product((1, 0), repeat=8):
    r = [
        (a1, a2, a3, 1),
        (1, a4, a5, a6),
        (1, 1, a7, a8)
    ]

    if len(r) != len(set(r)):
        continue

    for v in itertools.permutations("xywz"):
        if [f(**dict(zip(v, i))) for i in r] == [0, 0, 0]:
            print(*v)
