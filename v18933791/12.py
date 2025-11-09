from os import pread


with open("17.txt") as f:
    d = list(map(int, f.readlines()))
    k = list(filter(lambda x: x % 10 == 5, d))
    mi = min(k)
    r = []
    for i in range(1, len(d)):
        f = d[i -1]
        s = d[i]
        mip = min([f, s])
        if str(mip)[-1] != "5":
            continue
        if (f ** 2 + s ** 2) >= mi ** 2:
            continue
        r.append((f ** 2 + s ** 2)) 
print(len(r))
print(max(r))



        
