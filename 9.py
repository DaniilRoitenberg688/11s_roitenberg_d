with open("9.txt") as file:
    r = 0
    d = file.readlines()
    for i in d:
        i = list(map(int, i.strip().split()))
        mi = min(i)
        if i.count(mi) != 2 and i.count(mi) != 3:
            continue
        i = [x for x in i if x != mi]
        if len(set(i)) != len(i):
            continue
        
        mir = min(i)
        mar = max(i)
        i = [x for x in i if x != mir and x != mar]
        if (mir ** 2 + mar ** 2) > sum(i) ** 2:
            continue
        r += 1
print(r)
