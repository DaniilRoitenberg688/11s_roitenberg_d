print("x w z y")
for x in range(0, 2):
    for w in range(0, 2):
        for z in range(0, 2):
            for y in range(0, 2):
                f1 = x and not(y)
                f2 = y == z
                f3 = not(w)
                if (f1 or f2 or f3) == 0:
                    print(x, w, z, y)
