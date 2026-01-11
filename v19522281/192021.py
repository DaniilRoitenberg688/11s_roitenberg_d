def f(n, m):
    if n <= 25:
        return m % 2 == 0
    if m == 0:
        return 0
    h = [f(n - 3, m - 1), f(n - 6, m - 1), f(n // 3, m - 1)]
    return any(h) if (m + 1) % 2 == 0 else all(h)


print([i for i in range(26, 100) if f(i, 2)])
print([i for i in range(26, 100) if not f(i, 1) and f(i, 3)])
print([i for i in range(26, 100) if not f(i, 2) and f(i, 4)])
