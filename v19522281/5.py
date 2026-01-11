def f(n):
    r = ""
    while n > 0:
        r = str(n%3) + r
        n //=3
    return r

r = []
for i in range(10 ** 6, 10, -1):
    t = f(i)
    if i % 3 == 0:
        t += t[-2] + t[-1]
    else:
        t += f((i % 3)*5)
    k = int(t, 3)
    if k <= 173:
        r.append(k)


print(max(r))

