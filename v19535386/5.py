c = 0
for i in range(10**6, 10**7):
    b=bin(i)[2:]  
    n = i
    for v in range(3):
        s = str(n)
        if sum(map(int, s)) % 2 == 0:
            b += "0"
        else:
            b += "1"
        n = int(b, 2)
    if 123_456_789 <= n <= 1_987_654_321:
        c+=1

print(c)


    
