def f(x, y):
    return (2 * x + y != 70) or (x < y) or (a < x)


for a in range(100, -1, -1):
    b = []
    for x in range(10**2):
        for y in range(10**2):
            b.append(f(x, y))
    if all(b):
        print(a)
        break

