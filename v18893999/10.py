with open("10.txt") as f:
    r = 0
    for i in f.readlines():
        d = i.split()
        if len(set(d)) != len(d):
            continue
        even = list(filter(lambda x: int(x) % 2 == 0, map(int, d)))
        odd = list(filter(lambda x: int(x) % 2, map(int, d)))
        if len(even) <= len(odd):
            continue
        if sum(even) >= sum(odd):
            continue
        r += 1
print(r)
        
            
