with open("24.txt") as f:
    l = f.readline()


r = 0

for s in range(len(l)):
    for e in range(s+r, len(l)):
        d = l[s:e+1]
        if d.count("A") > 2 or d.count("B") > 2:
            break
        else:
            r = len(d)
            
print(r)
