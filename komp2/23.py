def f(m, n):
    if m == 20:
        return 0
    if m > n:
        return 0
    if m == n:
        return 1
    return f(m+1, n) + f(m+2, n) + f(m*3, n)

print(f(4, 16) * f(16, 22))
