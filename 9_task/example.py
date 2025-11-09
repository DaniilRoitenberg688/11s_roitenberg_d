with open("9.txt") as f:
    c = []
    for s in f:
        s=s.strip()
        a = list(map(int, s.split()))
        c.append(a)



