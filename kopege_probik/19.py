def f(n, k):
    if n >= 55:
        return k % 2 == 0
    if k == 0:
        return 0
    h = [f(n + 1, k - 1), f(n + 4, k - 1), f(n * 3, k - 1)]
    return any(h) if (k + 1) % 2 == 0 else all(h)


print([i for i in range(1, 55) if f(i, 2)])
print([i for i in range(1, 55) if not f(i, 1) and f(i, 3)])
print([i for i in range(1, 55) if not f(i, 2) and f(i, 4)])
