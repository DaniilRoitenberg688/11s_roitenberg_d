with open("9.txt") as f:
    d = f.readlines()
    r = 0
    for i in d:
        i = list(map(int, i.strip().split()))
        if len(set(i)) != len(i):
            continue
        mi = min(i)
        ma = max(i)
        k = i[:]
        i = [j for j in i if j != mi and j != ma]
        if 2*(mi+ma) != 3 * sum(i):
            continue
        print(k)
        print(i)
        r +=1
print(r)
