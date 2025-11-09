with open("24.txt") as f:
    d = list(f.read())
    a = 0
    b = 0
    r = 0
    c = 0
    for i in d:
        if i == "A":
            a += 1
        if i == "B":
            b += 1
        c += 1
        if a >= 2 and b >= 2:
            r = max([c, r])
            c = 0
            a = 0
            b = 0
print(r)

