import itertools

def f(x, y, w, z):
    return (x or y) and (not (y == z)) and not w


for a1, a2, a3, a4 in itertools.product((0,1), repeat=4):
    t = [
        (a1, 1, a2, 1),
        (0, 0, 1, a3),
        (0, a4, 1, 1)
    ]
    if len(set(t)) != len(t):
        continue
    for v in itertools.permutations("xywz"):
        if [f(**dict(zip(v, i))) for i in t] == [1, 1, 1]:
            print(*v)
