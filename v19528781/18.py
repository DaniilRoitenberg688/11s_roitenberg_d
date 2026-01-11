with open("18.txt") as f:
    d = f.readlines()

d = list(map(lambda x: float(x.strip()), d))


r = 0

for s in range(len(d)):
    for e in range(s, len(d)):
        line = d[s:e+1]
        if len(set(line)) != len(line):
            break
        if sorted(line, reverse=True) != line:
            break
        r = max(r, sum(line))
print(r)

        

