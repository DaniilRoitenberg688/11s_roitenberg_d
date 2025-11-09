res = []
for i in range(174457, 174505 + 1):
    d = []
    for j in range(2, i // 2):
        if len(d) == 2:
            break
        if i % j == 0:
            d.append(j)
    if len(d) == 2:
        res.append(d)

res = sorted(res, key=lambda x: x[1] * x[0])
for i in res:
    print(*sorted(i))


        
