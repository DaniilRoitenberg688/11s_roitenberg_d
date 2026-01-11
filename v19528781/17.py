with open("17.txt") as file:
    d = file.readlines()
    fedor = int(min(filter(lambda x: x.strip()[-1] == "7", d), key=int))
    r = []
    for i in range(1, len(d)):
        f = d[i].strip()
        s = d[i-1].strip()
        if (s[-1] == "7" and f[-1] == "7") or (s[-1] != "7" and f[-1] != "7"):
            continue
        if int(f) ** 2 + int(s) ** 2 >= fedor ** 2:
            continue
        r.append(int(f) ** 2 + int(s) ** 2)

print(len(r))
print(max(r))
            
     
        

