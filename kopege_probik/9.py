r = 0
with open("9.txt") as f:
    d = f.readlines()
    for i in d:
        l = list(map(int, i.strip().split()))
        c = list(filter(lambda x: x % 2 == 0, l))
        if len(c) != 2:
            continue
        m = min(l)
        if sum(l) - m < m ** 2:
            continue
        r += 1
        
        
print(r)
            
