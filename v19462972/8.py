f = 0
for i in range(1000, 9999 + 1):
    if len(set(str(i))) != 4:
        continue
    i = str(i)
    for k in range(0,10):
        if k % 2 == 0:
            i = i.replace(str(k), "0")
        else:
            i = i.replace(str(k), "1")
    print(i)
    if "00" in i or "11" in i:
        continue
    f += 1
    
print(f)