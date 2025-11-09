with open("24.txt", "r") as f:
    l = f.read()
    c = 0
    r = 0
    for i in range(1, len(l)):
        if l[i] == "a" and l[i - 1] == "d" or l[i] == "d" and l[i - 1] == "a":
            if r < c:
                r = c
            c = 0
        else:
            c += 1
    print(r)
