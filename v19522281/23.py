def f(n,m):
    if n == 20:
        return 0
    if n < m:
        return 0
    if m == n:
        return 1
    return f(n-2, m) + f(n//2, m)

print(f(80,40)*f(40,1))
