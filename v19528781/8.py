from string import printable


p = printable[:13]


def f(n):
    r = ''
    while n > 0:
        r = p[n%13] + r 
        n //= 13
    return r

c = 0

for i in range(1, 10**7):
    t = f(i)
    if len(t) < 2:
        continue
    if len(set(t)) != len(t):
        continue
    tf = list(map(lambda x: p.index(x), list(t)))
    if sorted(tf) != tf:
        continue
    c += 1

print(c)
    
