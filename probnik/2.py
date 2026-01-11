import itertools


def f(x, y ,z ,w):
    return (x and not y) or (y == z) or not w

for a1, a2, a3, a4, a5 in itertools.product((0,1), repeat=5):
    t = [
        (a1, 0, a2, a5),
        (1, 0, a3, 0),
        (1, a4, 0, 0)
    ]

    if len(set(t)) != len(t):
        continue
    for v in itertools.permutations("xywz"):
        if [f(**dict(zip(v, k))) for k in t] == [0, 0, 0]:
            print(*v)
