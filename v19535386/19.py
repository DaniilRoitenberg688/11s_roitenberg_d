def f(n, m, k):
    if m + n <= 165:
        return k % 2 == 0
    if k == 0:
        return 0
    h = [f(n-2, m, k-1), f(n//3, m, k-1), f(n, m-2, k-1), f(n, m//3, k-1)]
    return any(h) if (k+1) % 2 ==0 else all(h)


print([i for i in range(149, 10**4) if f(17, i, 2)])
print([i for i in range(149, 10**4) if not f(17, i, 1) and f(17, i, 3)])
print([i for i in range(149, 10**4) if not f(17, i, 2) and f(17, i, 4)])


