with open("1-7.txt") as f:
    data = f.readlines()
    n = -200_000
    for i in data:
        m = int(i)
        if abs(m) % 100 != 33:
            continue
        n = max(n, m)
    r = []
    for i in range(2, len(data)):
        a = int(data[i])
        b = int(data[i - 1])
        c = int(data[i - 2])
        k = (
            10 <= abs(a) <= 99,
            10 <= abs(b) <= 99,
            10 <= abs(c) <= 99,
        )
        if k.count(True) < 2:
            continue
        
        if sum((a, b, c)) ** 2 > n:
            continue
        r.append((a, b, c))
print(len(r))
print(sum(max(r, key=sum)))



