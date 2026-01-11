from itertools import permutations, product


def f(x, y, w, z):
    return (x and (not y)) or (y == z) or (not w)


for a1, a2, a3, a4 in product((0,1)):
    t = [
        (a1, a2, 0, 0),
        (1, 0, a3, 0),
        (1, 0, 1, a4)
    ]
    if len(set(t)) != len(t):
        continue

    for v in permutations("xywz"):
        if [f(**dict(zip(v, i))) for i in t] == [0, 0, 0]:
            print(*v)
