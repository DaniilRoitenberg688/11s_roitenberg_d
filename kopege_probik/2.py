import itertools

t = [(0, 0, 1, 1), (0, 1, 1, 1), (1, 1, 1, 0)]


def f(x, y, z, w):
    return (not x or y or not z) and (x or not y) or not w


for i in itertools.permutations("xywz"):
    if [f(**dict(zip(i, v))) for v in t] == [0, 0, 0]:
        print(*i)
