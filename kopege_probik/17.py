with open("17.txt") as f:
    d = list(map(lambda x: int(x.strip()), f.readlines()))
    m = sum(d) / len(d)
    r = []
    for i in range(1, len(d)):
        f = d[i]
        s = d[i - 1]
        if f < m and s < m:
            if f % 10 == 9 or s % 10 == 9:
                r.append((s, f))

print(len(r))
print(sum(max(r, key=sum)))
