with open("9.txt") as f:
    d = f.readlines()
    r = 0
    for l in d:
        i = list(map(int, l.strip().split()))
        c = list(filter(lambda x: i.count(x) > 1, i))
        nc = list(filter(lambda x: i.count(x) == 1, i))
        if len(nc) == 0 or len(c) == 0:
            continue
        if sum(nc) / len(nc) <= sum(c) / len(c):
            continue
        r += 1

print(r)
