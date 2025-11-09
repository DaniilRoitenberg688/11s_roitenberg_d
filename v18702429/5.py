res = 0
for i in range(100):
    a = bin(i)
    print(a)
    s = sum(map(int, list(a[2:])))
    a = a + str(s % 2)
    s = sum(map(int, list(a[2:])))
    a = a + str(s % 2)
    if int(a, 2) > res:
        res = int(a, 2)
print(res)
    


