with open('9.txt') as f:
    r = 0
    for i in f.readlines():
        a = list(map(int, i.split()))
        if len(a) == len(set(a)):
            continue
        m = max(a)
        if a.count(m) != 1:
            continue
        k = {}
        for j in a:
            if j not in k:
                k[j] = 1
            else:
                k[j] += 1
        s = 0
        for l, o in k.items():
            if o != 1:
                s += o * l
        if s < m:
            continue
        r += 1
print(r)
