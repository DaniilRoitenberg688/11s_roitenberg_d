def f(n, k):
    if n == 16:
        return 0
    if n < k:
        return 0
    if n == k:
        return 1
    if n % 3 == 0:
        return f(n - 2, k) + f(n // 3, k)
    else:
        return f(n - 2, k) + f(n - 4, k)


print(f(36, 4))
