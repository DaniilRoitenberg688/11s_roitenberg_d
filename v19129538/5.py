res = 0
for n in range(123_456_789, 456_789_012 + 1):
    b = bin(n)[2:]
    if n % 2 == 0:
        b = "11" + b
    else:
        b = "1" + b + "10"
    r = int(b, 2)
    if r > res:
        res = r
print(res)
