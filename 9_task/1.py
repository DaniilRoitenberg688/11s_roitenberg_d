r = 0
with open("92.txt") as f:
    for i in f:
        l = i.strip()
        l = list(map(int, l.split()))
        if len(l) != len(set(l)):
            continue
        mi = min(l)
        ma = max(l)
        if not((mi + ma) / 2 > sum(l) / len(l)):
            continue
        r += 1

print(r)
